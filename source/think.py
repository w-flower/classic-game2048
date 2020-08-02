from time import sleep
import random


def think(get, lst):
    '''思考列表并改变'''

    if get == 'w':  #向上
        for _ in range(3):  #两次执行
            un_temp_enumerate = [
                int('-' + str(i)) for i in range(1,
                                                 len(lst) + 1)
            ]  #倒序索引
            for j, i in zip(un_temp_enumerate, lst[::-1]):  # 从下往上遍历行
                '''
                    0 2 0 0 --> [0, 2, 0, 0] 结果    --> [8, 2, 4, 0]
                    4 0 0 0 --> [4, 0, 0, 0] 4和4叠加, 0不动, 继续向上移
                    0 0 4 0 ....             4向上移, 0不动
                    4 0 0 0 --> [4, 0, 0, 0] 4向上移, 0不动
                    '''
                for cout, k in enumerate(i):  #遍历每一个数据
                    try:  #最后一格是不能索引[j-1]的, 加上错误判断
                        if k == 0:
                            continue
                        if lst[j - 1][cout] == k or lst[
                                j - 1][cout] == 0:  #如果上一格是0或者单位相等的话就上移
                            lst[j - 1][cout] += k  # or lst[j-1][cout] *= 2
                            lst[j][cout] = 0  # 这一格清零
                    except:
                        break
    elif get == 's':  #向下
        for _ in range(3):  #两次执行, 避免遗漏
            for j, i in enumerate(lst):  # 从下往上遍历行
                for cout, k in enumerate(i):
                    try:
                        if k == 0:
                            continue
                        if lst[j + 1][cout] == k or lst[j + 1][cout] == 0:
                            lst[j + 1][cout] += k
                            lst[j][cout] = 0
                    except:
                        break
    elif get == 'a':  #向左
        '''
            将每一格分别执行即可
            '''

        un_temp_enumerate = [
            int('-' + str(i)) for i in range(1,
                                             len(lst) + 1)
        ]  #倒序索引
        for _ in range(3):
            for cout, i in enumerate(lst):
                for j, k in zip(un_temp_enumerate, i[::-1]):
                    try:
                        if k == 0:
                            continue

                        if lst[cout][j - 1] == k or lst[cout][
                                j - 1] == 0:
                            lst[cout][j - 1] += k
                            # print('{}放到了{}上'.format((cout, j), (cout, j-1)))
                            lst[cout][j] -= k
                    except:
                        break
    elif get == 'd':  #向右

        for _ in range(3):
            for cout, i in enumerate(lst):
                for j, k in enumerate(i):
                    try:
                        if k == 0:
                            continue
                        if lst[cout][j + 1] == k or lst[cout][j + 1] == 0:
                            lst[cout][j + 1] += k
                            lst[cout][j] -= k
                    except:
                        break
    else:
        print("pass")
        return False
    return lst


def add(lst, add):  # 新增格子
    '''
        新增格子
        return: 失败返回Flase, 成功返回True
        '''
    for i in range(add):
        have_zero = []

        for j, i in enumerate(lst):
            for tempcout, temp in enumerate(i):
                if temp == 0:
                    have_zero.append(str(j) + ' ' + str(tempcout))
        try:
            xy = have_zero[random.randint(0, len(have_zero) - 1)]
            lst[int(xy.split(' ')[0])][int(
                xy.split(' ')[1])] = [2, 2, 0, 2, 4, 2, 2][random.randint(0, 5)]
        except:
            return False
    return lst