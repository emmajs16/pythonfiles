import sys

for line in sys.stdin:
    s = line.replace("/n","")

    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ##counts = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"24":0,"24":0,"25":0}

    total_letters = []
    simplicity = 0

    for i in s:
        counts[ord(i)-97]+=1
    for values in  counts:
        if values != 0:
            total_letters.append(values)
            simplicity +=1
    ordered_letters = sorted(total_letters, key=int)
    elements_to_remove = len(ordered_letters)-2
    total = sum(ordered_letters)
    keep = (ordered_letters[len(ordered_letters)-1]+ordered_letters[len(ordered_letters)-2])
    print(total-keep)
