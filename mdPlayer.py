# Author Dahni
# Comunity : Genius Code Party
# Github : Masdahni1337
from typing import Text
import py_cui
import os
import logging
import json
import time
from py_cui import widget_set
from py_cui.widgets import TextBox
from pygame import mixer

class baseData:
    pathMusik = "D:\Backup\Musik\Luar" #change with your path music
    pathList = "E:\Elite Spirit\Audio\Instrumental" #change with your path playlist
    ngulang = False # if you wanna loop, just change False to True

def listmusik():
    nSong = []
    nameSong = []
    if os.path.exists(baseData.pathMusik):
        i = 0
        for filemptri in os.listdir(baseData.pathMusik):
            if filemptri.endswith(".mp3"):
                i += 1
                nSong.append(i)
                nameSong.append(filemptri)
    iMusik = [{"No":val[0], "Song":val[1]} for val in zip(nSong, nameSong)]
    with open('song.json', 'w') as svjson:
        json.dump(iMusik, svjson, sort_keys=True, indent=4)
    return nameSong

def listplay():
    pnList = []
    pnSong = []
    if os.path.exists(baseData.pathList):
        i = 0
        for filemptri in os.listdir(baseData.pathList):
            if filemptri.endswith(".mp3"):
                i += 1
                pnList.append(i)
                pnSong.append(filemptri)
    iMusik = [{"No":val[0], "Song":val[1]} for val in zip(pnList, pnSong)]
    with open('playlist.json', 'w') as svjson:
        json.dump(iMusik, svjson, sort_keys=True, indent=4)
    return pnSong
        
class MdPlayer:
    listmusik()
    def __init__(self, master: py_cui.PyCUI):

        self.master = master
        self.listmusik =  self.master.add_scroll_menu('List Music', 0, 0, row_span=7, column_span=3)
        self.listmusik.set_selected_color(py_cui.BLACK_ON_WHITE)
        self.listmusik.add_item_list(listmusik())
        self.listmusik.add_key_command(py_cui.keys.KEY_SPACE, self.itemMusik)
        self.listmusik.add_key_command(py_cui.keys.KEY_BACKSPACE, self.pauseMusik)

        self.playlist =  self.master.add_scroll_menu('Playlist', 0, 3, row_span=7, column_span=3)
        self.playlist.set_selected_color(py_cui.BLACK_ON_WHITE)
        self.playlist.add_item_list(listplay())
        self.playlist.add_key_command(py_cui.keys.KEY_SPACE, self.itemPl)
        self.playlist.add_key_command(py_cui.keys.KEY_BACKSPACE, self.pauseMusik)
        self.playing = self.master.add_text_box('Playing', 7, 0, column_span=6)

    def itemMusik(self):
        mixer.init()
        filemusik = "{}\{}".format(baseData.pathMusik, self.listmusik.get())
        mixer.music.load(filemusik)
        if(baseData.ngulang == True):
            mixer.music.play(loops=-1)
            self.playing = self.master.add_text_box('Playing', 7, 0, column_span=6, initial_text='{}...'.format(self.listmusik.get()))
        elif mixer.music.play() == None:
            songQueue = []
            nameSong = []
            okk = self.listmusik.get_selected_item_index()
            if listmusik()[okk] == self.listmusik.get():
                for idx in range(okk, len(listmusik())):
                    xo = listmusik()[idx]
                    quefile = "{}\{}".format(baseData.pathMusik, xo)
                    songQueue.append(quefile)
                    nameSong.append(xo)
            for ii in range(0, len(songQueue)):
                mixer.music.queue(songQueue[ii-ii+1])
                self.playing = self.master.add_text_box('Playing', 7, 0, column_span=6, initial_text='{}...'.format(nameSong[ii-ii+1]))
        else:
            mixer.music.play()
        self.playing = self.master.add_text_box('Playing', 7, 0, column_span=6, initial_text='{}...'.format(self.listmusik.get()))
            # print('f')
                
    def pauseMusik(self):
        mixer.music.pause()

    def itemPl(self):
        mixer.init()
        filemusik = "{}\{}".format(baseData.pathList, self.playlist.get())
        mixer.music.load(filemusik)
        if(baseData.ngulang == True):
            mixer.music.play(loops=-1)
        else:
            mixer.music.play()
        self.playing = self.master.add_text_box('Playing', 7, 0, column_span=6, initial_text='{}...'.format(self.playlist.get()))


root = py_cui.PyCUI(8, 6)
root.set_title('MD Player')
root.enable_logging(logging_level=logging.ERROR)
s = MdPlayer(root)
root.start()
