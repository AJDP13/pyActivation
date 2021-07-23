try:
    from tkinter import Tk, Label, Button
except ImportError:
    print("Error importing reuired library tkinter")

class Activation:

    def __init__(self, title="Activation", sizeX = 300, sizeY=300, dispX=0, dispY=0, resizeX = True, resizeY = True, fullscreen = False, topmost = False):
        self.__title = title
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__dispX = dispX
        self.__dispY = dispY
        self.__resizeX = resizeX
        self.__resizeY = resizeY
        self.__fullscreen = fullscreen
        self.__topmost = topmost