import random
from game_data import data
from art import logo, vs

score = 0

# first person
first_index = random.randint(0, 49)
first_data = data[first_index]

while True:
    #second person
    second_index = random.randint(0, 49)
    while first_index == second_index:
        second_index = random.randint(0, 49)
    second_data = data[second_index]

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}.")
    print(vs)
    print(f"Against A: {second_data['name']}, a {second_data['description']}, from {second_data['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a' and first_data['follower_count'] < second_data['follower_count']:
        break
    elif answer == 'b' and second_data['follower_count'] < first_data['follower_count']:
        break
    
    score += 1

    #The second person becomes the first person
    first_data = second_data
    first_index = second_index

print(logo)
print(f"Sorry that's wrong. Final score: {score}.")