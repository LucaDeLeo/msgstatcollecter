import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import TXTloader

plt.style.use('seaborn')

#chat = open(TXTloader.TXT[0], "r", encoding="utf-8")
chat = open('demo.txt', "r", encoding="utf-8") 


#----Plot-messages-variables------
daysPltMess = []
hourPltMess = []

#----Messages-Per-Hour-variables--
MessagesPerHour=[]
HourMPH=[]

#----Messages-Overtime------------
MessagesOvertime=[]
DayMO=[]

#---------------------------------

class user:
    def __init__(self):
        self.dias=0
        self.

dias = []
days_total = 0
msgs_total = 0
day_messages = 0
users = {"System Messages": 0}

for line in chat:
    part = line.partition(" - ")
    try:
        date = datetime.datetime.strptime(part[0], "%m/%d/%y, %I:%M %p")
    except ValueError as err:
        continue

    sender = part[2].partition(":")[0]
    if '\n' not in sender:
        users.update({sender: users.setdefault(sender, 0) + 1})
    else:
        users.update({"System Messages": users.get("System Messages") + 1})

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
    if not(DMO in DayMO):
        DayMO.append(DMO)
        MessagesOvertime.append(0)
    MessagesOvertime[DayMO.index(DMO)] += 1

    #----------Messages-Per-Hour------------
    hMPH = datetime.datetime(2000,1,1,date.hour)
    if not(hMPH in HourMPH):
        HourMPH.append(hMPH)
        MessagesPerHour.append(0)
    HourMPH = sorted(HourMPH)
    MessagesPerHour[HourMPH.index(hMPH)] += 1

    #----Plot-messages-variables------
    daysPltMess.append(date.date())
    hourPltMess.append(datetime.datetime(2000,1,1,date.hour,date.minute))
    #---------------------------------

#----Plot-Total-Messages-Overtime

def Plot_TotalMessagesOvertime(msg,days1):

    l=(days1[-1]-days1[0]).days
    e=11*l/(51*10)
    s=l/(51*10)
    b=e-s
    br=round(b,0)
    if s<1:
        s=0
    sr=round(s,0)
    br2=round(b/2,0)
    cota=0
    msg2=[]
    days2=[]
    msg3=[]
    days3=[]
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
    ax.set(title="Total Messages Overtime")
    ax.bar(days3,msg3,width=datetime.timedelta(days=br))
    fig.autofmt_xdate()

    ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')
    plt.tight_layout()
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.show()

#----Plot-Messages-Overtime----

def Plot_MessagesOvertime(msg,days):
    fig, ax =plt.subplots()
    ax.set(title="Messages Overtime")
    ax.set_xlim(days[-1]-datetime.timedelta(days=183),days[-1])
    ax.stackplot(days,msg)
    fig.autofmt_xdate()

    ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')
    plt.tight_layout()
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.show()
#----Plot-Messages-Per-Day-----

def Plot_MessagesPerHour(msg,hour):
    fig, ax = plt.subplots()
    ax.set(title="Messages Per hour")
    ax.plot(hour,msg,'-o')
    fig.autofmt_xdate()

    ax.fmt_xdata = mdates.DateFormatter('%I %p')
    plt.tight_layout()
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%I %p'))
    plt.show()
#----Plot-messages-------------
def Plot_DayVsHour(day,hour):
    fig, ax = plt.subplots()
    ax.set(title="Daily messages")
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
#------------------------------

Plot_TotalMessagesOvertime(MessagesOvertime,DayMO)
Plot_MessagesOvertime(MessagesOvertime,DayMO)
#Plot_DayVsHour(daysPltMess,hourPltMess)
#Plot_MessagesPerHour(MessagesPerHour,HourMPH)

#dias[-1][1] = day_messages (no estoy seguro de haber borrado esto en algún momento)


#print(users)
#print(msgs_total / len(dias))
#print(msgs_total)
#print(dias2)
