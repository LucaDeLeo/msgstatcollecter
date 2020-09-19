chat = """3/12/17, 7:56 AM - Luca: Kenneth
3/12/17, 10:12 AM - Kenneth: Que honda pa
3/12/17, 10:39 AM - Luca: No dormi en toda la noche y estoy re al pedo
3/12/17, 10:39 AM - Luca: Venite si queres
3/12/17, 11:05 AM - Kenneth: Compramos piza piola
3/12/17, 11:05 AM - Luca: Dale
3/14/17, 12:37 PM - Luca: Tengo ganas de pasar el día haciendo matemática y encontré unos problemas piola de olimpiadas matemática
3/14/17, 12:37 PM - Luca: S
3/14/17, 12:37 PM - Luca: Venite si querés
3/14/17, 1:08 PM - Kenneth: Estoy en lo de mi primo
3/14/17, 1:11 PM - Luca: 👌🏻
3/14/17, 1:11 PM - Luca: Avisame el jueves y vamos juntos a las charlas
3/14/17, 1:17 PM - Kenneth: De una
3/14/17, 1:17 PM - Kenneth: Mañana estoy al pedo
3/14/17, 2:05 PM - Luca: Mañana almuerzo con mi abuelo
3/14/17, 2:05 PM - Luca: A la tarde hacemos algo
3/15/17, 3:09 PM - Luca: Estas al pedo?
3/15/17, 3:36 PM - Kenneth: Casi
3/15/17, 3:36 PM - Kenneth: A las 5 tengo que ir a ayudar a mi tía con un estan de ropa
3/15/17, 3:37 PM - Kenneth: En no se donde
3/15/17, 3:37 PM - Kenneth: Re específico soy
3/15/17, 3:37 PM - Kenneth: Ni ganas de fijarme ahora
3/15/17, 3:37 PM - Luca: Oka, mañana vamos a la charla
3/15/17, 3:37 PM - Luca: ?
3/15/17, 3:38 PM - Kenneth: Se
3/15/17, 3:38 PM - Kenneth: De una
3/15/17, 3:46 PM - Luca: Oka
3/15/17, 7:40 PM - Luca: <Media omitted>
3/15/17, 11:31 PM - Kenneth: Na esta bien
3/15/17, 11:32 PM - Kenneth: <Media omitted>
3/16/17, 6:43 AM - Luca: Jajajajaja
3/16/17, 6:43 AM - Luca: Re tiraron para arriba?
3/16/17, 6:43 AM - Luca: Te*
3/16/17, 7:01 AM - Kenneth: De una
3/16/17, 7:13 AM - Luca: Pero como
3/16/17, 7:13 AM - Luca: Osea no entiendo que querés decir con que te tiraron para arriba
3/16/17, 7:15 AM - Kenneth: Me subieron el ánimo
3/16/17, 7:17 AM - Luca: Ahhhhhh
3/16/17, 7:17 AM - Luca: Pensé que las modelos te habían hecho tipo trampolin
3/16/17, 7:18 AM - Kenneth: Claro
3/16/17, 9:13 AM - Kenneth: A que hora es esto?
3/16/17, 10:10 AM - Luca: <Media omitted>
3/16/17, 1:10 PM - Kenneth: Pa, yo voy yendo
3/16/17, 1:10 PM - Kenneth: Para agarrar lugar
3/16/17, 1:11 PM - Luca: Yo tamhieny
3/16/17, 1:11 PM - Luca: También
3/16/17, 1:11 PM - Kenneth: Tamhieny
3/16/17, 1:11 PM - Kenneth: Que buen apellido
3/16/17, 1:12 PM - Luca: Jajaj"""

dias = []
days_total = 0
msgs_total = 0
day_messages = 0
char_index = 0

while chat:
    message = chat.partition("\n")[0]
    chat = chat.partition("\n")[2]
    day = message.partition(",")[0]
    tmp = message.partition(", ")[2].partition(" - ")
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
print(dias)



