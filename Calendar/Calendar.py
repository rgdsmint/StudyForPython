import time


class Calendar:
    def __init__(self, targetDate, nowDate):
        self.targetDate = targetDate
        self.nowDate = nowDate
        self.JAN = 31
        self.FEB_unl = 28
        # 非闰年
        self.FEB_l = 29
        # 闰年
        self.MAR = 31
        self.APR = 30
        self.MAY = 31
        self.JUN = 30
        self.JUL = 31
        self.AUG = 31
        self.SEPT = 30
        self.OCT = 31
        self.NOV = 30
        self.DEC = 31
        self.division(self.targetDate, self.nowDate)
        days = self.calculation(self.t_year, self.t_month, self.t_day, 
                         self.n_year, self.n_month, self.n_day)
        print(days)
    def division(self, targetDate, nowDate):
        self.t_year = (int)(targetDate[0:4])
        self.t_month = (int)(targetDate[5:7])
        self.t_day = (int)(targetDate[8:10])

        self.n_year = (int)(nowDate[0:4])
        self.n_month = (int)(nowDate[5:7])
        self.n_day = (int)(nowDate[8:10])

    def calculation(self, t_year, t_month, t_day, n_year, n_month, n_day):
        days = 0
        if t_year == n_year:
            if t_month == n_month:
                if t_day == n_day:
                    pass
                elif t_day >= n_day:
                    days = t_day - n_day
                else:
                    pass
            elif t_day >= n_day:
                pass
            else:
                pass
        elif t_day >= n_day:
            pass
        else:
            pass
        return days
            

def main():
    tad = "2018-09-08"
    nod = time.strftime('%Y-%m-%d')
    cl = Calendar(tad, nod)


if __name__ == '__main__':
    main()