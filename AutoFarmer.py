#To install Library use "pip install 'library name'"
import json 
import time
import ctypes
import random
import pyautogui # install
import websocket #install
import threading #install
import requests #install
from pynput.keyboard import Key, Controller #install pynput

################################################################################################################################################################

# Set your specific channel ID here
specific_channel_id = 'PUT YOUR CHANNEL ID HERE'

# Replace with your token
token = "PUT YOUR TOKEN HERE"

# Replace with coordinates for Dismiss button
xDismiss, yDismiss = #Your coordinates should be in form x,y(example: 420, 1266)

# Replace with coordinates for Farm button
xFarm, yFarm = #Same here for the "Farm" button this time

################################################################################################################################################################

keyboard = Controller()

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("Heartbeat begin")
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d" : None
        }
        send_json_request(ws, heartbeatJSON)
        print("Heartbeat sent")
reconnect_delay = 5
while True:
    try:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=10&encoding=json')
        event = receive_json_response(ws)

        heartbeat_interval = event['d']['heartbeat_interval'] / 1000
        threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

        payload = {
            'op' : 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": "windows",
                    "$browser": "chrome",
                    "$device": 'pc'
                }
            }
        }

        send_json_request(ws, payload)

        last_event_time = time.time()
        simulate_click_enabled  = True

        def simulate_mouse_click():
            while True:
                time.sleep(1)
                if (time.time() - last_event_time >= 10 and simulate_click_enabled):
                    print("No embed reaction received. Auto click in 2 seconds")
                    time.sleep(2)
                    pyautogui.click()

        mouse_click_thread = threading.Thread(target = simulate_mouse_click)
        mouse_click_thread.daemon = True
        mouse_click_thread.start()

        while True:

            if ctypes.WinDLL("User32.dll").GetKeyState(0x14): #Checks if Caps Lock is on and if True stops the program
                print("Caps Lock is on! Program stopped")
                exit(0)


            event = receive_json_response(ws)

            try:
                if 'channel_id' in event['d'] and event['d']['channel_id'] == specific_channel_id:

                    last_event_time = time.time()

                    author_username = event['d']['author']['username']
                    message_content = event['d']['content']
                    embeds = event['d']['embeds']

                    print(f"{author_username}: {message_content}")
                    
                    for embed in embeds:
                        # Extract and print information from each embed
                        embed_title = embed.get('title', 'No Title')
                        embed_description = embed.get('description', 'No Description')

                        time.sleep(round(random.uniform(2.7,3.3),2)) #Delay between clicks


                        if (embed_title == "Antibot Verification"):
                            time.sleep(1)
                            codeList = embed_description.split(" ")
                            code = codeList[8][:-5].strip("*")
                            print(code)
                            answer = "/verify " + code
                            print(answer)

                            for char in answer: #Type the command + code
                                keyboard.press(char)
                                keyboard.release(char)
                                time.sleep(0.12)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            pyautogui.moveTo(xDismiss, yDismiss) #Remove private embed
                            time.sleep(2)
                            pyautogui.click()
                            pyautogui.moveTo(xFarm, yFarm) #Go to Farm again
                            time.sleep(1)

                        pyautogui.click()

                    op_code = event["op"]
                    if op_code == 11:
                        print('Heartbeat received')

            except Exception as e:
                print("")
    except websocket.WebSocketException as e:
        simulate_click_enabled = False
        print(f"WebSocket Exception: {e}")
        print(f"Attempting to reconnect in {reconnect_delay} seconds...")
        time.sleep(reconnect_delay)
        simulate_click_enabled = True
        print("Reconnection attempt complete")
        reconnect_delay *= 2


