from urllib import request
from zipfile import ZipFile
from io import BytesIO
from os import getcwd, mkdir, path

urlPlace = "https://downloads.sourceforge.net/project/java-game-lib/Official%20Releases/LWJGL%202.9.3/lwjgl-2.9.3.zip?r" \
       "=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fjava-game-lib%2Ffiles%2FOfficial%2520Releases%2FLWJGL%25202.9.3" \
       "%2Flwjgl-2.9.3.zip%2Fdownload&ts=1530563265 "

cwd = getcwd()[:-10]

with ZipFile(BytesIO(request.urlopen(urlPlace).read()), 'r') as lwjgl:
    for name in lwjgl.namelist():
        if 'native/' in name:
            if name[-1] == "/":
                dirName = cwd + name[name.index('native'):].replace("/", "\\")
                if not path.exists(dirName):
                    mkdir(cwd + name[name.index('native'):].replace("/", "\\"))
            else:
                file = lwjgl.read(name)
                fileName = name[name.index('native'):].replace("/", "\\")
                with open(cwd + fileName, "wb") as outFile:
                    outFile.write(file)

