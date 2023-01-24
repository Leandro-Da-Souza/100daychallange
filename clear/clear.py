import os
"""
import sys
sys.path.append('/Users/leandrodasouza/Develop/Python/100DaysChallange/clear')
"""
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
