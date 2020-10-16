def read_lines(name_file):
    '''
    прочитать файл, вернуть список строк
    '''
    file = open(name_file, 'r')
    new_line = chr(10)
    text = file.read()
    lines = text.split(new_line)
    file.close()
    return list(filter(lambda line: len(line) > 0, lines))


def print_lines(lines):
    for i in range(len(lines)):
        print(i+1, '\t', lines[i])

