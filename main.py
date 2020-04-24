from tkinter import *
import time
import datetime
import pygame


pygame.init()
root =Tk()
root.title("MUSIC BOX")
root.geometry('1172x700+0+0')
root.configure(background='white')



abc=Frame(root,bg="powderblue",bd=10,relief=RIDGE)
abc.grid()


abc1=Frame(abc,bg="powderblue",bd=10,relief=RIDGE)
abc1.grid()
abc2=Frame(abc,bg="powderblue",bd=3,relief=RIDGE)
abc2.grid()
abc3=Frame(abc,bg="powderblue",bd=0,relief=RIDGE)
abc3.grid()


str1=StringVar()
str1.set("Just like music")
Date1=StringVar()
time1=StringVar()


Date1.set(time.strftime("%d/%m/%Y"))
time1.set(time.strftime("%H:%M:%S"))
#====================================================================================
def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)


def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)



def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)



def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)


def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)


def value_Cs():
    str1.set("C#")
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play(0)

#=========================================label with title==========================


Label(abc1,text="Piano keys", font=('arial',25,'bold'),padx=8,pady=8,bd=4,bg="powderblue",
fg="white",justify=CENTER).grid(row=0,column=0,columnspan=11)


#==========================================label for  second title=======================================


txtDate=Entry(abc1,textvariable=Date1, font=('arial',18,'bold'),bd=34,bg="powder blue",
fg="white",width=28,justify=CENTER).grid(row=1,column=0,pady=1)



txtDisplay=Entry(abc1,textvariable=str1, font=('arial',18,'bold'),bd=34,bg="powderblue",
fg="white",width=28,justify=CENTER).grid(row=1,column=1,pady=1)



txtTime=Entry(abc1,textvariable=time1, font=('arial',18,'bold'),bd=34,bg="powderblue",
fg="white",width=28,justify=CENTER).grid(row=1,column=2,pady=1)



#======================================buttons==================================================


btns1=Button(abc2,width=6,height=6,text="C#",bd=4, font=('arial',18,'bold'),command=value_Cs,bg="black",fg="white")
btns1.grid(row=0,column=0,padx=5,pady=5)
btns2=Button(abc2,width=6,height=6,text="D#",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns2.grid(row=0,column=2,padx=5,pady=5)

btns3=Button(abc2,width=6,height=6,text="F#",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns3.grid(row=0,column=4,padx=5,pady=5)

btns4=Button(abc2,width=6,height=6,text="F#",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns4.grid(row=0,column=6,padx=5,pady=5)
btns5=Button(abc2,width=6,height=6,text="F#",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns5.grid(row=0,column=8,padx=5,pady=5)
btns6=Button(abc2,width=6,height=6,text="C#1",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns6.grid(row=0,column=10,padx=5,pady=5)



btns7=Button(abc2,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="black",fg="white")
btns7.grid(row=0,column=12,padx=5,pady=5)


#=================================================white buttons================================================



btn1=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn1.grid(row=0,column=0,padx=5,pady=5)


btn2=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn2.grid(row=0,column=2,padx=5,pady=5)


btn3=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn3.grid(row=0,column=3,padx=5,pady=5)


btn4=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn4.grid(row=0,column=4,padx=5,pady=5)



btn5=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn5.grid(row=0,column=5,padx=5,pady=5)



btn6=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn6.grid(row=0,column=6,padx=5,pady=5)



btn7=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn7.grid(row=0,column=7,padx=5,pady=5)


btn8=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn8.grid(row=0,column=8,padx=5,pady=5)



btn9=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn9.grid(row=0,column=9,padx=5,pady=5)


btn10=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn10.grid(row=0,column=10,padx=5,pady=5)



btn11=Button(abc3,width=6,height=6,text="D#1",bd=4, font=('arial',18,'bold'),bg="white",fg="black")
btn11.grid(row=0,column=11,padx=5,pady=5)








root.mainloop()