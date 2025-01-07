from pynput import keyboard
from ui.interface import update_text_color
from operations.rage_script import start_threads, stop_all_threads

script_enabled = False

# Pornirea listener-ului pentru taste
def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def on_press(key):
    if key == keyboard.Key.f2:
        toggle_script()




def toggle_script():
    global script_enabled, mouse_thread

    if not script_enabled:
        script_enabled = True
        print("AK Spray: ENABLED")
        update_text_color(script_enabled)
        start_threads()
    else:
        script_enabled = False
        print("AK Spray: DISABLED")
        update_text_color(script_enabled)
        stop_all_threads()

