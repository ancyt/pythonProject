fp=open("C:\\Users\\AncyThomas\\Documents\\fileop.txt")
data=(fp.read())

lines=data.split("\n")
for line in lines:
    words=line.split(" ")
    for word in words:
        print(word)
fp.close()