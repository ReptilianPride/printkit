class Colors:
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
