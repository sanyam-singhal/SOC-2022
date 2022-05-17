import numpy as np


'''
The MDP has 6 states: 0,1,2,3,4,5. The state 5 is the terminal state and the system can start in any state among 0 to 4.

Possible actions and their resultant landing state and rewards are given in the arrays defined in the class.

For each current_state_action tuple allowed, the corresponding next state and reward is given by the element having the same
index as the tuple in its array.

To access the environment, we create an object of it.

To simulate, you pass a state-action tuple (s,a) to the sample_reward() function, which updates the current state and returns a reward.

For simplicity of handling, actions have been set as integers as well. Actions are 0,1,2 (sorry for possible confusion 
with state indices but this ensures easier implementation). Allowed actions from each state are given in the current_state_action tuple array.
In each tuple in that array, the first element corresponds to current state and the second 
element corresponds to the action.
'''

class Environment():
    def __init__(self):
        self.start_state=np.random.randint(low=0,high=4,dtype=int,size=1)[0]
        self.terminal_state=5
        self.state=self.start_state
        self.done=False
        self.current_state_action=np.array([(0,2),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(4,0)])
        self.next_state=np.array([5,1,0,2,1,3,2,4,3])
        self.rewards=np.array([-2,-1,+1,-1,+1,-1,+1,-1,+1])

    def close(self):
        self.state=self.terminal_state

    def sample_reward(self, current_state_action_tuple):
        action_tuple_index=-1
        for i in range(self.current_state_action.shape[0]):
            check= (self.current_state_action[i]==np.array(current_state_action_tuple))
            if check.sum()==2:
                action_tuple_index=i

        if action_tuple_index==-1:
            print("No change in state")
            return 0
            
        else:
            self.state=self.next_state[action_tuple_index]
            reward=self.rewards[action_tuple_index]
            return reward

'''
Your objective is to learn the optimal policy and the associated optimal value function.

Note that the state number 5 has been set as the terminal state so it
should have the value 0. 

For states 1,2,3, there are two possible actions (0,1). For state 4, there is only possible action (0).

For state 0, there are two actions (1,2), but the behaviour is different from states 1,2,3.
'''

env_obj=Environment()

'''
What are valid operation that you can do?
1. Accessing the current state using state attribute of the environment object.
2. View the current_state_action array and chose which action to take.
3. To reach the next state, call the function sample_reward of the Environment class. It sets 
the next state in the state attribute of the object and returns a numerical reward.

'''

#-------Your code starts here---------------