import collections
import math

number = int(input())
main_list = []
main_dict = {}
counter = 0
for i in range(number):
    text = input().split()
    for j in text:
        if j not in main_dict.keys():
            main_dict[j] = counter
            counter += 1
    this_list = collections.Counter(text)
    main_list.append(this_list)

for i in range(len(main_list)):
    for j in main_dict.keys():
        if j not in main_list[i].keys():
            main_list[i][j] = 0

for i in range(len(main_list)):
    keys = sorted(main_list[i].keys())
    my_dict = {}
    for j in keys:
        my_dict[j] = main_list[i][j]
    main_list[i] = my_dict

for i in range(len(main_list)):
    answer = -1
    answer_max = -1
    for j in range(len(main_list)):
        res = 0
        if i != j:
            first_list = list(main_list[i].values())
            second_list = list(main_list[j].values())
            for k in range(len(first_list)):
                res += first_list[k] * second_list[k]
            first = 0
            for value in list(main_list[i].values()):
                first += value ** 2
            first = math.sqrt(first)
            second = 0
            for value in list(main_list[j].values()):
                second += value ** 2
            second = math.sqrt(second)
            res = res / (first * second)

            if res > answer_max:
                answer_max = res
                answer = j

    print(answer + 1)

# for i in range(len(main_list)):
#     answer = -1
#     answer_max = -1
#     for j in range(len(main_list)):
#         res = 0
#         if i != j:
#             for key in main_list[i].keys():
#                 if key in main_list[j].keys():
#                     res += main_list[i][key] * main_list[j][key]
#             first = 0
#             for value in main_list[i].values():
#                 first += value ** 2
#             first = math.sqrt(first)
#             second = 0
#             for value in main_list[j].values():
#                 second += value ** 2
#             second = math.sqrt(second)
#             res = res / (first + second)
#
#             if res > answer_max:
#                 answer_max = res
#                 answer = j
#
#     print(answer + 1)
