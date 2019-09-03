from os import listdir
from os.path import isfile, join
import eyed3

mypath = '/Users/zsoltsipos/Downloads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.__contains__("mp3")]

audiofile = eyed3.load(join(mypath, onlyfiles[3]))

#audiofile.tag.save()

print(audiofile.tag.title)
print(audiofile.tag.artist)