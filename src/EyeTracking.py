from tkinter import *
from threading import *
import time
import sys
        

class Window(Frame):
    def __init__(self, parent, acc=1):
        Frame.__init__(self, parent)
        self.parent = parent            
        self.initUI()
        self.acc = acc    
        
                
    def initUI(self):        
        self.parent.title("Window")        
        self.parent.attributes('-fullscreen', True)        
        self.bind("<KeyPress>", self.inputKey)
        self.pack()
        self.focus_set()                
        
        
        self.canvas = Canvas(self.parent, 
            width=self.parent.winfo_screenwidth(),
            height=self.parent.winfo_screenheight(),
            bg="black",                      
            )
        self.canvas.pack()   
        
        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()     

    def horizontal(self):
        start = time.time()
        xy = (0, self.height / 2)
        sign = 1
        delta = 70 * self.acc       
        while time.time() - start < self.time:
            r = abs(2*xy[0] - self.width)
            
            if r > self.width * 0.70:
                r = self.width * 0.70
            elif r < self.width * 0.70:
                r = self.width * 0.01                
            
            r = 1.0 - r / self.width 
            
            if xy[0] < 0:
                sign = 1
            if xy[0] > self.width:
                sign = -1    
            xy = (xy[0] + sign * delta * r, xy[1])             
            self.update(xy)            
            time.sleep(1/60)
            
        self.canvas.delete(ALL)
        
    def vertical(self):
        start = time.time()
        xy = (self.width / 2, 0)
        sign = 1
        delta = 50 * self.acc        
        while time.time() - start < self.time:
            r = abs(2*xy[1] - self.height)
            
            if r > self.height * 0.70:
                r = self.height * 0.70
            elif r < self.height * 0.70:
                r = self.height * 0.01                
            
            r = 1.0 - r / self.height
            
            if xy[1] < 0:
                sign = 1
            if xy[1] > self.height:
                sign = -1    
            xy = (xy[0], xy[1] + sign * delta * r)             
            self.update(xy)            
            time.sleep(1/60)
            
        self.canvas.delete(ALL)
    
    def diagonal1(self):
        start = time.time()
        xy = (0, 0)
        sign = 1
        delta = 80 * self.acc       
        while time.time() - start < self.time:
            r = abs(2*xy[0] - self.width)
            
            if r > self.width * 0.70:
                r = self.width * 0.70
            elif r < self.width * 0.70:
                r = self.width * 0.01                
            
            r = 1.0 - r / self.width
            
            if xy[0] < 0:
                sign = 1
            if xy[0] > self.width:
                sign = -1    
            xy = (xy[0] + sign * delta * r, 
                  (xy[0] + sign * delta * r) * self.height / self.width)             
            self.update(xy)            
            time.sleep(1/60)
            
        self.canvas.delete(ALL)               
    
    def diagonal2(self):
        start = time.time()
        xy = (0, self.height)
        sign = 1
        delta = 80 * self.acc        
        while time.time() - start < self.time:
            r = abs(2*xy[0] - self.width)
            
            if r > self.width * 0.70:
                r = self.width * 0.70
            elif r < self.width * 0.70:
                r = self.width * 0.01                
            
            r = 1.0 - r / self.width
            
            if xy[0] < 0:
                sign = 1
            if xy[0] > self.width:
                sign = -1    
            xy = (xy[0] + sign * delta * r, 
                  self.height - (xy[0] + sign * delta * r) * self.height / self.width)             
            self.update(xy)            
            time.sleep(1/60)
            
        self.canvas.delete(ALL)
        
    
    def center(self):
        start = time.time()
        self.drawCircle(self.width/2, self.height/2, 20, fill="red")
        while time.time() - start < self.time:
            pass
            
        self.canvas.delete(ALL)

    def update(self, obj):       
        self.canvas.delete(ALL)
        self.drawCircle(int(obj[0]), int(obj[1]), 20, fill="red")        
        Frame.update(self)

    def drawCircle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)        
        
    def inputKey(self, e):
        if e.char == 'q':                      
            self.parent.quit()            
        elif e.char == 'e':         
            self.time = 0   
            self.canvas.delete(ALL)                                    
        elif e.char == '1':
            self.time = 120
            self.th = Thread(target=self.horizontal, args=())
            self.th.start()
        elif e.char == '2':
            self.time = 120
            self.th = Thread(target=self.vertical, args=())
            self.th.start()
        elif e.char == '3':
            self.time = 120
            self.th = Thread(target=self.diagonal1, args=())
            self.th.start()
        elif e.char == '4':
            self.time = 120
            self.th = Thread(target=self.diagonal2, args=())
            self.th.start()
        elif e.char == '5':
            self.time = 120
            self.th = Thread(target=self.center, args=())
            self.th.start()
    
                    
        
        
        
def main():
    if len(sys.argv) == 1:
        acc = 1
    else:    
        acc = float(sys.argv[1])
    
    root = Tk()
    app = Window(root, acc)
    app.mainloop()
    
if __name__ == '__main__':
    main()
    