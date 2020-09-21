import re
import datetime

chat = open("demo.txt", "r", encoding="utf-8")


dias = []
days_total = 0
msgs_total = 0
day_messages = 0

for line in chat:
    part = line.partition(" - ")
    try:
        date = datetime.datetime.strptime(part[0], "%m/%d/%y, %I:%M %p")
    except ValueError as err:
        continue

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

dias[-1][1] = day_messages


print(msgs_total / len(dias))