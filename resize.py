import pygetwindow
def resize():
    win = pygetwindow.getWindowsWithTitle('888casino')[0]
    win.restore()
    win.moveTo(0,0)
    win.size = (600, 600)