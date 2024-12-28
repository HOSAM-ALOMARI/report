import pyautogui as pat
import time

for i in range(100):
    print(f"Iteration {i+1}:")
    print(pat.position()) 

    pat.click(x=868, y=125, duration=1)
    pat.click(x=1056, y=460, duration=1)
    pat.click(x=1150, y=529, duration=1)
    pat.click(x=1150, y=479, duration=1)
    pat.click(x=1178, y=527, duration=1)
    pat.click(x=1161, y=477, duration=1)
    pat.click(x=1178, y=410, duration=1)
    pat.click(x=1044, y=611, duration=2)
    pat.click(x=1161, y=593, duration=2)
    
    time.sleep(5)  
