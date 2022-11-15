import pandas as pd
import datetime
date_list = []
data = {
    "name":"",
    "state":"",
}
name = []
stat = []
class Csv:
    def __init__(self, info):
        self.date = datetime.datetime.now()
        self.date1 = self.date.strftime("%y%b%d")
        self.dic = info
        with open("log_dats.txt", mode="r") as file:
            self.check = file.read()

        self.tocsv()
    def tocsv(self):
        for name1, value in self.dic.items():
            stat.append(value)
            name.append(name1)

        for i in range(0,len(stat)):
            if stat[i] == 1:
                stat[i] = "yes"
            else:
                stat[i]= "no"

        data["name"] = name
        data["state"] = stat
        df = pd.DataFrame(data)
        name_file = f'attendance({self.date1}).csv'
        date_list.append(name_file)
        if name_file not in self.check:
            with open("log_dats.txt", mode="a") as file:
                file.write(name_file+"\n")
        df.to_csv(f'attendance({self.date1}).csv', index=False, header=True)