def optimizedCost(seat_number):
    # Definition of all options in a nested dictionary format
    choices = {
        'small': {'capacity': 5, 'cost': 5000},
        'medium': {'capacity': 10, 'cost': 8000},
        'large': {'capacity': 15, 'cost': 12000}
    }
    
    total_cost = {}
    # Two-variable for-loop for convenient access to nested dictionary
    for size, details in choices.items():
        # Use integer division instead of normal division allows for the program to adjust to capacities
        # that are not fully divisible by the given values
        units_required = (seat_number + details['capacity'] - 1) // details['capacity']
        # Tabulate total number of units needed for each size option
        total_cost[size] = units_required * details['cost']
    
    # Determine the option with lowest costs as well as number of units needed
    best_choice = min(total_cost, key=total_cost.get)
    minimum_cost = total_cost[best_choice]
    num_units = minimum_cost//choices[best_choice]['cost']

    # Return optimal cost, best option, and units required 
    return best_choice, minimum_cost, num_units