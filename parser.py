import configparser
import my_functions


def data_file_has_an_comments(tsv_file):
    """
    Checking if tsv or csv file has a comments
    """
    for row in tsv_file:
        if row[0] == '#':
            tsv_file.seek(0)
            next(tsv_file)
            return True
        else:
            return False


def opening_and_parsing_file():
    config = configparser.ConfigParser()
    config.read('input.ini')
    file_name = config['FileName']['FileName']

    with open(file_name, 'r') as tsv_file:
        if data_file_has_an_comments(tsv_file):
            next(tsv_file)

        # get the number of columns
        for line in tsv_file.readlines():
            array = my_functions.split(line, delimiters=',')
        num_of_columns = len(array)

        tsv_file.seek(0)
        if data_file_has_an_comments(tsv_file):
            next(tsv_file)

        data = []
        included_cols = [5, 6, 7]
        number_of_rows = 0
        for row in tsv_file:
            reader = my_functions.split(row, '\t')
            data.append(reader)

        number_of_rows = len(data)
        result = []
        inner_list = []
        # Adding needed columns
        for j in included_cols:
            i = 0
            while i < number_of_rows:
                result.append(data[i][j])
                i = i + 1
            inner_list.append(result)
            result = []

        for i in inner_list:
            print(i)

opening_and_parsing_file()


