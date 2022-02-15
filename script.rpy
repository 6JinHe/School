
# Characters
define x = Character("Me")
define m = Character(_("Mom"), color="#ea9a9b")
define a = Character(_("Alarm"), color="#e51f1f")
define b = Character(_("Bob"), color="#fceef2")
define d = Character(_("Professor David"), color="#fceef2")
define s = Character(_("Students"), color="#73fc8a")

# Test score
default test = 0


# DAY 1 (made by Angel)
label start:
    "{b}DAY 1{/b}"
    "{i}I partied so hard yesterday… I don't even remember what my name is.{/i}"

    $ player_name = renpy.input("What is my name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"
    
    x "Oh, I'm %(player_name)s."

    menu:
        "{i}Knock knock!!{/i}"

        "Hello?":
            jump hello

        "WT* is your problem?":
            jump problem


label hello:
    scene bg morning
    with fade

    show sleepy1
    x "aghhh... hello? Who are you?"

    hide sleepy1
    show mom1
    m "Wake up %(player_name)s!"

    hide mom1
    show sleepy2
    x "Okay mom..."
    hide sleepy2

    show mom2
    m "What do you want for breakfast?"

    menu:

        "A hamburger":
            jump hamburger

        "Nothing":
            jump nothing


label problem:
    scene bg morning
    with fade

    show shout
    x "WT* is your problem?"

    hide shout
    show momangry
    m "%(player_name)s, who do you think you are?!"
    m "Okay... No breakfast for you!"
    hide momangry

    jump nothing


label hamburger:
    scene bg kitchen
    with fade

    "You go to the dinning room."
    "Your mom gives you a hamburger."
    x "*munch munch*"
    x "It's delicious!"

    scene black
    "After eating the breakfast your mom drives you to school."

    jump schoolintro1


label nothing:
    scene black

    "You eat nothing."
    "You go directly to school."

    x "I'm so hungry...  I should have ate something!"

    jump schoolintro3


label schoolintro1:
    scene bg corridor

    "You enter school."

    show school1
    x "Hey Bob, what's up!"

    hide school1
    show bob
    b "All good, how are you?"

    hide bob
    show school
    x "Pretty good."
    x "My mom prepared me a hamburger and it was so damn tasty."

    jump school1


label schoolintro2:
    scene bg corridor

    show school1
    x "Hey Bob, what's up!"

    hide school1
    show bob
    b "All good, how are yaou?"

    hide bob
    show school
    x "Well, I'm not in my mood."
    x "I just had a fight with my mom and I had no breakfast."
    b "Sad."

    jump school1


label schoolintro3:
    scene bg corridor

    show school1
    x "Hey Bob, what's up!"

    hide school1
    show bob
    b "All good, how are you?"

    hide bob
    show school
    x "Well, I'm not in my mood."
    x "I had no breakfast."
    b "Sad."

    jump school1


label school1:
    scene bg classroom
    "You enter the classroom"

    show teacher
    d "Hey %(player_name)s and Bob, the class already started, silence please."

    hide teacher
    
    menu:

        "Continue talking":
            jump talking

        "Stop talking":
            jump nottalking


label talking:
    show school1
    x "Hey Bob, did you know that I have a dog called Bob?"

    hide school1
    show bob1
    b "Who tf asked dude?"

    hide bob1
    show teacherangry1
    d "..."

    hide teacherangry1
    show teacherangry
    d "I told you to stop talking!"

    hide teacherangry
    show teacherwhatever
    d "Whatever..."

    hide teacherwhatever


label nottalking:
    show teacher
    d "Tomorrow we have the final exam."
    d "Hence, today we will review everything."

    hide teacher
    show school2
    x "Oh my god. I wanted to play Valorant today! I forgot about the exam."

    scene black
    "The class was extremely boring."
    "School ends."

    "I go home and fall sleep."





# DAY 2 (made by He)
label day2:
    "{b}DAY 2{/b}"
    a "BEEP BEEP BEEP BEEP BEEP!"

    "You slam the alarm on the ground."

    menu:  

        "Sleep some more":
            jump sleep

        "Wake up":
            jump wake


label sleep: 
    scene bg morning
    with fade

    m "{i}KNOCK KNOCK KNOCK{/i}, wake up, it's time for school!"
    show sleep
    x "mhm."
    hide sleep
    m "{i}KNOCK KNOCK KNOCK{/i}, WAKE UP!"
    show sleep
    x "agh, 5 more minutes."
    hide sleep
    m "If you don't wake up, tomorrow you won't ever see your videogame collection again."
    show main 
    x "ugh, fine."
    hide main

    "You wake up, take a shower and get changed."
    "Because you woke up late, you decided to skip breakfast."

    jump school


label wake:
    scene bg kitchen
    with fade
    "You wake up, take a shower and go downstairs."

    menu:

        "Eat eggs with bacon":
            jump bacon

        "Eat cereal":
            jump cereal

        "Drink poison":
            jump poison 

label bacon:
    "*Munch Munch*. It was delicious."
    jump school

label cereal:
    "The milk was expired. It tasted terrible. Look at the expiration date next time."
    jump school

label poison:
    "Your head starts spinning as you slowly begin to lose consciousness."
    "You died. What did you expect?"
    scene bg died
    with fade

    menu: 

        "The end":
            return 

        "Go back":
            jump wake


label school:

    "You change into your uniform and get prepared for school."
    "You go to school."

    scene bg corridor
    with fade

    "On your way to the locker, you meet your friend Bob."
    show bob
    b "Yo, what's up? Did you study for the exam?"
    hide bob
    
    menu:

        "Yes, I studied a bit":
            jump studied

        "What exam?":
            jump no


label studied:

    show bob1
    b "Nice. People say the exam is really hard. Good luck."
    hide bob1
    show school
    x "Thank you man."
    hide school

    jump exam


label no:

    show bob2
    b "Bro, it's over for you."
    hide bob2
    show bob1
    b "They say that the exam is gonna be really hard this time."
    hide bob1
    show school
    x "Nah, I'm fine bro. Trust me."
    hide school


label exam: 

    scene bg classroom
    with fade
    show teacher
    d "Good morning students. Ready or not, today is the day of the final exam."
    hide teacher
    s "*sighs*"
    show teacher
    d "The exam is going to consist of 90 minutes. Only pen and calculator allowed. Good luck."
    hide teacher


label easy:

    $ answer1 = renpy.input("What is 2+2?")
    if answer1 == "4":
        $ test += 1
    if answer1 == "4":
        x "This is so easy for me."
    else:
        x "GRRRR"

    $ answer2 = renpy.input("What is 2-2?")
    if answer2 == "0": 
        $ test += 1
    if answer2 == "0":
        x "Nice."
    else: 
        x "Hmm."

    $ answer3 = renpy.input("What is 2x2?")
    if answer3 == "4": 
        $ test += 1
    if answer3 == "4":
        x "Isi pisi."
    else: 
        x "Shibal!"        

    $ answer4 = renpy.input("What is 2/2?")
    if answer4 == "1": 
        $ test += 1
    if answer4 == "1":
        x "Good."
    else: 
        x "Yikes."

scene bg 5years
with dissolve
pause 2

if test == 4:
    jump success
else:
    jump beggar

label success:

    scene black
    "After getting full marks in your exam, you were admitted in Hogwarts, and recognized as one of the geniuses of the 21st century."
    "After graduating, you decide to..."
        
    menu: 

        "Invest in Bitcoin":
            jump bitcoin
        "Become an entrepreneur":
            jump entrepreneur

label beggar: 

    scene black
    "No university wanted to accept you due to your horrible grades. Your mom kicked you out of the house for scoring so bad in your exam and accused you to be adopted. Maybe you should have studied." 
    "You become a street beggar."
    scene bg died
    with fade
    pause 2

return

label bitcoin:

    scene bg stock
    with fade

    "Bitcoin dropped rapidly in the next year."
    "As you were wasting your time investing in bitcoin, you couldn't pay your rent and no one accepted you for a job."
    "You become a street beggar."
    scene bg died
    with fade
    pause 2

return

label entrepreneur:

    "You and Bob work together to create ZESLA and SPACEZ. You become one of the most influential entrepreneur."
    "Due to your natural charisma, you find a beautiful wife and conceive two kids."

    scene bg end
    with pixellate 
    pause 2

    # This ends the game.

return
