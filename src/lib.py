
# import os
import requests
import time
import random
import sys


# REMOVE FILES


# def removefiles():
#     folder_path = (r'.')
#     # using listdir() method to list the files of the folder
#     test = os.listdir(folder_path)
#     # taking a loop to remove all the images
#     # using "" extension to remove only png images
#     # using os.remove() method to remove the files
#     for images in test:
#         if images.endswith(".png"):
#             os.remove(os.path.join(folder_path, images))

# PATH

def PATH(file):
    BMPMatrix = './screen/' + file + '.png'
    return BMPMatrix


# RANDOM TIMES


def randnum(i, f):
    return random.randint(i, f)


# PROGRESSBAR


def progress(count, total, status=''):
    bar_len = 38
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 0)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write(':: %s :: %s%s [[%s]]\r' % (status, percents, '%', bar))
    sys.stdout.flush()


# LARRY
def larry():
    LARRY = ["Let The Carnage Begin", "The Stage Is Set, The Green Flag Drops!",
             "Is About To Blow", "Unleash His Hard Fury", "Go Go SLP"]
    return LARRY[randnum(0, 4)]

# GA


def ga(ev):
    ACCOUNT = sys.argv[2]

    payload = {
        'v': 1,
        'tid': 'UA-111264361-1',
        'cid': 'Autoxie',
        't': 'event',
        'ec': ev,
        'ea': ACCOUNT.upper() + ' ON windows',
        'el': 'windows'
    }

    progress(0, 100, 'LOADING...')

    r = requests.post("http://www.google-analytics.com/collect", data=payload)

    if r.ok:
        progress(100, 100, ev)
        time.sleep(1)
    else:
        progress(0, 100, 'TRACKING ERROR!')
        time.sleep(1)
