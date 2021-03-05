from tkinter import*
from random import*

color='black'
width=2
clicked=[False,False]

colors=['white','red','orange','mediumvioletred','gold','green','blueviolet','cyan','blue','bisque','black']
colors_btns=[]

def palitra(event):
    global color
    t=event.widget
    color=t['bg']

def random_color():
    global color
    rd_color='#%0x%0x%0x'%(randint(0,15),randint(0,15),randint(0,15))
    color=rd_color    
    
def draw(event):
    global color, width, c
    x=event.x
    y=event.y
    c.create_oval(x-width,y-width,x+width,y+width,fill=color,outline=color)

def width_config():
    global entry, width
    width=int(entry.get())

def clear():
    global c
    c.delete('all')

def filled():
    global c, color
    c.config(bg=color)

def rubber():
    global color, c
    color=c['bg']

a=Tk()
a.title('Mini Paint')
a.iconbitmap('images/icon.ico')
a.resizable(width=False,height=False)

#цвета
for i in range(len(colors)):
    b=Button(bg=colors[i],width=1,height=1)
    b.bind('<Button-1>',palitra)
    colors_btns.append(b)
    b.grid(row=1,column=i)        

print(len(colors))
#иконки
im=PhotoImage(file='images/filled.gif')
im1=PhotoImage(file='images/rubber.gif')

c=Canvas(a,width=700,height=500,bg='white')
c.grid(row=0,columnspan=27)

rd_button=Button(text='random color',command=random_color)
rd_button.grid(row=1,column=18)

rubber_btn=Button(image=im1,command=rubber)
rubber_btn.grid(row=1,column=19)

submit_btn=Button(text='Submit',command=width_config)
submit_btn.grid(row=1,column=15)

entry=Entry(bd=3,width=9)
entry.grid(row=1,column=16)

filled_button=Button(image=im,command=filled)
filled_button.grid(row=1,column=12)

clear_btn=Button(text='Очистить',command=clear)
clear_btn.grid(row=1,column=22)

a.bind('<B1-Motion>',draw)
a.mainloop()
