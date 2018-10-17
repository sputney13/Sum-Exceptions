import os.path

def add_file_lines(filename):
    check = os.path.isfile(filename)
    if check == False:
        raise FileNotFoundError("File must exist on machine.")
    totalsum = 0
    testfile = open(filename, "r")
    lines_list = testfile.readlines()
    for line in lines_list:
        try:
            val = int(line)
        except ValueError:
            continue
        totalsum += val
    return totalsum
