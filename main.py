def run_quiz():
    # Dictionary of questions with their correct answers
    questions = {
        "Jon Snow is a Targaryen. (True/False)": True,
        "Arya Stark's direwolf is named Ghost. (True/False)": False,
        "Daenerys Targaryen has three dragons. (True/False)": True,
        "Tyrion Lannister is known as the Kingslayer. (True/False)": False,
        "The Iron Throne is made of 1000 swords. (True/False)": False,
    }

    score = 0  # Initialize score to 0
    total_questions = len(questions)  # Total number of questions
    passing_score = total_questions // 2  # Define passing score as half of total questions

    # Iterate through each question
    for question, correct_answer in questions.items():
        print(question)  # Print the question
        while True:
            # Get user input and convert it to lowercase
            user_answer = input("Enter your answer (True/False): ").strip().lower()
            if user_answer in ['true', 'false']:
                user_answer = user_answer == 'true'  # Convert to boolean
                break  # Break the loop if input is valid
            else:
                print("Invalid input. Please enter True or False.")

        # Check if user's answer matches the correct answer
        if user_answer == correct_answer:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print(f"Incorrect. The answer was: {correct_answer}")

    # Determine if quiz is passed or failed based on score
    results = "passed" if score >= passing_score else "failed"
    # Print final score and result
    print(f"Well done, you finished the quiz!\nYour score is: {score}/{total_questions}. You have {results} the quiz.")

    while True:
        # Ask user if they want to restart the quiz
        user_input = input("Do you want to restart the quiz? (yes/no): ").strip().lower()
        if user_input in ['yes', 'no']:
            break  # Break the loop if input is valid
        else:
            print("Invalid input. Please select Yes or No.")

    if user_input == 'yes':
        run_quiz()  # Restart quiz if user wants to
    else:
        print("Thank you for playing!")  # End program if user does not want to restart

# Run the quiz for the first time
run_quiz()
