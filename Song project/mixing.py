#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     06/03/2014
# Copyright:   (c) Admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    songList = ['Dukes','DragRace','AreYouSureHank','OutlawBit','WagonWheel','CountryBoyCanSurvive','GoneCountry', 'Cruise']
    songLyrics = {}
    songList, songLyrics = readSongs(songList, songLyrics)
    #print(songLyrics)
    mixed = mixLyrics(songLyrics, songLyrics[songList[0]], songLyrics[songList[1]])
    f2 = open('output.txt', 'w')
    f2.write(' '.join(mixed))
    #print (' '.join(mixed))

def readSongs(songList, songLyrics):
     for title in songList:
         f = open(title+'.txt', 'r')
         songLyrics[title]=f.read()
     return songList, songLyrics

def mixLyrics(songLyrics, songA, songB):
    wordsA = songA.split()
    wordsB = songB.split()
    mixed = []
    i=0
    lastSwitch=0
    while i<len(wordsA):
        j=0
        mixed.append(wordsA[i])
        while j<len(wordsB):
            tempA = wordsA[i]
            tempB  = wordsB[j]
            if tempA == tempB and len(tempA)>2 and lastSwitch>2:
                wordsA, wordsB = wordsB, wordsA
                i,j = j,i
                wordsA=wordsA[i:]
                wordsB=wordsB[j+1:]
                i=0
                lastSwitch=0
                break;
            else:
                j+=1


        i+=1
        lastSwitch+=1

    return mixed

if __name__ == '__main__':
    main()
