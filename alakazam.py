import time
import random
import sys
import bb
import ishedoki

rounds = 0

def lycheesHell():
    global rounds
    print("Welcome to Jackpotted! If you want to play endless mode, go play endless mode and stop wasting my damn time :D")
    input("Press Enter to continue... ")
    print("\n???: What's this...?")
    time.sleep(1.5)
    print("\n???: Your first opponent!")
    time.sleep(1.5)
    print("\n???: Let's give a big hand to...")
    time.sleep(1.5)
    print("\n???: BB Gunderson!")
    input("\n(R̴͖̉ ̴͙͋e̶̡͗ ̴͔͆a̴̞͗ ̶̫̕d̵̩̈́ ̴̬̂y̷̻̏...?)\n(press enter :D) ")
    time.sleep(1.5)
    rounds = 1
    result = bb.bb_test_fight()
    if result == "player_dead":
      print("\n???: Amen. BB moves on to the next round!")
      time.sleep(1.5)
      print("\n???: Don't worry, you'll feel...")
      time.sleep(1.5)
      print("\n???: ...JACKPOTTED eventually.")
      time.sleep(1.5)
      sys.exit()
    print("\n???: Onto round 2. Congrats!")
    time.sleep(1.5)
    print("\n???: Feeling that rush of Jackpot?")
    time.sleep(1.5)
    print("\n???: Addictive, isn't it?")
    time.sleep(1.5)
    print("\n???: Let's see if we can feed that addiction...")
    time.sleep(1.5)
    print("\n???: Here's Ishedoki. He's more like you. I'll enjoy seeing that rebel die.")
    input("\n(R̴͖̉ ̴͙͋e̶̡͗ ̴͔͆a̴̞͗ ̶̫̕d̵̩̈́ ̴̬̂y̷̻̏...?)\n(press enter :D) ")
    rounds = 2
    result = ishedoki.ishedoki_test_fight()
    if result == "player_dead":
      print("\n???: Amen. Ishedoki moves on to the next round!")
      time.sleep(1.5)
      print("\n???: Don't worry, you'll feel...")
      time.sleep(1.5)
      print("\n???: ...JACKPOTTED eventually.")
      time.sleep(1.5)
      sys.exit()
    print("\n???: Onto round 3. Congrats!")
    time.sleep(1.5)
    print("\n???: You can't lose, now can you?")
    time.sleep(1.5)
    print("\n???: That's right! You may deny it, but you know you're really starting to feel... JACKPOTTED.")
lycheesHell()