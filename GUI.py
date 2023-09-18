from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware 
ledRed = LED(14)
ledBlue = LED(15)
ledGreen = LED(18)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

### EVENT FUNCTIONS ###
def ledRedToggle():
     if ledRed.is_lit:
          ledRed.off()
          ledRedButton1["text"] = "Turn Red LED on"
     else:
          ledRed.on()
          ledRedButton1['text'] = "Turn Red LED off"
def ledBlueToggle():
     if ledBlue.is_lit:
          ledBlue.off()
          ledBlueButton2["text"] = "Turn Blue LED on"
     else:
          ledBlue.on()
          ledBlueButton2['text'] = "Turn Blue LED off"
def ledGreenToggle():
     if ledGreen.is_lit:
          ledGreen.off()
          ledGreenButton3["text"] = "Turn Green LED on"
     else:
          ledGreen.on()
          ledGreenButton3['text'] = "Turn Green LED off"
def ledAllToggle():
     if ledRed.is_lit & ledBlue.is_lit & ledGreen.is_lit:
          ledRed.off()
          ledBlue.off()
          ledGreen.off()
          ledAllButton4['text']="Turn All LED on"     
     else:
          ledRed.on()
          ledBlue.on()
          ledGreen.on()     
          ledAllButton4['text']="Turn All LED off"   

###WIDGETS###
ledRedButton1 = Button(win,  text = 'Turn Red LED On', font= myFont, command=ledRedToggle,  bg= 'tomato', height =1, width=24)
ledRedButton1.grid(row=1, column=0)
ledBlueButton2 = Button(win,  text = 'Turn White LED On', font= myFont, command=ledBlueToggle,  bg= 'aquamarine', height =1, width=24)
ledBlueButton2.grid(row=2, column=0)
ledGreenButton3 = Button(win,  text = 'Turn Green LED On', font= myFont, command=ledGreenToggle,  bg= 'green yellow', height =1, width=24)
ledGreenButton3.grid(row=3, column=0)
ledAllButton4= Button(win,  text = 'Turn All LED On', font= myFont, command=ledAllToggle,  bg= 'bisque2', height =1, width=24)
ledAllButton4.grid(row=4, column=0)
