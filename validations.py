import re
import csv
from random import randrange
from modelUser import User
from tkinter import messagebox

# Constants
#CACHE = list()
PATH_CSV = "./docs/nodes.csv" 
PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$')

def _init_cache() -> tuple:
    with open(PATH_CSV, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=' ')
        user = User()
        for row in reader:
            if row == None:
                return ([],[])
            else:
               *_, user.id , _ = row
        return ([user],[user.id])



def validation_data(user_response, password_response):
    if PATTERN_USER.search(user_response) == None or PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user', "Credenciales no válidas")
    else:
        messagebox.showinfo('user', "Usuario registrado")
        CACHE,CACHE_ID = _init_cache()
        print(CACHE,CACHE_ID)
        with open(PATH_CSV, "a+") as csvfile:
            file_writer = csv.writer(csvfile, delimiter=' ')
            user = User(user_response, password_response)
            num = randrange(1000)
            while num in CACHE_ID:
                num = randrange(1000)
            user.id = num
            user.next_node = num if not CACHE else CACHE[len(CACHE)-1].id 
            CACHE.append(user)
            print(user)
            file_writer.writerow(user.get_data())
