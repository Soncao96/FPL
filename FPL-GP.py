# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:16:17 2023

@author: caoth
"""


import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd

#Set Up Main Objectives and Constraints
fpl = pd.read_excel(r'C:\Users\caoth\Desktop\materials forest\PyOp\FPLfixed.xLsx', sheet_name= 'test')
p= len(fpl)

model = pyo.ConcreteModel()

model.x = pyo.Var(range(0,p), within=pyo.Binary)

x= model.x


model.s1minus = pyo.Var(bounds=(0,None))
model.s1plus = pyo.Var(bounds=(0,None))
model.s2minus = pyo.Var(bounds=(0,None))
model.s2plus = pyo.Var(bounds=(0,None))
model.s3minus = pyo.Var(bounds=(0,None))
model.s3plus = pyo.Var(bounds=(0,None))
model.s4minus = pyo.Var(bounds=(0,None))
model.s4plus = pyo.Var(bounds=(0,None))
model.s5minus = pyo.Var(bounds=(0,None))
model.s5plus = pyo.Var(bounds=(0,None))
model.s6minus = pyo.Var(bounds=(0,None))
model.s6plus = pyo.Var(bounds=(0,None))
model.s7minus = pyo.Var(bounds=(0,None))
model.s7plus = pyo.Var(bounds=(0,None))

#Set up Goals (In this model, we will have 7 goals/metrics), positive and negative deviations
s1a = model.s1minus
s1b = model.s1plus
s2a = model.s2minus
s2b = model.s2plus
s3a = model.s3minus
s3b = model.s3plus
s4a = model.s4minus
s4b = model.s4plus
s5a = model.s5minus
s5b = model.s5plus
s6a = model.s6minus
s6b = model.s6plus
s7a = model.s7minus
s7b = model.s7plus

model.obj = pyo.Objective(expr = s1a+s2a+s3a+s4a+s5a+s6a+s7a,sense=1)
#Note: In this, I consider all of the importance level of those goals will be equal (weight = 1). If you want to stress more, for example, the Shots stat (weight = 1)
# while other stats stressed a bit less (e can set a lighter weight = 0.8) then the expression will be: expr = s1a+ 0.8*s2a + 0.8*s3a +0.8*s4a + 0.8*s5a + 0.8*s6a + 0.8*s7a
# All in all, simply set the weight( imprtance level) of every stats and remember to multiply their weight in the objective function

#Setting up constraint

#Goal constraints

model.C1 = pyo.Constraint(expr = sum([x[p]*fpl.Shots[p] for p in fpl.index]) +s1a -s1b ==43*15)

model.C2 = pyo.Constraint(expr = sum([x[p]*fpl.KeyPass[p] for p in fpl.index]) +s2a -s2b ==16*15)

model.C3 = pyo.Constraint(expr = sum([x[p]*fpl.CleanSheets[p] for p in fpl.index[fpl.Position == 'Gk']]) +s3a -s3b ==5*2)

model.C4 = pyo.Constraint(expr = sum([x[p]*fpl.CleanSheets[p] for p in fpl.index[fpl.Position == 'Def']]) +s4a -s4b ==4*5)

model.C5 = pyo.Constraint(expr = sum([x[p]*fpl.TotalSaves[p] for p in fpl.index[fpl.Position == 'Gk']]) +s5a -s5b ==45*2)

model.C6 = pyo.Constraint(expr = sum([x[p]*fpl.AccCross[p] for p in fpl.index[fpl.Position == 'Def']]) +s6a -s6b ==16*5)

model.C7 = pyo.Constraint(expr = sum([x[p]*fpl.Mins[p] for p in fpl.index]) +s7a -s7b ==1300*15)


#FPL rules Constraints
model.cost = pyo.Constraint(expr = sum([x[p]*fpl.Cost[p] for p in fpl.index]) == 100)
model.limit = pyo.Constraint(expr = sum([x[p] for p in fpl.index]) ==15)

model.team1 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'ARS']]) <= 3)
model.team2 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'AVL']]) <= 3)
model.team3 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'BHA']]) <= 3)
model.team4 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'BRE']]) <= 3)
model.team5 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'CHE']]) <= 3)
model.team6 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'CRY']]) <= 3)
model.team7 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'EVE']]) <= 3)
model.team8 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'LEE']]) <= 3)
model.team9 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'LEI']]) <= 3)
model.team10 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'LIV']]) <= 3)
model.team11 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'MCI']]) <= 3)
model.team12 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'MUN']]) <= 3)
model.team13 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'NEW']]) <= 3)
model.team14 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'SOU']]) <= 3)
model.team15 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'TOT']]) <= 3)
model.team16 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'WHU']]) <= 3)
model.team17 = pyo.Constraint(expr =sum([x[p]for p in fpl.index[fpl.Team == 'WOL']]) <= 3)


model.position1 = pyo.Constraint(expr =sum([x[p] for p in fpl.index[fpl.Position == 'Gk']])  == 2)
model.position2 = pyo.Constraint(expr =sum([x[p] for p in fpl.index[fpl.Position == 'Def']])  == 5)
model.position3 = pyo.Constraint(expr =sum([x[p] for p in fpl.index[fpl.Position == 'Mid']])  == 5)
model.position4 = pyo.Constraint(expr =sum([x[p] for p in fpl.index[fpl.Position == 'Att']])  == 3)

#Note: Since week 2, you normally only want to make 1 or 2 transfers, which means you need to add another constraints to keep about 14-15 players in your previous week
#To do that, you should pay attention to the ID of your player in the data table (or in the results section from optimization)
#For example if I want to Keep David De Gea (ID = 238) in my squad still, my code would be:
# model.test = pyo.Constraint(expr = sum([x[p]for p in fpl.index[fpl.ID == 238]]) == 1)


#Solving the problem
opt = SolverFactory('gurobi')
opt.solve(model)
model.pprint()

fpl['activated'] = 0
for p in fpl.index:
    fpl.activated[p] = pyo.value(x[p])
 
print('\n\nAll FPL:')
print(fpl)
 
print('\nSelected FPL:')
print(fpl[fpl.activated==1])
 
print('\nTotal fpl:', )

fplcost = sum([pyo.value(x[p])*fpl.Cost[p] for p in fpl.index])
print(fplcost)
print('Z=',pyo.value(model.obj))
print(pyo.value(s1a))
print(pyo.value(s1b))
print(pyo.value(s2a))
print(pyo.value(s2b))
print(pyo.value(s3a))
print(pyo.value(s3b))
print(pyo.value(s4a))
print(pyo.value(s4b))
print(pyo.value(s5a))
print(pyo.value(s5b))
print(pyo.value(s6a))
print(pyo.value(s6b))


