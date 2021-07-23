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
        self.__destroyed = False
        self.show()

    def show(self): #Function to create window and show it
        if not self.__showing:
            self.__root = Tk()
            self.__root.geometry("{}x{}+{}+{}".format(self.__sizeX, self.__sizeY, self.__dispX, self.__dispY))
            self.__root.title(self.__title)
            self.__root.resizable(self.__resizeX, self.__resizeY)
            self.__root.attributes("-fullscreen", self.__fullscreen)
            self.__root.attributes("-topmost", self.__topmost)
            self.__root.attributes("-alpha", self.__alpha)
            self.__showing = True
            #return self.__root
        else:
            print("ActivationWindow: Window is already showing")

##Functions for changing attributes
    def fullscreen(self, option = True):
        if not self.__destroyed:
            if self.__fullscreen == option:
                if option:
                    print("ActivationWindow: Window is already fullscreen")
                else:
                    print("ActivationWindow: Window is already not fullscreen")
                #return False
            else:
                self.__root.attributes("-fullscreen", option)
                self.__fullscreen = option
                #return True
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
    def alpha(self, option):
        if not self.__destroyed:
            if not isinstance(option, float) or not isinstance(option, int):
                print("Given argument for alpha attribute is not a valid float/integer")
                #return False
            
            else:
                self.__root.attributes("-alpha", option)
                self.__alpha = option
                #return True
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")

    def position(self, X=0, Y=0):
        if not self.__destroyed:
            if isinstance(X, int) and isinstance(Y, int):
                self.__root.geometry("{}x{}+{}+{}".format(self.__sizeX, self.__sizeY, X, Y))
                self.__dispX = X
                self.__dispY = Y
                #return True
            else:
                print("ActivationWindow: Given arguments for X and Y position are not valid integers")
                #return False
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")

##Functions to return current attribute values
    def currentPositionX(self):
        if not self.__destroyed:
            return self.__dispX
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False
    
    def currentPositionY(self):
        if not self.__destroyed:
            return self.__dispY
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False
    
    def currentSizeX(self):
        if not self.__destroyed:
            return self.__sizeX
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False
    
    def currentSizeY(self):
        if not self.__destroyed:
            return self.__sizeY
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False

    def currentTopmostValue(self):
        if not self.__destroyed:
            return self.__topmost
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False

    def currentFullscreenValue(self):
        if not self.__destroyed:
            return self.__fullscreen
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False

    def currentWindowTitle(self):
        if not self.__destroyed:
            return self.__title
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False
    
    def currentAlpha(self):
        if not self.__destroyed:
            return self.__alpha
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False
    
    def showing(self):
        if not self.__destroyed:
            return self.__showing
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False


##Functions for activity window
    def destroy(self):
        if not self.__destroyed:
            self.__showing = False
            self.__destroyed = True
            self.__root.destroy()
        else:
            print("ActivationWindow: Window has been destroyed. Please run the show() function")
            return False