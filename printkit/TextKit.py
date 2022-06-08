from .ColorKit import TextColor

class cprint:
    def default(data):
        print(TextColor.default+str(data)+TextColor.default)
    def black(data):
        print(TextColor.black+str(data)+TextColor.default)
    def red(data):
        print(TextColor.red+str(data)+TextColor.default)
    def green(data):
        print(TextColor.green+str(data)+TextColor.default)
    def yellow(data):
        print(TextColor.yellow+str(data)+TextColor.default)
    def blue(data):
        print(TextColor.blue+str(data)+TextColor.default)
    def purple(data):
        print(TextColor.purple+str(data)+TextColor.default)
    def cyan(data):
        print(TextColor.cyan+str(data)+TextColor.default)
    def lightgrey(data):
        print(TextColor.lightgrey+str(data)+TextColor.default)
    def darkgrey(data):
        print(TextColor.darkgrey+str(data)+TextColor.default)
    def lightred(data):
        print(TextColor.lightred+str(data)+TextColor.default)
    def lightgreen(data):
        print(TextColor.lightgreen+str(data)+TextColor.default)
    def lightyellow(data):
        print(TextColor.lightyellow+str(data)+TextColor.default)
    def lightblue(data):
        print(TextColor.lightblue+str(data)+TextColor.default)
    def lightmagenta(data):
        print(TextColor.lightmagenta+str(data)+TextColor.default)
    def lightcyan(data):
        print(TextColor.lightcyan+str(data)+TextColor.default)
    def white(data):
        print(TextColor.white+str(data)+TextColor.default)
    def custom(data,color=''):
        print(color+data+TextColor.default)
