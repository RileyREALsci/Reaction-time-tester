import time
from tkinter import *
import random
import data_calling
from turtle import *
import statistics



root1 = Tk()
root1.wm_attributes()

content = Frame(root1).grid(column=0, row=0)
INACTIVE_BUTTON = PhotoImage(file="graphics/inactive.png")
ACTIVE_BUTTON = PhotoImage(file="graphics/active.png")
CHECK_BUTTON = PhotoImage(file="graphics/check_button.png")

START_BUTTON = PhotoImage(file="graphics/start_button.png")
STATUS_BUTTON = PhotoImage(file="graphics/status_button.png")
CLEAR_BUTTON = PhotoImage(file="graphics/clear_button.png")
YES_BUTTON = PhotoImage(file="graphics/yes_button.png")
NO_BUTTON = PhotoImage(file="graphics/no_button.png")
GRAPH_BUTTEN = PhotoImage(file="graphics/graph_button.png")
BACK_BUTTON = PhotoImage(file="graphics/back_button.png")

BACKGROUND = PhotoImage(file="graphics/background.png")

frame = Frame(borderwidth=5, relief="ridge",  width=800, height=400).grid(column=0, row=0, columnspan=3, rowspan=2)
frame = Label(borderwidth=5, relief="ridge",image=BACKGROUND, width=800, height=400).grid(column=0, row=0, columnspan=3, rowspan=2)
scoreDisplay = Label(background="black",foreground="white",text="Last Score",width=10,height=4)
Label.place(scoreDisplay,x=380,y=5)

class Menus():
    def __init__(self,master,menuType):

        match menuType:
            case "defend":
                self.score = time.time() - self.stampTime
                scoreMs = int(self.score * 1000)
                Label.config(scoreDisplay, text=(f"Speed\n{scoreMs} ms\n{scoreMs / 1000} sec"))
                self.playButton.destroy()
                dataSet = data_calling.Calls.CallData("click_data.txt",)
                dataSet.append(scoreMs)
                data_calling.Calls.WriteData("click_data.txt",dataSet)
            case "assault":
                self.assaultLabel.destroy()
                self.playButton.destroy()
            case "clear_data_false":
                self.yesButton.destroy()
                self.noButton.destroy()
                self.message.destroy()
                self.graphButten.destroy()
            case "clear_data_true":
                data_calling.Calls.WriteData("click_data.txt","")# Clearing the click data file.
                self.yesButton.destroy()
                self.noButton.destroy()
                self.message.destroy()
            case "statistics":
                self.backButton.destroy()
                self.meanLabel.destroy()
                self.medianLabel.destroy()
                self.modeLabel.destroy()
                self.stadardDeviationLabel.destroy()
            case _:
                pass

        self.master = master
        self.master.title("Reaction Speed App")

        self.canvas = Label(width=40,height=10,text="Riley the griffiths is the actual creator, of this cheap app\nits so cheap that its free so enjoy playing it\n I like to taste things good and hard and i think I like to\n fight things hard, things like dificult shit\n I like a chalenge you know\n shit like hard core stuff and shit and that and all and stuff\n so yeah have a good one mate and cobba, I feel like this has been a very Interlectal Conversation here\n")
        Label.place(self.canvas,x=400,y=100)
        
        self.startButton = Button(image=START_BUTTON,command=self.Start)
        Button.place(self.startButton,x=80,y=80)
        self.graphButten = Button(image=GRAPH_BUTTEN,command=self.Graph)
        Button.place(self.graphButten,x=80,y=120)
        self.clearButton = Button(image = CLEAR_BUTTON,command=self.ClearDataMenu)
        Button.place(self.clearButton,x=80,y=160)
        self.statisticsButton = Button(image=STATUS_BUTTON,command=self.Statistics)
        Button.place(self.statisticsButton,x=80,y=200)


    def Start(self):
        self.startButton.destroy()
        self.graphButten.destroy()
        self.clearButton.destroy()
        self.statisticsButton.destroy()

        self.playButton = Button(image=INACTIVE_BUTTON,command=lambda:Menus.Assault(self))
        Button.place(self.playButton,x=320,y=100)
        duration = random.randint(1.0,10.0)

        self.playButton.after((1000 * duration),lambda:Menus.Defend(self))

    def Defend(self):

        self.stampTime = time.time()
        Button.config(self.playButton,image=ACTIVE_BUTTON,command=lambda:Menus.__init__(self,self.master,"defend"))

    def Assault(self):
        
        self.assaultLabel = Label(image=CHECK_BUTTON)
        Label.place(self.assaultLabel,x=320,y=100)

        self.playButton.after((2000),lambda:Menus.__init__(self,self.master,"assault"))
    def Graph(self):

        dataSet = data_calling.Calls.CallData("click_data.txt",)
        
        Screen()
        addshape("graphics/graph_background.gif")

        bgpic("graphics/graph_background.gif")
        setup(width=1000,height=800,startx=0,starty=0)
        bgcolor((0,0,0))
        color((0.3,0.3,0.8))
        pensize(5)
        penup()
        goto(-500,-400)
        pendown()

        newXCordinate = 1000 / len(dataSet)
        newYCordinate = -400
        xCord = -500        

        for i in dataSet:

            pensize(5)
            yCord = (newYCordinate + i)
            xCord += newXCordinate
            goto(xCord,yCord)

        exitonclick()
        Menus.__init__(self,self.master,"Null")

    def ClearDataMenu(self):
        self.startButton.destroy()
        self.graphButten.destroy()
        self.clearButton.destroy()
        self.statisticsButton.destroy()

        self.message = Label(width=35,height=3,bg="black", fg="white",text="This action will delete all click data.\nContinue?")
        Label.place(self.message,x=260,y=120)
        self.yesButton = Button(image=YES_BUTTON,command=lambda:Menus.__init__(self,self.master,"clear_data_true"))
        Button.place(self.yesButton,x=260,y=180)
        self.noButton = Button(image=NO_BUTTON,command=lambda:Menus.__init__(self,self.master,"clear_data_false"))
        Button.place(self.noButton,x=420,y=180)
    
    def Statistics(self):
        self.startButton.destroy()
        self.graphButten.destroy()
        self.clearButton.destroy()
        self.statisticsButton.destroy()

        dataSet = data_calling.Calls.CallData("click_data.txt")
        try:

            mean = statistics.mean(dataSet)
            mean = int(mean)
            median = statistics.median(dataSet)
            median = int(median)
            mode = statistics.mode(dataSet)
            mode = int(mode)
            standardDeviation = statistics.stdev(dataSet)
            standardDeviation = int(standardDeviation)
        except:
            mean = 0
            median = 0
            mode = 0
            standardDeviation = 0


        self.meanLabel = Label(width=14,height=3,text=f"Mean\n{mean}",bg="#000000",fg="#ffffff")
        Label.place(self.meanLabel,x=365,y=80)

        self.medianLabel = Label(width=14,height=3,text=f"Median\n{median}",bg="#000000",fg="#ffffff")
        Label.place(self.medianLabel,x=365,y=120)

        self.modeLabel = Label(width=14,height=3,text=f"Mode\n{mode}",bg="#000000",fg="#ffffff")
        Label.place(self.modeLabel,x=365,y=160)

        self.stadardDeviationLabel = Label(width=14,height=3,text=f"Standard Deviation\n{standardDeviation}",bg="#000000",fg="#ffffff")
        Label.place(self.stadardDeviationLabel,x=365,y=200)        

        self.backButton = Button(image=BACK_BUTTON,command=lambda:Menus.__init__(self,self.master,"statistics"))
        Button.place(self.backButton,x=80,y=340)

Menus(root1,"Null")
root1.mainloop()