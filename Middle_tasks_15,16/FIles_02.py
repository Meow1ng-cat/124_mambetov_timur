import csv
import time

with open('rows_300.csv', mode='w', newline='') as cvsfile:
    timewriter = csv.writer(cvsfile, delimiter=';')
    for i in range(0, 300):
        newline = [str(i), str(time.strptime(time.asctime())[2])+"."+str(time.strptime(time.asctime())[1])+"."+
                   str(time.strptime(time.asctime())[0])+" "+str(time.strptime(time.asctime())[3])+":"+str(time.strptime(time.asctime())[4]),
                   str(time.strptime(time.asctime())[5]), str(round((time.time() * 1000) % 1000))]
        timewriter.writerow(newline)
        time.sleep(0.01)
    