from art import logo,vs
from game_data import data
import os
import random

score = 0
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)


should_continue = True
while should_continue:

    print(logo)


    name_a= account_a['name']
    descr_a= account_a['description']
    country_a = account_a['country']

    name_b= account_b['name']
    descr_b= account_b['description']
    country_b = account_b['country']


    print(f"Compare A: {name_a}, a {descr_a},from {country_a}")
    print(vs)
    print(f"Against B: {name_b}, a {descr_b}, from {country_b}")

    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']

    print(f"Hint: A is {followers_a} and B is {followers_b} ")


    question = input("Who has more followers? Type 'A' or 'B':").lower()

    if  question == "a":
        if followers_a > followers_b:
            score += 1
            print(f"You are right,Your curent score is {score}")
        else:
            should_continue = False
            os.system('cls')
            print(f"You are wrong,final score is {score}")
    elif question == "b":
        if followers_b > followers_a:
            score += 1
            print(f"You are right,Your curent score is {score}")

        else:
            should_continue = False
            os.system('cls')
            print(f"You are wrong,Your final score is {score}")

    account_a = account_b
    account_b = random.choice(data)