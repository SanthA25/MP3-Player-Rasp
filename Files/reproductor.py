#pyuic5.exe -x plotter.ui -o plotter.py

#se importan las librerias
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

#se crea la lista y se agregan las canciones
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
	
	#se agregan las canciones al widget de lista
        for i in playlist:
            pos = 0
            self.listWidget.insertItem(pos,i)
            pos += 1
	
	#se establece por default al primer item
        self.listWidget.setCurrentRow(0)
        self.lineEdit.setReadOnly(True)
        #------------------------------------
	#botones y acciones a realizar
        self.listWidget.itemClicked.connect(self.playSong)
        self.playpButton.clicked.connect(self.playPause)
        self.stopButton.clicked.connect(self.stopSong)
        self.nextButton.clicked.connect(self.nextSong)
        self.prevButton.clicked.connect(self.prevSong)
	
    #cada vez que se de un click cualquier item de la lista, se reproduce esa cancion 	
    def playSong(self):
	#se carga la cancion seleccionada y se reproduce
        song = self.listWidget.currentItem().text()[4:]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
	
	#se muestran los datos de la cancion en reproduccion
        audiofile = eyed3.load(song)
        album_n = ''.join(map(str,audiofile.tag.track_num))
        self.lineEdit.setText("")
        self.lineEdit.setText(audiofile.tag.artist + " - " + audiofile.tag.title + " | " + audiofile.tag.album + " - " + album_n[0])
        # print(type(audiofile.tag.track_num))
        # print(''.join(map(str,audiofile.tag.track_num)))

    #verifica el estatus de la cancion y se reproduce o pausa segun el status
    def playPause(self):
        self.status = pygame.mixer.music.get_busy()
        if self.status:
            pygame.mixer.music.pause()
        if not self.status:
            pygame.mixer.music.unpause()
        self.status = not self.status

    #se para la reproduccion de la cancion actual
    def stopSong(self):
        pygame.mixer.music.stop()

    #se reproduce la siguiente cancion dentro de la lista
    def nextSong(self):
        self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
        self.playSong()

   #se reproduce la cancion anterior en la lista
    def prevSong(self):
        self.listWidget.setCurrentRow(self.listWidget.currentRow()-1)
        self.playSong()


if __name__ == "__main__":

	app = QtWidgets.QApplication([])
	window = Ui_MainWindow()
	window.show()
	app.exec_()
