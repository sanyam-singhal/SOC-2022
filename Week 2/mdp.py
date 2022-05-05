import numpy as np
import mdp_env

'''Still ongoing, do not try it yet'''


'''You access the underlying environment through the following class'''
class Environment:
    
    '''
    The init creates a copy of the underlying MDP as an object.
    To keep this file concise, I have put the underlying in a different file 'mdp_env.py'.
    '''

    def __init__(self):
        self.env=mdp_env.make()

    def close_env(self):
        self.env.close()

    def access_env(self, action):
        '''if you do not provide an action,
        the code chooses an action, uniformly at random'''
        if action==None:
            action=np.random.choice(self.env.actions)
        
        self.state, self.reward, self.done=self.env.step(action)
        '''
        Observations are position and velocity, which are continuous variables
        for now let us work with discretized version, and see how we can perform
        we may work with continous data later
        '''
        return self.state, self.reward, self.done
    
'''Your method to choose the best action'''
'''Essentially, your RL algorithm is the strategy to choose'''

def strategy(state, reward, done):
    next_action=None
    '''
    YOUR CODE COMES HERE
    FEEL FREE TO DECLARE ANY VARIABLES, LOCAL OT GLOBAL
    AVOID DECLARING ANY OTHER PARAMETER IN THE FUNCTION
    IDEALLY, YOUR ACTION SHOULD ONLY DEPEND ON THE CURRENT STATE,
    REWARD OBTAINED AFTER COMING TO THIS STATE, WHETHER OR NOT THE EPISODE 
    HAS ENDED (IGNORE THE INFO PART FOR NOW)
    '''
    return next_action

problem=Environment()

'''Play around with number of iterations to generate episodes
of different lengths. At times, they would be shorter than 1000 because the 
agent reaches the terminal state before 1000th iteration'''

'''In this problem, the terminal state is the mountain top'''
number_iterations=1000

for i in range(0,number_iterations):
    next_action=strategy()
    next_state, obtained_reward, done= problem.access_env()

    '''
    It would be useful to print states and rewards to see how
    the problem is evolving.
    '''