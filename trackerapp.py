from datetime import date
import csv

dt= date.today()
dt= dt.strftime("%d/%m/%y")

filename = "text.csv"
exp = []
stopped = False
with open(filename, 'a',newline="") as file:
    csvwriter =csv.writer(file)
    while not stopped:
        xp = int(input("what the expenses are (type o value): "))
        if xp==0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
file.close()
print("your expenses today are, ", exp)
print("your total is", sum(exp))
