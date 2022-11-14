
def plus_one(input_list):
    given_number, result_list, digits_count = 0, [], 1
    while input_list:
        digit = input_list.pop()
        given_number += digit * digits_count
        digits_count *= 10

    given_number += 1

    while given_number:
        digit = given_number % 10
        result_list.insert(0, digit)
        given_number //= 10
    return result_list


def v2_plus_one(input_list):
    # remove leading zero
    while input_list and input_list[0] == 0:
        input_list.remove(0)
    remainder, idx = 0, len(input_list) - 1
    for digit in reversed(input_list):
        if remainder and digit > 8:
            idx = change_digit_to_zero(idx, input_list)
            continue
        elif not remainder and digit > 8:
            remainder += 1
            idx = change_digit_to_zero(idx, input_list)
            continue
        input_list[idx] = digit + 1
        break
    if len(input_list) == 0:
        input_list.append(1)
    return input_list


def change_digit_to_zero(idx, input_list):
    input_list[idx] = 0
    if idx == 0:
        input_list.insert(0, 1)
    idx -= 1
    return idx


def test_plus_one():
    test_cases_ans = {
        'inputs': [
            [0, 1, 2, 3],
            [0, 1, 2, 0],
            [0],
            [9, 9, 9, 9, 9],
            [1, 9, 9, 9, 9, 9, 9],
            [0, 6, 0, 6, 4, 8, 8, 1],
        ],
        'outputs': [
            [1, 2, 4],
            [1, 2, 1],
            [1],
            [1, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [6, 0, 6, 4, 8, 8, 2],
        ]

    }
    passed = 1
    for idx, _input in enumerate(test_cases_ans['inputs']):
        assert v2_plus_one(_input) == \
               test_cases_ans['outputs'][idx]
        print('\npassed: ', passed)
        passed += 1
