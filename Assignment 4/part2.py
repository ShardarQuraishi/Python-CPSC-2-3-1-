import pygame

pygame.init()

#set up the window
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rush hour")

black = 0,0,0
grey=220,220,220
# gameDisplay=300
# gridSize=300+6

gameDisplay.fill(grey)

pygame.draw.line(gameDisplay,black, (100,0), (100,300), 3)
pygame.draw.line(gameDisplay,black, (200,0), (200,300), 3)
pygame.draw.line(gameDisplay,black, (0,100), (300,100), 3)
pygame.draw.line(gameDisplay,black, (0,200), (300,200), 3)
class car():
#using the sys module to input data from a .txt file
    import sys
    tFile=open(sys.argv[1],"r")
    text = []
    for line in tFile:
        text.append(line.strip('\n'))
    carData = []
    for index in text:
        carData.append(index.split(','))
        #print(carData)
    tFile.close()
    numberofcar = 1
    totalCars = len(carData)
#empty carlist is made, the car data will be appended in later
    carList = []
    ls1= [0, 0, 0, 0, 0, 0]
    ls2= [0, 0, 0, 0, 0, 0]
    ls3= [0, 0, 0, 0, 0, 0]
    ls4= [0, 0, 0, 0, 0, 0]
    ls5= [0, 0, 0, 0, 0, 0]
    ls6= [0, 0, 0, 0, 0, 0]


#this is the initializer method of the class car which is automatically called when a new point is created

    def __init__(self):
        self.orientation = self.carData[self.numberofcar - 1][0] #Need to be changed
        self.size =  int(self.carData[self.numberofcar - 1][1])
        self.posy =  int(self.carData[self.numberofcar - 1][2])
        self.posx =  int(self.carData[self.numberofcar - 1][3])
        self.carnumber = self.numberofcar
        car.numberofcar +=1
        # print(self.carnumber, self.orientation, self.size, self.posy, self.posx)
        self.carList.append(self)
#assigning car number to each car
        if car.numberofcar == car.totalCars +1:
            car.numberofcar = 1
#the grid is made by joining all the lists together
    @classmethod
    def  makeGrid(cls):
        grid = [cls.ls1, cls.ls2, cls.ls3, cls.ls4, cls.ls5, cls.ls6]
        cls.grid = grid
#making class method which prints the grid and contents in it in a 6 by 6 table form
    @classmethod
    def printGrid(cls):
        for i in range(len(cls.grid)):
            for j in range(len(cls.grid[i])):
                print(cls.grid[i][j], end=' ')
            print()

#this class method is responsible for appending the raw data into the empty grid
    @classmethod
    def addlist(cls, self):
        orientation = self.orientation
        size = self.size
        posx = self.posx
        posy = self.posy

        if posy == 0:
            self.carinsert(cls.ls1, cls.ls2, cls.ls3)
        elif posy == 1:
            self.carinsert(cls.ls2, cls.ls3, cls.ls4)
        elif posy == 2:
            self.carinsert(cls.ls3, cls.ls4, cls.ls5)
        elif posy == 3:
            self.carinsert(cls.ls4, cls.ls5, cls.ls6)
        elif posy == 4:
            self.carinsert(cls.ls5, cls.ls6, None)
        elif posy == 5:
            self.carinsert(cls.ls6, None, None)


    def carinsert(self, ls1, ls2, ls3):
        if self.orientation == "h":
            for i in range(self.size):
                ls1[self.posx + i] = self.carnumber
        else:
            ls1[self.posx] = self.carnumber
            ls2[self.posx] = self.carnumber
            if self.size == 3:
                ls3[self.posx] = self.carnumber
#method used for the movement of the cars
    def movecar():
        carmove = int(input("Please enter the car number: "))
#while loop used to check in values entered are within the range, in this case
#carmove must me between 1 and the total number of cars
        while (carmove<1 or carmove>car.totalCars):
            carmove=int(input("Please enter number between 1 and %d: "%car.totalCars))

        mCar= car.carList[carmove-1]
        # print(mCar.orientation, mCar.carnumber

#if the orientation of the car selected is horizontal, condition checks are made to see if the selected car can move
        if (mCar.orientation == "h"):
            if(mCar.carnumber==car.grid[mCar.posy][0] and car.grid[mCar.posy][mCar.posx + mCar.size]!=0):
                print("Sorry, this car cannot be moved")
            elif(mCar.carnumber == car.grid[mCar.posy][-1] and car.grid[mCar.posy][mCar.posx -1]!=0):
                print("Sorry, this car cannot be moved")
            elif(car.grid[mCar.posy][mCar.posx -1]!=0 and car.grid[mCar.posy][mCar.posx + mCar.size]!=0):
                print("Sorry, this car cannot be moved")
            else:
            #if the car passed the checks successfully, it's passed on to the making movement part
            #here the user is asked how many spaces they want to move the car and in which direction
                cShift=0
                while(cShift!="r" or cShift!="l"):
                    cShift=input("Please input direction of movement r or l: ")
                    break
                    return cShift
                #if the movement selected is RIGHT
                if(cShift == "r"):
                    #if statement to see if car can move in that direction
                    if(mCar.carnumber == car.grid[mCar.posy][-1] or car.grid[mCar.posy][mCar.posx + mCar.size]!=0):
                        print("illegal entry")
                    else:
                        #using a for loop to check number of zeroes in the path of the car AKA steps it can take
                        zeroCount=0
                        for i in range(mCar.posx,6):
                            if car.grid[mCar.posy][i]==0:
                                zeroCount+=1
                        print("%d steps are available: "%zeroCount)
                        #user inputs the number of steps to be moved which is again put into a while loop to range check
                        stepMove=int(input("how many steps do you want to go? "))
                        while(stepMove>zeroCount or stepMove<0):
                            stepMove=int(input("how many steps do you want to go? "))
                        #this is the part where the car is moved
                        for i in range(mCar.posx+mCar.size,mCar.posx+mCar.size+stepMove):
                            car.grid[mCar.posy][i]=carmove
                            car.grid[mCar.posy][mCar.posx]=0
                            mCar.posx+=1
                        car.printGrid()
                #if the movement selected is LEFT
                else:
                    # if(car.grid[mCar.posy][mCar.posx + mCar.size]!=0 or mCar.carnumber == car.grid[mCar.posy][-1]):
                    #     print("illegal entry")
                    # else:
                        zeroCount=0
                        for i in range(mCar.posx,-1,-1):
                            if car.grid[mCar.posy][i]==0:
                                zeroCount+=1
                        print("%d steps are available: "%zeroCount)
                        stepMove=int(input("how many steps do you want to go? "))
                        while(stepMove>zeroCount or stepMove<0):
                            stepMove=int(input("how many steps do you want to go? "))
                        for i in range(mCar.posx,mCar.posx-stepMove,-1):
                            car.grid[mCar.posy][i-1]=carmove
                            car.grid[mCar.posy][mCar.posx+mCar.size-1]=0
                            mCar.posx-=1
                        car.printGrid()

#if the slected car's orientation is verticle
        elif (mCar.orientation == "v"):
            if(mCar.carnumber==car.grid[0][mCar.posx] and car.grid[mCar.posy + mCar.size][mCar.posx]!=0):
                print("Sorry, this car cannot be moved")
            elif(mCar.carnumber == car.grid[-1][mCar.posx] and car.grid[mCar.posy -1][mCar.posx]!=0):
                print("Sorry, this car cannot be moved")
            elif(car.grid[mCar.posy -1][mCar.posx]!=0 and car.grid[mCar.posy + mCar.size][mCar.posx]!=0):
                print("Sorry, this car cannot be moved")
            else:
                cShift=0
                while(cShift!="u" or cShift!="d"):
                    cShift=input("Please input direction of movement up or down by u or d: ")
                    break
                    return cShift
                #if the direction of the movement selected is UPWARD
                if(cShift == "u"):
                    if(mCar.carnumber == car.grid[-1][mCar.posy] or car.grid[mCar.posx][mCar.posx + mCar.size]!=0):
                        print("illegal entry")
                    else:
                        zeroCount=0
                    for i in range(mCar.posy,-1,-1):
                        if car.grid[i][mCar.posx]==0:
                            zeroCount+=1
                    print("%d steps are available: "%zeroCount)
                    stepMove=int(input("how many steps do you want to go? "))
                    while(stepMove>zeroCount or stepMove<0):
                        stepMove=int(input("how many steps do you want to go? "))
                    for i in range(mCar.posy,mCar.posy+stepMove-mCar.size): #PROBLEM
                        car.grid[i+1][mCar.posx]=carmove
                        car.grid[mCar.posy-1][mCar.posx]=0
                        mCar.posy-=1
                    car.printGrid()#PROBLEM

#if the direction of the movement selected is DOWNWARD
                else:
                    zeroCount=0
                    for i in range(mCar.posy,6):
                        if car.grid[mCar.posx][i-1]==0:
                            zeroCount+=1
                    print("%d steps are available: "%zeroCount)
                    stepMove=int(input("how many steps do you want to go? "))
                    while(stepMove>zeroCount or stepMove<0):
                        stepMove=int(input("how many steps do you want to go? "))
                    for i in range(mCar.posy-mCar.size,mCar.posy-mCar.size+stepMove):
                        car.grid[mCar.posy+mCar.size][mCar.posx]=carmove
                        car.grid[mCar.posy][mCar.posx]=0
                        mCar.posy+=1
                    car.printGrid()


def main():
    #making cars, initially
    car1 = car()
    car2 = car()
    car3 = car()
    car4 = car()
    car5 = car()
    car6 = car()
    car7 = car()
    car8 = car()
    car9 = car()
    car10 = car()
    car11 = car()
    car12 = car()
    car13 = car()
    car14 = car()
    car15 = car()

    for i in range(car.totalCars):
        car.addlist(car.carList[i])
    car.makeGrid()
    car.printGrid()
    game = True
    while game == True:
        car.movecar()
GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = true

        print(event)
