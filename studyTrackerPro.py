def save_entry(subject_studied, hours_spent):
    with open("studytracker.txt", "a") as study_tracker:
        study_tracker.write(f"{subject_studied.lower()},{hours_spent}\n")
    
    print("Subject Logged")
    
def load_entries():
    
    try:
        with open("studytracker.txt", "r") as study_tracker:
            study_logs = study_tracker.readlines()
            
    except FileNotFoundError as err:
        print(err)
        return
    
    entries = []
        
    for study_log in study_logs:
        lines = study_log.strip().split(",") 
        if len(lines) == 2:
            try:
                
                entries.append((lines[0].lower(), int(lines[1]))) 
            except ValueError:
                pass
    return entries
    
def show_summary(entries):
    if not entries:
        print("Nothing to summarize")
        return
    
    total_studied_hours = sum([h for _,h in entries]) 
    print(f"Total hours studied is {total_studied_hours} hours") 
    
    
    # shows most studied subject
    tracker = {}
    
    for s,h in entries:
        tracker[s.capitalize()] = tracker.get(s.capitalize(), 0) + h
    
    most_studied = max(tracker, key=tracker.get)
    print(f"Most studied subject is {most_studied}")
    
    # present a summary as a dictionary
    summary = {s : f"{h} hours studied" for s,h in tracker.items()}
    print(summary)
    
        # show subjects studied for over four hours
    greater_hours = [s.capitalize() for s,h in tracker.items() if h > 4]
    
    
    if greater_hours:
        print(f"Subjects studied for over 4 hours are: ")
        for subject in greater_hours:
            print(subject)
    else:
        print("No subject has passed 4 hours yet.")

def main():
    while True:
        
        print("\n--- Study Tracker ---")
        print("1. Log new study")
        print("2. Show summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        
        if choice == "1":
            subject_studied = input("What subject did you study: ")
            hours_logged = input("How many hours did you read for: ")
            
            if hours_logged.isdigit():
                save_entry(subject_studied, hours_logged)
            else: 
                print("Please enter a valid number")
        
        elif choice == "2":
            entries = load_entries()
            show_summary(entries)
            
        elif choice == "3":
            print("Goodbye.")
            break

        else :
            print("Invalid choice, Exiting")
        
main()
