import random
from replit import clear
import art
import game_data

def user_guess():
    guess = input("Which is more popular? 'A' or 'B': ")
    return guess

def comparison(picks, guess):
    max_count = 0
    for i in range(0 ,len(picks)):
        if picks[i]['follower_count'] > max_count:
            max_count = picks[i]['follower_count']
    if guess.lower() == "a":
        guess = picks[0]['follower_count'] 
    elif guess.lower() == "b":
        guess =  picks[1]['follower_count']
    if guess >= max_count:
        print("That's Correct!")
        is_playing = True
        return is_playing
    elif guess < max_count:
        print("Incorrect! Game Over...")
        is_playing = False
        return is_playing
    
def famous_pick():
    picks = []
    contender1 = random.choice(game_data.data)
    picks.append(contender1)
    contender2 = random.choice(game_data.data)
    while contender1 == contender2:
        contender2 = random.choice(game_data.data)
    picks.append(contender2)
    return picks

def play_game(num):
    print(art.logo)
    num = num
    if num > 0:
        print("That was correct!")
        print(f"Current Streak: {num}\n")
    picks = famous_pick()
    print(f"A: {picks[0]['name']}, a/an {picks[0]['description']} from {picks[0]['country']} ")
    print(art.vs)
    print(f"B: {picks[1]['name']}, a/an {picks[1]['description']} from {picks[1]['country']} ")
    guess = user_guess()
    is_playing = comparison(picks=picks, guess=guess)
    if is_playing == True:
        clear()
        num+=1
        play_game(num)
    
    else:
        print("That's incorrect...")
        print(f"Your streak was {num}.")
        print("Thanks for playing!")
        
play_game(0)