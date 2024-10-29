import streamlit

# Fitness function to calculate how close the candidate string is to the target
def calculate_fitness(candidate, target):
    return sum(1 for i, j in zip(candidate, target) if i == j)

# Generate a random string of the same length as the target
def random_string(length):
    return [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length)]

# Mutate the string based on the mutation rate
def mutate(parent, mutation_rate):
    child = parent[:]
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.choice('abcdefghijklmnopqrstuvwxyz')
    return child

# Main genetic algorithm function
def genetic_algorithm(target, mutation_rate):
    # Create a random starting string
    current = random_string(len(target))
    generation = 1
    fitness = calculate_fitness(current, target)

    # Continue until the target string is found
    while fitness < len(target):
        print(f"String: {current} Generation: {generation} Fitness: {fitness}")

        # Create a mutated child
        child = mutate(current, mutation_rate)
        child_fitness = calculate_fitness(child, target)

        # Replace parent if the child is better or equal
        if child_fitness >= fitness:
            current = child
            fitness = child_fitness

        generation += 1

    print("Target found")
    print(f"String: {current} Generation: {generation} Fitness: {fitness}")

# Get user input
name = input("Enter your name: ").lower()
mutation_rate = float(input("Enter your mutation rate (e.g., 0.1): "))

# Run the genetic algorithm with the input name as the target
genetic_algorithm(list(name), mutation_rate)
