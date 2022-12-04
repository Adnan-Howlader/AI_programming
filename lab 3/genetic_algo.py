import random
with open('input.txt') as f:
        content = f.readlines()##read the input file line by line 
        content = [x.strip() for x in content]
        
        


N=int(content[0][0])
first_line_len=len(content[0])
Target=int(content[0][2:first_line_len])
print('target',Target)


Players=[]





content=list(filter(('').__ne__, content))

for i in range(1,len(content)):
     
    
      player=content[i].split(' ')
      Players.append((player[0],player[1]))
     
   
Player_names=[]

for i in range(len(Players)):
    Player_names.append(Players[i][0])
    
    
states=[]
for i in range(8):
   random_list=[] 
   for i in range(0,N):
     n = random.randint(0,1)
     random_list.append(n)
   states.append(random_list)




def calculate_fitness(states,Players):
    fitness_array=[]
    
    for state in states:
        fitness=0
        
        for i in range(0,len(state)):
            if state[i]==1:
                fitness+=int(Players[i][1])

        fitness_array.append(fitness)

    return fitness_array

    
def crossover(selected_states):
    children_states=[]
    random_index=N//2
    for i in range(0,len(selected_states)-1):

        
        child1=selected_states[i][:random_index]+selected_states[i+1][random_index:]
        child2=selected_states[i+1][:random_index]+selected_states[i][random_index:]
        children_states.append(child1)
        children_states.append(child2)
       

   
    return children_states
  
    

def selection(states,fitness_array):
    ##select the best 5 states
    best_states=[]
    for i in range(5):
        best_states.append(states[fitness_array.index(max(fitness_array))])
        fitness_array.remove(max(fitness_array))
    return best_states

def mutation(children_states):
    ##mutate random index of the children states
    for i in range(len(children_states)):
        random_index=random.randint(0,N-1)
        if children_states[i][random_index]==1:
            children_states[i][random_index]=0
        else:
            children_states[i][random_index]=1

    return children_states

def evaluation(target,children_states,Players):
    ##calculate fitness of the children states using the function calculate_fitness
    fitness_array=calculate_fitness(children_states,Players)
    ##check if the target is reached and return the state array
    
    for i in range(len(fitness_array)):
        if fitness_array[i]==target:
            print(Player_names)
            print('fitness of the children',fitness_array[i])
            return children_states[i]

    return None




for i in range(5000):
    fitness_array=calculate_fitness(states,Players)

    selected_states=selection(states,fitness_array)

    children_states=crossover(selected_states)

    ##mutation
    children_states=mutation(children_states)
    

    ##evaluation
    target_state=evaluation(Target,children_states,Players)
    if target_state!=None:
        
        print(target_state)
        break
    else:
        states=children_states.copy()
        if i==4999:
            print(Player_names)
            print(-1)
  
        

    


    


