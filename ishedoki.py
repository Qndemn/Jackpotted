import time
import sys
import random

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

def ishedoki_test_fight():
    global hp
    print("「この果てなき歌に、また一つ音が加わる！」終わりなき旋律に新たな響きが重なるように、我らはかつて共に歩み、この地を離れる未来すらあったかもしれない。だが無情にも運命は我らを再びここへ導いたのだ――さあ、兄弟よ、姉妹よ、最後にもう一度、我と共に踊ろうではないか")
    input("(enter to continue) ")
    time.sleep(1)

    turns = 0
    ehp = 5
    hp = 5

    shells = 36
    lives = 12
    blanks = shells - lives
    chamber = ["live"] * lives + ["blank"] * blanks
    random.shuffle(chamber)

    print(f"Lives: {lives}")
    time.sleep(1.5)

    cooldown = 0
    ecooldown1 = 0
    ecooldown2 = 0

    while hp > 0 and ehp > 0:
        turns += 1

        # --- DRAW SHELL ---
        if not chamber:
            shells, lives, blanks, chamber = reload_chamber(36, 12)
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
        print(f"Ishedoki Hp: {ehp}")
        print(f"Ishedoki Cooldown 1: {ecooldown1}")
        print(f"Ishedoki Cooldown 2: {ecooldown2}\n")
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
                shells, lives, blanks, chamber = reload_chamber(36, 12)
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
            if current_shell == "live":
                lives -= 1
            else:
                blanks -= 1

            time.sleep(1)

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

        # --- ENEMY TURN ---
        if ehp <= 0:
            break

        time.sleep(2)
        print("-==== ENEMY TURN ====-")

        if not chamber:
            shells, lives, blanks, chamber = reload_chamber(36, 12)
        if not chamber:
            continue
        current_shell = chamber.pop(0)
        shells -= 1

        # --- AI DECISION ---
        if shells >= 32:
            ishedoki_choice = "enemy"
        elif shells >= 10 and hp >= 2 and ecooldown1 == 0:
            ishedoki_choice = "ability1"
        elif shells >= 10 and hp >= 2:
            ishedoki_choice = "enemy"
        elif ehp == 1 and shells >= 5 and lives >= 3 and ecooldown2 == 0:
            ishedoki_choice = "ability2"
        elif ehp >= 2 and shells >= 21 and lives < 7:
            ishedoki_choice = "self"
        else:
            ishedoki_choice = "enemy"

        print("They choose to shoot " + ishedoki_choice + "." if ishedoki_choice in ["self","enemy"] else "They used their ability.")
        time.sleep(1)

        # --- ENEMY SHOOTS SELF ---
        if ishedoki_choice == "self":
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

        # --- ENEMY SHOOTS PLAYER ---
        elif ishedoki_choice == "enemy":
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

            # Forced self-shot
            if not chamber:
                shells, lives, blanks, chamber = reload_chamber(36, 12)
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

        # --- ABILITY 1 ---
        elif ishedoki_choice == "ability1":
            print("They used Piano Played!")
            print("They add 5 random shells and reshuffle the chamber.\n")
            time.sleep(2)

            ecooldown1 = 3
            for _ in range(5):
                time.sleep(0.25)
                print("CLICK")
                shell = random.choice(["live","blank"])
                chamber.append(shell)
                if shell == "live":
                    lives += 1
                else:
                    blanks += 1
            shells += 5

            random.shuffle(chamber)
            print("\n\n")
            time.sleep(1.5)

        # --- ABILITY 2 ---
        elif ishedoki_choice == "ability2":
            print("They used Cello Strummed!")
            print("They remove 1 live shell and 3 blanks!")
            time.sleep(2)

            ecooldown2 = 4

            removed_shells = 0
            if "live" in chamber:
                chamber.remove("live")
                lives -= 1
                removed_shells += 1

            for _ in range(3):
                if "blank" in chamber:
                    chamber.remove("blank")
                    blanks -= 1
                    removed_shells += 1
            shells -= removed_shells
            print("\n\n")
            time.sleep(1.5)

        # --- COOLDOWNS ---
        time.sleep(1.5)
        if ecooldown1 > 0:
            ecooldown1 -= 1
        if ecooldown2 > 0:
            ecooldown2 -= 1

        # --- RELOAD ---
        if shells <= 0 or not chamber:
            shells, lives, blanks, chamber = reload_chamber(36, 12)