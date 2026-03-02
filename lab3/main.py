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
def update_Q(Q, state, action, reward, next_state, alpha, gamma):
    current_q_value = Q[state, action] #get the current q-val
    max_future_q = np.max(Q[next_state]) #look at the possible actions in next state and select ,ax q-value.
    td_target = reward + gamma * max_future_q #compute TD value
    td_error = td_target - current_q_value 
    Q[state, action] = current_q_value + alpha * td_error

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
