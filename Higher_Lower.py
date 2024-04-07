def questionsforhigher():
    questions = [
    ["What is the name of the largest moon of Saturn?", "Titan", "Second-largest moon in the Solar System."],
    ["What is the highest mountain on Earth?", "Mount Everest", "Located in the Himalayas."],
    ["In astrophysics, what is the name of the largest black hole discovered?", "Tonneau", "It has a mass of over 40 billion times that of the Sun."],
    ["What is the highest point on Mars?", "Olympus Mons", "The tallest volcano in the solar system."],
    ["In biology, what is the largest mammal on Earth?", "Blue Whale", "Can reach lengths of over 100 feet."],
    ["What is the highest waterfall in the world?", "Angel Falls", "Located in Venezuela, it has a total height of 3,212 feet."],
    ["In astrophysics, what is the name of the largest known star?", "UY Scuti", "It is a hypergiant star in the constellation Scutum."],
    ["What is the highest recorded temperature on Earth in degree centigrade?", "56.7", "Recorded in Furnace Creek Ranch, Death Valley, USA, on July 10, 1913."],
    ["In biology, what is the tallest tree species?", "Coast Redwood", "They can reach heights exceeding 350 feet."],
    ["What is the highest recorded speed of a manned vehicle in km/h?", "39,897", "Achieved by Apollo 10 during re-entry to Earth on May 26, 1969."],
    ["What is the deepest point in Earth's oceans?", "Mariana Trench", "Located in the western Pacific Ocean, it reaches a depth of about 36,070 feet."],
    ["In astrophysics, what is the most massive planet in our solar system?", "Jupiter", "It has a mass more than 300 times that of Earth."],
    ["What is the highest mountain known in our solar system?", "Olympus Mons", "It is an extinct volcano and the tallest planetary mountain known."],
    ["Which club did Cristiano Ronaldo start his professional football career with?", "Sporting Lisbon", "He made his senior debut for Sporting Lisbon in 2002."],
    ["How many FIFA Ballon d'Or awards has Cristiano Ronaldo won as of 2022?", "5", "He won the Ballon d'Or in 2008, 2013, 2014, 2016, and 2017."],
    ["Which club did Cristiano Ronaldo join after leaving Manchester United in 2009?", "Real Madrid", "He joined Real Madrid for a then-world record transfer fee."],
    ["What is the name of Cristiano Ronaldo's first son?", "Cristiano Ronaldo Jr.", "He was born on June 17, 2010."],
    ["In which year did Cristiano Ronaldo return to Manchester United?", "2021", "He rejoined Manchester United after leaving Juventus."],
    ["Which national team has Cristiano Ronaldo represented in international football?", "Portugal", "He is one of Portugal's most capped and highest-scoring players."],
    ["What is the total number of UEFA Champions League titles won by Cristiano Ronaldo?", "5", "He won the Champions League with Manchester United and Real Madrid."],
    ["At which club did Cristiano Ronaldo play before joining Juventus?", "Real Madrid", "He played for Real Madrid from 2009 to 2018."],
    ["What is Cristiano Ronaldo's jersey number at Manchester United?", "7", "He wears the number 7 jersey, which he also wore during his first spell at the club."],
    ["In which year did Cristiano Ronaldo win the UEFA European Championship with Portugal?", "2016", "Portugal won the Euro 2016 tournament held in France."],
    ]
    return questions
def higher():
    questions=questionsforhigher()
    import random
    
    score=0
    
    x=True
    while x==True:
        q=random.choice(questions)
        questions.remove(q)
        print("--------------------------")
        print(f"score point is : {score}")
        print("--------------------------")
        print(f"question : {q[0]}\nhints : {q[2]}")
        answer=input("the answer is :").lower()
        if answer==q[1].lower():
            score+=1
        else:
            print(" wrong answer")
            print("answer was ", q[1])
            x=False

            
def questionsforlower():
    questions_lower = [
    ["What is the name of the smallest planet in our solar system?", "Mercury", "It has a diameter of about 4,880 kilometers (3,032 miles)."],
    ["In biology, what is the smallest living organism?", "Mycoplasma genitalium", "It is a type of bacteria measuring about 200-300 nanometers."],
    ["What is the lowest point on land on Earth?", "Dead Sea", "Located between Israel and Jordan, it sits at around 430 meters (1,412 feet) below sea level."],
    ["In astrophysics, what is the least massive type of star?", "Red Dwarf", "They have masses less than 0.4 times that of the Sun."],
    ["What is the lowest recorded temperature on Earth in degree centigrade?", "-89.2", "Recorded at the Soviet Union's Vostok Station in Antarctica on July 21, 1983."],
    ["What is the name of the smallest bird species?", "Bee Hummingbird", "It measures about 5 centimeters (2 inches) in length."],
    ["In geology, what is the lowest point on the surface of the Earth?", "Challenger Deep", "It is the deepest known part of the Earth's seabed in the Mariana Trench."],
    ["What is the least popuylated country in the world?", "Vatican City", "It is an independent city-state with a population of fewer than 1,000 people."],
    ["What is the smallest bone in the human body?", "Stapes", "It measures about 3 millimeters in length."],
    ["What is the lowest flying bird?", "Bar-headed Goose", "They are known for migrating at extremely high altitudes over the Himalayas."],
    # Add or modify more questions about lower and lowest things as needed
    ]
    return(questions_lower)

def lower():
    questions_lower=questionsforlower()
    import random
    
    score=0
    
    x=True
    while x==True:
        q=random.choice(questions_lower)
        questions_lower.remove(q)
        print("--------------------------")
        print(f"score point is : {score}")
        print("--------------------------")
        print(f"question : {q[0]}\nhints : {q[2]}")
        answer=input("the answer is :").lower()
        if answer==q[1].lower():
            score+=1
        else:
            print(" wrong answer")
            print("answer was ", q[1])
            x=False

def mixed():
    questions=questionsforhigher()+questionsforlower()
    score=0
    import random
    x=True
    while x==True:
        q=random.choice(questions)
        questions.remove(q)
        print("--------------------------")
        print(f"score point is : {score}")
        print("--------------------------")
        print(f"question : {q[0]}\nhints : {q[2]}")
        answer=input("the answer is :").lower()
        if answer==q[1].lower():
            score+=1
        else:
            print(" wrong answer")
            print("answer was ", q[1])
            x=False
def main():
    choice=input("which you want to play? higher or lower or random").lower()
    if choice == "higher":
        print('''  ___ ___ .___  ________  ___ ________________________ 
 /   |   \|   |/  _____/ /   |   \_   _____/\______   \\
/    ~    \   /   \  ___/    ~    \    __)_  |       _/
\    Y    /   \    \_\  \    Y    /        \ |    |   \\
 \___|_  /|___|\______  /\___|_  /_______  / |____|_  /
       \/             \/       \/        \/         \/ 
    
    ''')
        higher()
    elif choice=='lower':
        print('''
.__                              
|  |   ______  _  __ ___________ 
|  |  /  _ \ \/ \/ // __ \_  __ \\
|  |_(  <_> )     /\  ___/|  | \/
|____/\____/ \/\_/  \___  >__|   
                        \/       
    ''')
        lower()
    else:
        print('''
.__    .__       .__                 .__                              
|  |__ |__| ____ |  |__   ___________|  |   ______  _  __ ___________ 
|  |  \|  |/ ___\|  |  \_/ __ \_  __ \  |  /  _ \ \/ \/ // __ \_  __ \\
|   Y  \  / /_/  >   Y  \  ___/|  | \/  |_(  <_> )     /\  ___/|  | \/
|___|  /__\___  /|___|  /\___  >__|  |____/\____/ \/\_/  \___  >__|   
     \/  /_____/      \/     \/                              \/       
    ''')
        mixed()
user=input("do you want to play higher lower game? (y/n)?")
if user[0]=='y':
    main()
