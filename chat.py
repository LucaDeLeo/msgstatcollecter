chat = open("demo.txt", "r", encoding="utf-8")

dias = []
days_total = 0
msgs_total = 0
day_messages = 0
char_index = 0

for line in chat:
    day = line.partition(",")[0]
    tmp = line.partition(", ")[2].partition(" - ")
    hour = tmp[0]
    text = tmp[2]
    msgs_total += 1
    if not dias:
        dias.append([day,0])
    if dias[-1][0] != day:
        dias.append([day,0])
        dias[-2][1] = day_messages
        day_messages = 0
        days_total += 1
    else:
        day_messages += 1

dias[-1][1] = day_messages

print(msgs_total / len(dias))