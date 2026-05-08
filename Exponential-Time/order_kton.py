def letter_combinations(digits):
    if len(digits) == 0:
        return []

    result = [""]
    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")

        letters = digit_to_letters[digit]
        new_result = []
        for prefix in result:
            for letter in letters:
                new_result.append(prefix + letter)

        result = new_result
    return result


digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

