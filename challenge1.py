from datetime import datetime
import os

def save_data(subject, hours):
    date = datetime.now()
    time = date.strftime("%H:%M:%S")
    file_name = date.strftime("%Y-%m-%d.txt")
    if not os.path.exists("logs"):
        os.mkdir("logs")

    with open(f"logs/{file_name}", "a") as study_hour:
        study_hour.write(f"[{time}] {subject.capitalize()} - {int(hours)} hours\n")
        print("Data saved")

def main():
    
        
    subject = input("What subject did you study? ")
    hours = input("For how many hours? ")
    
    save_data(subject, hours)
    
    review = input("Do you want to review today's log: (y/n) ").lower()
    
    if review == "y":
        date = datetime.now().strftime("%Y-%m-%d.txt")
        with open(f"logs/{date}", "r") as study_hours:
            
            print(study_hours.read())
    elif review == "n":
        print("Alright, Another time")
    else:
        print("Wrong input, Exiting")
        
if __name__ == "__main__":
    main()