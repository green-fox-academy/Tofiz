list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
need_to_contains = [4, 8, 12, 16]

def is_all_element_in_the_list(need_to_contains, list_of_numbers):
    for element in need_to_contains:
        if not element in list_of_numbers:
            return False
        return True
print(is_all_element_in_the_list(need_to_contains, list_of_numbers))