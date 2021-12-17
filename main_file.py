import random
from game_data import data
from art import logo
from replit import clear
random_num_a = 0


#generates 2 random numbers
def gen_random_num():
    random_num_1 = random.randint(0, 49)
    random_num_2 = random.randint(0, 49)
    while random_num_1 == random_num_2 or random_num_1 == random_num_a:
        random_num_1 = random.randint(0, 49)
        random_num_2 = random.randint(0, 49)
    return random_num_1, random_num_2


#Generates 2 random numbers
random_numbers = gen_random_num()
random_num_a = random_numbers[0]
random_num_b = random_numbers[1]

#assigns variables for choice a
name_a = data[random_num_a]["name"]
follower_count_a = int(data[random_num_a]["follower_count"])
description_a = data[random_num_a]["description"]
country_a = data[random_num_a]["country"]

#assigns variables for choice B
name_b = data[random_num_b]["name"]
follower_count_b = int(data[random_num_b]["follower_count"])
description_b = data[random_num_b]["description"]
country_b = data[random_num_b]["country"]


def print_answer(name_1, followers_1, name_2, followers_2):
    '''prints the names and answers'''
    print(
        f"{name_1} has {followers_1} million followers.\n{name_2} has {followers_2} million followers\n"
    )


#----------The Game----------
#Welcome print:
#(NOTE: the VS logo was skipped because it takes up too much space)
print(logo)
choice = ""
answer = ""
score = 0

while choice == answer:
    print(
        f"Which has more instragram followers?\nA: {name_a}, a {description_a} from {country_a}\nVS:\nB:  {name_b}, a {description_b} from {country_b}"
    )

    choice = input("Type A or B: ").lower()

    if follower_count_a > follower_count_b:
        answer = "a"
    else:
        answer = "b"

    if choice == answer:
      clear()
      print("Correct!")
      print_answer(name_a, follower_count_a, name_b, follower_count_b)
      score += 1

      #assigns variables for choice a
      random_a_hold = random_num_a
      random_num_a = random_num_b
      name_a = name_b
      follower_count_a = follower_count_b
      description_a = description_b
      country_a = country_b

      #generate random numbers. (random_numbers[0] won't be the same as 'a' )
      random_numbers = gen_random_num()
      while random_numbers[0] == random_a_hold:
          random_numbers = gen_random_num()
      random_num_b = random_numbers[0]

      #assigns variables for choice B
      name_b = data[random_num_b]["name"]
      follower_count_b = int(data[random_num_b]["follower_count"])
      description_b = data[random_num_b]["description"]
      country_b = data[random_num_b]["country"]

    else:
        print("Wrong answer!")
        print_answer(name_a, follower_count_a, name_b, follower_count_b)
