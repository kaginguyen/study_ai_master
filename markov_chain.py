import numpy as np
import random as rm



# Possible states
states = ["A","B","C"]

# Possible sequences of states
state_transition_sequences = [["AA","AB","AC"],["BA","BB","BC"],["CA","CB","CC"]]

# Transition probability matrix
state_transition_matrix = [[0.2,0.6,0.2],[0.1,0.5,0.4],[0.3,0.3,0.4]]

# Double chek if state_transition_matrix is setup correctly
for transition in state_transition_matrix:
    tmp = map(float, transition)
    total = round(sum(tmp), 1)
    if total != 1: 
        raise ValueError(f"Transition Matrix probabilities are incorrect {transition}")


# Parse sequences and matrix into dict for easy access during calculation 
state_transition_matrix_parsed = {}
i = 0 

for i in range(len(state_transition_sequences)): 
    _states = state_transition_sequences[i]
    _values = state_transition_matrix[i] 
    for j in range(len(_states)):
        state_transition_matrix_parsed[_states[j]] = _values[j] 

    i+= 1 

print("State Transition Matrix: ", state_transition_matrix_parsed)



def state_forecast(period):
    # Randomly choose the starting state
    starting_state = np.random.choice(states)
    print("Start state: " + starting_state)

    # History list of state changes
    state_list = [starting_state]

    # Base probability 
    prob = 1
    prob_list = [str(prob)]
    

    i = 0
    while i != period: 
        starting_state_index = states.index(starting_state)

        # Randomly choose a sequence based on the probability of the transition matrix 
        state_sequence = np.random.choice(state_transition_sequences[starting_state_index],replace=True,p=state_transition_matrix[starting_state_index])

        # Because each transition is independent, to calculate the probability of the state_list we just need to multiply the transition probability 
        prob = prob * state_transition_matrix_parsed.get(state_sequence) 
        prob_list.append(str(state_transition_matrix_parsed.get(state_sequence)))

        # Reset starting_state for the next period 
        starting_state = state_sequence[-1] 
        state_list.append(starting_state) 

        i += 1


    print("Possible states: ", str(state_list))
    print("End state after ", str(period), " periods: ", starting_state)
    print("Probability of the possible sequence of states: ",  " * ".join(prob_list), " = ", str(prob))


# Function that forecasts the possible state for the next 2 periods
state_forecast(2)