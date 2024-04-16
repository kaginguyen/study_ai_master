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


# Generate a random list based on the given probability and calculate the possibility of having that list
def state_forecast(period: int):
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


state_forecast(2)



# Given a starting distribution of samples, what would be the final distribution of them with the given probability 
states_starting_distribution = [1000, 1000, 1000]

def state_distribution_forecast(starting_distribution: list, period: int):  

    i = 0
    states_starting_distribution = starting_distribution 

    while i != period: 
        # Reset after each period 
        _sample_to_A = 0
        _sample_to_B = 0
        _sample_to_C = 0

        for j in range(len(starting_distribution)): 
            _sample_to_A += states_starting_distribution[j] * state_transition_matrix[j][0]
            _sample_to_B += states_starting_distribution[j] * state_transition_matrix[j][1]
            _sample_to_C += states_starting_distribution[j] * state_transition_matrix[j][2]
        
        states_starting_distribution = [_sample_to_A, _sample_to_B, _sample_to_C]
        i += 1
        print(f"Sample Distribution after {i} periods: ", str(states_starting_distribution))


state_distribution_forecast(states_starting_distribution, 10) 