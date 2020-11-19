import csv


move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

answer_route = []
f_map = []


def load_map():
    with open('map/test.csv')as f:
        reader = csv.reader(f)
        for row in reader:
            tmp_row = [int(x) for x in row]
            f_map.append(tmp_row)
            # f_map.append(row.strip('\n'))
    # 墙壁设置为-1，通道设置为0，书架标号
    # print(f_map)


def update_route(route):
    global answer_route
    answer_route = []
    for i in route:
        answer_route.append(i)
    # print(answer_route)
    pass


# 深度优先搜索
def dfs(now_x, now_y, target, n, min_n, route):

    route.append((now_x, now_y))

    if f_map[now_x][now_y] == target and min_n > n:
        update_route(route)
        min_n = n
        return

    f_map[now_x][now_y] = -1
    
    for i in range(4):
        tmp_x = now_x + move_x[i]
        tmp_y = now_y + move_y[i]
        if 0 <= tmp_x < len(f_map) and 0 <= tmp_y < len(f_map[0]) and (f_map[tmp_x][tmp_y] == 0 or f_map[tmp_x][tmp_y] == target):
            # print(tmp_x, tmp_y, f_map[tmp_x][tmp_y])
            f_map[now_x][now_y] = -1
            dfs(tmp_x, tmp_y, target, n+1, min_n, route)
            f_map[now_x][now_y] = 0
            route.pop()

    return


def PathPlanning():
    load_map()
    # 获取位置、目标

    # 开始x， 开始y， 目标编号， 步骤
    dfs(0, 1, 3, 0, 9999999, [])
    print(answer_route)
    pass

# load_map()
PathPlanning()