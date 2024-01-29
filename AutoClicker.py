import time
import threading
from pynput.mouse import Button as MouseButton, Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener, KeyCode, Key
import random


class AutoClicker(threading.Thread):
  def __init__(self, delay, btn):
    super(AutoClicker, self).__init__()
    self.delay = delay
    self.btn = btn
    self.running = False
    self.program_running = True

  def start_clicking(self):
    self.running = True
    print("Starting clicking")
  def stop_clicking(self):
    self.running = False
    print("Stopping clicking")
  
  def exit(self):
    self.stop_clicking()
    self.program_running = False

  def run(self):
    while self.program_running:
      while self.running:
        mouse.click(self.btn)
        # time.sleep(self.delay)
        time.sleep(random.uniform(0.03, 0.06))
      time.sleep(0.1)


delay = 0.001
toggle_key = Key.ctrl_l
kill_key = KeyCode(char='i')
mouse = MouseController()
btn = MouseButton.left


click_thread = AutoClicker(delay, btn)
click_thread.start()

def on_press(key):
  if key == toggle_key:
    if click_thread.running:
      click_thread.stop_clicking()
    else:
      click_thread.start_clicking()

  elif key == kill_key:
    click_thread.exit()
    listener.stop()

with KeyboardListener(on_press=on_press) as listener:
  listener.join()