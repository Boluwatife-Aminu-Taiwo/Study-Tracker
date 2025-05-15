import csv
from datetime import datetime

FILENAME = "studytracker.csv"

def save_entry(subject, hours):
    # storin the date in now .strftime (is the format of the date and time you want it to store it in)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([subject.lower(), hours, now])
    print("Entry saved.")

def load_entries():
    entries = []
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    subject, hours, timestamp = row
                    entries.append((subject, int(hours), timestamp))
    except FileNotFoundError:
        print("No data file found yet.")
    return entries

def show_summary(entries):
    if not entries:
        print("No data to summarize.")
        return

    total_hours = sum([h for _, h, _ in entries])
    print(f"\nTotal study time: {total_hours} hours")

    subject_totals = {}
    for subject, hours, _ in entries:
        subject_totals[subject] = subject_totals.get(subject, 0) + hours

    print("\nStudy time by subject:")
    for subject, hours in subject_totals.items():
        print(f"- {subject.capitalize()}: {hours} hrs")

    most_studied = max(subject_totals, key=subject_totals.get)
    print(f"\nMost studied subject: {most_studied.capitalize()}")

    print("\nRecent logs:")
    for subject, hours, time in entries[-5:]:  # show last 5 logs
        print(f"{time} → {subject.capitalize()} ({hours} hrs)")

def main():
    while True:
        subject = input("\nWhat subject did you study? ")
        hours = input("How many hours? ")

        if not hours.isdigit():
            print("Invalid input for hours. Try again.")
            continue

        save_entry(subject, int(hours))

        see_summary = input("View progress? (y/n): ").lower()
        if see_summary == "y":
            entries = load_entries()
            show_summary(entries)

        again = input("Log another? (y/n): ").lower()
        if again != "y":
            print("Goodbye.")
            break


main()