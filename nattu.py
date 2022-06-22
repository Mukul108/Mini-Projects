import time
# I imported time so that user can read it 
print("Hi! 😃😃")
input("Say hello to Nattu: ")
print("My name is Nattu")
time.sleep(1)
name = "Nattu🤖: What is  your name"
print(name)
x=input()
time.sleep(1) 
print("Nattu🤖: "+ x+" is a very cool name🤘🤘🤘")
# if your age is greater than 30 it would say young else old in a funny way
time.sleep(2)
y=int(input("Nattu🤖: What is your age: "+ x+" :"))
if y<30:
   print("Nattu🤖: Oh you are so young "+ x+"🔥🔥🔥")
else:
   y>30
   print("Nattu🤖: Oh my god! your\nyoungness has gone🤣🤣🤣🤣,\nsorry sorry I was just joking ")
   time.sleep(3)
z=input("Nattu🤖: hey "+x+" where do you live: ")
print("Nattu🤖: wow \n"+ z+" is a amazing place I will visit it soon\n through google map🤣🤣🤣. ")
time.sleep(3)
a=input("Nattu🤖: Who is your favourite \ncharacter in marvel (Spiderman🕷️🕸️ or Ironman🧠):")
s=a.lower()
# there are two different reply for spiderman and ironman and by chance if didnot typed bith of them the output will be different
if s=="spiderman":
   print("Nattu🤖: Good choice but I like\n ironman(the intelligent one)")
elif s=="ironman":
   print("Nattu🤖: Great choice👌👌👌")
else:
   print("Nattu🤖: Let's leave this question😅😅")
time.sleep(2)
print("Nattu🤖: Well I have got all your information 😼😼\nIf you dont want your privacy to be leaked \ngive me a star 🌟 ")
time.sleep(2)
input(" your response to this betrayal:")
print("Nattu🤖: I assume you abused me🤔🤔🤔")
time.sleep(2)
print("Nattu🤖: you are a boring person "+x+"😩😩😵😵 \nI will talk to you later")
