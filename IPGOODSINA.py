#coded S237N3   《》KingHacker 《》

#majol of script
import time
import random

def change_ip():
         while True:
             new_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
             print(f"Changing IP to: {new_ip}")
             time.sleep(5)

change_ip()
