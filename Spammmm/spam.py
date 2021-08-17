import pyautogui
import time

isi = input("apa isi pesannya? (bisa paste dari clipboard):  ")
spam = int(input("berapa kali spam?  "))
delay = int(input("berapa kali permilidetik munculnya?  "))

print("\n\n1.tekan enter (5detik)")
print("2.minimize kode ini/biarkan")
print("3.masuk ke browser/sosmed")
mulai = input("tekan enter...")


print("prosess...")

time.sleep(5)


for i in range(0,spam):         #Just Funn...
	if isi != "":
		pyautogui.typewrite(isi+" {}".format(i)+"..")     
		#pyautogui.typewrite(isi)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")

