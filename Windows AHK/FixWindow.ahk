; Adjust the title below to match the window title of "Habbo Hotel: Origins"
WinTitle := "Habbo Hotel: Origins"

; Wait until the window is found
WinWait, %WinTitle%

; Get the screen dimensions
ScreenWidth := A_ScreenWidth
ScreenHeight := A_ScreenHeight

; Get the window dimensions
WinGetPos, WinX, WinY, WinWidth, WinHeight, %WinTitle%

; Calculate new position to move the window down to the center of the screen
NewX := (ScreenWidth - WinWidth) / 2
NewY := (ScreenHeight - WinHeight) / 2 + 100  ; Move down by 100 pixels to center lower

; Move the window to the new position
WinMove, %WinTitle%, , %NewX%, %NewY%
