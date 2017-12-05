from random import shuffle

list =[]
def getDeck(name):
    f = open(name,"r")
    for line in f:
        list.append(line.strip())
    f.close()
def sh():
    shuffle(list)

def draw(x):
    for i in range (0,x):
        print(list[0])
        list.append(list.pop(0))

def peek(x):
    for i in range (0,x):
        print(list[i%len(list)])
def banish(x):
    list.append(list.pop(x%len(list)))

def swap(x,y):
    temp = list[x%len(list)]
    list[x%len(list)] = y
    list[y%len(list)] = temp

def show():
    for x in list:
        print(x)


def write(name):
    f = open(name,"w")
    for x in list:
        f.write(x)
    f.close()
getDeck("deck")
sh()
