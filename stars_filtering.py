import math
import my_functions


def computing_range_of_square() -> tuple:
    ra = my_functions.interface_for_config_file('RA')
    dec = my_functions.interface_for_config_file('DEC')
    fov_h = my_functions.interface_for_config_file('Fov_h')
    fov_v = my_functions.interface_for_config_file('Fov_v')

    # square's weight left number
    square_w_l = ra - fov_h / 2
    # square's weight right number
    square_w_r = ra + fov_h / 2
    # square's height left number
    square_h_l = dec - fov_v / 2
    # square's height right number
    square_h_r = dec + fov_v / 2

    return square_w_l, square_w_r, square_h_l, square_h_r


def filtering_by_coordinates(data: list) -> list:
    """
    parameter args is an return value of computing_range_of_square() function
    """
    range_of_square = computing_range_of_square()
    filtered_stars = []
    for i in data:
        if (range_of_square[0] <= float(i[0]) <= range_of_square[1]) and \
                (range_of_square[2] <= float(i[1]) <= range_of_square[3]):
            filtered_stars.append(i)

    return filtered_stars


def checking_number_of_stars(filtered_stars: list) -> int:
    """
    checking if given number of stars bigger than filtered stars
    """
    number_of_stars = my_functions.interface_for_config_file('NumberOfStars')
    if len(filtered_stars) < number_of_stars:
        number_of_stars = len(filtered_stars)

    return int(number_of_stars)

# def distance_colculation(filtered_stars: list):
#     number_of_stars = checking_number_of_stars(filtered_stars)
#
#     result = []
#     while i < number_of_stars:
#         result.append(filtered_stars[i])
#
#         distance = math.sqrt(pow(float(filtered_stars[i][0]) - float(RA_DEC_TUPLE[0]), 2) +
#                              pow(float(filtered_stars[i][1]) - float(RA_DEC_TUPLE[1]), 2))
#         result[i].append(distance)
#         i = i + 1
#
# def euclidean_distance(filtered_stars: list):
#
#     distance =

