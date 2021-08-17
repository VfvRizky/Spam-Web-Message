import pyautogui
import webbrowser
import time

message = input("apa isi pesannya? (bisa paste dari clipboard):  ")
repeats = int(input("berapa kali spam?  "))
delay = int(input("berapa kali permilidetik munculnya?  "))

print("\n\n1.tekan enter (5detik)")
print("2.minimize kode ini/biarkan")
print("3.masuk ke browser/sosmed")
isLoaded = input("tekan enter...")


print("prosess...")

time.sleep(5)


for i in range(0,repeats):         #Just Funn...
	if message != "":
		pyautogui.typewrite(message+" {}".format(i)+"..")     
		#pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")

