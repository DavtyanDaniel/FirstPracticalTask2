import stars_filtering
import parser


data = parser.opening_and_parsing_file()
for i in data:
    print(i[0])

filtered_stars = stars_filtering.filtering_by_coordinates(data)

print(filtered_stars)

