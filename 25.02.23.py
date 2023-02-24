import math
import requests
import time

EarthMass = 5.97600 * (pow(10,24))
MKSmass = 420 * (pow(10,3))
G = 6.6743 * (pow(10,-11))

while 'TaskChoice' not in globals():
    try: 
        TaskChoice = int(input('Выберите задачу для расчета. Введите 0 для расчета с вводом массы и расстояние и 1 для рассчета силы гравитаионного взаимодейсвтия с МКС:  '))
        if (TaskChoice != 0) and (TaskChoice != 1):
            print('Введите 0 или 1')
            del TaskChoice
    except:
        print('Вы ввели некоректное значение, введите 0 или 1')


if TaskChoice == 0: 
    while 'Mass' not in globals():
        try: 
            Mass = float(input('Введите массу обьекта(масса луны 730000000000000000000000): '))
        except:
            print('Вы ввели некоректное значение')
    while 'Distance' not in globals():
        try: 
            Distance = float(input('Введите расстояние между обьектами(расстояние до луны 384000000): '))
        except:
            print('Вы ввели некоректное значение')
else:
    timestamp = time.time()
    print("Сейчас: "+str(time.localtime(timestamp)[3])+":"+str(time.localtime(timestamp)[4])+" "+str(time.localtime(timestamp)[2])+"."+str(time.localtime(timestamp)[1])+"."+str(time.localtime(timestamp)[0]))
    while time.localtime(timestamp)[3] != 12:
        timestamp = timestamp - 3600
    Mass = MKSmass
    MKSparametrs = str(requests.get("https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+str(timestamp)).json())
    altitude = str()
    for i  in range (0,7):
        altitude +=   MKSparametrs[MKSparametrs.find("altitude") + 11 + i]
    altitude = float(altitude)
    print('Высота МКС в '+str(time.localtime(timestamp)[3])+":"+str(time.localtime(timestamp)[4])+" "+str(time.localtime(timestamp)[2])+"."+str(time.localtime(timestamp)[1])+"."+str(time.localtime(timestamp)[0])+" была ", altitude, "километра")
    Distance = altitude * pow(10,3)

F = G*Mass*EarthMass/(pow(Distance,2))

ExponentCount = 0
while F >= 100:
    F = F/10
    ExponentCount += 1

print("Сила гравитационного взаимодействия равна: ", round(F,2)," * 10 ^",ExponentCount)



