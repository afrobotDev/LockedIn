def count_names(list_of_lists, target_name):
    total = 0
    for names_list in list_of_lists:
        for name in names_list:
            if target_name == name:
                total += 1
    return total
