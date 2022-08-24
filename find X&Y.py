from random import choices ,randint
# import numpy as np

# 6X+4Y -74 =0
#find the x and y

sol_size=2

#initialise population
def initial_pop(sol_size: int):
  pop =[]
  for i in range(100):
    pop.append(choices([0,1,2,3,4,5,6,7,8,9],k=2))
  return pop

#fitness evaluation
def fitness( a: list):
  a=6*a[0]+4*a[1]-74
  return abs(a)

#selecting select_parents
def select_parents(pop: list):
  ranked_pop =[]
  for s in pop:
    ranked_pop.append((fitness(s), s))
  ranked_pop.sort()
  
  parents = []
  for p in ranked_pop[:10]:
    parents.append(p[1])

  return parents



#creting next next_generation
def offsring(parents: list, length:int =sol_size):
  children =[]
  #crossover
  for i in range(0, 10, 2):
    a=parents[i]
    b=parents[i+1]
    p=randint(1, length-1)
    children.append(a[0:p]+b[p:])
    children.append(b[0:p]+a[p:])
  #mutation
  for c in children:
    index= choices([0,1])
    m= choices([-1,1])
    c[index[0]] += m[0]

  return children



current_population = initial_pop(sol_size)
best_solution=choices([-1],k=sol_size)


#evolution
for i in range(100):
  print(f"==========GENERATION {i} ===============")
  
  parents = select_parents(current_population)
  for p in range(5):
    print(parents[p],"  ", fitness(parents[p]))
  print("generation's best soltionn: ",parents[0])

  #updating best_solution
  if fitness(best_solution) > fitness(parents[0]):
    best_solution = parents[0]
  print("Best Solution till now",best_solution)
  #print(fitness(best_solution))
  print("\n")
  next_generation = offsring(parents)
  current_population = next_generation

################
print(f"X: {best_solution[0]} Y: {best_solution[1]}")
print(fitness(best_solution))



