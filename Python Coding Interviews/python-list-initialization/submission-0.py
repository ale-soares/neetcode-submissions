from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    new_list = [0] * size

    for i, n in enumerate(new_list):
        if i == index:
            new_list[i] = value
    
    return new_list


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
