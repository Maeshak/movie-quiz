def run_quiz():
  questions = {
    "Jon Snow is a Targaryen. (True/False)": True,
    "Arya Stark's direwolf is named Ghost. (True/False)": False,
    "Daenerys Targaryen has three dragons. (True/False)": True,
    "Tyrion Lannister is known as the Kingslayer. (True/False)": False,
    "The Iron Throne is made of 1000 swords. (True/False)": False,
  }

score = 0
total_questions = len(questions)

for question, correct_answer in questions.items():
  print(question)
  user_answer = input("Enter your answer (True/False): ").lower() == "true"
  if user_answer == correct_answer:
    print("Correct!")
    score += 1
  else:
    print("Incorrect!")
user_answer = input("Enter your answer (True/False): ")

if user_answer not in ['True', 'False']:
  print('invalid output. Please enter True or False.')

if str(correct_answer == user_answer):
  score += 1
  print('correct,well done')
else:
  print(f"Incorrect, the answer was: {correct_answer}")

passing_score = total_questions // 2
results = "passed" if score >= passing_score else "failed"
print(f"Well done, you did great! Your score is: {score}/{total_questions}. You have {result} the quiz.")
 
while True:
  user_input = input("Do you want to restart the quiz? (yes/no): ")
if user_input not in ['Yes', 'No']:
  print("Invalid input, please select Yes or No")

if user_input == 'Yes':
  run_quiz()
else:
  print("Thank you for playing")

#run the quiz
run_quiz()