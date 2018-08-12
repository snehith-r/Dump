import os
import random
import platform
try:
    from msvcrt import getch #For windows
except ImportError: #For linux and maybe mac...
    def getch():
    
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def pressedkey():
	return getch() 

a=[[" " for i in range(60) ] for j in range(30) ]
for i in range(30):
	for j in range(60):
		if i==0 or i==29 or j==0 or j==59 :
			a[i][j]="X"
def gamemap():
	for i in range (30):
		for j in range(60):
			if i==0 or i==29 or j==0 or j==59:
				print(a[i][j],end='')
			else:
				print(a[i][j],end='')
		print()
pos="@"
x,y=28,1
a[28][1]=pos
def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') #For linux.. I don't know what to do about mac :/
	gamemap()
	
updater()

while True:
	pressedkey = getch()
	if pressedkey is 'w' or pressedkey is 'W':
		a[x][y]=" "
		x=x-1
		if x!=0:
			a[x][y]="@"
		else:
			print("wall")
			exit()
		updater()

	elif pressedkey is 's' or pressedkey is 'S':
		a[x][y]=" "
		x=x+1
		if x!=29:
			a[x][y]="@"
		else:
			print("wall")
			exit()
		updater()

	elif pressedkey is 'a' or pressedkey is 'A':
		a[x][y]=" "
		y=y-1
		if y!=0:
			a[x][y]="@"
		else:
			print("wall")
			exit()
		updater()

	elif pressedkey is 'd' or pressedkey is 'D':
		a[x][y]=" "
		y=y+1
		if y!=59:
			a[x][y]="@"
		else:
			print("wall")
			exit()
		updater()



	