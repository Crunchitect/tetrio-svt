import pygame, win32con, win32api, win32gui

def go_transparent(colorkey: tuple[int]) -> None:
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*colorkey), 0, win32con.LWA_COLORKEY)

    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)