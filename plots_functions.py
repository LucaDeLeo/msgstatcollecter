# plots_functions.py
# -*- coding: utf-8 -*-

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

plt.style.use('seaborn')

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



#------Porsentual-Distribution------------

def Plot_PiePorsentage(users,msgs):
    vals=[]
    usrval=[]
    for num,usr in enumerate(users):
        if num!=0 and num!=1:
            x=users[usr][0]*100/msgs
            vals.append(x)
            usrval.append(usr)



    fig, ax = plt.subplots()
    size = 0.25

    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3)*4)

    ax.pie(vals,labels=usrval , radius=1, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='k'),autopct='%1.1f%%')

    ax.set(aspect="equal", title='Messages Distribution')
    plt.show()

#-------Words-per-text--------------

def Plot_WordsPerText(users):
    vals=[]
    usrval=[]
    for num,usr in enumerate(users):
        if num!=0:
            x=np.mean(users[usr][7])
            vals.append(x)
            usrval.append(usr)


    fig, ax = plt.subplots()
    bar = ax.barh(usrval, vals)
    rects = ax.patches
    for rect in rects:
    # Get X and Y placement of label from rect
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2

        # Number of points between bar and label; change to your liking
        space = -30
        # Vertical alignment for positive values
        ha = 'left'

        # If value of bar is negative: place label to the left of the bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label to the right
            ha = 'right'

        # Use X value as label and format number
        label = '{:,.1f}'.format(x_value)

        # Create annotation
        plt.annotate(
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
    plt.show()










