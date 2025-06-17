#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Hardlink indexing and management utilities for Linker."""

import pathlib
import os
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class HardlinkEntry:
    path: pathlib.Path
    nlink: int
    inode: int
    is_hardlink: bool  # True if nlink > 1
    is_dir: bool


def scan_hardlinks(base_path: pathlib.Path) -> List[HardlinkEntry]:
    """
    Recursively scan for all files and directories under base_path, identifying hardlinks.

    Args:
        base_path: The root directory to scan.

    Returns:
        List of HardlinkEntry objects.
    """
    entries = []
    for root, dirs, files in os.walk(base_path):
        root_path = pathlib.Path(root)
        for name in files:
            file_path = root_path / name
            try:
                stat = file_path.stat()
                nlink = stat.st_nlink
                inode = stat.st_ino
                is_hardlink = nlink > 1
                entries.append(HardlinkEntry(
                    path=file_path,
                    nlink=nlink,
                    inode=inode,
                    is_hardlink=is_hardlink,
                    is_dir=False
                ))
            except OSError:
                continue  # Permission denied or other error
        for name in dirs:
            dir_path = root_path / name
            try:
                stat = dir_path.stat()
                nlink = stat.st_nlink
                inode = stat.st_ino
                # For directories, is_hardlink is always False (no hardlinks to dirs)
                entries.append(HardlinkEntry(
                    path=dir_path,
                    nlink=nlink,
                    inode=inode,
                    is_hardlink=False,
                    is_dir=True
                ))
            except OSError:
                continue
    return entries 