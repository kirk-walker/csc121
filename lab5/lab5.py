import random

def print_intro():
    print("""
        Welcome to Hoth!
    
        The Empire is after you!
        You must travel across the frozen plain 
        and get back to the Rebellion.
    """)

def main():
    print_intro()
    
    done = False
    
    miles = 0
    thirst = 0
    tiredness = 0
    empire_distance = -20
    canteen = 3
    
    while done == False:
        oasis = False
        print("""
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.
        
        """)
        choice = input("What will you choose? ")
        #Quit
        if choice.upper() == "Q":
            done = True
        #Status Check
        elif choice.upper() == "E":
            print(f"""
        Miles traveled: {miles}
        Drinks in canteen: {canteen}
        The Empire is {empire_distance} miles behind you!
            """)
        #Rest for the night    
        elif choice.upper() == "D":
            tiredness = 0
            print(f"""
        Your wampa is well rested,
        but the Empire has drawn closer...
            """)
            empire_distance += random.randrange(7,14)
        #Ahead Full Speed    
        elif choice.upper() == "C":
            miles_traveled_fast = random.randrange(10, 20)
            
            miles += miles_traveled_fast
            thirst += 1
            tiredness += random.randrange(1,3)
            empire_distance += random.randrange(7,14)

            print(f"""
        You have traveled {miles_traveled_fast} miles.
            """)
            if random.randrange(20) == 0:
                oasis = True

        #Ahead moderate speed
        elif choice.upper() == "B":
            miles_traveled_moderate = random.randrange(5,12)

            miles += miles_traveled_moderate
            thirst += 1
            tiredness += 1
            empire_distance += random.randrange(7,14)

            print(f"""
        You have traveled {miles_traveled_moderate} miles.
            """) 
            if random.randrange(20) == 0:
                oasis = True

        #Drink from canteen
        elif choice.upper() == "A":
            if canteen >= 1:
                canteen -= 1
                thirst = 0
                print("""
        You took a drink.
                """)
            else:
                print("""
        Your canteen is empty.
                """)

        elif thirst >= 4:
            print("""
        You are thirsty!
            """)
        
        elif thirst >= 6:
            print("""
        You died of thirst!
            """) 
            done = True

        elif tiredness >= 4:
            print("""
        Your wampa is getting tired!
            """)

        elif tiredness >= 8:
            print("""
        Your wampa has passed away from being to tired.
            """)
            
            done = True

        elif empire_distance > miles:
            print("""
        The Empire has caught you!
            """)

        elif empire_distance >= miles - 15:
            print("""
        The Empire is getting close!
            """)

        elif miles >= 200:
            print("""
        You made it to the Rebellion!
            """)
        
        elif oasis == True:
            print("""
        You found as Oasis!
        You've taken a nice drink, your canteen is full
        and your wampa is rested.    
            """)
            canteen = 3
            thirst = 0 
            tiredness = 0
        
          

if __name__ == '__main__':
    main()