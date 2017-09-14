morse = {"A":"13","B":"3111","C":"3131","D":"311","E":"1","F":"1131","G":"331","H":"1111","I":"11","J":"1333","K":"313","L":"1311","M":"33","N":"31","O":"333","P":"1331","Q":"3313","R":"131","S":"111","T":"3","U":"113","V":"1113","W":"133","X":"3113","Y":"3133","Z":"3311","1":"13333","2":"11333","3":"11133","4":"11113","5":"11111","6":"31111","7":"33111","8":"33311","9":"33331","0":"33333"}

from time import sleep 
from gpiozero import LED 
morse_led = LED(17) 
#this is for indicating the next word in the sentence 
blue_led = LED(27)

message = input("Enter your message... : ") 
word_list = message.split(" ")

for word in word_list : 
    for letter in word : 
        morse_letter = morse[letter.capitalize()] 
        for m in morse_letter : 
            morse_led.blink(int(m),1,1) 
        sleep(2) 
# this is for indicating the next word in the sentence. 
    blue_led.blink(1,1,1) 
    sleep(3)
    
    
    
#It did not work . why?
#If I change the line: 

morse_led.blink(int(m),1,1)

#with

morse_led.on() 
sleep(int(m)) 
morse_led.off() 
sleep(1)

#then it works..
