import random
import time

time.sleep(1)

lifeline_used = False

print("******welcome to kbc*********".center(100))
print("******this is your host: sarvesh khupat *********".center(100))


print("******TOTAL QUESTION WE HAVE 5 IN WHICH ALL QUESTIONS HAVE A PRICE*********".center(100))
print("******LETS PLAY !KAUN BANEGA CROREPATI!*********".center(100))

Userinterface = input("ENTER YOUR NAME TO REGISTRATION: ")

total_money = 0 

print(" Q1. Who is known as the “Missile Man of India”? ")
A = "1. JAWAHARLAL NEHRU"
B = ("2. VIKRAM SARABHAI".center(30))
C = ("3. APJ ABDUL KALAM")
D = ("4. HOMI J BHABHA".center(30)) 
print(A + B)
print(C + D)
print("FOR AUDIENCE POLL USE KEYWORD: 0 ")
choices = int(input("enter the option:" ))


#LIFELINE SECTION
if choices == 0:
    if not lifeline_used:
        lifeline_used = True
        print("\nAudience poll result:\n")
        print("1. JAWAHARLAL NEHRU  →", random.randint(0, 100), "%")
        print("2. VIKRAM SARABHAI   →", random.randint(0, 100), "%")
        print("3. APJ ABDUL KALAM   →", random.randint(0, 100), "%")
        print("4. HOMI J BHABHA     →", random.randint(0, 100), "%")
        choices = int(input("enter the option:" ))
    else:
        print("Lifeline already used.")
        choices = int(input("Enter your answer (1-4): "))
        
        
        
if (choices == 3):
    
    print("this is right answer and you won 1000rs")
    total_money += 1000
    
  
else:
    print("you choose wrong option")
    print(f"game over","{Userinterface},your money prize is:",total_money)
    exit()




print("Q2. The capital city of Australia is:")
E = "1.Sydney"
F = "2. Melbourne".center(30)
G = "3.Canberra" 
H = "4.Perth".center(21)
print(E + F)
print(G + H)
print("Enter 0 for Audience Poll Lifeline\n")
choices = int(input("enter the option:" ))


if choices == 0:
    if not lifeline_used:
        lifeline_used = True
        print("\nAudience poll result:\n")
        print("1 →", random.randint(0, 100), "%")
        print("2 →", random.randint(0, 100), "%")
        print("3 →", random.randint(0, 100), "%")
        print("4 →", random.randint(0, 100), "%")
        
        choices = int(input("\n now enter your option: "))
    else:
        print("Lifeline already used.")
        choices = int(input("Enter your answer: "))
    
    
        
if (choices ==3):
    print("that's the correct answer and you won 2000")
    total_money += 2000
else:
    print("that's the wrong answer")
    print(f"game over","{Userinterface},your money prize is:",total_money)
    exit()


print("Q3. Which planet is known as the “Red Planet”?")
I = "1.Venus"
J = "2.Mars".center(30)
K = "3.Jupiter"
L = "4.Saturn".center(28)
print(I + J)
print(K + L)
print("Enter 0 for Audience Poll Lifeline\n")
choices = int(input("enter your option:"))

if choices == 0:
    if not lifeline_used:
        lifeline_used = True
        print("\nAudience poll result:\n")
        print("1 →", random.randint(0, 100), "%")
        print("2 →", random.randint(0, 100), "%")
        print("3 →", random.randint(0, 100), "%")
        print("4 →", random.randint(0, 100), "%")
        
        choices = int(input("\n now enter your option: "))
    else:
        print("Lifeline already used.")
        choices = int(input("Enter your answer: "))
        
        
        
if (choices == 2):
    print("that's your correct option and you won 3000")
    total_money += 3000
else:
    print("that's the wrong answer")
    print(f"game over","{Userinterface},your money prize is:",total_money)
    exit()



print("Q4. In which year did India gain independence?")
M = " 1. 1942"
N = " 2. 1945".center(30)
O = " 3. 1947"
P = " 4. 1950".center(30)
print(M + N)
print(O + P)
print("Enter 0 for Audience Poll Lifeline\n")
choices = int(input("enter your option:"))

if choices == 0:
    if not lifeline_used:
        lifeline_used = True
        print("\nAudience poll result:\n")
        print("1 →", random.randint(0, 100), "%")
        print("2 →", random.randint(0, 100), "%")
        print("3 →", random.randint(0, 100), "%")
        print("4 →", random.randint(0, 100), "%")
        
        choices = int(input("\n now enter your option: "))
    else:
        print("Lifeline already used.")
        choices = int(input("Enter your answer: "))
if (choices == 3):
    print("that's the correct option and you won 4000")
    total_money +=4000
else:
    print("thats the wrong answer")
    print(f"game over""{Userinterface},your money prize is:",total_money)
    exit()


print("Q5. Who is the current Prime Minister of India (2026)?")
Q = "1. Rahul Gandhi"
R = "2.Narendra Modi".center(30)
S = "3.Amit Shah"
T = "4.Arvind Kejriwal".center(40)
print(Q + R)
print(S + T)
print("Enter 0 for Audience Poll Lifeline\n")
choices = int(input("enter your option:"))

if choices == 0:
    if not lifeline_used:
        lifeline_used = True
        print("\nAudience poll result:\n")
        print("1 →", random.randint(0, 100), "%")
        print("2 →", random.randint(0, 100), "%")
        print("3 →", random.randint(0, 100), "%")
        print("4 →", random.randint(0, 100), "%")
        
        choices = int(input("\n now enter your option: "))
    else:
        print("Lifeline already used.")
        choices = int(input("Enter your answer: "))
if (choices == 2):
    print("that's the correct answer and you won 5000rs")
    total_money +=5000 
else:
    print("that's the wrong answer")
    print(f"game over","{Userinterface},your money prize is:",total_money)
    exit()


print("that's the our game hope you like it!")
print("your winning amount is generating soon.....")
time.sleep(2)
print(f"{Userinterface}, your prize pool is", total_money)


