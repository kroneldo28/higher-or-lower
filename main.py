# Lets's build the game or higher or lower 
#which gives the player two celebreties and ask who has the most followers.

# TODOs
# Handle the cases when the user enters neither a nor b as an answer

# Done
# Make sure A is different from B
# Prompt the comparison between A and B
# Actualy compare A and B
# Print the dictionary properly




import game_data
import art
import random
import replit

def compare(dict_a, dict_b, ans):
  """The Function takes 2 dictionaries and an answer a or b. It returns True if the answer is set to the dictionary that has more followers or False otherwise"""
  if ans == 'a' and dict_a['follower_count'] >= dict_b['follower_count']:
    return True
  elif ans == 'b' and dict_b['follower_count'] >= dict_a['follower_count']:
    return True
  else:
    return False

def prompt_comparison(dict_a, dict_b):
  """Prompt the comparison between A and B"""
  print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}.")
  print(art.vs)
  print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}.")

def good_answer_prompt(dict_a, dict_b, score):
  replit.clear()
  print(art.logo)
  print(f"You're right! Current score: {score}.")
  prompt_comparison(dict_a, dict_b)

def wrong_answer_prompt(score):
  replit.clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")

def choose(list_of_dictionaries, dic):
  """The function takes the list of dictionaries and a dictionary and returns a random dictionary within that list that is different from the dictionary given as a parameter"""
  answer = random.choice(list_of_dictionaries)
  found = False
  while not found:
    if answer == dic:
      answer = random.choice(list_of_dictionaries)
    else:
      found = True
  return answer

def start(data):
  """The game itself"""
  score = 0
  wrong_answer = False
  celeb_a = random.choice(data)
  celeb_b = choose(data, celeb_a)

  print(art.logo)
  prompt_comparison(celeb_a, celeb_b)

  while not wrong_answer:
    answer = input("Who has more followers? 'A' or 'B': ").lower()
    if compare(celeb_a, celeb_b, answer):
      score += 1
      celeb_a = celeb_b
      celeb_b = choose(data, celeb_a)
      good_answer_prompt(celeb_a, celeb_b, score)
    else:
      wrong_answer = True
      wrong_answer_prompt(score)


data = game_data.data
start(data)