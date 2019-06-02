
import os
import easygui as g
import sys
import random

set1 = {1,1,0}


set3 = ([1,2])

print(set1)
print(set3)

# open('C:\\Users\\NAN\\Documents\\Python\\FishC-pratice\\test.txt')


print(os.getcwd()) #  当前路径

# while True:
#     g.msgbox('HI, welcome to the first game')
#
#     msg = 'What do you want to learn'
#     title = 'Mini Game'
#     choices = ['fall in love', 'learn python', 'learn LOL']
#
#     choice = g.choicebox(msg, title, choices)
#
#     g.msgbox('You picked: ' + str(choice), '!')
#
#     msg = 'Do you want to restart?'
#
#     title = 'Please pick something'
#
#     if g.ccbox(msg, title):
#         pass
#     else:
#         sys.exit(0)


class Person:
    __name = 'Aaron'

    def getName(self):
        print(self.__name)


class Ticket():
    def __init__(self, weekend=False, childs=False):
        self.exp1 = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if childs:
            self.discount = 0.5
        else:
            self.discount = 1

    def calc_price(self, num):
        return self.exp1 * self.inc * self.discount * num


adult = Ticket()
child = Ticket(childs=True)
print('2 adaults + 1 child the weekday price is : %.2f' % (adult.calc_price(2) + child.calc_price(1)))

directions = ['U','D','R','L']

class Fish():
    def __init__(self, num):
        self.__x = random.randint(0, 10)
        self.__y = random.randint(0, 10)
        self.__direction = directions[random.randint(0, 3)]
        self.num = num
        self.eaten = False
        
    def move(self):
        if self.__direction == 'U':
            if self.__x == 10:
                self.__x = 0
            else:
                self.__x += 1
        if self.__direction == 'D':
            if self.__x == 0:
                self.__x = 10
            else:
                self.__x -= 1
        if self.__direction == 'R':
            if self.__y == 10:
                self.__y = 0
            else:
                self.__y += 1
        if self.__direction == 'L':
            if self.__y == 0:
                self.__y = 10
            else:
                self.__y -= 1
        
    def position(self):
        return [self.__x, self.__y]

class Turtle():
    def __init__(self):
        self.__x = random.randint(0, 10)
        self.__y = random.randint(0, 10)
        self.__move = random.randint(1,2)
        self.__direction = directions[random.randint(0, 3)]
        self.__life = 100
        self.die = False

    def life_left(self):
        return self.__life

    def move(self):
        if self.__life > 0:
            self.__life -= 1
            if self.__life == 0:
                self.die = True
            if self.__direction == 'U':
                if self.__x >= 9:
                    if self.__x == 10:
                        self.__x = 1
                    else:
                        self.__x = 0
                else:
                    self.__x += self.__move
            if self.__direction == 'D':
                if self.__x <= 1:
                    if self.__x == 1:
                        self.__x = 10
                    else:
                        self.__x = 9
                else:
                    self.__x -= self.__move
            if self.__direction == 'R':
                if self.__y >= 9:
                    if self.__y == 10:
                        self.__y = 1
                    else:
                        self.__y = 0
                else:
                    self.__y += self.__move
            if self.__direction == 'L':
                if self.__y <= 1:
                    if self.__y == 1:
                        self.__y = 10
                    else:
                        self.__y = 9
                else:
                    self.__y -= self.__move
        else:
            self.die = True

    def eat(self):
        if self.__life > 80:
            self.__life = 100
        else:
            self.__life += 20
    
    def position(self):
        return [self.__x, self.__y]
            

fishs = []
turtle = Turtle()
print(turtle.position())

for x in range(0, 10):
    fishs.append(Fish(x))

fishleft = len(fishs)

while True:
    if turtle.die or fishleft == 0:
        if not fishleft:
            print('Game over! fish lost')
        else:
            for fish in fishs:
                print('-----')
                print(fish.eaten)
            print('Game over! fish win')
        print('Game is over ')
        break
    else:
        turtle.move()
        print(turtle.life_left())
        for fish in fishs:
            fish.move()
            if fish.position() == turtle.position() and not fish.eaten:
                turtle.eat()
                fish.eaten = True
                print('fish - ', fish.num, 'has been eaten')
                fishleft -= 1
                print('Fish left:', fishleft)



            
        
p = Person()
p.getName()