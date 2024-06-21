### Windows Guide

#### AutoHotkey Scripts for Window Manipulation

This guide explains how to use AutoHotkey scripts to manipulate window size and position for specific applications on Windows.

### Prerequisites

- Windows
- [AutoHotkey](https://www.autohotkey.com/) installed

### Instructions for Each Script

#### 1. Script to Change Window Height

- **Purpose**: This script adjusts the height of the specified window without changing its width or position.

##### Usage:

1. **Install AutoHotkey**: If not already installed, download and install AutoHotkey from [https://www.autohotkey.com/](https://www.autohotkey.com/).

2. **Edit the Script**:
   - Open the script file (`ChangeHeight.ahk`) in a text editor.
   - Modify the `WinTitle` variable to match the title of the application window you want to resize.
   - Adjust the `NewHeight` variable to your desired window height.

3. **Run the Script**:
   - Double-click the `ChangeHeight.ahk` file to execute the script.
   - The script will resize the specified window to the new height while maintaining its current width and position.

#### 2. Script to Change Window Width

- **Purpose**: This script adjusts the width of the specified window without changing its height or position. Be cautious with extreme width changes as it may affect what is visible on screen.

##### Usage:

1. **Install AutoHotkey**: If not already installed, download and install AutoHotkey from [https://www.autohotkey.com/](https://www.autohotkey.com/).

2. **Edit the Script**:
   - Open the script file (`ChangeWidth.ahk`) in a text editor.
   - Modify the `WinTitle` variable to match the title of the application window you want to resize.
   - Adjust the `NewWidth` variable to your desired window width.

3. **Run the Script**:
   - Double-click the `ChangeWidth.ahk` file to execute the script.
   - The script will resize the specified window to the new width while maintaining its current height and position.

#### 3. Script to Center Window

- **Purpose**: This script centers the specified window on the screen.

##### Usage:

1. **Install AutoHotkey**: If not already installed, download and install AutoHotkey from [https://www.autohotkey.com/](https://www.autohotkey.com/).

2. **Edit the Script**:
   - Open the script file (`CenterWindow.ahk`) in a text editor.
   - Modify the `WinTitle` variable to match the title of the application window you want to center.

3. **Run the Script**:
   - Double-click the `CenterWindow.ahk` file to execute the script.
   - The script will move the specified window to the center of the screen.

### Notes

- Ensure that the `WinTitle` variable in each script matches exactly with the title of the application window as it appears in the Windows title bar.
- When adjusting window width, be mindful that extreme changes may affect what is visible on screen. Experiment with different widths to find what works best for you.
- These scripts use AutoHotkey's `WinMove` command to manipulate window size and position based on screen coordinates. Adjustments may be needed based on specific application behaviors.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Acknowledgments

- Thank you to the AutoHotkey community for their scripting resources.
