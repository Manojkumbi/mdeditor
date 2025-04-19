# GitHub Markdown Editor

A web-based IDE for editing GitHub repositories with Markdown support, syntax highlighting, and file management capabilities.

## Features

### Authentication
- GitHub Personal Access Token authentication
- Secure token storage
- Auto-login with saved tokens
- User profile display with avatar

### Repository Management
- Browse and select repositories
- Search repositories
- Switch between repositories
- Display current repository name

### File Explorer
- Hierarchical file tree view
- Navigate through directories
- File and folder icons
- Modified file indicators
- Back navigation in directories
- Context menu for file operations

### File Operations
- Create new files
- Create new folders
- Rename files and folders
- Delete files and folders
- Save file changes
- Reset unsaved changes

### Editor Features
- Monaco Editor integration (VS Code-like experience)
- Syntax highlighting for multiple languages
- IntelliSense and code completion
- Line numbers
- Word wrap
- Bracket pair colorization
- Minimap
- Custom scrollbars

### Preview Features
- Live Markdown preview
- HTML preview
- Toggle between edit and preview modes
- Syntax highlighting in code blocks
- Responsive layout

### UI Features
- Dark theme
- Responsive design
- Mobile optimization
- Toast notifications
- Loading indicators
- Context menus
- Keyboard shortcuts

## Getting Started

### Prerequisites
- A GitHub account
- A GitHub Personal Access Token with 'repo' scope

### Creating a GitHub Token
1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token"
3. Select the 'repo' scope
4. Copy the generated token

### Logging In
1. Open the application in your browser
2. Paste your GitHub Personal Access Token
3. Click "Connect to GitHub"
4. You'll be redirected to the main interface upon successful authentication

## Usage Guide

### Navigating Repositories
1. Click the repository selector in the top bar
2. Use the search box to filter repositories
3. Click on a repository to select it
4. The file tree will load with the repository contents

### Working with Files

#### Opening Files
- Click on a file in the file tree to open it
- The editor will load with syntax highlighting based on file extension
- The current file name will display in the top bar

#### Creating Files
- Right-click in the file tree and select "New File"
- Enter the file name with extension
- The file will be created in the current directory

#### Creating Folders
- Right-click in the file tree and select "New Folder"
- Enter the folder name
- The folder will be created in the current directory

#### Renaming Files/Folders
- Right-click on the item and select "Rename"
- Enter the new name
- The item will be renamed while preserving its contents

#### Deleting Files/Folders
- Right-click on the item and select "Delete"
- Confirm the deletion
- The item and its contents will be removed

### Editing Files

#### Basic Editing
- Type directly in the editor
- Use standard keyboard shortcuts (Ctrl+S to save, etc.)
- The editor provides syntax highlighting and code completion

#### Saving Changes
- Click the "Save" button in the top bar
- Use Ctrl+S (Cmd+S on Mac) keyboard shortcut
- A success toast will appear when saved

#### Discarding Changes
- Click the "Reset" button to revert unsaved changes
- Use Ctrl+Z (Cmd+Z on Mac) keyboard shortcut
- Confirm when prompted

### Previewing Content

#### Markdown Preview
- For Markdown files, click the "Preview" button
- The content will render with proper formatting
- Code blocks will have syntax highlighting
- Click "Edit" to return to the editor

#### HTML Preview
- For HTML files, click the "Preview" button
- The HTML will render in a sandbox iframe
- Click "Edit" to return to the editor

### Keyboard Shortcuts
- `Ctrl+S` / `Cmd+S`: Save file
- `Ctrl+Z` / `Cmd+Z`: Reset changes
- `Escape`: Close context menus
- `Ctrl+F` / `Cmd+F`: Find in file
- `Ctrl+H` / `Cmd+H`: Replace in file

## Supported File Types
- Markdown (.md)
- HTML (.html)
- JavaScript (.js, .jsx)
- TypeScript (.ts, .tsx)
- CSS (.css)
- JSON (.json)
- YAML (.yml, .yaml)
- Python (.py)
- Java (.java)
- C/C++ (.c, .cpp)
- Go (.go)
- Rust (.rs)
- Ruby (.rb)
- PHP (.php)
- SQL (.sql)
- Shell scripts (.sh, .bash, .zsh)
- Plain text (.txt)
- Git configuration (.gitignore)

## Tips and Tricks
- Use the context menu (right-click) for quick access to file operations
- The file tree shows modified files with a dot indicator
- The editor automatically detects file types and applies appropriate syntax highlighting
- Use the repository search to quickly find repositories in large accounts
- The sidebar can be toggled to maximize editor space
- Toast notifications provide feedback for all operations

## Troubleshooting

### Common Issues
- **Authentication Failed**: Ensure your token has the 'repo' scope and hasn't expired
- **File Not Saving**: Check your internet connection and token permissions
- **Preview Not Working**: Ensure the file has the correct extension (.md or .html)
- **Editor Not Loading**: Try refreshing the page or clearing browser cache

### Error Messages
- "Invalid token": Your GitHub token is invalid or expired
- "Failed to get contents": Repository access issue or network problem
- "File was modified elsewhere": Concurrent edits detected, reload to get latest version
- "Rate limit exceeded": Too many API requests, wait before trying again

## Security Notes
- Your GitHub token is stored locally in your browser
- The token is never sent to any server other than GitHub's API
- Log out when using shared computers to clear your token
- Use tokens with minimal required permissions

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (landscape mode recommended)

## Contributing
Feel free to submit issues and enhancement requests! 