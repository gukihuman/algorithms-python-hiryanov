def fence_color():
    """Return the colors of asked parts of the fence."""
    days = int(input())
    my_list = list()
    for i in range(days):
        my_list.append([]) # [start, end, iteration, color]
        my_list[i].append(int(input()))
        my_list[i].append(int(input()))
        my_list[i].append(int(input()))
    checkings = int(input())
    colors = list()
    finded = 0
    for i in range(checkings):
        checking = int(input())
        for k in range(len(my_list)):
            if checking > my_list[k][0]:
                if checking < my_list[k][1]:
                    color = my_list[k][2]
                    finded = 1
        if finded == 1:
            colors.append(color)
        else:
            colors.append(0)
        finded = 0
    final_str = str()
    for i in range(len(colors)):
        final_str += ''.join(str(colors[i]))
        final_str += ' '
    final_str = final_str[:-1]
    return final_str

print(fence_color())