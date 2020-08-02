# 2048

这是一款2048小游戏 
游戏规则请自行搜索, 此小游戏模仿网络自创

这款游戏有许多瑕疵, 求各位大佬指出

**作者**

feilong-hello(邮箱: 1040778649@qq.com)

**我为什么开发这个游戏**

因为我是一个新手, 我想训练一下我的算法, 起初只是控制台程序, 但是后来我又想练练界面编程,  于是就变成了GUI

开始我的愿望是这样的:
```python
import 2048
win = 2048(aim=1024, side_length=4, add=1)
win.start()
```
可是失败了QAQ


## 如何开始
**pip**

```shell
pip install wxpython
cd 2048
python Calculator.py
```

## 所用的库
- random 
- time
- os
- wxpython(wx)

## 用的软件
- wxformbuider
- python3.8.3

## 文件说明
- img:图片
- source:我也不知道是什么, 乱写的.
    - CalculatorFrame : 主菜单
    - think : 2048计算
    - record : 战绩
- Calculator : 主文件

## 功能:
- 战绩:通过本地record.txt存储
- 简陋的日志:bug.txt
- 2048主功能
- 难度调整
- 人机对战(开发中)

## 怎么玩
### 目标
获得2048方块(可以调整为其他方块)

### 操作
- w: 方块向上
- a: 方块向左
- s: 方块向下
- d: 方块向右



我会一直勤快的更新的~~