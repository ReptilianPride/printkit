class BgColor:
    default="\033[49m"
    black="\033[40m"
    red="\033[41m"
    green="\033[42m"
    yellow="\033[43m"
    blue="\033[44m"
    magenta="\033[45m"
    cyan="\033[46m"
    lightgrey="\033[47m"
    darkgrey="\033[100m"
    lightred="\033[101m"
    lightgreen="\033[102m"
    lightyellow="\033[103m"
    lightblue="\033[104m"
    lightmagenta="\033[105m"
    lightcyan="\033[106m"
    white="\033[107m"
    
class bgcolor:
    def default():
        print(BgColor.default)
    def black():
        print(BgColor.black)
    def black():
        print(BgColor.black)
    def red():
        print(BgColor.red)
    def green():
        print(BgColor.green)
    def yellow():
        print(BgColor.yellow)
    def blue():
        print(BgColor.blue)
    def magenta():
        print(BgColor.magenta)
    def cyan():
        print(BgColor.cyan)
    def lightgrey():
        print(BgColor.lightgrey)
    def darkgrey():
        print(BgColor.darkgrey)
    def lightred():
        print(BgColor.lightred)
    def lightgreen():
        print(BgColor.lightgreen)
    def lightyellow():
        print(BgColor.lightyellow)
    def lightblue():
        print(BgColor.lightblue)
    def lightmagenta():
        print(BgColor.lightmagenta)
    def lightcyan():
        print(BgColor.lightcyan)
    def white():
        print(BgColor.white)
    def custom(color=''):
        print(color)

