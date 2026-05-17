import time
import random
import sys

money = 0

def reload_chamber(max_shells, max_lives):
    print("RELOADING...")
    time.sleep(1.5)
    shells = max_shells
    lives = max_lives
    blanks = shells - lives
    chamber = ["live"] * lives + ["blank"] * blanks
    random.shuffle(chamber)
    print(f"Lives: {lives}")
    time.sleep(1.5)
    return shells, lives, blanks, chamber

def habi_test_fight():
    global hp
    print("「ならば、死闘だ。」")
    input("(enter to continue) ")
    time.sleep(1)

    ehp = 6
    hp = 6
    turns = 0

    shells = 24
    lives = 3
    blanks = shells - lives
    chamber = ["live"] * lives + ["blank"] * blanks
    random.shuffle(chamber)

    cooldown = 0
    turn = "player"   # <<< THE FIX

    while hp > 0 and ehp > 0:

        # ============================
        # ======== PLAYER TURN ========
        # ============================
        if turn == "player":
            turns += 1

            # --- DRAW SHELL ---
            if not chamber:
                shells, lives, blanks, chamber = reload_chamber(24, 3)
            if not chamber:
                continue
            current_shell = chamber.pop(0)
            shells -= 1

            print(f"-==== ROUND {turns} ====-")
            time.sleep(0.25)

            print("\n- YOUR STATS -")
            print(f"Hp: {hp}")
            print(f"Cooldown: {cooldown}\n")
            time.sleep(0.5)

            print("- ENEMY STATS -")
            print(f"Habidachi Hp: {ehp}\n")
            time.sleep(0.35)

            print(f"Shells left: {shells}\n")
            time.sleep(0.25)

            choice = input("Shoot [S]elf or [E]nemy, or use [A]bility? ").strip().lower()

            # --- PLAYER SHOOTS SELF ---
            if choice == "s":
                print(); time.sleep(0.5); print(); time.sleep(0.5)
                print(f"<< {current_shell} >>")

                if current_shell == "live":
                    print("<< BAM >>")
                    hp -= 1
                    lives -= 1
                    if hp == 0:
                        print("you die haha :D")
                        return "player_dead"
                else:
                    blanks -= 1

            # --- PLAYER SHOOTS ENEMY ---
            elif choice == "e":
                print(); time.sleep(0.5); print(); time.sleep(0.5)
                print(f"<< {current_shell} >>")

                if current_shell == "live":
                    print("<< BAM >>")
                    cooldown = 0
                    ehp -= 1
                    lives -= 1
                    if ehp == 0:
                        print("they die haha :D")
                        return "enemy_dead"
                else:
                    blanks -= 1

                # Forced self-shot
                if not chamber:
                    shells, lives, blanks, chamber = reload_chamber(24, 3)
                if not chamber:
                    continue
                if ehp > 0 and chamber:
                    input("Your turn (enter) ")
                    print(); time.sleep(0.5); print(); time.sleep(0.5)

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
                    else:
                        blanks -= 1

            # --- SPIN ABILITY ---
            elif choice == "a" and cooldown == 0:
                print("Spinning chamber...")
                cooldown = 1
                time.sleep(1)

                print(f"Ejecting current shell... ({current_shell})")
                time.sleep(1)

                if current_shell == "live":
                    lives -= 1
                else:
                    blanks -= 1

                # Flip next shell
                if chamber and random.random() > 0.5:
                    if chamber[0] == "blank":
                        chamber[0] = "live"
                        lives += 1
                        blanks -= 1
                    else:
                        chamber[0] = "blank"
                        blanks += 1
                        lives -= 1

                print("Chamber spun.")

            elif choice == "a":
                print("ability on cooldown")

            else:
                print("INVALID")
                hp -= 1
                if hp == 0:
                    print("you die haha :D")
                    return "player_dead"

            turn = "enemy"   # <<< SWITCH TURN
            continue

        # ============================
        # ======== ENEMY TURN ========
        # ============================
        if turn == "enemy":

            if not chamber:
                shells, lives, blanks, chamber = reload_chamber(24, 3)
            if not chamber:
                continue
            current_shell = chamber.pop(0)
            shells -= 1

            print("-==== ENEMY TURN ====-")
            time.sleep(1)

            # --- HABIDACHI AI ---
            livechance = lives / shells if shells > 0 else 0
            if choice == "a":
                habi_choice = "enemy"
            elif shells >= 15 and livechance <= 0.2:
                habi_choice = "self"
            elif livechance >= 0.2:
                habi_choice = "enemy"
            elif shells <= 10 and ehp == 1:
                habi_choice = "enemy"
            elif shells <= 10 and livechance >= 0.5 and hp == 1:
                habi_choice = "enemy"
            elif shells <= 10 and ehp >= 2 and livechance >= 0.25:
                habi_choice = "self"
            else:
                habi_choice = "self"

            print(f"They choose to shoot {habi_choice}.")
            time.sleep(1)

            # --- ENEMY SHOOTS SELF ---
            if habi_choice == "self":
                print(); time.sleep(0.5); print(); time.sleep(0.5)
                print(f"<< {current_shell} >>")

                if current_shell == "live":
                    print("<< BAM >>")
                    ehp -= 1
                    lives -= 1
                    if ehp == 0:
                        print("they die haha :D")
                        return "enemy_dead"
                else:
                    blanks -= 1
                    print("HIBACHI TRIGGERS! Habidachi gets an extra turn.")
                    time.sleep(1.5)
                    continue   # <<< STAYS IN ENEMY TURN

            # --- ENEMY SHOOTS PLAYER ---
            elif habi_choice == "enemy":
                print(); time.sleep(0.5); print(); time.sleep(0.5)
                print(f"<< {current_shell} >>")

                if current_shell == "live":
                    print("<< BAM >>")
                    hp -= 1
                    lives -= 1
                    if hp == 0:
                        print("you die haha :D")
                        return "player_dead"
                    else:
                        print("HIBACHI TRIGGERS! Habidachi gets an extra turn.")
                        time.sleep(1.5)
                        continue   # <<< STAYS IN ENEMY TURN
                else:
                    blanks -= 1

                # Forced self-shot
                if not chamber:
                    shells, lives, blanks, chamber = reload_chamber(24, 3)
                if not chamber:
                    continue
                if hp > 0 and chamber:
                    current_shell = chamber.pop(0)
                    shells -= 1

                    print("(They must now shoot themselves)")
                    time.sleep(1)
                    print(); time.sleep(0.5); print(); time.sleep(0.5)

                    print(f"<< {current_shell} >>")
                    if current_shell == "live":
                        print("<< BAM >>")
                        ehp -= 1
                        lives -= 1
                        if ehp == 0:
                            print("they die haha :D")
                            return "enemy_dead"
                    else:
                        blanks -= 1

            turn = "player"   # <<< SWITCH TURN
            continue