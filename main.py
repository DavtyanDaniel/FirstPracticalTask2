import datetime
import stars_filtering
import parser
import my_functions


def main(file_path_or_name: str= my_functions.interface_for_config_file("FileName"),
         ra: float= my_functions.interface_for_config_file('RA'),
         dec: float= my_functions.interface_for_config_file('DEC'),
         fov_h: float= my_functions.interface_for_config_file('Fov_h'),
         fov_v: float= my_functions.interface_for_config_file('Fov_v'),
         number_of_stars: float = my_functions.interface_for_config_file('NumberOfStars')):

    max_ra = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)[0]
    min_ra = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)[1]
    min_dec = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)[2]
    max_dec = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)[3]

    filtered_stars = parser.opening_and_parsing_file(file_path_or_name, max_ra, min_ra, min_dec, max_dec)
    filtered_stars = my_functions.sort(filtered_stars)
    filtered_stars = stars_filtering.distance_calculation(filtered_stars, ra, dec, number_of_stars)
    filtered_stars = my_functions.sort(filtered_stars)

    for i in filtered_stars:
        print(i)



if __name__ == "__main__":
    main()
