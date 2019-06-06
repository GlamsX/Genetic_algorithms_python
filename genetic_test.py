#!/usr/bin/env python3

##
## EPITECH PROJECT, 2019
## genc
## File description:
## genetic algorithme
##

import sys
import random
import string
import math
from turtle import *

population = []
a_map = []

class Point(object):
    COUNT = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return ("Point(%s,%s)"%(self.X, self.Y))

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return (math.sqrt(dx**2 + dy**2))


class Individu(object):

    def __init__(self, init = False, map_point = []):
        self.score = 0
        self.route = []
        if init:
            self.set_route(map_point)

    def set_route(self, map_point):
        random.shuffle(map_point)
        self.route = map_point
        for p in range(len(map_point) - 1) :
            self.score += map_point[p].distance(map_point[p+1])

    def croisement(self, other):
        child = Individu()
        wdth = len(self.route)/2
        index = wdth / 2
        index = int(index)
        first_segment = self.route[:index]
        last_segment  = []
        for i in range(len(self.route)) :
            if other.route[i] not in first_segment :
                last_segment.append(other.route[i])
        child.set_route(first_segment + last_segment)
        return child

    def show_me(self):
        turtle.clearscreen()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.up()
        pen.setpos(self.route[0].X, self.route[0].Y)
        for point in self.route :
            pen.goto(point.X, point.Y)
            pen.down()
            pen.dot()
        pen.goto(self.route[0].X, self.route[0].Y)


def init_map(nb):
    global a_map
    del a_map[:]
    for i in range(nb):
        p = Point(random.randint(1, 300), random.randint(1, 300))
        a_map.append(p)

def init_pop(nb, map_point):
    global population
    del population[:]
    for i in range(nb):
        i = Individu(True, map_point)
        population.append(i)

def selection(pop):
    pop.sort(key=lambda x: x.score, reverse=True)

def croisement(pop):
    new_pop = []
    best_pop = population[85:]
    for i in range(len(pop)-15) :
        new_pop.append(random.choice(best_pop).croisement(random.choice(population[20:85])))
    return new_pop + best_pop

def play(nb_gene, nb_point) :
    init_map(nb_point)
    init_pop(100, a_map)
    best_score = 1000000
    for i in range(nb_gene) :
        global population
        population = croisement(population)
        selection(population)
        if best_score > population[99].score :
            best_score = population[99].score
            print ("meilleur score : " + str(population[99].score))
            population[99].show_me()


if __name__ == '__main__':
    play(100, 100)
