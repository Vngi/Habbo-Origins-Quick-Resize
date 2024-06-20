#####Mac Guide: 

# Hammerspoon Window Management

This guide explains how to use Hammerspoon, a powerful automation tool for macOS, to automatically center a window with a specific title.

## Prerequisites

- macOS
- [Hammerspoon](https://www.hammerspoon.org/) installed

## Installation

1. **Download and Install Hammerspoon**:
   - Visit [Hammerspoon.org](https://www.hammerspoon.org/) and download the latest version.
   - Install Hammerspoon by dragging it to your Applications folder.

2. **Create Configuration File**:
   - Open Terminal.
   - Create the `.hammerspoon` directory in your home folder if it doesn't exist:
     ```sh
     mkdir -p ~/.hammerspoon
     ```
   - Open your favorite text editor and create a file named `init.lua` in the `.hammerspoon` directory:
     ```sh
     touch ~/.hammerspoon/init.lua
     ```

3. **Add the Script**:
   - Copy and paste the following Lua script into `init.lua`:
     ```lua
     -- Adjust the title below to match the window title of "Habbo Hotel: Origins"
     local winTitle = "Habbo Hotel: Origins"

     -- Function to center the window
     local function centerWindow()
         local win = hs.window.find(winTitle)
         if win then
             local screen = win:screen()
             local screenFrame = screen:frame()
             local winFrame = win:frame()

             local newX = (screenFrame.w - winFrame.w) / 2
             local newY = (screenFrame.h - winFrame.h) / 2 + 100 -- Move down by 100 pixels to center lower

             win:setFrame(hs.geometry.rect(newX, newY, winFrame.w, winFrame.h))
         end
     end

     -- Watch for the window to appear and then center it
     hs.window.filter.new(winTitle)
         :subscribe(hs.window.filter.windowCreated, function()
             hs.timer.doAfter(1, centerWindow)
         end)

     -- Reload Hammerspoon configuration automatically
     hs.pathwatcher.new(os.getenv("HOME") .. "/.hammerspoon/", hs.reload):start()
     hs.alert.show("Config loaded")
     ```

4. **Reload Hammerspoon Configuration**:
   - Launch Hammerspoon from the Applications folder.
   - Click on the Hammerspoon menu bar icon and select "Reload Config".

## Usage

- The script will automatically center the window titled "Habbo Hotel: Origins" when it is created, moving it 100 pixels down from the center of the screen.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements.

## License

This project is licensed under the MIT License.



### AutoHotkey Scripts for Window Manipulation

#### Scripts Overview

This repository contains AutoHotkey scripts to manipulate window size and position for specific applications on Windows.

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
   - Open the script file (`FixWindow.ahk`) in a text editor.
   - Modify the `WinTitle` variable to match the title of the application window you want to center.
   - Adjust the `ScreenWidthFraction` and `ScreenHeightFraction` variables if you want to center the window differently.
   - Giving you the ability to move it around without issues!

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

- Thank you to AutoHotkey community for their scripting resources.
