import os
import git
from chardet.universaldetector import UniversalDetector
import codecs
import io


def GitHubDownLoad(githubLink: str):
    try:
        git.Git().clone(githubLink)
    except:
        print("Error")


print("Enter a link to the repository")
githubLink = str(input())
nameRep = githubLink[19:]
nameRep = nameRep[nameRep.find("/")+1:]
print(nameRep)
GitHubDownLoad(githubLink)
fileOut = io.open(nameRep+".txt","w",encoding="utf-8")
os.chdir(nameRep)
file = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        path = os.path.join(root, name)
        if path.find(".git") != -1:
            continue
        file.append(path)

for filename in file:
    detector = UniversalDetector()
    with open(filename, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
            detector.close()
    encoding = detector.result["encoding"]
    fileObj = codecs.open(filename, "r", encoding,errors='ignore')
    try:
        text = fileObj.read()
    except:
        print("Cant read" + filename)
        print(encoding)
        fileObj.close()
        continue
    fileObj.close()
    fileOut.write("\n")
    fileOut.write(filename)
    fileOut.write("\n")
    fileOut.write("_______________________________________________________________")
    fileOut.write("\n")
    fileOut.write(text)
    fileOut.write("\n")
    fileOut.write("_______________________________________________________________")
