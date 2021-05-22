import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import TXTloader

plt.style.use('seaborn')

#chat = open(TXTloader.TXT[0], "r", encoding="utf-8")
chat = open('demo.txt', "r", encoding="utf-8")


#----Save-the-usernames-----------
users = {"System Messages": [0]}
#----Everyone-username------------
users.update( {"Total": [0,[],[],[],[],[],[]] } )


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
        users.update({sender: users.setdefault(sender, [0,[],[],[],[],[],[]])})
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

    #---------------------------------------


#----Plot-Total-Messages-Overtime

def Plot_TotalMessagesOvertime(users,graphs=[0]):
    # Podes elegir cuales y cuantos graficos queres con graphs, de 1 en adelante

    key = 0

    for num,usr in enumerate(users):


        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1
        if num in graphs and num != 0:

            days1 = users[usr][1]
            msg   = users[usr][2]

            l = (days1[-1]-days1[0]).days
            e = 11*l/(51*10)
            s = l/(51*10)
            b = e-s
            br = round(b,0)
            if s < 1:
                s = 0
            sr = round(s,0)
            br2 = round(b/2,0)
            cota = 0
            msg2 = []
            days2 = []
            msg3 = []
            days3 = []

            for i in range(l):
                daycomp=days1[0]+datetime.timedelta(days=i)
                cota+=1
                if daycomp in days1:
                    msg2.append(msg[days1.index(daycomp)])
                else:
                    msg2.append(0)
                if cota==br+sr:
                    suma=0
                    for j in range(cota):
                        suma=suma+msg2[i-j]

                    days3.append(days1[0]+datetime.timedelta(days=i-br2))
                    msg3.append(suma/cota)
                    cota=0

            fig, ax =plt.subplots()
            ax.set(title="Total Messages Overtime "+ usr)
            ax.bar(days3,msg3,width=datetime.timedelta(days=br))
            fig.autofmt_xdate()

            ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')
            #plt.tight_layout()
            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.show()

#----Plot-Messages-Overtime----

def Plot_MessagesOvertime(users,graphs=[0]):#(msg,days):


    key = 0
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            key = 1
            graphs = [num]
        if num in graphs and num != 0:
            days=users[usr][1]
            msg=users[usr][2]

            fig, ax =plt.subplots()
            ax.set(title="Messages Overtime "+ usr)
            ax.set_xlim(days[-1]-datetime.timedelta(days=183),days[-1])
            ax.stackplot(days,msg)
            fig.autofmt_xdate()

            ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')
            #plt.tight_layout()
            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.show()

#----Plot-messages-------------
def Plot_DayVsHour(users,graphs=[0]):
    key = 0
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1

        if num in graphs and num != 0:
            day=users[usr][3]
            hour=users[usr][4]

            fig, ax = plt.subplots()
            ax.set(title="Daily messages "+ usr)
            ax.plot(day,hour,'.')
            fig.autofmt_xdate()

            ax.fmt_xdata = mdates.DateFormatter('%Y/%m/%d')
            ax.fmt_ydata = mdates.DateFormatter('%I:%M %p')
            plt.tight_layout()
            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
            ax.get_yaxis().set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    plt.show()
    #--------Cosas que quiero averiguar---------------    
    #plt.setp(plt.gca().xaxis.get_majorticklabels(),    
    #     'rotation', 45)                           
    #plt.legend()    
    #plt.gca().xaxis.set_major_locator(mdates.MonthLocator(None,1,5))
    #plt.gca().yaxis.set_major_locator(mdates.HourLocator())    

#----Plot-Messages-Per-Hour----

def Plot_MessagesPerHour(users,graphs=[0]):

    key = 0
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1

        if num in graphs and num != 0:
            hour=users[usr][6]
            msg=users[usr][5]

            fig, ax = plt.subplots()
            ax.set(title="Messages Per hour "+ usr)
            ax.plot(hour,msg,'-o')
            fig.autofmt_xdate()

            ax.fmt_xdata = mdates.DateFormatter('%I %p')
            plt.tight_layout()
            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%I %p'))
    plt.show()
#------------------------------


#Plot_TotalMessagesOvertime(users,(1,3))

#Plot_MessagesOvertime(users,(1,3))

#Plot_DayVsHour(users,(1,3))

#Plot_MessagesPerHour(users,(1,3))


#print(users["Luca"][0])
#print(users["Kenneth"][0])

#print(msgs_total / len(dias))
#print(msgs_total)
#print(dias2)
