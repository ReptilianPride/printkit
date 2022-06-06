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
        print(Colors.default+str(data)+Colors.default)
    def black(data):
        print(Colors.black+str(data)+Colors.default)
    def red(data):
        print(Colors.red+str(data)+Colors.default)
    def green(data):
        print(Colors.green+str(data)+Colors.default)
    def yellow(data):
        print(Colors.yellow+str(data)+Colors.default)
    def blue(data):
        print(Colors.blue+str(data)+Colors.default)
    def magenta(data):
        print(Colors.magenta+str(data)+Colors.default)
    def cyan(data):
        print(Colors.cyan+str(data)+Colors.default)
    def lightgrey(data):
        print(Colors.lightgrey+str(data)+Colors.default)
    def darkgrey(data):
        print(Colors.darkgrey+str(data)+Colors.default)
    def lightred(data):
        print(Colors.lightred+str(data)+Colors.default)
    def lightgreen(data):
        print(Colors.lightgreen+str(data)+Colors.default)
    def lightyellow(data):
        print(Colors.lightyellow+str(data)+Colors.default)
    def lightblue(data):
        print(Colors.lightblue+str(data)+Colors.default)
    def lightmagenta(data):
        print(Colors.lightmagenta+str(data)+Colors.default)
    def lightcyan(data):
        print(Colors.lightcyan+str(data)+Colors.default)
    def white(data):
        print(Colors.white+str(data)+Colors.default)
    def custom(data,color=''):
        print(color+data+Colors.default)
