def generate_binary_string(n: int): 
    base_list = ["1", "0"]
    for i in range(n-1): 
        updated_list = []
        for element in base_list:
            new_value_w0  = element + "0"
            new_value_w1  = element + "1"
            updated_list.append(new_value_w1)
            updated_list.append(new_value_w0) 
        base_list = updated_list 

    return updated_list 




def pick_gifts(n_items: int, n_choices: int): 
    possible_outcomes = generate_binary_string(n_choices) 
    qualified_outcomes = []

    for outcome in possible_outcomes: 
        binary_list = list(outcome)
        outcome_total = sum(int(x) for x in binary_list)
        if outcome_total == n_items: 
            qualified_outcomes.append(outcome) 

    return len(qualified_outcomes), qualified_outcomes 


result, result_list = pick_gifts(3, 5)
print(result_list)
print(result) 
