# Virtual_Farmer_Auto_Farming
This program can be used to afk farm Virtual Farmer bot on Discord

The code gives you the ability to afk farm by autoclicking the "Farm" button and type the verify message
when needed. It works only while you are not using your PC(you should not move your cursor).

**WARNING:** 
1. The Auto Farm works for the current version(1.3.5.1) of the Virtual Farmer BOT. If the BOT version is different
use the code at your own risk.
2. Non-BOT acounts acting like BOTs could be banned from Discord, so again use the code at your own risk.



To be able to run the code you will need to install:
1. pyautogui
2. websocket
3. threading
4. requests
5. pynput

To install use the command "pip install 'name of library'"(example: pip install websocket)



Before we start, enable Developer mode (settings>advanced>Developer Mode)

You'll also have to change a few things in the code so it will be able to run properly for you. In lines between 12-26 is a block of code (you can't miss it) with the information about the acount, the channel and the pissitions for the buttons:
1. Change the channel ID. You should use the ID of your text channel in a string (for example: "1142540178209120376"). To get channel's ID just press right click on the name of the channel and choose the last option
(you have to enable Developer mode first).
2. Change the token. You have to type the token of the account you are going to use for this. To find this token(Opend Discord from browser or install better discord and enable "dev tools". You will only need to do this once so I recomend you to go with the browser)
go to a text channel, press ctrl+shift+i click "Network" on the top bar type anything in the chat, you will see the "typing" appear under the "Name", click on it and scroll down in the list that appears next to it until you find the **Request Headers**,
from there you need to copy the token next to "authorization" and paste it as string in the code.
3. Change the click coordinates for the "Dismiss" button and the "Farm" button to fit your screen's resolution. Use the resolutionCalculator.py to calculate the coordinates for each one.
You want the coordinates of the "Dismiss" button so you can remove the message only visible to you that confirms your verification, so the chat doesn't move upwards every time you verify.
You want the coordinates of the "Farm" button so the program can automatically move the cursor on the "Farm" button and click while you are afk.


When you run the code you have to place the cursor on the "Farm" button and press the first click (make sure you are not in a verification stage when you do that), after that it will do the rest (It's important to not move the cursor while farming)
The program will give you feedback from time to time ("Heartbeat received") so you will know it's still running. It will also give you feedback no event received for sometime and will activate an autoclicker (to prevent BOT from stoping due to "no 'Farm' button activation").
If at some point for any reason the BOT lose connection with the Discord servers it will repeatedly try to reconnect until it does and continue farming.
It's important to use a private channel, because if anyone types something in the channel you are farming it's going to mess up your calculations and prevent the BOT from farming
It doesn't work if the Caps-Lock is enabled so if you want to stop it at any point just enable the Caps-Lock and wait untill it clicks the next farm, or you can just click it manually





**How to use the resolutionCalculator.py**

For this you will also have to install "keyboard" (the same way as before)

Just run the resolutionCalculator.py, place the cursor on the field/button you want, press the "spacebar" and it will print the current coordinates of the cursor. You can do this as many times as you want. To terminate the program just press "esc"

While calculating:
1. Make sure that BOTs message is on the bottom of the text channel while calculating for the "Farm" button
2. Calculate the coordinates of the "Dismiss" button, while it is visible to you (Don't try to guess where it whould be... You might need to play untill verification needed for this one. just type the verification message and calculate the coordinates for the "Dismiss")
3. Make sure that the cursor is on the right place-button
