import math

n = int(input())
q = int(input())
is_vertical = True

main_vector = [1] * n

for i in range(q):
    statement = input()
    if statement == "T":
        is_vertical = not is_vertical
    elif statement.startswith("dot"):
        dot_number = statement.split()[1:]
        if is_vertical:
            continue
        elif len(main_vector) != len(dot_number):
            continue
        else:
            dot_sum = 0
            for j in range(len(dot_number)):
                dot_sum += int(dot_number[j]) * main_vector[j]
            print(dot_sum)
    elif statement.startswith("out"):
        out_number = statement.split()[1:]
        k = int(out_number[-1])
        out_number = out_number[:len(out_number)-2]
        if not is_vertical:
            continue
        elif k > len(main_vector):
            continue
        else:
            new_list = []
            for j in out_number:
                new_list.append(main_vector[k-1] * int(j))
            main_vector = new_list
            is_vertical = False
    elif statement.startswith("cross"):
        cross_number = statement.split()[1:]
        if len(main_vector) != 3:
            continue
        else:
            x1 = main_vector[1] * int(cross_number[2]) - main_vector[2] * int(cross_number[1])
            x2 = main_vector[2] * int(cross_number[0]) - main_vector[0] * int(cross_number[2])
            x3 = main_vector[0] * int(cross_number[1]) - main_vector[1] * int(cross_number[0])
            cross_list = [x1, x2, x3]
            length = math.sqrt(x1**2 + x2**2 + x3**2)
            x1 = "{:.4f}".format(cross_list[0]/length)
            x2 = "{:.4f}".format(cross_list[1]/length)
            x3 = "{:.4f}".format(cross_list[2]/length)
            print(x1, x2, x3)
    elif statement.startswith("had"):
        had_number = statement.split()[1:]
        if len(main_vector) != len(had_number):
            continue
        had_list = []
        for j in range(len(main_vector)):
            had_list.append(main_vector[j] * int(had_number[j]))
        main_vector = had_list
    elif statement == "print":
        if is_vertical:
            for j in main_vector:
                print(j)
        else:
            print_string = ""
            for j in main_vector:
                print_string += str(j) + " "
            print_string = print_string.strip()
            print(print_string)
    elif statement.startswith("reset"):
        reset_number = statement.split()[1:]
        main_vector = [1] * int(reset_number[0])

