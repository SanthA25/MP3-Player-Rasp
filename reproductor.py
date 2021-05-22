#pyuic5.exe -x plotter.ui -o plotter.py
import os
import sys
import time
import eyed3
from PyQt5 import QtGui, QtCore
from mp3 import *
from pygame import *
import pygame

pygame.mixer.init()
pygame.display.init()

playlist = []
playlist.append ( "[9] CJ - Whoopty.mp3" )
playlist.append ( "[8] ACDC - Highway To Hell.mp3" )
playlist.append ( "[7] Bee Gees - Stayin' Alive.mp3" )
playlist.append ( "[6] OneRepublic - Secrets.mp3" )
playlist.append ( "[5] Panic! at the Disco - High Hopes.mp3" )
playlist.append ( "[4] Simple Plan - Perfect.mp3" )
playlist.append ( "[3] The Goo Goo Dolls - Iris.mp3" )
playlist.append ( "[2] Masked Wolf - Astronaut In The Ocean.mp3" )
playlist.append ( "[1] Coldplay - Yellow.mp3" )
playlist.append ( "[0] Jaden - Rainbow Bap.mp3" )

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        for i in playlist:
            pos = 0
            self.listWidget.insertItem(pos,i)
            pos += 1

        self.listWidget.setCurrentRow(0)
        self.lineEdit.setReadOnly(True)
        #------------------------------------
        self.listWidget.itemClicked.connect(self.playSong)
        self.playpButton.clicked.connect(self.playPause)
        self.stopButton.clicked.connect(self.stopSong)
        self.nextButton.clicked.connect(self.nextSong)
        self.prevButton.clicked.connect(self.prevSong)

    def playSong(self):
        song = self.listWidget.currentItem().text()[4:]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        audiofile = eyed3.load(song)
        album_n = ''.join(map(str,audiofile.tag.track_num))
        self.lineEdit.setText("")
        self.lineEdit.setText(audiofile.tag.artist + " - " + audiofile.tag.title + " | " + audiofile.tag.album + " - " + album_n[0])
        # print(type(audiofile.tag.track_num))
        # print(''.join(map(str,audiofile.tag.track_num)))

    def playPause(self):
        self.status = pygame.mixer.music.get_busy()
        if self.status:
            pygame.mixer.music.pause()
        if not self.status:
            pygame.mixer.music.unpause()
        self.status = not self.status

    def stopSong(self):
        pygame.mixer.music.stop()

    def nextSong(self):
        self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
        self.playSong()

    def prevSong(self):
        self.listWidget.setCurrentRow(self.listWidget.currentRow()-1)
        self.playSong()


if __name__ == "__main__":

	app = QtWidgets.QApplication([])
	window = Ui_MainWindow()
	window.show()
	app.exec_()
