

number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def number_to_int(roman):
    i, sum_value = 0, 0
    element = len(roman)

    while i < element:
        if i != element - 1 and number[roman[i]] < number[roman[i + 1]]:
            sum_value += number[roman[i + 1]] - number[roman[i]]
            i += 2
            # continue
        else:
            sum_value += number[roman[i]]
        i += 1
    return sum_value


# Considering a valid inputs
roman_input = input("Enter a valid inputs: \n")  # "MCMIV"
_number = number_to_int(roman_input)

print(f"Integer form of Roman Numeral is {_number}")
