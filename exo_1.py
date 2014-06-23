from Tkinter import *
import time


x=30
y=380
x2=5
x3=55
xr=200
yr=200
score=0
vit=15

def start():
    global x,x2,x3,yr,score,y,xr,vit
    x=x+vit
    x2=x2+vit
    x3=x3+vit
    can.coords(carre,x-10,y-10,x+10,y+10)
    can.coords(carre2,x2-10,y-10,x2+10,y+10)
    can.coords(carre3,x3-10,y-10,x3+10,y+10)
    if x+10>=400:
        x=0
    if x2+10>=400:
        x2=0
    if x3+10>=400:
        x3=0
    if yr>=y-10 and yr<=y+10:
        if xr>=x-10 and xr<=x+10:
            score=score+1
            time.sleep(2)
            x=30
            y=380
            x2=5
            x3=55
            xr=200
            yr=200
        if xr>=x2-10 and xr<=x2+10:
            score=score+1
            time.sleep(2)
            x=30
            y=380
            x2=5
            x3=55
            xr=200
            yr=200
        if xr>=x3-10 and xr<=x3+10:
            score=score+1
            time.sleep(2)
            x=30
            y=380
            x2=5
            x3=55
            xr=200
            yr=200
        aff.set(score)
        can.coords(balla,xr-5,yr-5,xr+5,yr+5)
    can.coords(carre,x-10,y-10,x+10,y+10)
    can.coords(carre2,x2-10,y-10,x2+10,y+10)
    can.coords(carre3,x3-10,y-10,x3+10,y+10)
        
    fenszy.after(100,start)
def vitessepl():
    global vit
    vit=vit+5
def vitessemo():
    global vit
    vit=vit-5
def depl(key):
    global yr
    touche=key.keysym.lower()
    if touche=='up':
        yr=yr-10
    if touche=='down':
        yr=yr+10
    if yr+6>=399:
        yr=0
    if yr<=0:
        yr=400
    can.coords(balla,xr-5,yr-5,xr+5,yr+5)
        

fenszy=Tk()
fenszy.title("jeu carre ballon")
fenszy.minsize(300,500)



can=Canvas(fenszy,width=400,height=400,bg="red")
can.pack()
carre=can.create_rectangle(x-10,y-10,x+10,y+10,fill="black")
carre2=can.create_rectangle(x2-10,y-10,x2+10,y+10,fill="black")
carre3=can.create_rectangle(x3-10,y-10,x3+10,y+10,fill="black")
balla=can.create_oval(xr-5,yr-5,xr+5,yr+5,fill="blue")
Button(fenszy,text="START",command=start).pack()
Button(fenszy,text="+",command=vitessepl).pack()
Button(fenszy,text="-",command=vitessemo).pack()
aff=StringVar()
Label(textvariable=aff).pack()

fenszy.bind("<Key>",depl)
fenszy.mainloop()
