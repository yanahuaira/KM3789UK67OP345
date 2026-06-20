
print ("Hi Kimia!, since you are a very busy scientist "
       "\nI created this hoping I can meet you (but I understand if it is 
       \n not a good time")
question1 = "Would you share some of your time with me?"
choices1 = {
        "A": "Absolutely, I will be happy to make time so we can get to know each other :D",
        "B": "I am not interested in meeting a clever, loyal, commited, disciplined, slightly good looking latino"
    }

print (question1)
for key in choices1:
    print (f"{key}: {choices1[key]}")
a1 = input("Please type your answer: ").strip().upper()
while a1 =="B" or a1 not in choices1:
    if a1 not in choices1:
        print("Please select A or B")
        a1 = input("Please type your answer: ").strip().upper()
    else:
              print("It makes no sense to choose that answer, please try again :(. "
                    "Answer A might be the correct answer ;)")
              a1 = input("Please type A or B: ").strip().upper()

print("Awesome! I really appreciate you making time.")

#question 2

print ("The next two weeks I am available after 5 pm any day during weekdays, "
       "\nand I can adapt to anytime during weekends")

q2= "Which day would work best for you?"
ch2= {"A": "Monday", "B": "Tuesday", "C": "Wednesday","D": "Thursday","E": "Friday","F": "Saturday", "G": "Sunday"}
print (q2)
for key in ch2:
    print (f"{key}: {ch2[key]}")
weekday_key = {"A", "B", "C", "D", "E"}
weekend_key = {"F", "G"}
a2 = input("Please type your answer ").strip().upper()

while a2 not in ch2:

        print("Invalid choice. Please choose one of:", ", ".join(ch2.keys()))
        a2 = input("Please type your answer: ").strip().upper()


if a2 in weekday_key:
            print ("Then we could have dinner. I am not sure if you have dietary restriction "
                   "\n(maybe pork?). "
                    "\nI though of some options.")

            q3= "Which would you prefer?"
            ch3= {"A": "Italian", "B": "Sushi", "C": "Middle-eastern", "D": "Asian", "E": "Other"}
            print(q3)
            for key in ch3:
                print (f"{key}: {ch3[key]}")
            a3 = input("Please type your answer ").strip().upper()
            while a3 not in ch3:
                print ("Invalid choice. Please choose one of:", ", ".join(ch3.keys()))
                a3 = input("Please type your answer: ").strip().upper()
            print ("That sounds good to me!")

else:
    print ("Great! Weekends give much more options. Here are some.")
    q4= "which would you prefer to do?"
    ch4= {"A": "Easy morning walk followed by brunch", "B": "Dinner/lunch and soccer match", "C": "Strawberry picking and lunch/breakfast", "D": "Try a new cafeteria or icecream (I have a few places in mind)" }
    print(q4)
    for key in ch4:
            print (f"{key}: {ch4[key]}")
    a4 = input("Please type your answer ").strip().upper()
    while a4 not in ch4:
        print ("Invalid choice. Please choose one of:", ", ".join(ch4.keys()))
        a4 = input("Please type your answer: ").strip().upper()
    print ("That sounds good to me!")

print ("For any of these plans (except picking strawberries) "
       "\nthere are options in NH. However, I am more than happy to pick you up "
       "\nif you are willing to go outside of NH. I think that will allow us to "
       "\nvisit some new places.")
q5= "Which sounds more like you?"
ch5= {"A": "I love NH and I want to stay here forever, lets stay close", "B": "Take me out of here! lets go as far as possible."}
print(q5)
for key in ch5:
    print (f"{key}: {ch5[key]}")
a5 = input ("Please type your answer").strip().upper()

while a5 not in ch5:
    print("Invalid choice. Please choose one of:", ", ".join(ch5.keys()))
    a5 = input("Please type your answer: ").strip().upper()

if a5 == "A":
    print("This gives us a good idea of what to do. ")

else:
    print("This gives us a good plan. "
          "\nDepending on your choices time might need to be "
          "\nre-adjusted depending of the activity")

a6 = input ("Type the time and address to meet/pick you up:")
a7 = input ("Anything else you would like to add?")
print ("Here is a summary of your answers")

print(f"Q1: {a1} - {choices1[a1]}")
print(f"Q2: {a2} - {ch2[a2]}")

if "a3" in globals() and a3 is not None:
    print(f"Q3: {a3} - {ch3[a3]}")

if "a4" in globals() and a4 is not None:
    print(f"Q4: {a4} - {ch4[a4]}")

print(f"Q5: {a5} - {ch5[a5]}")

print ("Time (it can be in month if needed jaja) and Address:", a6)
print ("Additional info:", a7)

print ("Would you be so kind to send me the summary please? "
       "\nIf you don't have time, have to much going on your life right now, or"
       "\nyou are not interested, I understand. I would really like the opportunity "
       "\nto know you Kimia :) ")
