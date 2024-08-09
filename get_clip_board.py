"""
Author: Yair Balilti
Description: Get the clipboard history (Winkey + V) from TextInputHost.exe dump.
You need a clean dump without any history (or download the attached one), and another dump with the history:

To get the strings you can use: SysinternalsSuite\strings.exe TextInputHost.dmp > strings.txt
"""
import sys



def strings_from_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data
    
def main():
    if len(sys.argv) != 3:
        print("Usage: {script_name} <clean_string_TextInputHost.exe> <string_dump_TextInputHost.exe>".format(script_name=sys.argv[0]))
        return 0

    clean_strings = sys.argv[1]
    dump_strings = sys.argv[2]
    clean_strings = strings_from_file(clean_strings)
    dump_strings = strings_from_file(dump_strings)

    print(set(dump_strings) - set(clean_strings))
    


main()