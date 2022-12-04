import random
##alpha beta pruning

INPUT=input("Enter your id:")

##if any number in input is 0 replace with 8
INPUT=INPUT.replace("0","8")

min_num=int(INPUT[4])

##take nearest value

max_num=int(int(INPUT[7]+INPUT[6])*1.5)

total_points_to_win=int(INPUT[7]+INPUT[6])

total_shuffles=int(INPUT[3])





##print min and max number

print(min_num,max_num,total_shuffles)

##generate a list of 8 digits between min and max

list1=random.sample(range(min_num,max_num),8)
print(list1)



def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    global MIN,MAX
   
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 
        
        for i in range(0, 2):
             
            val = minimax(depth + 1, nodeIndex * 2 + i,False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
 
            
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
 
        
        for i in range(0, 2):
          
            val = minimax(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
 
           
            if beta <= alpha:
                break
          
        return best




MAX, MIN = 1000, -1000


print("Generated 8 random points between the minimum and maximum point limits : ",list1)
print("total points to win : ",total_points_to_win)
print("achieved points : ",minimax(0, 0, True, list1, MIN, MAX))
if minimax(0, 0, True, list1, MIN, MAX)>=total_points_to_win:
    print("optimus prime wins")
else:
    print("Megatron wins")

value_list=[]


for i in range(total_shuffles):
    #suffle the list
    random.shuffle(list1)
    value=minimax(0, 0, True, list1, MIN, MAX)
    value_list.append(value)

print("list of points achieved after each shuffle : ",value_list)
print("the maximum points achieved after shuffling is : ",max(value_list))
##count how many time optimus prime wins

count=0
for i in value_list:
    if i>=total_points_to_win:
        count+=1
print("optimus prime wins ",count," times out of ",total_shuffles," times")















