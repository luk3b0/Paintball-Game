import random

diff = int(input("Do you want 1, 3, or 5 lives): ")) #lives

if diff == 1:
 p_health = 1
 c_health = 1
elif diff == 3:
  p_health = 3
  c_health = 3
elif diff == 5:
  p_health = 3
  c_health = 3



choices = ["left", "middle", "right"]

while c_health != 0 and p_health != 0:
    p_move = input("Do you want to move left, middle, or right? ").lower()

    while p_move not in choices:
        p_move = input("Invalid choice. Please choose left, middle, or right: ").lower()

    c_move = random.choice(choices)

    p_shoot = input("Would you like to shoot at the left, middle, or right? ").lower()

    while p_shoot not in choices:
        p_shoot = input("Invalid choice. Please choose left, middle, or right: ").lower()

    c_shoot = random.choice(choices)

    if c_shoot == p_move:
        p_health -= 1
        print("You were hit and are now on " + str(p_health) + " lives")
    else:
        print("The computer missed")

    if p_shoot == c_move:
        c_health -= 1
        print("You hit the computer and it's now on " + str(c_health) + " lives")
    else:
        print("You missed")

if p_health == 0:
    print("You lost, better luck next time")
elif c_health == 0:
    print("Congratulations, you won!")
elif p_health == c_health == 0:
    print("Its a draw")
