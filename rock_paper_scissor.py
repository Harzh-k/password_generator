import random

# ASCII art for each choice
art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissor": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Rules: what each choice beats
rules = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

# User input
user_choice = input("Enter your input (rock, paper, scissor): ").lower()

if user_choice not in art:
    print("Enter a valid input!!")
    exit()

print(art[user_choice])
print(f"You chose: {user_choice}")

# Computer choice
computer_choice = random.choice(list(art.keys()))
print(art[computer_choice])
print(f"Computer chose: {computer_choice}")

# Result
if user_choice == computer_choice:
    print("It's a Draw!!")
elif rules[user_choice] == computer_choice:
    print("🎉 You Win!!!")
else:
    print("💻 Computer Wins!!!")
