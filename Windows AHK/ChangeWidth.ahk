; Adjust the title below to match the window title of "Habbo Hotel: Origins"
WinTitle := "Habbo Hotel: Origins"

; Wait until the window is found
WinWait, %WinTitle%

; Get the current window position and size
WinGetPos, WinX, WinY, WinWidth, WinHeight, %WinTitle%

; Set the new width (you can adjust this value)
NewWidth := 1450  ; Change this to your desired width

; Move and resize the window with the new width, keeping the same height and position
WinMove, %WinTitle%, , WinX, WinY, %NewWidth%, WinHeight
