import my_functions


def data_file_has_an_comments(tsv_file) -> bool:
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
    file_name = my_functions.interface_for_config_file('FileName')

    with open(file_name, 'r') as tsv_file:
        if data_file_has_an_comments(tsv_file):
            next(tsv_file)

        data = []
        included_cols = [5, 6, 7, 22]
        # Adding all data to list
        for row in tsv_file:
            reader = row.split('\t')
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

        return inner_list


