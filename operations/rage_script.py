import pyautogui
import os
import threading

stop_threads = False
threads = []

from arguments.arguments import image_folder, final_position_local, region



# Main function of CLICK-DRAG-RELEASE
def find_and_drag(start, end, pas, image_folder, final_position, region):
    print("Căutăm imaginile pe ecran...")
    global stop_threads
    while not stop_threads:
        for i in range(start, end, pas):
            if stop_threads:  # Verifică dacă trebuie să oprească
                print(f"Thread-ul pentru {start}-{end} s-a oprit.")
                return
            image_path = os.path.join(image_folder, f"{i}.png")
            print(f"Verificăm imaginea: {image_path}")

            try:
                location = pyautogui.locateOnScreen(image_path, confidence=0.8, region=region)

                if location is not None:
                    print(f"Imagine găsită la {location}!")
                    center = pyautogui.center(location)

                    print(f"Mutăm cursorul la {center} și apăsăm click stânga...")
                    pyautogui.moveTo(center)
                    pyautogui.mouseDown()

                    print(f"Mutăm obiectul la poziția finală {final_position}...")
                    pyautogui.moveTo(final_position, duration=0)

                    print("Eliberăm click stânga.")
                    pyautogui.mouseUp()

                    print("Acțiune finalizată cu succes!")
                    break

            except pyautogui.ImageNotFoundException:
                print(f"Imaginea {image_path} nu a fost găsită. Continuăm să căutăm...")

def start_threads():
    global threads, stop_threads
    stop_threads = False  # Resetează flag-ul de oprire

    threads = [
        threading.Thread(target=find_and_drag, args=(1, 7, 1, image_folder, final_position_local, region), daemon=True),
        threading.Thread(target=find_and_drag, args=(7, 13, 1, image_folder, final_position_local, region), daemon=True),
        threading.Thread(target=find_and_drag, args=(13, 19, 1, image_folder, final_position_local, region), daemon=True),
    ]

    for thread in threads:
        thread.start()

def stop_all_threads():
    global stop_threads, threads
    stop_threads = True  # Setează flag-ul pentru a opri firele
    for thread in threads:
        thread.join()  # Așteaptă ca toate firele să se oprească
    threads = []  # Curăță lista firelor
    print("Toate firele s-au oprit.")
