# Group: Medhashree Adhikari, Jana Vadillo, Bonsen Yusuf
# Due Date: Sunday, March 01, 2026

# Packages
import numpy as np
import matplotlib.pyplot as plt
import random

gamma = 0.9


n_sims = 10000
##learning algorithm variables 
init_state = 12
terminal_states = [0, 15]

states = np.arange(16)
moves= ['left', 'right', 'up', 'down']
#States 
R_move = -1
R_terminal = 0
#Rewards


#set by us


"""
Adapted from DoubleQlearning_2026_Eliott.pptx but ADJUSTED based on approach
Pick an action for the current state using an epsilon-greedy policy.
"""
def update_pos(old_state, action):
    state = old_state
    if action == 'left':
        if old_state not in (0, 4, 8, 12): # not on left wall
            state = old_state - 1
    elif action == 'right':
        if old_state not in (3, 7, 11, 15): # not on right wall
            state = old_state + 1
    elif action == 'up':
        if old_state >= 4: # not on top wall
            state = old_state - 4
    elif action == 'down':
        if old_state <= 11: # not on bottom wall
            state = old_state + 4
    return state


"""
Update the Q-value for a given state-action pair using the Q-learning rule/equation.
Q: Q-table storing action-value estimates (Q[s,a])
state(int): the current state s where the agent takes action
action(int): the action taken by the agent.
reward(float): the immediate reward received after taking the action.
next_state(int): the state the agent transitions to after doing an action.
alpha(float): the learning rate/step size.
gamma(float): the discount factor which determines how much futur rewards are vlaued comapred to immediate reward.
returns: void
"""
def update_Q(Q, state, action, alpha):
    action_index = moves.index(action)
    current_q_value = Q[state, action_index] #get the current q-val
    next_state = update_pos(state, action)

    R = R_move
    if next_state in terminal_states:
        R = R_terminal


    max_future_q = np.max(Q[next_state]) #look at the possible actions in next state and select ,ax q-value.

    td_target = R + gamma * max_future_q #compute TD value
    td_error = td_target - current_q_value 
    Q[state, action_index] = current_q_value + alpha * td_error
    return(Q, next_state)



def run_episode(Q,T, experiment):
    state = init_state
    P = 0
    while True:
        T+= 1
        P+=1 
        alpha = [0.1, 1/T, 0.1, 1/T, 0.1 ,1/P][experiment]#select approprate parameters
        explore = [0.25, 1/T, 1/T, 0.1, 0.1, 0.1][experiment]#select apropriate parameters

        if np.random.random() < explore:#agent chooses to explore
            action = np.random.choice(moves)
        else: 
            max = np.max(Q[state])
            best_actions = np.where(Q[state] == max)[0]
            action_index  = np.random.choice(best_actions)
            action = moves[action_index]#be greedy
        

  
        Q, state = update_Q(Q, state,action,alpha)

        if state in terminal_states:
            break
    return (P,T, Q)


def run_simulation(experiment, n_episodes):
    sim_lengths = [[] for _ in range(n_episodes)]  # Pre-initialize with empty lists for each episode
    for sim in range(n_sims):
        
        print(experiment, sim)
        Q = np.zeros((16,4))
        T = 0
        for episode in range(n_episodes):
            P,T, Q = run_episode(Q, T, experiment)
            sim_lengths[episode].append(P)  # Dynamically append to the episode's list
            # print("\n Run number", episode, ": ", P)
            # print(Q)
    avg_len = [] 
    for episode in range(len(sim_lengths)):  # Iterate over indices
        avg_len.append(np.average(sim_lengths[episode]))  # Dynamically append average
    return(avg_len)
    
    ## need to do, add code to plot avg reinforcement and avg len for each episode


def main():
    episodes = [5, 10,25, 50, 100, 150, 200]
    for episode in episodes:
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))
        n_episodes = episode
        for x in range(6):

            avg_len = run_simulation(x, n_episodes)
            axs[0].plot(avg_len, label = x+1)
            axs[1].plot(np.array(avg_len)*-1, label = x+1)
        axs[0].set_xlabel("Episode Index")
        axs[0].set_ylabel("Average Episode Duration Across Simulations")
        axs[0].legend()
        axs[1].set_xlabel("Episode Index")
        axs[1].set_ylabel("Average reinforcement Across Simulations")
        axs[1].legend()
        title = f"{episode} episodes"

        fig.suptitle(title+  ' avg in 10,000 sims')
        plt.tight_layout()
        plt.savefig(title + '.png')

    return()

main()
