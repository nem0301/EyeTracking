class TrackingPointer:
    defaultMovementSpeed = 40;
    directionOfMovement = True;
    x = 0;
    y = 0;
    
    
    def __init__ (self, width, height):
        self.width = width;
        self.height = height;  
        self.slope = float(height) / float(width);         
    
    def horizontalMoving(self):
        
        if self.directionOfMovement:
            if self.x > self.width:
                self.directionOfMovement = False;
            else:
                self.x += self.defaultMovementSpeed           
        else:
            if self.x < 0:
                self.directionOfMovement = True;
            else:
                self.x -= self.defaultMovementSpeed
        
        self.y = self.height / 2;
        
    def veticalMoving(self):
        
        if self.directionOfMovement:
            if self.y > self.height:
                self.directionOfMovement = False;
            else:
                self.y += self.defaultMovementSpeed;           
        else:
            if self.y < 0:
                self.directionOfMovement = True;
            else:
                self.y -= self.defaultMovementSpeed
        
        self.x = self.width / 2;    
        
    def diagonalMoving1(self):
        
        if self.directionOfMovement:
            if self.x > self.width:
                self.directionOfMovement = False;
            else:
                self.x += self.defaultMovementSpeed ;           
        else:
            if self.x < 0:
                self.directionOfMovement = True;
            else:
                self.x -= self.defaultMovementSpeed ;
        
        self.y = self.slope * self.x;
        
    def diagonalMoving2(self):
        
        if self.directionOfMovement:
            if self.x > self.width:
                self.directionOfMovement = False;
            else:
                self.x += self.defaultMovementSpeed ;           
        else:
            if self.x < 0:
                self.directionOfMovement = True;
            else:
                self.x -= self.defaultMovementSpeed ;
        
        self.y = self.height - self.slope * self.x;
    
    def center(self):
        self.x = self.width / 2;
        self.y = self.height / 2;
            