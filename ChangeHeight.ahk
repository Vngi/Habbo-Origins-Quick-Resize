; Adjust the title below to match the window title of "Habbo Hotel: Origins"
WinTitle := "Habbo Hotel: Origins"

; Wait until the window is found
WinWait, %WinTitle%

; Get the current window position and size
WinGetPos, WinX, WinY, WinWidth, WinHeight, %WinTitle%

; Set the new height (you can adjust this value)
NewHeight := 1150  ; Change this to your desired height

; Move and resize the window with the new height, keeping the same width and position
WinMove, %WinTitle%, , WinX, WinY, WinWidth, %NewHeight%
