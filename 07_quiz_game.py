def quize_game():
    print("Welcome sir in quize game ")
    score = 0

    questions = [{ "qustion" : "which one is the caoital of india  ",
                  "options" : "a)hedrabad  b)channai  c)benglore  d)new delhi ",
                  "answer" : "D"            
                } ,
   
                {
                    "qustion": "What is Python?",
                    "options": "A) A snake  B) A programming language  C) A car  D) A game",
                    "answer": "B",
                    }
    ]
    for i , q in enumerate(questions,1):
        print(f"\nqustion {i}  :  {q['qustion']}")
        print(q["options"])
        

        user_answer = input("enter your answer in A/B/C/D").upper()

        if (user_answer == q["answer"]):
            print("ypur answer is  correct      :")
            score += 1

        else :
            print("your answer is wrong    :")

    print("\ngame over......")
    print(f"your score is {score} outof {len(questions)} ")





quize_game()