import billboard
from PyLyrics import *

lyrics = []      #list for lyrics found of the top songs
songs = []       #list for songs in the top no duplicates
names = []       #list of the name of the songs to avoid duplicates

chart = billboard.ChartData('hot-100')                  #get hot 100
while chart.previousDate > "2017-12-01":                #up to date
    for song in chart:
        if song.title not in names:
            songs.append(song)                          #append song
            names.append(song.title)                    #append title to avoid duplicates
    chart = billboard.ChartData('hot-100', chart.previousDate)

for song in songs:
    try:
        'print(song.title+" by "+song.artist)'
        lyrics.append(PyLyrics.getLyrics(song.artist, song.title))               #append lyrics
    except Exception as e:              #if lyrics not found
        print(e)

f = open("lyrics.txt", "w+")                #write lyrics to file
f.write(str(len(lyrics))+" "+str(len(songs))+"\n")
for x in lyrics:
    f.write(x)

f.close()
