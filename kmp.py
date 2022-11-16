import time

# function builds prefix array for KNP algo
def patterninator(pattern):
    length = 0  # length of the previous longest prefix suffix

    res = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            res[i] = length
            i += 1
        else:
            if length != 0:
                length = res[length - 1]
            else:
                res[i] = 0
                i += 1
    return res


def knp_algo(pattern, text):
    pref = patterninator(pattern)
    text_len = len(text)
    pattern_len = len(pattern)
    j = 0
    i = 0
    while (text_len - i) >= (pattern_len - j):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_len:
            # print("Found pattern at index " + str(i - j))
            j = pref[j - 1]
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = pref[j - 1]
            else:
                i += 1


# Avg Case
def test_1():
    time_0 = time.time_ns()
    for i in range(1, 100001):
        knp_algo("aaaabaaaaaaba", "aaba")
    time_1 = time.time_ns()
    print((time_1-time_0)/100000, ' ns')


# Best Case
def test_2():
    time_0 = time.time_ns()
    for i in range(1, 100001):
        knp_algo("kp", "kp")
    time_1 = time.time_ns()
    print((time_1 - time_0) / 100000, ' ns')


# Worst Case
def test_3():
    time_0 = time.time_ns()
    for i in range(1, 100001):
        knp_algo("kkkkkkkkkkkkkkkkp", "kp")
    time_1 = time.time_ns()
    print((time_1 - time_0) / 100000, ' ns')


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
