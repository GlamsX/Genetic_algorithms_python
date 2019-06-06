#!/usr/bin/env python

##
## EPITECH PROJECT, 2019
## genetic-algorithme
## File description:
## [enter description here]
##

import sys
import random
import string

password = sys.argv[1]
population_size = 100
mutation_rate = 0.1
chromosome_size = len(password)

def generate_random_nucleotide():
    return (random.choice(string.letters))

def generate_chromosomes(size):
    chromosome = ""
    index = 0

    for index in range(size):
        chromosome += generate_random_nucleotide()
    return (chromosome)

def generate_population(size):
    population = []
    index = 0

    for index in range(size):
        population.append(generate_chromosomes(chromosome_size))
    return (population)

def get_random_chromosome(list):
    index = random.randint(0,len(list))
    chromosome = list[index]
    return (chromosome)

def score_chromosome(chromosome):
    index = 0
    match = 0

    for index in range(len(chromosome)):
        if chromosome[index] == password[index]:
            match += 1
    return (float(match) / float(chromosome_size))

def scrore_chromosomes_in_list(list):
    score_list = []
    index = 0
    score = 0

    for index in range(len(list)):
        score = score_chromosome(list[index])
        score_list.append(score)
    return (score_list)

def selection(score_list):
    index = 0
    all_value = 0
    new_score_list = []

    for index in range(len(score_list)):
        all_value += score_list[index]
    index = 0
    for index in range(len(score_list)):
        new_score_list.append(score_list[index] / all_value)
    return (new_score_list)

if __name__ == "__main__":
    list = generate_population(population_size)
    score_list = scrore_chromosomes_in_list(list)
    print(selection(score_list))
