### macOS Guide

#### Hammerspoon Window Management

This repository includes a script for managing window size and position on macOS using Hammerspoon.

### Prerequisites

- macOS
- [Hammerspoon](https://www.hammerspoon.org/) installed

### Installation

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

### Usage

- The script will automatically center the window titled "Habbo Hotel: Origins" when it is created, moving it 100 pixels down from the center of the screen.

### Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements.

### License

This project is licensed under the MIT License.