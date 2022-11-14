from typing import List


def cal_number_of_lights(array: List[int], power: int) -> int:
    skip_count, num_of_lights, length, idx, bulb = power, 0, len(array), 0, \
                                                   False
    while idx < length:
        max_idx = min(idx + power - 1, length - 1)
        min_idx = max(idx - power + 1, 0)
        for i in range(max_idx, min_idx - 1, -1):
            if array[i] == 1:
                bulb = True
                break
        if not bulb:
            return -1
        num_of_lights += 1
        bulb = False
        idx = max_idx
        idx += power
    return num_of_lights


def test_cal_number_of_lights():
    test_cases_ans = {
        'inputs': [
            ([0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 3),
            ([0, 0, 1, 0, 1, 1, 0, 1, 0, 0], 3),
            ([0, 0, 1, 0, 1, 1, 0, 0, 0, 0], 3),
            ([0, 1, 0, 0, 1, 0, 0, 1], 2),
            ([0, 1, 0, 1, 1, 0, 0, 1], 2),
            ([ 1, 1, 1, 1 ], 3),
            ([1, 1, 0, 0, 1, 1], 1),
            ([ 1, 1, 1 ], 6),
            ([ 1, 1, 0, 0, 1, 1 ], 1)
        ],
        'outputs': [
            2,
            2,
            2,
            3,
            3,
            1,
            -1,
            1,
            -1,
        ]

    }
    passed = 1
    for idx, _input in enumerate(test_cases_ans['inputs']):
        assert cal_number_of_lights(_input[0], _input[1]) == \
               test_cases_ans['outputs'][idx]
        print('\npassed: ', passed)
        passed += 1
