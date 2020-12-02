'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
# Prints the instructions for the game
print("- You are a car in the game rocket league. Your goal is to drive down field and score the ball in the net. ")
print("- You are being chased by your teammate who thinks they are better than you. If they reach the ball"
      "before you, they'll throw off your shot, and allow your opponents to score in the open net they left unattended")
print("- You have a limited amount of boost that can help you get there. If you run out the game is over.")
print("- Selecting full speed uses more boost, selecting moderate speed uses less boost")
print("- You can refill your boost by stopping at a boost pad, but your teammate will keep driving")
print("- As your car drives it slowly veers off the course of the ball, you may need to straighten it out occasionally")
print("- If you veer too far off course you may run into obstacles")

# Sets necessary game variables
done = False
boost = 8
boostpads = 3
angle = 0
distancetraveled = 0
distanceremaining = 200
teammatepos = -20
turns = 0
while done is False:
    # action menu. user can select on of the options to perform an action
    print("1) Straighten your car")
    print("2) Drive at moderate speed.")
    print("3) Drive at full speed")
    print("4) Refill your boost")
    print("5) Status check")
    print("Q) Quit")
    action = input("Choose an action from the menu")

    # Straightens out the car
    if action == "1":
        angle = 0
        print("You're headed straight for the ball")
    # Moves the car at moderate speed
    elif action == "2":
        distance = random.randint(5, 12)
        distancetraveled = distancetraveled + distance
        angle += 1
        boost -= 1
        print("Moving at moderate speed you drove", distance, "meters")
    # Moves the car at full speed
    elif action == "3":
        distance = random.randint(10, 20)
        distancetraveled = distancetraveled + distance
        angle += 1
        boost -= random.randint(1, 3)
        print("Moving at full speed you drove", distance, "meters")
    # Refills the users boost level
    elif action == "4":
        if boostpads > 0:
            boost = 8
            boostpads -= 1
            print("You stopped to refill your boost.")
        else:
            print("No more available boost pads")
    # Allows user to check their status
    elif action == "5":
        print("Your boost level is:", boost)
        print("Remaining boostpads:", boostpads)
        print("Steering angle:", angle)
        print("Your teammate is", distancetraveled - teammatepos, "meters behind")
    # Allows the user to quit the game
    elif action.lower() == "q":
        print("You quit.")
        done = True
    else:
        print("Please select a valid option")
        continue

    # if the car veers too far off course you lose
    if angle > 6:
        print("You veered off course and let your teammate pass you. He attempted to do a ceiling shot but whiffed "
              "due to his poor arial control, letting your opponent score")
        done = True
    # if the car starts to veer off course, theres a chance you will encounter an obstacle
    elif angle > 3:
        print("You are starting to veer off course")
        chance = random.randint(3, 4)
        obstacles = ["You veered too far off course and ran into an opposing car, slowing you down. Your teammate "
                     "begins to close the distance", "You started to veer off to the left and slowed to re-adjust "
                                                     "your car. Your teammate is starting to catch up"]
        if chance == 3:
            print(random.choice(obstacles))
            teammatepos += random.randint(12, 22)
            continue
    # end the game if the user runs out of boost
    if boost <= 0:
        print("You ran out of boost! Your teammate passed you and whiffed an open net. Your opponent scores a long "
              "goal to end the 4 minute overtime")
        done = True
    # notify the user if they are low on boost
    elif boost <= 3:
        print("you are running low on boost")

    if distancetraveled <= teammatepos:
        print("Your teammate bumped you from behind knocking you off course. They whiff an open net and your opponent "
              "dribbles the ball to score the game winning goal")
    # if the user makes it to the ball they win
    if distancetraveled >= 200:
        print("You win!")
        done = True












