try:
    from tkinter import Tk, Label, Button
except ImportError:
    print("Error importing reuired library tkinter")

class Activation:

    def __init__(self, title="Activation", sizeX = 300, sizeY=300, dispX=0, dispY=0, resizeX = True, resizeY = True, fullscreen = False, topmost = False, alpha=1):
        self.__title = title
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__dispX = dispX
        self.__dispY = dispY
        self.__resizeX = resizeX
        self.__resizeY = resizeY
        self.__fullscreen = fullscreen
        self.__topmost = topmost
        self.__showing = False
        self.__alpha = alpha

    def show(self):
        self.__root = Tk()
        self.__root.geometry("{}x{}+{}+{}".format(self.__sizeX, self.__sizeY, self.__dispX, self.__dispY))
        self.__root.title(self.__title)
        self.__root.resizable(self.__resizeX, self.__resizeY)
        self.__root.attributes("-fullscreen", self.__fullscreen)
        self.__root.attributes("-topmost", self.__topmost)
        self.__root.attributes("-alpha", self.__alpha)
