import time, pyxhook, sys
from random import randint as random
width = 40
height = 20
ch = ''
def OnKeyPress(event):
    global ch
    ch = event.Key
hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
def printat(x: int, y: int, s): print("\033["+str(y)+";"+str(x)+"H"+s, end="")
segments = [[width/2, height/2], [width/2+1, height/2]]
direction = [0, 1]
food = [random(2, width-1), random(2, height-1)]
score = 0
while True:
    if ch == 'w' and not direction[1] == 1: direction = [0, -1]
    elif ch == 's' and not direction[1] == -1: direction = [0, 1]
    elif ch == 'a' and not direction[0] == 1: direction = [-1, 0]
    elif ch == 'd' and not direction[0] == -1: direction = [1, 0]
    segments.append([segments[-1][i]+direction[i] for i in range(2)])
    if sum([food[i] == segments[-1][i] for i in range(2)]) == 2:
        score += 1
        food = [random(2, width-1), random(2, height-1)]
    else:
        del segments[0]
    if any([sum([segments[j][i] == segments[-1][i] for i in range(2)]) == 2 for j in range(len(segments)-1)]) or segments[-1][0]%width==0 or segments[-1][1]%height==0:
        print("GAME OVER: "+str(score))
        break
    for i in range(width*2):
        for j in range(height*2):
            printat(i, j, " ")
    for i in range(width):
        printat(i, height, "#")
    for j in range(height):
        printat(width, j, "#")
    printat(0, 0, "")
    for i, seg in enumerate(segments):
        printat(int(seg[0]), int(seg[1]), "%" if i == len(segments)-1 else "@")
    printat(int(food[0]), int(food[1]), "*")
    printat(int(width/2), height+2, "SCORE: "+str(score))
    sys.stdout.flush()
    time.sleep(0.12 if direction[0] != 0 else 0.2)