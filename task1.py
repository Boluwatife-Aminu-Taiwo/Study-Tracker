languages = ["Python", "Javascript", "SQL"]

study_hours = {
    "Python": 15,
    "Javascript": 7,
    "SQL": 10
}

for lang in study_hours:
    print(lang)

def most_studied(obj):
    max_hour = 0
    top_lang = ""
    
    for lang, hours in obj.items():
        if hours > max_hour:
            max_hour = hours
            top_lang = lang
            
    return top_lang

print(most_studied(study_hours))