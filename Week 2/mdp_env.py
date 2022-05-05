import numpy as np

'''Still ongoing, do not try it yet'''

class Env():
    def __init__(self):
        self.start_state=0
        self.terminal_state=None
        self.state=self.start_state
        self.done=False
        self.actions=np.array([])
        self.rewards=np.array([])

    def close(self):
        self.state=self.terminal_state

    def step(self, action):
        self.state=None
        self.reward=None
        if self.state==self.terminal_state:
            self.done=True

        return self.state, self.reward, self.done

def make():
    env_object=Env()
    return env_object