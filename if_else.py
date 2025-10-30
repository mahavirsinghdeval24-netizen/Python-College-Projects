def evaluate_score(score):
    print(f"Evaluating score: {score}")
    if score>=90:
        print("Excellent! Your grade is A.\n")
    elif score>=80:
        print("Well done! Your grade is B.\n")
    elif score>=70:
        print("Good job! Your grade is C.\n")
    elif score>=60:
        print("You passed. Your grade is D.\n")
    else:
        print("Unfortunately, Your grade is F.\n")

print("\n---Evaluating Scores---")
evaluate_score(85)
evaluate_score(96)
evaluate_score(63)
evaluate_score(55)

def check_pass(pas):
    if(len(pas)>=8):
        if any(char.isdigit() for char in pas):
            print("Password is valid!\n")
        else:
            print("Password is long enough, but lacks digits!\n")
    else:
        print("Password is too short!\n")

print("\n---Evaluating passwords---")
check_pass("short")
check_pass("short_pass_12345")
check_pass("short_password")