task =input("Enter the task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no)")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task "
    case "medium":
        reminder = f"'{task}' is a medium priority task "
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority.")
        
if time_bound == "yes":
    reminder += "that requires attention today."
elif time_bound == "no":
    reminder +=  ". consider completing it soon."
else:
    print("Invalid input.")
    
print("\nReminder" + reminder)