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
<<<<<<< HEAD
def update_Q(Q, state, action, reward, next_state, alpha, gamma=gamma, terminal_states=terminal_states):
    """Q-learning update: Q[s,a] <- Q[s,a] + alpha*(target - Q[s,a])."""
    current_q = Q[state, action]

    if next_state in terminal_states:
        target = reward
    else:
        target = reward + gamma * np.max(Q[next_state])

    Q[state, action] = current_q + alpha * (target - current_q)
    return Q[state, action]
=======
def update_Q(S, ):
    print('implement')
>>>>>>> 9c53fa3edf58946e52eebdece302da40890f39b6

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
