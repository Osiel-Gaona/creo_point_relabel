import os

# http://patorjk.com/software/taag/#p=display&f=Small%20Slant&t=Creo%20Point%20Label
header_1 = "\
\n\
    _____               ___       _      __    __        __       __ \n\
   / ___/______ ___    / _ \___  (_)__  / /_  / /  ___ _/ /  ___ / / \n\
  / /__/ __/ -_) _ \  / ___/ _ \/ / _ \/ __/ / /__/ _ `/ _ \/ -_) /  \n\
  \___/_/  \__/\___/ /_/   \___/_/_//_/\__/ /____/\_,_/_.__/\__/_/   \n"



header_2 = """How to use:
Fill all parameters below, prefix can be nothing, 
start and end numbers must be integers
sufix can be nothing
when done a file text "label_points.txt" will be generated.
In Creo, edit definition of your offset points so the coordinates 
window is open, make sure you have selected a reference (CSYS).
Do not close the window and go to File, Manage Session then select
Play trail file and browse to the text file generated.

"""


header_3 = "\
                     [Consecutive]   \n\
                       [start #]     \n\
                           |         \n\
                           |         \n\
A1F,A2F,A3F...   AnF = [A][n][F]     \n\
                        /     \      \n\
                       /       \     \n\
                 [Prefix]   [Suffix] \n"

colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'turquoise': '\033[96m',
    'gray': '\033[32m',
}


def colorize(string, color):
    if color not in colors:
        return string
    else:
        return colors[color] + string + '\033[0m'


def main():
    os.system('mode 70,40')
    os.system('cls')
    print(colorize(header_1, 'pink'))
    print(colorize('version OCL 0.1', 'green'))
    print(colorize(header_2, 'turquoise'))
    print(colorize(header_3, 'red'))
    try:
        prefix = input("Enter prefix [can be nothing]: ")
        start_num = input("Enter start number: ")
        end_num = input("Enter end number: ")
        suffix = input("Enter Suffix [can be nothing]: ")
        row_start = input("Start at row [0]:")
        num = int(start_num)
        if row_start == '':
        	row_start = 0
        else:
        	row_start = int(row_start)
        if end_num > start_num:
        	range_num = (int(end_num) - int(start_num)) + 1
        	reverse = 'no'
        if end_num < start_num:
        	range_num = (int(start_num) - int(end_num)) + 1
        	reverse = 'yes'
        a1 = "~ Select `Odui_Dlg_00` `t1.CSysPntsTbl` 2 `okit_wdg_table_row_"
        a2 = "` `Name`"
        b = "~ Activate `Odui_Dlg_00` `t1.rename`"
        c1 = "~ Update `Odui_Dlg_00` `t1.PntNameInpPnl` `"
        c2 = "`"
        with open("label_points.txt", 'w+') as f:
            for _ in range(range_num):
                f.write(a1 + str(row_start) + a2 + '\n')
                f.write(b + '\n')
                f.write(c1 + prefix + str(num) + suffix + c2 + '\n')
                row_start += 1
                if reverse == 'no':
                	num += 1
                if reverse == 'yes':
                	num -= 1

        input("File Done")
    except:
        print()
        print('Error:')
        print('Prefix = ',prefix)
        print('Start num = ',start_num)
        print('End num = ',end_num)
        print('Suffix = ',suffix)
        input("Check your input and try again...")
        main()


if __name__ == "__main__":
    main()
