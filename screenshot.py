import pyautogui
from os import chdir,path # we use os module to intreact with operating system


chdir(path.join(path.expanduser('~'), 'Desktop')) # Here  we set the path to desktop



img = pyautogui.screenshot(region = (12,25,300,100)) #If you do not want to take a full screen screenshot then you can use region
                                                           # where you pass the tupple

img.save("screenshot.jpg")


print("Screenshot Saved to Desktop")
