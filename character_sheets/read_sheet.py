
# read a character sheet text-file
# and parse the data into a format that program's can use 
# read line-by-line 

def read_file(filename):
    # parse the contents of the file
    pass 


import sys
def main():
    # from the terminal , take value from the line
    if len(sys.argv) < 2 : 
        # not enough command line arguments
        filename = input(" name of file to read from?: ")
    else: # the file name is on the command line
        filename = sys.argv[1]
    # print("length of argv: ", len(sys.argv))
    read_file(filename)

main()