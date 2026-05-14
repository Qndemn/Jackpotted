import time
import sys
import random

money = 0

def bb_test_fight():
    global hp, rounds
    print("Yer gon' get a taste a' hot lead, bucko! (or buckette, depending on gender. Feel the wrath of feminism! Does that sound sexist...? Uh... LET'S SHOOT EACH OTHER FOR MONEY NOW)")
    input("(enter to continue) ")
    time.sleep(1)
    rounds = 0
    ehp = 3 + rounds
    hp = 3 + rounds
    shells = 12
    lives = 2
    blanks = shells - lives
    chamber = ["live"] * lives + ["blank"] * blanks
    random.shuffle(chamber)
    cooldown = 0
    ecooldown = 0
    rage_shot = False
    while hp > 0 and ehp > 0:
        rounds += 1
        # --- DRAW SHELL ---
        current_shell = chamber.pop(0)
        shells -= 1
        print(f"-==== ROUND {rounds} ====-")
        time.sleep(0.25)
        print("\n- YOUR STATS -")
        print(f"Hp: {hp}")
        print(f"Cooldown: {cooldown}\n")
        time.sleep(0.5)
        print("- ENEMY STATS -")
        print(f"BB Gunderson Hp: {ehp}")
        print(f"BB Gunderson Cooldown: {ecooldown}\n")
        time.sleep(0.35)
        print(f"Shells left: {shells}\n")
        time.sleep(0.25)
        choice = input("Shoot [S]elf or [E]nemy, or use [A]bility? ").strip().lower()
        # --- PLAYER SHOOTS SELF ---
        if choice == "s":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                hp -= 1
                lives -= 1
                if hp == 0:
                    print("you die haha :D")
                    return "player_dead"
        # --- PLAYER SHOOTS ENEMY ---
        elif choice == "e":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                print("(Cooldown reset)")
                cooldown = 0
                ehp -= 1
                lives -= 1
                if ehp == 0:
                    print("they die haha :D")
                    return "enemy_dead"
            # Enemy forced self-shot
            if not chamber:
              # reload here
              shells = 12
              lives = 2
              blanks = shells - lives
              chamber = ["live"] * lives + ["blank"] * blanks
              random.shuffle(chamber)
            if ehp > 0 and len(chamber) > 0:
                input("Your turn (enter) ")
                print()
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                current_shell = chamber.pop(0)
                shells -= 1
                print(f"<< {current_shell} >>")
                if current_shell == "live":
                    print("<< BAM >>")
                    hp -= 1
                    lives -= 1
                    if hp == 0:
                        print("you die haha :D")
                        return "player_dead"
        # --- SPIN ABILITY ---
        elif choice == "a" and cooldown == 0:
            print("Spinning chamber...")
            cooldown = 1
            time.sleep(1)
            print(f"Ejecting current shell... ({current_shell})")
            time.sleep(1)
            # 50/50 flip of NEXT shell
            if len(chamber) > 0:
                if random.random() > 0.5:
                    chamber[0] = "live" if chamber[0] == "blank" else "blank"
            print("Chamber spun.")
        elif choice == "a" and cooldown > 0:
            print("ability on cooldown")
        else:
            print("INVALID")
        # --- ENEMY TURN ---
        if ehp <= 0:
          break
        time.sleep(2)
        print("-==== ENEMY TURN ====-")
        if not chamber:
          # reload here
          shells = 12
          lives = 2
          blanks = shells - lives
          chamber = ["live"] * lives + ["blank"] * blanks
          random.shuffle(chamber)
        current_shell = chamber.pop(0)
        shells -= 1
        if shells >= 10:
          bb_choice = "self"
        elif shells < 10:
          if ecooldown == 0:
            if random.random() < 0.75:
              bb_choice = "ability"
            else:
              bb_choice = "enemy"
          else:
            bb_choice = "enemy"
        if bb_choice in ["self", "enemy"]:
            print(f"They choose to shoot {bb_choice}.")
        else:
            print("They used their ability.")
        time.sleep(1)
        # --- ENEMY SHOOTS SELF ---
        if bb_choice == "self":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                ehp -= 1
                if rage_shot:
                  ehp -= 1
                  rage_shot = False
                lives -= 1
                if ehp == 0:
                    print("they die haha :D")
                    return "enemy_dead"
        # --- ENEMY SHOOTS PLAYER ---
        elif bb_choice == "enemy":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                hp -= 1
                if rage_shot:
                  hp -= 1
                  rage_shot = False
                lives -= 1
                if hp == 0:
                    print("you die haha :D")
                    return "player_dead"
            time.sleep(1)
            # Enemy forced self-shot
            if not chamber:
              # reload here
              shells = 12
              lives = 2
              blanks = shells - lives
              chamber = ["live"] * lives + ["blank"] * blanks
              random.shuffle(chamber)
            if hp > 0 and len(chamber) > 0:
                current_shell = chamber.pop(0)
                shells -= 1
                print("(They must now shoot themselves)")
                time.sleep(1)
                print()
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print(f"<< {current_shell} >>")
                if current_shell == "live":
                    print("<< BAM >>")
                    ehp -= 1
                    if rage_shot:
                      ehp -= 1
                      rage_shot = False
                    lives -= 1
                    if ehp == 0:
                        print("they die haha :D")
                        time.sleep(2)
                        return "enemy_dead"
        # --- ENEMY SPIN ABILITY ---
        elif bb_choice == "ability":
            ecooldown = 4
            rage_shot = True
            print("They used Rage Shot!")
            time.sleep(1.5)
            print("They deal x2 Damage on their next turn.")
        time.sleep(1.5)
        if bb_choice != "ability":
          rage_shot = False
        if ecooldown > 0:
          ecooldown -= 1
        if shells <= 0:
          print("RELOADING...")
          time.sleep(1.5)
          shells = 12
          lives = 2
          blanks = shells - lives
          chamber = ["live"] * lives + ["blank"] * blanks
          random.shuffle(chamber)
bb_test_fight()