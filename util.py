import numpy as np
import random
import pickle


def about(n):
    s = n/10
    n = np.random.normal(n, scale=s)
    return n

def create_messages(msg_list, adlink, emojis):
    msg = random.choice(msg_list)
    emoji = random.choice(emojis)
    msg = msg + ' ' + emoji
    messages = [msg, adlink]
    return messages

def generate_phone(n_digits=9, ddi='55', ddd='34', first_numbers='988'):
    digits = [0,1,2,3,4,5,6,7,8,9]
    phone = [i for i in ddi + ddd + first_numbers]
    n = n_digits - len(first_numbers)
    for i in range(n):
        phone.append(str(random.choice(digits)))
    return ''.join(phone)

def generate_phone_list(n):
    phone_list = []
    for _ in tqdm(range(n)):
        phone_list.append(generate_phone())
    phone_list = list(set(phone_list))
    return phone_list

def read_pickle(file):
    with open(file, 'rb') as handle:
         load = pickle.load(handle)
    return load

def to_pickle(var, dir):
    directory = dir + '.pickle'
    with open(directory, 'wb') as handle:
        pickle.dump(var, handle)
    return