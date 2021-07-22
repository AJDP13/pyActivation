from winreg import HKEY_CLASSES_ROOT, HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, KEY_READ, KEY_WRITE, REG_BINARY, REG_CREATED_NEW_KEY, REG_DWORD_BIG_ENDIAN, REG_DWORD_LITTLE_ENDIAN, REG_EXPAND_SZ, REG_FULL_RESOURCE_DESCRIPTOR, REG_MULTI_SZ


try:
    import winreg
except ImportError:
    print("Error importing Winreg!")

#KEY LOCATIONS - CONSTANTS
HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
HKEY_CURRENT_CONFIG = winreg.HKEY_CURRENT_CONFIG

#KEY TYPES - CONSTANTS
REG_BINARY = winreg.REG_BINARY
REG_DWORD = winreg.REG_DWORD
REG_CREATED_NEW_KEY = winreg.REG_CREATED_NEW_KEY
REG_DWORD_BIG_ENDIAN = winreg.REG_DWORD_BIG_ENDIAN
REG_DWORD_LITTLE_ENDIAN = winreg.REG_DWORD_LITTLE_ENDIAN
REG_EXPAND_SZ = winreg.REG_EXPAND_SZ
REG_FULL_RESOURCE_DESCRIPTOR = winreg.REG_FULL_RESOURCE_DESCRIPTOR
REG_MULTI_SZ = winreg.REG_MULTI_SZ
REG_LINK = winreg.REG_LINK

#KEY ACCESS - CONSTANTS
KEY_ALL_ACCESS = winreg.KEY_ALL_ACCESS
KEY_READ = winreg.KEY_READ
KEY_WRITE = winreg.KEY_WRITE


class RegistryKey:

    def __init__(self, name="RegKey", access = KEY_READ, KeyLocation = HKEY_CURRENT_USER, path = "Software/RegistryKeys", type = REG_DWORD, value = ""):
        self.__name = name
        self.__access = access
        self.__KeyLocation = KeyLocation
        self.__path = path
        self.__type = type
        self.__value = value

    def create_key(self):
        try:
            with winreg.ConnectRegistry(None, type) as hkey:
                with winreg.CreateKey(hkey, self.__path) as sub_key:
                    winreg.SetValueEx(sub_key, self.__name, 0, self.__type, self.__value)
                    return True
        except Exception as e:
            print("Exception occured: {}".format(e))

    def read_key(self):
        try:
            with winreg.ConnectRegistry(None, self.__KeyLocation) as hkey:
                with winreg.OpenKey(hkey, self.__path, 0, self.__access) as key:
                    return winreg.QueryValueEx(key, self.__name)[0];

        except Exception as e:
            print("Exception occured: {}".format(e))