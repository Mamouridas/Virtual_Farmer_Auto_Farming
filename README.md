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



Before we start, enable Developer mode if you are using the Discord app (settings>advanced>Developer Mode)

You'll also have to change a few things in the code so it will be able to run properly for you:
1. Change the channel ID in line 35. You should use the ID of your text channel in a string (for example: "1142540178209120376"). To get channel's ID just press right click on the name of the channel and choose the last option
(you have to enable Developer mode first).
2. Change the token in line 44. You have to type the token of the account you are going to use for this. To find this
token, go to a text channel, press ctrl+shift+i click "Network" on the top bar type anything in the chat, you will see the "typing" appear under the "Name", click on it and scroll down in the list that appears next to it until you find the **Request Headers**, from there you need to copy the token next to "authorization" and paste it as string in the code.
3. Change the click coordinates for your chat bar (line 83), the "Dismiss" button (line 96) and the "Farm" button (line 99) to fit your screen's resolution. Use the resolutionCalculator.py to calculate the coordinates for each one of the above.
You want the coordinates of the chat bar so the program automatically click and type the verify code when needed
you want the coordinates of the "Dismiss" button so you can remove the message only visible to you that confirms your verification, so it won't destroy all the other clicks
You want the coordinates of the "Farm" button so the program can automatically move the cursor on the "Farm" button and click while you are afk.


When you run the code you have to place the cursor on the "Farm" button and press the first click (make sure you are not in a verification stage when you do that), after that it will do the rest (It's important to not move the cursor while farming)
The program will give you feedback from time to time ("Heartbeat received") so you will know it's still running
It doesn't work if the Caps-Lock is enabled. If you want to stop it at any point just enable the Caps-Lock and wait untill it clicks the next farm, or you can just click it manually





**How to use the resolutionCalculator.py**

For this you will also have to install "keyboard" (the same way as before)

Just run the resolutionCalculator.py, place the cursor on the field/button you want, press the "spacebar" and it will print the current coordinates of the cursor. You can do this as many times as you want. To terminate the program just press "esc"

While calculating:
1. Make sure that BOTs message is on the bottom of the text channel while calculating for the "Farm" button
2. Calcilate the coordinates of the "Dismiss" button, while it is visible to you (you might need to play untill verification needed and answer so you can see and calculate the coordinates for the "Dismiss" button)
3. Make sure that the cursor is on the right place-button
