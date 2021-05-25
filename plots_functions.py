# plots_functions.py
# -*- coding: utf-8 -*-

import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.patches as mpatches
plt.style.use('seaborn')

def Plot_TotalMessagesOvertime(users,graphs=[0],fig=0,ax=0):
    # Podes elegir cuales y cuantos graficos queres con graphs, de 1 en adelante
    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1
    key = 0
    usrlabels=[]
    for num,usr in enumerate(users):


        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1
        if num in graphs and num != 0:
            usrlabels.append(usr)

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

            ax.bar(days3,msg3,width=datetime.timedelta(days=br))
            fig.autofmt_xdate()

            ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')

            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))

    ax.set_title("Total Messages Overtime")
    ax.legend(usrlabels,loc='upper left',bbox_to_anchor=(0.8, 3.00), shadow=True)

    if showfig == 1:
        plt.show()

#----Plot-Messages-Overtime----

def Plot_MessagesOvertime(users,graphs=[0],fig=0,ax=0):#(msg,days):
    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1
    key = 0
    usrlabels=[]
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            key = 1
            graphs = [num]

        if num in graphs and num != 0:
            usrlabels.append(usr)

            days=users[usr][1]
            msg=users[usr][2]
            ax.set_xlim(days[-1]-datetime.timedelta(days=183),days[-1])
            plot=ax.stackplot(days,msg)
            #ax.set_label([usr])
            fig.autofmt_xdate()

            ax.fmt_xdata =mdates.DateFormatter('%Y/%m/%d')
            #plt.tight_layout()

            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    ax.set_title("Messages Over Time")

    if showfig == 1:
        plt.show()

#----Plot-messages-------------
def Plot_DayVsHour(users,graphs=[0],fig=0,ax=0):
    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1
    key = 0
    usrlabels=[]
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1

        if num in graphs and num != 0:
            usrlabels.append(usr)

            day=users[usr][3]
            hour=users[usr][4]

            ax.plot(day,hour,'.')
            fig.autofmt_xdate()

            ax.fmt_xdata = mdates.DateFormatter('%Y/%m/%d')
            ax.fmt_ydata = mdates.DateFormatter('%I:%M %p')

            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
            ax.get_yaxis().set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.set_title("Daily messages")

    if showfig == 1:
        plt.subplots_adjust(top=0.88)
        plt.show()

#----Plot-Messages-Per-Hour----

def Plot_MessagesPerHour(users,graphs=[0],fig=0,ax=0):

    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1
    key = 0
    usrlabels=[]
    for num,usr in enumerate(users):

        if graphs == [0] or key == 1:
            graphs = [num]
            key = 1

        if num in graphs and num != 0:
            usrlabels.append(usr)
            hour=users[usr][6]
            msg=users[usr][5]

            ax.plot(hour,msg,'-o')
            fig.autofmt_xdate()

            ax.fmt_xdata = mdates.DateFormatter('%I %p')
            #plt.tight_layout()
            ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%I %p'))
    ax.set_title("Messages per Hour")
    ax.get_xaxis().set_visible(True)


    if showfig == 1:
        plt.subplots_adjust(top=0.88)
        plt.show()

#------Porsentual-Distribution------------

def Plot_PiePorsentage(users,fig=0,ax=0):
    vals=[]
    usrval=[]
    for num,usr in enumerate(users):
        if num!=0 and num!=1:
            x=users[usr][0]*100/users["Total"][0]
            vals.append(x)
            usrval.append(usr)


    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1
    size = 0.25

    #cmap = plt.get_cmap("tab20c")
    #outer_colors = cmap(np.arange(3)*4)

    ax.pie(vals,labels=usrval , radius=1,wedgeprops=dict(width=size, edgecolor='k'),autopct='%1.1f%%')

    ax.set(aspect="equal", title='Messages Distribution')
    if showfig == 1:
        plt.show()

#-------Words-per-text--------------

def Plot_WordsPerText(users,fig=0,ax=0):

    showfig=0
    if ax==0:
        fig, ax = plt.subplots()
        showfig=1

    vals=[]
    usrval=[]
    for num,usr in enumerate(users):
        if num!=0 and num!=1:
            x=np.mean(users[usr][7])
            vals.append(x)
            usrval.append(usr)

            bar = ax.barh(usr, x)
            rects = ax.patches
            for rect in rects:
            # Get X and Y placement of label from rect
                x_value = rect.get_width()
                y_value = rect.get_y() + rect.get_height() / 2

                # Number of points between bar and label; change to your liking
                space = -20
                # Vertical alignment for positive values
                ha = 'left'

                # Use X value as label and format number
                label = '{:,.1f}'.format(x_value)

            # Create annotation
                ax.annotate(
                    label,                      # Use `label` as label
                    (x_value, y_value),         # Place label at bar end
                    xytext=(space, 0),          # Horizontally shift label by `space`
                    textcoords='offset points', # Interpret `xytext` as offset in points
                    va='center',                # Vertically center label
                    ha=ha,                      # Horizontally align label differently for positive and negative values
                    color = 'white')            # Change label color to white

        # Set subtitle
    tfrom = ax.get_xaxis_transform()
    ax.get_xaxis().set_visible(False)
    ax.grid(False)
    ax.set(title="Number of words per text")
    #Set x-label
    #ax.set_xlabel('', color='#525252')
    if showfig == 1:
        plt.show()


def firstdate(part):
    l=0
    error=[]
    for z in range(2):
        if z == 0 and l==0:
            try:
                indate="%m/%d/%y, %I:%M %p"
                fdate=datetime.datetime.strptime(part,indate)
            except ValueError as err:
                error.append(err)
                continue
            l=1

        elif z == 1 and l==0:
            try:
                indate="%d/%m/%Y, %I:%M %p"
                fdate=datetime.datetime.strptime(part,indate)
            except ValueError as err:
                error.append(err)
                continue
            l=1
    if l == 1:
        print("The (.txt) document time format is " +indate+ " , load successfully.")
    else:
        indate=""
        print("This is not a WhatsApp (.txt) document or the (.txt) document time format has not yet been loaded.")
    return(indate)



def ColectInf(chat):

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
    keydate=0
    for line in chat:
        part = line.partition(" - ")

        if keydate==0:
            indate=firstdate(part[0])
            keydate=1
        try:
            date = datetime.datetime.strptime(part[0], indate)
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
        users["Total"][0] += 1
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
    return(users,len(indate))



def msgStatCol(TXT):

    chat = open(TXT[0], "r", encoding="utf-8")
    users, lenerror=ColectInf(chat)

    if lenerror != 0:
        #Plot_TotalMessagesOvertime(users,(2,3))
        #Plot_MessagesOvertime(users,(1,3))
        #Plot_DayVsHour(users,(2,3))
        #Plot_MessagesPerHour(users,(1,3))
        #Plot_PiePorsentage(users)
        #Plot_WordsPerText(users)
        #plt.show()

        fig= plt.figure()

        ax0=plt.subplot2grid((6,8),(0,0),1,2)
        ax1=plt.subplot2grid((6,8),(0,2),1,6)
        ax2= plt.subplot2grid((6,8),(1,0),2,3)
        ax3= plt.subplot2grid((6,8),(1,3),2,5)
        ax4= plt.subplot2grid((6,8),(3,0),3,3)
        ax5= plt.subplot2grid((6,8),(3,3),3,5)

        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)

        Plot_WordsPerText(users,fig,ax0)
        Plot_TotalMessagesOvertime(users,(2,3),fig,ax1)
        Plot_MessagesPerHour(users,(2,3),fig,ax2)
        Plot_MessagesOvertime(users,(2,3),fig,ax3)
        Plot_PiePorsentage(users,fig,ax4)
        Plot_DayVsHour(users,(2,3),fig,ax5)

        ax0.tick_params(labelbottom=True)
        ax1.tick_params(labelbottom=True)
        ax2.tick_params(labelbottom=True)
        ax3.tick_params(labelbottom=True)
        ax4.tick_params(labelbottom=True)
        ax5.tick_params(labelbottom=True)

        plt.subplots_adjust(top=0.88)
        plt.show()

    else:
        print("Try with other txt file.")



















