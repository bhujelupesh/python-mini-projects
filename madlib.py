import random

def katha():
    value = random.randint(1,6)
    
    if value == 1:
        story = f"The {adjective} dog {verb} {adverb} to the park. It found a {noun} and started {verb}ing with it. Everyone laughed at the {adjective} dog."
        return story
    
    elif value == 2:
        story = f"A {adjective} wizard {verb} {adverb} on a {noun}. Along the way, he met a {adjective} dragon that could {verb} {adverb}. They became friends and {verb} together."
        return story
    
    elif value == 3:
        story = f"In a {adjective} cave, a {noun} was hidden. A {adjective} pirate {verb} {adverb} to find it. After {verb}ing for hours, the pirate finally discovered the {noun}."
        return story
    
    elif value == 4:
        story = f"A {adjective} cat {verb} {adverb} in the moonlight. It found a {noun} and started {verb}ing around it. The neighbors watched the {adjective} performance."
        return story
    
    elif value == 5:
        story = f"A {adjective} car {verb} {adverb} down the street. It almost hit a {noun} but {verb} just in time. The driver was very {adjective} after the {noun}."
        return story
    
    else:
        story = f"In a {adjective} garden, flowers {verb} {adverb}. A {adjective} child found a {noun} and started {verb}ing it. The garden was full of {adjective} surprises."
        return story

print("Welcome to Mad Libs!")

noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

print("\nHere's your story:")
print(katha())