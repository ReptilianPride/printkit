
class ForeColors:
    default='\033[39m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    yellow='\033[33m'
    blue='\033[34m'
    magenta='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    lightyellow='\033[93m'
    lightblue='\033[94m'
    lightmagenta='\033[95m'
    lightcyan='\033[96m'
    white='\033[97m'

class bgColors:
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

class cprint:
    def default(data):
        print(ForeColors.default+str(data))
    def black(data):
        print(ForeColors.black+str(data))
    def red(data):
        print(ForeColors.red+str(data))
    def green(data):
        print(ForeColors.green+str(data))
    def yellow(data):
        print(ForeColors.yellow+str(data))
    def blue(data):
        print(ForeColors.blue+str(data))
    def magenta(data):
        print(ForeColors.magenta+str(data))
    def cyan(data):
        print(ForeColors.cyan+str(data))
    def lightgrey(data):
        print(ForeColors.lightgrey+str(data))
    def darkgrey(data):
        print(ForeColors.darkgrey+str(data))
    def lightred(data):
        print(ForeColors.lightred+str(data))
    def lightgreen(data):
        print(ForeColors.lightgreen+str(data))
    def lightyellow(data):
        print(ForeColors.lightyellow+str(data))
    def lightblue(data):
        print(ForeColors.lightblue+str(data))
    def lightmagenta(data):
        print(ForeColors.lightmagenta+str(data))
    def lightcyan(data):
        print(ForeColors.lightcyan+str(data))
    def white(data):
        print(ForeColors.white+str(data))
    def custom(data,color=''):
        print(color+data)

class bgcolor:
    def default(data):
        print(bgColors.default+str(data))
    def black(data):
        print(bgColors.black+str(data))
    def black(data):
        print(bgColors.black+str(data))
    def red(data):
        print(bgColors.red+str(data))
    def green(data):
        print(bgColors.green+str(data))
    def yellow(data):
        print(bgColors.yellow+str(data))
    def blue(data):
        print(bgColors.blue+str(data))
    def magenta(data):
        print(bgColors.magenta+str(data))
    def cyan(data):
        print(bgColors.cyan+str(data))
    def lightgrey(data):
        print(bgColors.lightgrey+str(data))
    def darkgrey(data):
        print(bgColors.darkgrey+str(data))
    def lightred(data):
        print(bgColors.lightred+str(data))
    def lightgreen(data):
        print(bgColors.lightgreen+str(data))
    def lightyellow(data):
        print(bgColors.lightyellow+str(data))
    def lightblue(data):
        print(bgColors.lightblue+str(data))
    def lightmagenta(data):
        print(bgColors.lightmagenta+str(data))
    def lightcyan(data):
        print(bgColors.lightcyan+str(data))
    def white(data):
        print(bgColors.white+str(data))
    def custom(data,color=''):
        print(color+data)

