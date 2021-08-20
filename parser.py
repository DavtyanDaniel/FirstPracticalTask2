import my_functions
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
    Function is opening, parsing file, and filtering them with the help
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


if __name__ == "__main__":
     ra = my_functions.interface_for_config_file("RA")
     dec = my_functions.interface_for_config_file("DEC")
     fov_հ = my_functions.interface_for_config_file('Fov_h')
     fov_v = my_functions.interface_for_config_file("Fov_v")

     square = stars_filtering.computing_range_of_square(ra, dec, fov_հ, fov_v)

     data = opening_and_parsing_file('337.all.tsv', square[0], square[1], square[2], square[3])
     for i in data:
         print(i)

