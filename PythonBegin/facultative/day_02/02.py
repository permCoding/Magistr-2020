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
    # result = []
    # for line in lines:
    #     if len(line) > 0:
    #         result.append(line)
    # return result

def print_lines(lines):
    for line in lines:
        print(line)


lines = read_lines('01.py')
print_lines(lines)