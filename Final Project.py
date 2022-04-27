# Sketch - an object that holds the value and actions for the sketchpad with the following attributes and methods: o Attributes
        
    # size - size of the square canvas (determined when the object is initialized) 
    # Xpos - current x position of the turtle (0-size-1, initial = 0) 
    # ypos - current y position of the turtle (0-size-1, iniital = 0) 
    # direction - current direction of the turtle (U, D, L, R, initial = U) 
    # pen - pen is up or down (U, D, initial = U)
    # canvas - two dimensional list containing spaces or "*" (initial = "") 
    # Methods 
        # init (self, size)
        # Sets the size attribute based on the "size" parameter 
        # Sets the xpos attribute to 0 
        # Sets the ypos attribute to 0 
        # Sets the direction attribute to U 
        # Sets the pen attribute to U
        # Set the canvas to a two dimensional array (size x size) initialized to a space 
class Scetch:
    def __init__(self, size):
        self.size=size
        self.ypos=0
        self.xpos=0
        self.direction='U'
        self.pen='U'
        self.canvas =[[' ' for i in range(self.size) ] for j in range(self.size)]
        
    # printsketch - no arguments
    def printsketch(self):
    # Prints the canvas line by line. Be sure to add a nice border. 
    #   Hint: Print the canvas from the last line to the zeroth line using a -1 step. 
    #   This will put the origin at the bottom. Print the current x position, y position, 
    #    and direction under the canvas.
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
        
    
    # penup - no arguments
    def penup(self):
        # Sets pen to up (U) 
        self.pen='U'
   
    # pendown - no arguments
    def pendown(self):
        # Sets pen to down (D)
        self.pen='D'
    
    # turnleft - no arguments
    def turnleft(self):
        # Sets direction to new direction Hint: Check the current direction to determine the new direction 
        if self.direction=='U':
            self.direction='L'
        elif self.direction=='L':
            self.direction='D'
        elif self.direction=='D':
            self.direction='R'
        elif self.direction=='R':
            self.direction='U'
            
    # turnright - no arguments
    def turnright(self):
        # Sets direction to new direction Hint: Check the current direction to determine the new direction 
        if self.direction=='U':
            self.direction='R'
        elif self.direction=='L':
            self.direction='U'
        elif self.direction=='D':
            self.direction='L'
        elif self.direction=='R':
            self.direction='D'
    
    # move(self, distance)
    def move(self, distance):
    # Moves the turtle from the current x and y position along the current direction. 
    # If the pen is down, then put a asterisk along the path
    # Hint: You will have a different code snippet for each direction. 
    # If the turtle bumps into a border, just stop at the border of the canvas.
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
                    #######################################################
file = open('/workspace/IFSC1202/Cshape.txt', 'r')
lines = file.readlines()       

# Command Meaning
# 1       Pen up
# 2       Pen down
# 3       Turn right
# 4       Tutn left
# 5,10    Move forward 10 spaces (or some other number)
# 6       Print the canvas

size=int(lines[0])
obj=Scetch(size)
for i in range(1, len(lines)):
    #print(lines[i])
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