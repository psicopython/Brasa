import json


def compilador(lines):
    keys = None
    with open("brasa/kwords.json",) as kwordsfile:
        keys = json.load(kwordsfile)

    newScript = []
    for line in lines:
        countT = line.count("\t")
        countN = line.count("\n")
        line = line.strip("\t")
        line = line.strip("\n")
        newLine = []
        anterior = None
        for word in line.split(" "):
            word = word.rstrip(" ")
            if anterior == "não"  and  word == "é":
                newLine.pop()
                newLine.append("is not ")
                continue
            newLine.append( str( keys.get(word) or word ) )
            anterior = word
        newScript.append( str((' ' * 4) * countT) + " ".join(newLine).rstrip() + "\n" * countN )
    return "".join(newScript)