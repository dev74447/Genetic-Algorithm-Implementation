from random import choices, randint
import numpy as np

#0/1 Knapsack problem
#profits
P=[60,80,100,120]
#weights
W=[5,10,20,30]
#constrains, total weight must be <= 50
C=50
sol_size = len(W)

#initialise population
def initial_pop(sol_size: int):
  pop =[]
  for i in range(100):
    pop.append(choices([0,1],k=sol_size))
  return pop

def fitness(a: list,p:list=P, w: list = W, c:int =C):
  if np.dot(a,w)>c:
    return -1
  return np.dot(a,p)

#selecting select_parents
def select_parents(pop: list):
  ranked_pop =[]
  for s in pop:
    ranked_pop.append((fitness(s), s))
  ranked_pop.sort()
  ranked_pop.reverse()
  parents = []
  for p in ranked_pop[:10]:
    parents.append(p[1])
  return parents



#creating next next_generation
def offsring(parents: list, length:int =sol_size):
  children =[]
  #crossover
  for i in range(0, 10, 2):
    a=parents[i]
    b=parents[i+1]
    p=randint(1, length-1)
    children.append(a[0:p]+b[p:])
    children.append(b[0:p]+a[p:])
  # mutation
    for c in children:
      index=randint(0,length-1)
      c[index]= 1-c[index]
  return children



current_population = initial_pop(sol_size)
best_solution=choices([0],k=sol_size)

for i in range(100):
  print(f"==========GENERATION {i} ===============")
  
  parents = select_parents(current_population)
  for p in range(5):
    print(parents[p],"  ", fitness(parents[p]))
  print("generation's best soltionn: ",parents[0])

  #updating best solutuion
  if fitness(best_solution) < fitness(parents[0]):
    best_solution = parents[0]
  print("Best Solution till now",best_solution)
  print("\n")


  next_generation = offsring(parents)
  current_population = next_generation

################
print("\nchoosen items")
print("W    P")
for i in range(sol_size):
  if best_solution[i]:
    print(W[i]," ",P[i])
    
  
print("MAX profit", fitness(best_solution))


