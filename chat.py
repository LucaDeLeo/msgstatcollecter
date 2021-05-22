import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from plots_functions import *
#import TXTloader

plt.style.use('seaborn')

#chat = open(TXTloader.TXT[0], "r", encoding="utf-8")
chat = open('demo.txt', "r", encoding="utf-8")


#----Save-the-usernames-----------
users = {"System Messages": [0]}
#----Everyone-username------------
users.update( {"Total": [0,[],[],[],[],[],[],[]] } )


#----Counting-Days-and-menssajes--
dias = []
days_total = 0
msgs_total = 0
day_messages = 0


#----Messages-Overtime------------Dias vs cantidad de mensajes
#users[][1] Dias en el que se cuentan la cantidad de mensajes users[][2]
#users[][2] Cantidad de mensajes para cada dia en users[][1]
#----Plot-messages-variables------Dias vs Horario
#users[][3] Dias en los que se mandaron mensajes
#users[][4] Horario en el que se mando un mensaje
#----Messages-Per-Hour-variables--Hora vs cantidad de mensajes
#users[][5] Cantidad de mensajes mandados en cierta hora [6]
#users[][6] La hora en la que se mandan mensajes de [5]
#---Words-per-text------------
#users[][7] La cantidad de palabras por linea para cada usuario
#---------------------------------


for line in chat:
    part = line.partition(" - ")
    try:
        date = datetime.datetime.strptime(part[0], "%m/%d/%y, %I:%M %p")
    except ValueError as err:
        continue

    #--------Save-the-usersnames-and-count-messages
    sender = part[2].partition(":")[0]
    if '\n' not in sender:
        users.update({sender: users.setdefault(sender, [0,[],[],[],[],[],[],[]])})
        users[sender][0] = users[sender][0] + 1
    else:
        users.update({"System Messages": users.get("System Messages")[0] + 1})

    #---------Counting-Days-----------------
    day = (date.year, date.month, date.day)
    msgs_total += 1
    if not dias:
        dias.append([day,0])
    if dias[-1][0] != day:
        dias[-1][1] = day_messages
        dias.append([day,0])
        day_messages = 0
        days_total += 1
    else:
        day_messages += 1

    #----------Messages-Overtime------------
    DMO = date.date()
    if '\n' not in sender:
        if not(DMO in users[sender][1]):
            users[sender][1].append(DMO)
            users[sender][2].append(0)
        users[sender][2][users[sender][1].index(DMO)] += 1

    if not(DMO in users["Total"][1]):
        users["Total"][1].append(DMO)
        users["Total"][2].append(0)
    users["Total"][2][users["Total"][1].index(DMO)] += 1

    #----Plot-messages-variables------
    if '\n' not in sender:
        users[sender][3].append(date.date())
        users[sender][4].append(datetime.datetime(2000,1,1,date.hour,date.minute))

    users["Total"][3].append(date.date())
    users["Total"][4].append(datetime.datetime(2000,1,1,date.hour,date.minute))


    #----------Messages-Per-Hour------------
    hMPH = datetime.datetime(2000,1,1,date.hour)

    if '\n' not in sender:
        if not(hMPH in users[sender][6]):
            users[sender][6].append(hMPH)
            users[sender][5].append(0)
        users[sender][6] = sorted(users[sender][6])
        users[sender][5][users[sender][6].index(hMPH)] += 1

    if not(hMPH in users["Total"][6]):
        users["Total"][6].append(hMPH)
        users["Total"][5].append(0)
    users["Total"][6] = sorted(users["Total"][6])
    users["Total"][5][users["Total"][6].index(hMPH)] += 1

    #---------Words-per-text------------- -
    if '\n' not in sender:
        WordsText=part[2].partition(":")[2]
        Words=WordsText.split()
        WPT=len(Words)
        users[sender][7].append(WPT)
        users["Total"][7].append(WPT)
    #---------------------------------------

#Plot_TotalMessagesOvertime(users,(1,3))

#Plot_MessagesOvertime(users,(1,3))

#Plot_DayVsHour(users,(1,3))

#Plot_MessagesPerHour(users,(1,3))

#Plot_PiePorsentage(users,msgs_total)

#Plot_WordsPerText(users)

#print(msgs_total / len(dias))
#print(msgs_total)
#print(dias2)
