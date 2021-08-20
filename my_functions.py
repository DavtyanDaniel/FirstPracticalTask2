import configparser


def interface_for_config_file(name_of_parameter: str):
    """
    This function is smth  like API for input.ini file
    """

    config = configparser.ConfigParser()
    config.read('input.ini')
    if name_of_parameter == "FileName":
        parameter = config['FileName']['FileName']
        return parameter
    else:
        parameter = config['Parameters'][name_of_parameter]
    return float(parameter)


def sort(sub_list: list) -> list:
    """
    Sorting by last element of list (bubble sort)
    """
    list1 = len(sub_list)
    for i in range(0, list1):
        for j in range(0, list1 - i - 1):
            if sub_list[j][-1] > sub_list[j + 1][-1]:
                tempo = sub_list[j]
                sub_list[j] = sub_list[j + 1]
                sub_list[j + 1] = tempo
    return sub_list



