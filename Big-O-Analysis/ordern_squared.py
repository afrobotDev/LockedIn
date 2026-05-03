def does_name_exist(first_names, last_names, full_name):
    if len(first_names) == 0 or len(last_names) == 0:
            return None
    for first in first_names:
        for last in last_names:
            name = ' '.join((first, last))
            if name == full_name:
                return True

    return False

