import datetime

def write_entry():
    entry = input("What's on your mind today?\n")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}\n{entry}\n\n")
    print("Entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r") as file:
            print("\nYour Diary:\n")
            print(file.read())
    except FileNotFoundError:
        print("No entries yet. Start writing!")

while True:
    choice = input("\n1. Write Entry\n2. Read Entries\n3. Exit\nChoose: ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")