from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware 
leds = {
     "Red": LED(14),
     "Blue": LED(15),
     "Green": LED(18),
}
     
## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

### EVENT FUNCTIONS ###
def ledToggle(led):
     if led.is_lit:
          led.off()
     else:
          ledRed.on()
##WIDGETS##
buttons = []
for name, led in leds.items():
     button = Button(win, text=f'Turn {name} LED On', font=myFont, command=lambda l=led: led_toggle(1), height=1, width=24)
     button.grid(row=len(buttons) +1, column=0)
     buttons.append(button)
     
def ledAllToggle():
     all_leds_on = all(led.is_lit for led in leds.values())
     for led in leds.values():
        if all_leds_on:
            led.off()
        else:
            led.on()   

###WIDGETS###
ledAllButton= Button(win,  text = 'Turn All LED On', font= myFont, command=ledAllToggle,  bg= 'bisque2', height =1, width=24)
ledAllButton.grid(row=len(leds)+1, column=0)
