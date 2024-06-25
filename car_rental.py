from functions import optimizedCost

# User input section
seat_capacity = int(input("Please input number (seat): "))
option, cost, units = optimizedCost(seat_capacity)

# Display results
print(f"{option} * {units}")
print(f"Total = PHP {cost}")