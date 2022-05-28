# Relevant references and background for problem formulation and solution

## 1. Using reinforcement learning for optimizing profits by allocating funds across multiple stocks (portfolio management)
[This paper](https://www.sciencedirect.com/science/article/pii/S0020025505003166?casa_token=6CCNXeGgUg8AAAAA:Qf1Tr_SzQOAxHaN7BeN5TZctMzH9ifZH8-oV2xDuvl9YCl0ODNlcdo8_c71WHd9WOoR1Ss3n6Q) creates an asset allocation strategy by creating a meta policy and then maximising its performance. 

### Background 

References: 

1. [Must read](https://www.instadeep.com/research/blog/a-simple-introduction-to-meta-reinforcement-learning/)

What is meta policy? Meta policy or Meta-RL is a generalization of Markov decision processes. In the typical RL, we formulate an MDP for the problem and find the optimal policy. In case of meta-RL, we create a probability distribution of MDP. 

A typical MDP is of the form M=(S,A,$\gamma$,T,R) where S is the state space, A is the action space, $\gamma$ is the discount rate, T is the transition probability function and R is the reward space. In case of meta RL: we have a probability distribution p($M_{i}$) over the MDPs $M_{i}=(S_{i},A_{i},\gamma _{i},T_{i},R_{i})$. In meta-rl, these individual MDPs are often called tasks.

Why should this be better? Intuitively, do you expect the stock market's behaviour to remaind same every day? If no, then certainly a fixed MDP is inadequate to capture the nuances of the market. One immediate solution that comes to mind is to allow MDPs to change in a certain manner that can be still optimized for maximum reward: say we vary the MDPs as per a certain probability distribution that we think, based on empirical observation of the stock market, best represents the change in behaviour of the market.