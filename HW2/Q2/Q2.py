import math
import collections


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")


class Methods:
    @staticmethod
    def left_index(points):
        minn = 0
        for i in range(1, len(points)):
            if points[i].x < points[minn].x:
                minn = i
            elif points[i].x == points[minn].x:
                if points[i].y > points[minn].y:
                    minn = i
        return minn
    @staticmethod
    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - \
              (q.x - p.x) * (r.y - q.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
    @staticmethod
    def convexHull(points, n):
        if n < 3:
            return
        l = Methods.left_index(points)
        hull = []
        p = l
        q = 0
        while (True):
            hull.append(p)
            q = (p + 1) % n
            for i in range(n):
                if (Methods.orientation(points[p],
                                points[i], points[q]) == 2):
                    q = i
            p = q
            if p == l:
                break
        return_list = []
        for each in hull:
            return_list.append(points[each])
        return return_list


city, country = [int(y) for y in input().split()]
country_points_dict = dict()
for i in range(city):
    this_city_country, x, y = [float(y) for y in input().split()]
    if this_city_country in country_points_dict.keys():
        country_points_dict[this_city_country].append(Point(x, y))
    else:
        country_points_dict[this_city_country] = [Point(x, y)]

country_convex_hull_dict = dict()
for key in country_points_dict.keys():
    country_convex_hull_dict[key] = Methods.convexHull(country_points_dict[key], len(country_points_dict[key]))

country_average_dict = dict()
for key in country_convex_hull_dict.keys():
    this_key_list = country_convex_hull_dict[key]
    x_sum = 0
    y_sum = 0
    for node in this_key_list:
        x_sum += node.x
        y_sum += node.y
    country_average_dict[key] = [x_sum / len(this_key_list), y_sum / len(this_key_list)]

result = ""
k = int(input())
for i in range(k):
    x, y = [float(y) for y in input().split()]
    selected_country = -1
    max_distance = math.inf
    for key in country_average_dict.keys():
        x_diff = x - country_average_dict[key][0]
        y_diff = y - country_average_dict[key][1]
        if x_diff * x_diff + y_diff * y_diff < max_distance:
            max_distance = x_diff * x_diff + y_diff * y_diff
            selected_country = key
    result += str(int(selected_country)) + " "
    country_points_dict[selected_country].append(Point(x, y))

result = result.strip()
print(result)

country_convex_hull_dict = dict()
for key in country_points_dict.keys():
    country_convex_hull_dict[key] = Methods.convexHull(country_points_dict[key], len(country_points_dict[key]))

country_convex_hull_dict = collections.OrderedDict(sorted(country_convex_hull_dict.items()))
country_convex_hull_dict = dict(country_convex_hull_dict)

for key in country_convex_hull_dict.keys():
    result = ""
    result += str(int(key)) + " "
    main_list = []
    for node in country_convex_hull_dict[key]:
        main_list.append([node.x, node.y])
    sorted_list = sorted(main_list, key=lambda coordinate: (coordinate[0], coordinate[1]))
    for i in sorted_list:
        result += "[" + "{:.2f}".format(i[0]) + ", " + "{:.2f}".format(i[1]) + "] "
    result = result.strip()
    print(result)
