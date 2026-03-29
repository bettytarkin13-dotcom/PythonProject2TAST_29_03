
def detect_duplicates():
    seen=set()
    duplicates_found=False

    while True:
        user_input=input("Enter a string(or 'quit' to quit): ")

        if user_input == 'quit':
            break

        if user_input in seen:
            duplicates_found=True
        else:
            seen.add(user_input)

        if duplicates_found:
            print("There is a duplicates")
        else:
            print("No duplicates")

detect_duplicates()


