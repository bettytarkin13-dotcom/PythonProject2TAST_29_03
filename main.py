#q 1

grades=[]
while True:
    user_input = input("Enter a grade (-999 to finish): ")
    try:
        grade= float(user_input)
    except ValueError:
        print("invalid input please ignore")
        continue

    if grade == -999:
        if len(grades)<10:
            print("at least 10 valid grades are required.continue entering grades")
            continue
        else:
            break

    if grade < 0 or grade > 100:
        print("invalid input please enter a valid grade between 0 and 100")
        continue

    grades.append(grade)
average = sum(grades)/len(grades)
max_grade = max(grades)

print("\n result:")
print(f"The class average:{average}")
print(f"The maximum grade is:{max_grade}")
print(f"number of valid grades entered:{len(grades)}")

