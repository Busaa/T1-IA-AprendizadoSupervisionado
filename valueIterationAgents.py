# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        # número de iterações q devem ser feitas
        for iteration in range(iterations):
            # faz uma cópia do dict anterior p atualizá-lo
            q_values = self.values.copy()
            # obtém todos os possiveis estados
            states = self.mdp.getStates()
            # para cada estado
            for state in states:
                # verifica se não está no estado terminal
                terminal_state = self.mdp.isTerminal(state)
                if not terminal_state:
                    # e nao estando,
                    # computa a melhor ação
                    best_action = self.computeActionFromValues(state)
                    # computa o valor da melhor ação
                    q_value = self.computeQValueFromValues(state, best_action)
                    # e atualiza aquele valor, naquela pos, na lista de valores
                    q_values[state] = q_value
            self.values = q_values




    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        next_state_n_prob = self.mdp.getTransitionStatesAndProbs(state, action)
        q_value = 0
        for next_state, prob in next_state_n_prob:
            reward = self.mdp.getReward(state, action, next_state)
            discount = self.discount
            next_q_value = self.getValue(next_state)
            q_value += prob * (reward + discount * next_q_value)
        return q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state):
            return None

        # else
        best_action = None
        # placeholder p melhor acao
        best_value = float("-inf")

        # todas possíveis ações
        actions = self.mdp.getPossibleActions(state)

        # para cada ação possível
        for action in actions:
            # descobre seu q-valor
            q_value = self.computeQValueFromValues(state, action)
            # e caso ele seja melhor doq o melhor até então
            if q_value > best_value:
                # atualiza o melhor q-valor
                best_value = q_value
                # e qual foi sua ação
                best_action = action

        return best_action


def getPolicy(self, state):
        return self.computeActionFromValues(state)

def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.computeActionFromValues(state)

def getQValue(self, state, action):
    return self.computeQValueFromValues(state, action)
