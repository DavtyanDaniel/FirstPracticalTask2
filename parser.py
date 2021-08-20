"""
This module is for functions that related to file opening and creating.
"""

from datetime import datetime

import stars_filtering


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


def opening_and_parsing_file(file_name, square_w_l, square_w_r, square_h_l, square_h_r):
    """
    Function not only opening and parsing the file but also filtering them with the help
    of filtering_by_coordinates function.
    """

    with open(file_name, 'r') as tsv_file:
        if data_file_has_an_comments(tsv_file):
            next(tsv_file)

        result = []

        for row in tsv_file:
            list_with_rows = row.split('\t')
            data = stars_filtering.filtering_by_coordinates(list_with_rows,
                                                            square_w_l,
                                                            square_w_r,
                                                            square_h_l,
                                                            square_h_r)
            if data is not None:
                result.append(data)

    return result


def writing_filtered_data_in_csv_file(filtered_stars: list):

    with open(f'{datetime.now()}.csv', 'w') as csv_file:
        header = "RA, DEC, ID, Magnitude, Dis_from_gv_point\n"
        csv_file.write(header)

        for i in filtered_stars:
            row_data = str(i[0]) + ',' + \
                       str(i[1]) + ',' + \
                       str(i[2]) + ',' + \
                       str(i[3]) + ',' + \
                       str(i[4]) + ',' + '\n'
            csv_file.write(row_data)
