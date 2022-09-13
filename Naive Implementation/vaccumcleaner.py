#Importing libraries
import numpy as np
import sys 
stdoutOrigin=sys.stdout 
sys.stdout = open("vaccum_cleaner_output.txt", "w")



#Environments

env = np.random.random((5,5))


#Actions
def clean(env,idx):
    env[idx[0],idx[1]] = 0 
     #It means dirt is cleaned
    return env

def move_right(idx): 
    return (idx[0],idx[1]+1)

def move_left(idx):
    return (idx[0],idx[1]-1)

def move_down(idx):
    return (idx[0]+1,idx[1])

#Displaying State
def display_cleaner(env,idx):
    
    print("Vaccum cleaner at: ",idx)
    print("The room currently: ")
    print(env)


#Main Functionality
def clean_room(env,idx):
    
    for i in range(env.shape[0]):

        if i%2 == 0:
            for _ in range(env.shape[0]-1):
                display_cleaner(env,idx)
                env = clean(env,idx)
                idx = move_right(idx)
            env = clean(env,idx)
            display_cleaner(env,idx)
            idx = move_down(idx)

            

        else :
            for _ in range(env.shape[0]-1):
                display_cleaner(env,idx)
                env = clean(env,idx)
                idx = move_left(idx)
            env = clean(env,idx)
            display_cleaner(env,idx)
            idx = move_down(idx)
            



env1 = np.round(np.random.random((5,5)),2)

idx = (0,0)
clean_room(env1,idx)



sys.stdout.close()
sys.stdout=stdoutOrigin