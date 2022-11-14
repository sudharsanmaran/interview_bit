
def find_max_triplet_sum(input_list):

    length = len(input_list)
    small_max, max_num, max_sum = 0, 0, 0
    for i in range(1, length):

        for j in range(i):
            if input_list[i] > input_list[j]:
                small_max = max(small_max, input_list[j])
        if small_max == 0:
            continue

        for k in range(i+1, length):
            if input_list[i] < input_list[k]:
                max_num = max(max_num, input_list[k])
        if max_num == 0:
            small_max = 0
            continue

        max_sum = max(max_sum, (small_max + input_list[i] + max_num))
        small_max, max_num = 0, 0
    return max_sum


def test_solve():
    test_cases_ans = {
        'inputs': [
            # [1, 3, 2, 8],
            # [2, 5, 3, 1, 4, 9],
            # [1, 2, 3],
            # [ 16542, 4834, 31116, 4640, 29659, 22705, 9931, 13978, 2307, 31674, 22387, 5022, 28746, 26925, 19073, 6271, 5830, 26778, 15574 ],
            [30525, 12550, 17470, 331, 31924, 28351, 14334, 22926, 10911, 19738,
             16337],
        ],
        'outputs': [
            # 12,
            # 16,
            # 6,
            # 79332,
            61944,
        ]


    }
    passed = 1
    for idx, _input in enumerate(test_cases_ans['inputs']):
        assert find_max_triplet_sum(_input) == \
               test_cases_ans['outputs'][idx]
        print('\npassed: ', passed)
        passed += 1
