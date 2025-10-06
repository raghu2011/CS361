import random
import math
def simulated_annealing_melody(quality_func, notes, initial_temp, cooling_rate, stopping_temp):
    # Randomly select an initial melody from the available notes
    currentmelody =random.sample(notes, len(notes))
    bestmelody =currentmelody[:]  # Removed invalid syntax
    temperature =initial_temp
    while temperature> stopping_temp:
        # Create a neighboring melody by swapping two notes
        neighbor_melody=currentmelody[:]
        i, j =random.sample(range(len(notes)), 2)
        neighbor_melody[i], neighbor_melody[j] = neighbor_melody[j], neighbor_melody[i]

        # Calculate the change in melody quality
        delta_quality =quality_func(neighbor_melody) - quality_func(currentmelody)

        if delta_quality < 0 or random.random() < math.exp(-delta_quality / temperature):
            currentmelody =neighbor_melody[:]
            if quality_func(currentmelody) < quality_func(bestmelody):
                bestmelody= currentmelody[:]
        # Gradually reduce the temperature
        temperature *=cooling_rate
    return bestmelody
def quality_func(melody):
    score = 0
    for i in range(len(melody) - 1):
        if melody[i] == 'Sa' and melody[i + 1] != 'Re':
            score += 10
    return score
# Get user input for the notes
user_input =input("Enter the notes for the melody separated by commas: ")
notes =[note.strip() for note in user_input.split(',')]
bestmelody = simulated_annealing_melody(quality_func,notes,initial_temp=1000,cooling_rate=0.95,stopping_temp=0.01)
print("Best Melody:", bestmelody)