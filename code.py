import os.path

# Initialize variables
total_age = 0
total_answers = [[0]*5 for _ in range(10)]
count = 0
filename = 'survey_data.txt'

# Load previous survey data if file exists
if os.path.exists(filename):
    with open(filename, 'r') as f:
        for line in f:
            age, *answers = map(int, line.split())
            total_age += age
            for i in range(10):
                total_answers[i][answers[i]-1] += 1
            count += 1

# Get survey data from user
while True:
    age = input("Enter age (or 'q' to quit): ")
    if age.lower() == 'q':
        break
    answers = input("Enter 10 answers separated by spaces (1-5): ").split()
    
    # Validate input and update variables
    try:
        age = int(age)
        answers = [int(answer) for answer in answers]
        if not all(1 <= answer <= 5 for answer in answers):
            raise ValueError
        total_age += age
        for i in range(10):
            total_answers[i][answers[i]-1] += 1
        count += 1
        # Save survey data to file
        with open(filename, 'a') as f:
            f.write(f"{age} {' '.join(str(answer) for answer in answers)}\n")
    except ValueError:
        print("Invalid input, please try again.")

# Calculate averages
if count > 0:
    avg_age = total_age / count
    print(f"Average age: {avg_age:.2f}")
    print("Average answers:")
    for i in range(10):
        total = sum(total_answers[i])
        if total > 0:
            avg_answer = sum((j+1)*total_answers[i][j] for j in range(5)) / total
            print(f"Question {i+1}: {avg_answer:.2f}")
        else:
            print(f"Question {i+1}: No data entered.")
else:
    print("No data entered.")
