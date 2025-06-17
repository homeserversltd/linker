# Linker TUI Utility

A modern, safe, and efficient terminal-based tool for managing hardlinks and directories, built with Python and Textual.

## Features
- **Browse** directories with nnn-like navigation
- **Create hardlinks** for files and directories (recursively)
- **Delete hardlinks** and directories (with safety checks)
- **Rename directories** with a modal prompt (`r`)
- **Create new directories** with a modal prompt (`n`)
- **Deploy (hardlink) selected items** with `d` or `p`
- **Multi-key support** for actions (e.g., deploy: `d`, `p`)
- **Modal dialogs** for safe, interactive input (rename, new dir)
- **Keyboard and mouse navigation**
- **Safety-first deletion**: Directories are only deleted if empty or contain only hardlinks

## Keybinds
| Key      | Action             | Description                       |
|----------|--------------------|-----------------------------------|
| h        | go_up              | Go up dir                         |
| j        | move_down          | Move down                         |
| k        | move_up            | Move up                           |
| l        | enter_dir          | Enter dir                         |
| space    | toggle_select      | Select                            |
| enter    | deploy             | Deploy (hardlink)                 |
| d, p     | deploy             | Deploy (hardlink)                 |
| delete   | delete_link        | Delete hardlink or dir            |
| r        | rename             | Rename hovered directory          |
| n        | new_dir            | Create new directory              |
| q        | quit               | Quit                              |

## Modal Dialogs
- **Rename** and **New Directory** actions use a reusable modal dialog for text input.
- Modal can be exited by:
  - Clicking OK (submits)
  - Clicking Cancel
  - Pressing `Enter` (when input is focused, submits)
  - Pressing `q` or `Escape` (cancels)

## Directory Deletion Safety
- **Directories are only deleted if:**
  - They are empty, or
  - They contain only hardlinks (files with `st_nlink > 1` and no subdirectories)
- **If a directory contains any non-hardlink file or subdirectory, deletion is skipped.**
- This prevents accidental data loss of unique files.
- (Optional: You can extend this with a force-delete or confirmation modal if needed.)

## Usage
Run the TUI as root for full hardlinking capability:
```sh
sudo linker
```

Navigate with vim keys, select files, and use the keybinds above for actions.

## Extensibility
- The modal dialog is generic and can be reused for any text input prompt.
- Keybinds are easily configurable in `config.py`.
- All actions are logged for diagnostics.

## Requirements
- Python 3.11+
- [Textual](https://github.com/Textualize/textual) >= 3.1.0
- [Rich](https://github.com/Textualize/rich) >= 14.0.0

## Authors, License & Distribution
- This tool is originated from and distributed as part of the HomeServer LLC product suite.
- Licensed under GPLv3.
