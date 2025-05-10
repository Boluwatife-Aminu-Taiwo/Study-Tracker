def save_entry(sub_studied, hours_studied):
    with open("studytime.txt", "a") as studytime_file:
        studytime_file.write(sub_studied + "," + hours_studied + "\n")
    print("Saved data!")

def load_entries():
    # using with open you would not need to close it but you have to indent what you want to do
    
    try: 
        with open("studytime.txt", "r") as studytime_files:
            lines = studytime_files.readlines()
    except FileNotFoundError as err:
        print(err)
        return[]
    
    entries = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2:
            entries.append((parts[0].lower(), int(parts[1])))
    return entries

def show_summary(entries):
    if not entries:
        print("No study data to summarize.")
        return
    
    total_hours = sum([h for _, h in entries])
    
    print("Total study hours: ", total_hours)
    
    # - This builds a **dictionary** that tracks total hours per subject.
    # - `.get(subject, 0)` means: “if subject already in dictionary, get its value; else, start at 0.”
    # - Then we add the current `hours` to it.

    # > So if the subject "python" shows up multiple times, it keeps accumulating total hours.
    tracker = {}
    
    for subject, hours in entries:
        tracker[subject] = tracker.get(subject, 0) + hours
        
    # max() finds the key (subject) with the highest value (hours) in the tracker dict.
    top_subject = max(tracker, key=tracker.get)
    print("Most studied subject: ", str(top_subject).capitalize())
    
def main():
    
    subject_studied = input("What subject did you study? ")
    hours_studied = input("How many hours? ")
    
    if not hours_studied.isdigit():
        print("Invalid hours. Please enter a number. ")
        return
    
    save_entry(subject_studied, hours_studied)
    
    feedback = input(" want to see your progress? (y/n): ").strip().lower()
    
    if feedback == "y":
        entries = load_entries()
        show_summary(entries)
    elif feedback == "n":
        print("alright. See you next session")
    else:
        print("Invalid input. Exiting")
        
main()