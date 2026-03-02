# Group: Medhashree Adhikari, Jana Vadillo, Bonsen Yusuf
# Due Date: Sunday, March 01, 2026
#
# Acknowledgements: 

# Packages
import numpy as np
import matplotlib.pyplot as plt
import random

gamma = 0.9


n_sims = 1000
##learning algorithm variables 
init_state = 12
terminal_states = [0, 15]

states = np.arange(16)
moves= ['left', 'right', 'up', 'down']
#States 
R_move = -1
R_terminal = 0
#Rewards


n_episodes = 10
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
            action = moves[np.argmax(Q[state])]#be greedy
        

  
        Q, state = update_Q(Q, state,action,alpha)

        if state in terminal_states:
            break
    return (P, Q)


def run_simulation(experiment):
    Q = np.zeros((16,4))
    T = 0
    avg_len =[]
    for episode in range(n_episodes):
        P, Q = run_episode(Q, T, experiment)
        avg_len = np.append(avg_len, P)
        print("\n Run number", episode, ": ", P)
        print(Q)
    
    ## need to do, add code to plot avg reinforcement and avg len for each episode


"""
X-axis: Episode number (in chronological order)
Y-axis: Average Reinforcement per Episode across simulations. 
"""
def plotReinforcement():
    plt.xlabel("Episode Number")
    plt.ylabel("Average Reinforcement per Episode Across Simulations")

    # plt.legend()
    plt.show() # Display the plot

"""
X-axis: Episode number
Y-axis: Average episode duration across simulations
"""
def plotDuration():
    plt.xlabel("Episode Number")
    plt.ylabel("Average Episode Duration Across Simulations")

    # plt.legend()
    plt.show() # Display the plot

def main():
    # plotReinforcement()
    # plotDuration()

    for x in range(6):
        run_simulation(x)

    print("AI Lab 3")
    return()

main()
