import pyautogui
import keyboard

space_pressed = False
esc_pressed = False

while True:
    key_event = keyboard.read_event()
    
    if key_event.event_type == keyboard.KEY_DOWN:
        if key_event.name == "space" and not space_pressed:
            print(pyautogui.position())
            space_pressed = True
        elif key_event.name == "esc" and not esc_pressed:
            print("Calculation complete!")
            exit(0)
    elif key_event.event_type == keyboard.KEY_UP:
        if key_event.name == "space":
            space_pressed = False
        elif key_event.name == "esc":
            esc_pressed = False

