class Record(object):
    def __init__(self):
        super().__init__()
        self.win = 0
        self.down = 0
        self.robot_win = 0
        self.robot_down = 0
        try:
            with open("record.txt", "r", encoding="utf-8") as f:
                tp = f.read()
            self.win = int(tp.split("\n")[0])
            self.down = int(tp.split("\n")[1])
            self.robot_win = int(tp.split("\n")[2])
            self.robot_down = int(tp.split("\n")[3])
        except:
            with open("record.txt", "w", encoding="utf8") as f:
                f.write("{}\n{}\n{}\n{}\n ".format(0, 0, 0, 0))
                print("战绩获取失败, 已重置")


    def record_win(self):
        self.win += 1
        with open("record.txt", "r+") as f:
            readall = f.readlines()
            readall[0] = str(int(readall[0].split("\n")[0]) + 1) + "\n"
        with open("record.txt", "w+") as f:
            for i in readall:
                f.write(i)

    def record_down(self):
        self.down +=1
        with open("record.txt", "r+") as f:
            readall = f.readlines()
            readall[1] = str(int(readall[1].split("\n")[0]) + 1) + "\n"
        with open("record.txt", "w+") as f:
            for i in readall:
                f.write(i)
    def record_robot_win(self):
        self.robot_win += 1
        with open("record.txt", "r+") as f:
            readall = f.readlines()
            readall[2] =  str(int(readall[2].split("\n")[0]) + 1) + "\n"
        with open("record.txt", "w+") as f:
            for i in readall:
                f.write(i)

    def record_robot_down(self):
        with open("record.txt", "r+") as f:
            readall = f.readlines()
            readall[3] = str(int(readall[3].split("\n")[0]) + 1) + "\n"
        with open("record.txt", "w+") as f:
            for i in readall:
                f.write(i)

    def record_time(self, time):
        with open("record.txt", "r+") as f:
            readall = f.readlines()
            if readall[4] != " ":
                readall = readall[0] + readall[1] + readall[2] + readall[3] + readall[4] + " " + str(time)
            else:
                readall = readall[0] + readall[1] + readall[2] + readall[3] + str(time)
        with open("record.txt", "w+") as f:
            for i in readall:
                f.write(i)

    def max_time(self):
        with open("record.txt", "r") as f:
            readall = f.readlines()
        try:
            readall = readall[4]
            readall = readall.split(" ")

            mini = readall[0]
            for i in readall:
                if i < mini:
                    mini = i
            return mini if mini != "" else False

        except:
            return False