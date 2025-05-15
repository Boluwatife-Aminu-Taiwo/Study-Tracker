import json
from datetime import datetime
import os

STUDY_FILE = "studytracker.json"

def load_sessions():
    if os.path.exists(STUDY_FILE):
        with open(STUDY_FILE, "r") as f:
            return json.load(f)
    return []

def save_session(subject, hours):
    sessions = load_sessions()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    session = {
        "subject": subject,
        "hours": int(hours),
        "time": timestamp
    }
    
    sessions.append(session)

    with open(STUDY_FILE, "w") as f:
        json.dump(sessions, f, indent=4)
    
    print("Session saved.")

def show_sessions():
    sessions = load_sessions()
    if not sessions:
        print("No sessions logged.")
        return
    
    for session in sessions:
        print(f"{session['time']} - {session['subject'].capitalize()} for {session['hours']} hour(s)")

def main():
    subject = input("What subject did you study? ")
    hours = input("For how many hours? ")
    save_session(subject, hours)

    review = input("Do you want to review all sessions? (y/n): ").lower()
    if review == "y":
        show_sessions()

if __name__ == "__main__":
    main()
