try:
    from tkinter import Tk, Label, Button
except ImportError:
    print("Error importing reuired library tkinter")

class ActivationWindow:

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

    def show(self): #Function to create window and show it
        self.__root = Tk()
        self.__root.geometry("{}x{}+{}+{}".format(self.__sizeX, self.__sizeY, self.__dispX, self.__dispY))
        self.__root.title(self.__title)
        self.__root.resizable(self.__resizeX, self.__resizeY)
        self.__root.attributes("-fullscreen", self.__fullscreen)
        self.__root.attributes("-topmost", self.__topmost)
        self.__root.attributes("-alpha", self.__alpha)

##Functions for changing attributes
    def fullscreen(self, option = True):
        if self.__fullscreen == option:
            if option:
                print("ActivationWin: Window is already fullscreen")
            else:
                print("ActivationWin: Window is already not fullscreen")
            return False
        else:
            self.__root.attributes("-fullscreen", option)
            self.__fullscreen = option
            return True
    def alpha(self, option):
        if not isinstance(option, float) or not isinstance(option, int):
            print("Given argument for alpha attribute is not a valid float/integer")
            return False
        
        else:
            self.__root.attributes("-alpha", option)
            self.__alpha = option
            return True

    def position(self, X=0, Y=0):
        if isinstance(X, int) and isinstance(Y, int):
            self.__root.geometry("{}x{}+{}+{}".format(self.__sizeX, self.__sizeY, X, Y))
            self.__dispX = X
            self.__dispY = Y
            return True
        else:
            print("ActivationWin: Given arguments for X and Y position are not valid integers")
            return False



##Functions for controlling window
    def destroy(self):
        self.__showing = False
        self.__root.destroy()