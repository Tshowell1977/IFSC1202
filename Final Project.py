class Sketch:
    def __init__(self, size):
        self.size=size
        self.ypos=0
        self.xpos=0
        self.direction='U'
        self.pen='U'
        self.canvas =[[' ' for i in range(self.size) ] for j in range(self.size)]    
    def printsketch(self):
        horiz ='+' + self.size*'-' + '+'
        print(horiz)
        for i in range(self.size):
            k=self.size-i-1
            print('|', end='')
            for j in range(self.size):
                print(self.canvas[k][j], end='')
            print('|')
        print(horiz)
        print('X = ', str(self.xpos)+ ' Y = '+ str(self.ypos)+ ' Direction = ' + self.direction)
    def penup(self):
        self.pen='U'
    def pendown(self):
        self.pen='D'
    def turnleft(self):
        if self.direction=='U':
            self.direction='L'
        elif self.direction=='L':
            self.direction='D'
        elif self.direction=='D':
            self.direction='R'
        elif self.direction=='R':
            self.direction='U'
    def turnright(self):
        if self.direction=='U':
            self.direction='R'
        elif self.direction=='L':
            self.direction='U'
        elif self.direction=='D':
            self.direction='L'
        elif self.direction=='R':
            self.direction='D'
    def move(self, distance):
        prevy=self.ypos
        prevx=self.xpos
        if self.direction=='U':
            if self.xpos + distance < self.size:
                self.xpos += distance
            else:
                self.xpos=self.size           
        if self.direction=='D':
            if self.xpos - distance >=0:
                self.xpos -= distance
            else:
                self.xpos=0            
        if self.direction=='R':
            if self.ypos + distance < self.size:
                self.ypos += distance
            else:
                self.xpos=self.size        
        if self.direction=='L':
            if self.ypos - distance >=0:
                self.ypos -= distance
            else:
                self.ypos=0    
        miny=min(prevy, self.ypos)
        maxy=max(prevy, self.ypos)
        minx=min(prevx, self.xpos)
        maxx=max(prevx, self.xpos)     
        if self.pen=='D':
            for i in range(miny, maxy+1):
                for j in range(minx, maxx+1):
                    self.canvas[j][i]='*'
file = open('/workspace/IFSC1202/Cshape.txt', 'r')
lines = file.readlines()       
size=int(lines[0])
obj=Sketch(size)
for i in range(1, len(lines)):
    if lines[i].find(',')==-1: 
        command=lines[i].strip()
        if command=='1':
            obj.penup()
        if command=='2':
            obj.pendown()
        if command=='3':
            obj.turnright()
        if command=='4':
            obj.turnleft()
        if command=='6':
            obj.printsketch()
    else:
        command, distance=lines[i].strip().split(',')
        obj.move(int(distance))