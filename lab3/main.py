# Group: Medhashree Adhikari, Jana Vadillo, Bonsen Yusuf
# Due Date: Monday, February 28, 2026
#
# Acknowledgements: 

# Packages
import numpy as np
import matplotlib.pyplot as plt

gamma = 0.9
T = 0
P = 0
alpha = [0.1, 1/T, 0.1, 1/T, 0.1 ,1/P]
explore = [0.25, 1/T, 1/T, 0.1, 0.1, 0.1]
n_sims = 1000
##learning algorithm variables 
init_state = 12
terminal_states = [0, 15]

states = np.arange(16)
#States 
R_move = -1
R_terminal = 0
#Rewards

n_episodes = 10
#set by us
def update_Q(S, ):
    print('implement')

def pick_move():
    print('implement')

def run_episode():
    T+=1

def run_simulation():
    for episode in range(n_episodes):
        run_episode()
        



def main():
    print("AI Lab 3")

main()