import time
import threading
from pynput.keyboard import Listener, KeyCode, Key, Controller

down_delay = 1
wait_delay = 1
button = KeyCode(vk=101)
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickButton(threading.Thread):
    def __init__(self, down_delay, wait_delay, button):
        super(ClickButton, self).__init__()
        self.down_delay = down_delay
        self.wait_delay = wait_delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                #101 - num 5
                keyboard.press(button)
                print('down')
                time.sleep(self.down_delay)
                print('up')
                keyboard.release(button)
                time.sleep(self.wait_delay)
            time.sleep(0.1)


keyboard = Controller()
click_thread = ClickButton(down_delay, wait_delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
