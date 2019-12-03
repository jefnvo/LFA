#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:02:08 2019

@author: jefferson
"""


resultFile = open("results.txt", "w")

#defining rules
sigma = ["0", "1"]
states = ["q0", "q1", "q2"]
initialState = states[0]
acceptState = states[2]
rules = [["q0 0 q1", "q0 1 q0"],["q1 0 q1", "q1 1 q2"],["q2 0 q2", "q2 1 q2"]]

#open string
inputFile = open("automato.txt", "r")
inputLines = inputFile.readlines()
inputFile.close()

signal = 1
for i in range(0, len(inputLines)):
    s = inputLines[i]
    if s.split('\n')[0] not in sigma:
       resultFile.write("A palavra nao faz parte do alfabeto definido") 
       resultFile.close()
       signal = 0
       break
if signal == 1:
    
    currentState = initialState
    for i in range(0, len(inputLines)):
       currentSymbol = inputLines[i].split('\n')[0]
       print currentSymbol
       for j in range(0, len(rules)):
           if currentState == rules[j][0].split()[0]:
               for k in range(len(rules[j])):
                   if currentSymbol == rules[j][k].split()[1]:
                       resultFile.write( currentState +" +"+ currentSymbol +" -> "+ rules[j][k].split()[2])
                       currentState = rules[j][k].split()[2]
                       break
                   
    if currentState != acceptState:
        resultFile.write("\n Não aceito")
    else:
        resultFile.write("\n Aceito")
    resultFile.close()
                   

