"""
This Module is for functions that related with stars filtering.
"""


def computing_range_of_square(ra, dec, fov_h, fov_v) -> tuple:
    """
    calculating the range of given FOV
    """
    # square's weight left number
    square_w_l = ra - fov_h / 2
    # square's weight right number
    square_w_r = ra + fov_h / 2
    # square's height left number
    square_h_l = dec - fov_v / 2
    # square's height right number
    square_h_r = dec + fov_v / 2

    return square_w_l, square_w_r, square_h_l, square_h_r


def filtering_by_coordinates(row: list,
                             square_w_l: float,
                             square_w_r: float,
                             square_h_l: float,
                             square_h_r: float) -> list:
    """
    filtering by ra/dec coordinates, for that we have to know the range of FOV, that's
    why in parameters list we have range of it.
    """
    included_cols = [5, 6, 7, 22]  # The columns that we needed(ra, dec, id, mag)

    if (square_w_l <= float(row[0]) <= square_w_r) and (square_h_l <= float(row[1]) <= square_h_r):
        content = list(row[k] for k in included_cols)
        return content


def checking_number_of_stars(filtered_stars: list, number_of_stars) -> int:
    """
    checking if given number of stars bigger than filtered stars
    """
    if len(filtered_stars) < number_of_stars:
        number_of_stars = len(filtered_stars)

    return int(number_of_stars)


def euclidean_distance(star: list, ra, dec) -> float:
    """
    Calculating by euclidean metric.
    """
    distance = ((float(star[0]) - ra) ** 2 + (float(star[1]) - dec) ** 2) ** 0.5
    return distance


def distance_calculation(filtered_stars: list, ra, dec, number_of_stars) -> list:
    """
    Function is calculating the distance of given number of stars
    """
    number_of_stars = checking_number_of_stars(filtered_stars, number_of_stars)
    i = 0
    result = []
    while i < number_of_stars:
        result.append(filtered_stars[i])
        distance = euclidean_distance(filtered_stars[i], ra, dec)
        result[i].append(distance)
        i = i + 1
    return result



