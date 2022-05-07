import numpy as np

std=1
mean=1
'''
This class simply generates a bandit problem with number of bandit arms
being `num_bandits`, which itself is chosen randomly. The numbers being sampled
from the gaussian are the reward associated with those arms.

For simplicity, I have restricted ourselved to nonnegative rewards and decimals upto 2 digits
to avoid any floating point calculation errors.
'''
class Bandit_arms:

    def __init__(self, num_bandits):
        self.bandits=np.round(np.absolute(np.random.normal(loc=mean, scale=std, size=num_bandits)), decimals=2)

    def return_array(self):
        return self.bandits


'''
Minimum: 5 bandit arms and maximum: 20 bandit arms.
'''

num_bandits=np.random.randint(low=5, high=20,size=1)[0]
bandit_problem=Bandit_arms(num_bandits).return_array()
print("True mean rewards",bandit_problem)

'''
This is technically cheating, you should not be aware of the true underlying 
reward through any means. It doesn't matter while learning this but keep it in mind
that this data is unavailable to you (no need for learning if we knew already!).
'''

'''
Now for each arm, when we pull it, we get modulus of nunber sampled
from a gaussian with mean defined in `bandit_problem` array and standard
deviation=std.

Keep in mind that first bandit arm would have index 0.
'''

def bandit_simulator(arm_index):
    reward=np.round(np.absolute(np.random.normal(loc=bandit_problem[arm_index], scale=std, size=1)), decimals=2)[0]
    return reward


'''
So, now we have an environment that generates a bandit problem
with a random number of arms and random mean rewards. We have a function to 
sample reward on "pulling" each of these arms. Now, try out algorithms that 
can come close to mean rewards.

Any rule based method won't work, since means change everytime you run the python file.
So, your algorithm must truly be able to learn as good as it can in a single run of this file.

As you must have understood by now, learning is an iterative procedure. Typically, to represent limited
computational and time resources, upper limits on allowed learning iterations are imposed. So, I am setting 
a variable that defines number of allowed iterations. Of course, while building, you play around with it.
'''

num_allowed_iterations=2000

'''
Except for the values of mean, std, num_iterations, I don't think you should
have the need to change any of code written to this point.
'''

estimated_means=np.zeros(shape=num_bandits, dtype=float)

#--------------------------
# the part that truly matters
def bandit_solving_algo(num_bandits):

    '''
    your algorithm comes here

    delete the pass statement once you start, it is 
    just a placeholder.
    '''
    pass

#---------------------------
print("Estimated mean rewards",estimated_means)
'''
YOUR ALGORITHM MUST NOT USE THE TRUE BANDIT MEAN REWARD ARRAY AT ANY STEP.
`num_bandits` VARIABLE PROVIDES YOU THE NUMBER OF BANDITS ARMS AND SIMPLY CALL THE
SIMULATOR FUNCTION. ANY ALGORITHM ACCESSING MEAN REWARD ARRAY IS OBVIOUSLY WRONG.
'''

'''
Underlying function checks how well your estimate is. Since, the learning is completed by this point
so accessing the true mean for checking is somewhat acceptable.
'''
def check(bandit_problem, estimate_means):
    errors=np.absolute(estimate_means-bandit_problem)
    print("Error in mean reward prediction for each arm:",errors)

check(bandit_problem, estimated_means)