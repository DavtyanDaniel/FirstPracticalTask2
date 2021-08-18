def split(string: str, delimiters=' ') -> list:
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)
    return result


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



