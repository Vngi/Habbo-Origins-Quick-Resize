import ctypes
import win32gui
import win32con
import win32api

def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        return None
    else:
        return hwnd

def set_window_size(hwnd, width, height):
    # Calculate the new position to center the window
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    new_x = (screen_width - width) // 2
    new_y = (screen_height - height) // 2

    # Set window size and position
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, new_x, new_y, width, height,
                          win32con.SWP_NOOWNERZORDER | win32con.SWP_FRAMECHANGED | win32con.SWP_NOZORDER)

def maximize_to_fullscreen(hwnd):
    # Get screen width and height
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Set window style to remove title bar and borders
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style &= ~win32con.WS_CAPTION
    style &= ~win32con.WS_THICKFRAME
    style &= ~win32con.WS_MINIMIZEBOX
    style &= ~win32con.WS_MAXIMIZEBOX
    style &= ~win32con.WS_SYSMENU
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    # Ensure the window is restored (not minimized or maximized)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    # Move and resize window to cover the entire screen
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, screen_width, screen_height,
                          win32con.SWP_NOOWNERZORDER | win32con.SWP_FRAMECHANGED | win32con.SWP_NOZORDER)

    # Force the window to redraw
    win32gui.UpdateWindow(hwnd)

    # Send WM_SIZE message to force the application to redraw its content
    win32gui.PostMessage(hwnd, win32con.WM_SIZE, win32con.SIZE_RESTORED, (screen_height << 16) | screen_width)

    # Simulate pressing F11 to switch to fullscreen mode if the application supports it
    ctypes.windll.user32.PostMessageW(hwnd, win32con.WM_KEYDOWN, win32con.VK_F11, 0)
    ctypes.windll.user32.PostMessageW(hwnd, win32con.WM_KEYUP, win32con.VK_F11, 0)

def make_fullscreen(hwnd, initial_width, initial_height):
    # Set initial window size
    set_window_size(hwnd, initial_width, initial_height)

    # Maximize to fullscreen
    maximize_to_fullscreen(hwnd)

if __name__ == "__main__":
    app_title = "Habbo Hotel: Origins"  # Replace with the exact title of the window
    hwnd = find_window(app_title)
    
    if hwnd:
        initial_width = 800  # Replace with your desired initial width
        initial_height = 600  # Replace with your desired initial height
        make_fullscreen(hwnd, initial_width, initial_height)
        print(f"Application '{app_title}' is now fullscreen.")
    else:
        print(f"Window with title '{app_title}' not found.")
