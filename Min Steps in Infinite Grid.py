from typing import List


def cal_number_of_steps(x_coordinates: List[int], y_coordinates: List[int]) -> int:
    if len(x_coordinates) == 1:
        return 0
    number_of_steps, x_pos, y_pos = 0, x_coordinates[0], y_coordinates[0]
    for x, y in zip(x_coordinates[1:], y_coordinates[1:]):
        x_needed, y_needed = abs(x_pos - x), abs(y_pos - y)
        number_of_steps += max(x_needed, y_needed)
        x_pos, y_pos = x, y
    return number_of_steps


def test_cal_number_of_steps():
    test_cases_ans = {
        'inputs': [([0, 1, 1], [0, 1, 2]),
                   ([9, 7], [-3, 9]),
                   ([-4, -6], [4, 6])],
        'outputs': [2, 12, 3]

    }
    passed = 1
    for idx, _input in enumerate(test_cases_ans['inputs']):
        assert cal_number_of_steps(_input[0], _input[1]) == test_cases_ans['outputs'][idx]
        print('\npassed: ', passed)
        passed += 1

