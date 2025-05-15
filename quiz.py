from question import Question
question_prompt = [
    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange\n\n",
    "\nWhat color are bananas? \n(a) Magenta \n(b) Yellow \n(c) Pink\n\n" ,
    "\nWhat color are strawberries? \n(a) Red \n(b) Blue \n(c) Grey\n\n" ,
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 10
            
    print("You scored " + str(score) + "/" + str(len(questions) * 10))
    
run_test(questions)