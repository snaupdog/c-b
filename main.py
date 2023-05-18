
# highscorefunctionality added
from tkinter import *
import tkinter.font as font

start=Tk()
font1 = font.Font(family='Comic Sans MS',size=20,weight="bold")
font2=font.Font(family='Comic Sans MS',size=40,weight="bold")
font3=font.Font(family='Comic Sans MS',size=95,weight="bold")
attemp=font.Font(family='Comic Sans MS',size=20,weight="bold")
attemp2=font.Font(family='Comic Sans MS',size=30,weight="bold")
payagain=font.Font(family='Comic Sans MS',size=20,weight="bold")


#STARTING SCREEN
start.geometry("700x700")   
bg=PhotoImage(file="sky.png")
startingscreen=Label(start,image=bg)
startingscreen.place(x=0,y=0,relheight=1,relwidth=1)


                            #  BUTTON FOR NEW WINDOW

def begin():
    window=Toplevel(start)
    window.geometry("800x529")
    global score
    score=0
    def playagain():
        window.destroy()
        start.geometry("700x700")
        high=open("highscore.txt","r")
        highscr=high.read()
        Label(start,text="highscore -"+highscr,font=attemp,fg="BLACK",bg="#e8ca4a").place(relx=0.8, rely=0.8, anchor=CENTER)
     
    x=PhotoImage(file="bg2.png")
    nx=Label(window,image=x)
    nx.place(x=0,y=0,relheight=1,relwidth=1)
    start.geometry("1x1")
    def getrand():
        global l2
        import random
        a=1000
        b=9999
        l2=random.randint(a,b)
        sdf=str(l2)
        l2=list(sdf)
        if(len(list(set(l2)))==len(l2)):   
            return l2         
        else:
            getrand()
    getrand()

# ------------------------------------------------------------
    print(l2)            #  PRINTS RANDOM GENERATED NUMBER


    def game(l1n):     
        
        global score
        score+=1
        enxtj=0
        cow=0
        bull=0
        global bb
        global cb
        cb.destroy()
        bb.destroy()
        for i in range(4):
            if(l1n==l2):  
                           # VICTORY SCREEN
                
                enxtj+=1
                scorestr=str(score)
                                 # Final guessing the word
                Label(window,text="YOU WIN",font=font3,fg="BLACK",bg="#df4b55").place(relx=0.5, rely=0.2, anchor=CENTER)
                Label(window,text="ATTEMPTS -"+scorestr,font=attemp,fg="BLACK",bg="#e8ca4a").place(relx=0.5, rely=0.5, anchor=CENTER)
                Button(window,text="PLAY AGAIN ?",font=payagain,command=playagain).place(relx=0.9, rely=0.9, anchor=CENTER)
                button_goback.destroy()


                f=open("highscore.txt","r")
                n=f.read()
                c1=int(n)
    
                print("gaeme nd")
                if(score<c1):
                    fs=open("highscore.txt","w")
                    fs.write(scorestr)
                    print("new highscore")
                    Label(window,text="YOU GOT A NEW HIGHSCORE",font=attemp2,fg="BLACK",bg="#e8ca4a").place(relx=0.5, rely=0.4, anchor=CENTER)


                break                  
            elif(l1n[i]==l2[i]):                         # Finding Number of cow
                cow+=1
            else:
                for j in range(4):     
                    if(l1n[i]==l2[j]):   #finding number of bull
                        bull+=1
        n=str(cow)
        n1=str(bull)
        #easy =str(set(easy))
# COW AND BULL BUTTON
        if (enxtj==0): 
            cb=Button(window,text=n,font=font2,)
            cb.place(relx=0.35, rely=0.55, anchor=CENTER)

            bb=Button(window,text=n1,font=font2,bg="#e8ca4c")
            bb.place(relx=0.65, rely=0.55, anchor=CENTER)
        
        
    def userinput(): 
        ns=iput.get()
        global l1
        l1=list(ns)
        if(len(list(set(ns)))==len(l1)): 
            game(l1)
        else:
            Label(window,text="do not enter duplicates",bg="black",fg="white").pack()
               
# ENTRY WIDGET

    iput=Entry(window,width=20)
    iput.place(relx=0.5, rely=0.8, anchor=CENTER)


    global cb
    global bb
    cb=Button(window,text="cow",bg="#e8ca4c")
    bb=Button(window,text="bull",bg="#e8ca4c")
    

    #SUBMIT BUTTON

    b=Button(window,text="ENTER",command=userinput,)
    b.place(relx=0.5, rely=0.9, anchor=CENTER)


    # GO BACK BUTTON

    def goback():
        window.destroy()
        start.geometry("700x700")
    
    button_goback=Button(window,text="BACK TO HOME SCREEN",command=goback)
    button_goback.place(relx=0.85, rely=0.1, anchor=CENTER)

    window.mainloop()
                        # STARTING SCREEN
# PLAY BUTTON
x=PhotoImage(file="PLAY.png")
startgame = Button(start,
    image=x,
    padx=10,pady=10,
    command=begin   
    )
startgame.place(relx=0.5, rely=0.6, anchor=CENTER)

# quit button
def endgame():
        quit()

high=open("highscore.txt","r")
highscr=high.read()
Label(start,text="highscore -"+highscr,font=attemp,fg="BLACK",bg="#e8ca4a").place(relx=0.8, rely=0.8, anchor=CENTER)

button_quit=Button(start,text="QUIT",command=endgame,)
button_quit.place(relx=0.9, rely=0.1, anchor=CENTER)



start.mainloop()

