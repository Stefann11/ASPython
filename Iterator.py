import os
from builtins import print

path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

folder = os.fsencode(path)

filenames = []
brojac=0

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.html') ):
        filenames.append(filename)
        brojac=brojac+1


if __name__ == "__main__":
    print(brojac)
    for i in range(0,len(filenames),1):
        print(filenames[i])