
def solve(input_list):
    sorted_list = sorted(input_list, reverse=True)
    k, j, m = sorted_list[0], 0, 0
    idx = 1
    while idx < len(sorted_list):
        if not j:
            if input_list.index(k) > input_list.index(sorted_list[idx]):
                j = sorted_list[idx]
                idx += 1
            else:
                k = sorted_list[idx]
                idx += 1
        if not m:
            if input_list.index(j) > input_list.index(sorted_list[idx]):
                m = sorted_list[idx]
                break
            else:
                j = sorted_list[idx]
                idx += 1

    return k + j + m





def test_solve():
    test_cases_ans = {
        'inputs': [
            [1, 3, 2, 8],
        ],
        'outputs': [
            [12]
        ]

    }
    passed = 1
    for idx, _input in enumerate(test_cases_ans['inputs']):
        assert solve(_input) == \
               test_cases_ans['outputs'][idx]
        print('\npassed: ', passed)
        passed += 1