import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import TXTloader

plt.style.use('seaborn')

chat = open(TXTloader.fname[0], "r", encoding="utf-8")

dias2 = []
hora2 = []
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

    #----Plot-messages-variables------
    daysPltMess.append(date.date())
    hourPltMess.append(datetime.datetime(2000,1,1,date.hour,date.minute))
    #---------------------------------

#----Plot-messages-------------
fig, ax = plt.subplots()
ax.plot(daysPltMess,hourPltMess,'.')
fig.autofmt_xdate()

ax.fmt_xdata = mdates.DateFormatter('%Y/%m/%d')
ax.fmt_ydata = mdates.DateFormatter('%I:%M %p')
plt.tight_layout()
#plt.legend()
plt.show()
#------------------------------



dias[-1][1] = day_messages

#print(users)
#print(msgs_total / len(dias))
#print(msgs_total)
#print(dias2)
