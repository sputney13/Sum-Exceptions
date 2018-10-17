import os.path

def main(filename):
    check_file_exists(filename)
    add_file_lines(filename)


def check_file_exists(filename):
    check = os.path.isfile(filename)
    if check == False:
        raise FileNotFoundError("File must exist on machine.")


def add_file_lines(filename):
    totalsum = 0
    testfile = open(filename, "r")
    lines_list = testfile.readlines()
    for val in lines_list:
        try:
            val = int(val)
        except ValueError:
            continue
        totalsum += val
    return totalsum
