import time
import sys
import random

# CHAMBERRRRR TESTIN'
# [Get this freak away from me :D]

money = 0
rounds = 0

def title_screen():
  print("[(=- J4¢₭₱Ø₮₮€Ð -=)]")
  print("Meaning: Describing the state of euphoria after you! Hit! THE! JACKPOooooOOOOOT!")
  print("Welcome! Ready... To... GAMBLE!!!???")
  input("\n(Enter to commence gambling) ")

title_screen()
print("\nDo you want to take the tutorial?")
tutorial = input("y/n ").strip().lower()
if tutorial in["y", "yes"]:
  print("Great! So, let's start with the basics.")
  time.sleep(1.5)
  print("On your turn, you can:")
  print("1. Shoot yourself (to progress)")
  print("2. Shoot opponent (to deal damage)")
  print("3. Use your ability (currently, the only ability is Spin. Ability cooldowns are reset when you shoot the enemy. On the stats bar, any number greater than 0, likely 1, will mean the ability is on cooldown.)")
  input("(Enter to continue) ")
  print("\nWhen shooting the opponent, you will then be obligated to shoot yourself.")
  print("This is to ensure that you can't always shoot the opponent; know the risks.")
  input("(Enter to continue) ")
  print("\nSpin, your ability, will eject the current shell, effectively progressing, as well as choosing the new shell. The new shell will be, if it is currently live or blank, it has a 50/50 of becoming the opposite.")
  input("(Enter to continue) ")
  print("\nWhen the chamber runs out, it will simply reload. This will NOT reset cooldowns.")
  print("\nNotes:")
  print("1. You will not know how many live rounds are left.")
  print("2. You will know how many shells overall are left.")
  print("3. The enemy can also use abilities, but has no actual AI to strategize with. Future enemies likely will, at least bosses. This is a trick, as all the enemies are gonna be bosses! IT'S A BOSS RUSH!! well right now you're fighting a dummy but still")
  input("(Enter to continue) ")
  print("\nThat's all! Enjoy!")
  time.sleep(1)
  print("\n"*40)
else:
  print("\nOnto the game!")
  time.sleep(1)
  print("\n"*40)

def chamber_test_randomchamber():
    shells = 36
    lives = 1
    rounds = 0
    for _ in range(shells):
        time.sleep(0.1)
        rounds += 1
        livechance = lives/shells
        shells -= 1
        if random.random() < livechance:
            print(f"<< BAM >> {rounds}")
            sys.exit()
        else:
            print(f">> BLANK << {rounds}")

# Bility A testifying
# [Why did you keep me in this room!? WITH THIS GUY!? WHY]

def ability_ideas():
    print("Actives:")
    time.sleep(1)
    print("Red Hand: 65% chance of turning next shell into live, does nothing if shell is already live. Then, get an extra turn to shoot.")
    time.sleep(1)
    print("Spin: Basic ability, 50/50 chance of live/blank switcheroo.")
    time.sleep(1)
    print("Magnifying Glass: Reveals current shell, then gives an extra turn to shoot.")
    time.sleep(1)
    print("Pill Bottle: Heal one HP")
    time.sleep(1)
    print("Prescription Medicine: 40/60 Heal two hp or lose one hp.")
    time.sleep(1)
    print("Beast of Rage: Lose one hp, force next shot you shoot to be live and next shot enemy shoots at you to be blank.")
    time.sleep(1)
    print("Bazooka: Take a 1/(remaining shells) chance, if succesful instantly kill the enemy. On failure, take one damage and skip your next turn.")
    time.sleep(1)
    print("Beer: Eject current shell. Can be used three times before cooldown.")
    time.sleep(1)
    print("Delphi's Oracle: Learn the next shot, but if it's live, it deals half damage, and if it's blank, you must shoot the opponent. Can be used twice before cooldown.")
    print("Passives:")
    time.sleep(1)
    print("Stratégie et patience: Everybody has +2 hp and take half damage.")
    time.sleep(1)
    print("Glass Cannon: Everybody has 1 hp.")
    time.sleep(1)
    print("Slow Burn: The longer the match progresses, the more damage you'll deal and the less damage you'll take.")
    time.sleep(1)
    print("LiveShell's Wrath: Every shot you shoot has a 25% chance of becoming Live. (Excluding last shells)")
    time.sleep(1)
    print("BlankShell's Calm: Every shot you shoot has a 25% chance of becoming blank. (Excluding last shells)")
    time.sleep(1)
    print("Marcato: (War Etude) Gain +1 hp for every 3 reloads.")
    time.sleep(1)
    print("Fackles and Shetters: Skip every other turn, always know the current shell type.")
    time.sleep(1)
    print("Contrarian: The original values for total blanks and lives are flipped, meaning there are more lives and less blanks.")

def doi_test_fight():
    global hp, rounds
    ehp = 3 + rounds
    hp = 3 + rounds
    shells = 24
    lives = 6
    blanks = shells - lives
    # NEW: chamber array
    chamber = ["live"] * lives + ["blank"] * blanks
    random.shuffle(chamber)
    rounds = 0
    cooldown = 0
    ecooldown = 0
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
        print(f"Dummy of Idiots hp: {ehp}")
        print(f"Dummy of Idiots Cooldown: {ecooldown}\n")
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
              shells = 24
              lives = 6
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
            if current_shell == "live":
                lives -= 1
            else:
                blanks -= 1
            # 50/50 flip of NEXT shell
            if len(chamber) > 0:
                if random.random() > 0.5:
                    chamber[0] = "live" if chamber[0] == "blank" else "blank"
                    if chamber[0] == "live":
                        lives += 1
                        blanks -= 1
                    else:
                        blanks += 1
                        lives -= 1
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
          shells = 24
          lives = 6
          blanks = shells - lives
          chamber = ["live"] * lives + ["blank"] * blanks
          random.shuffle(chamber)
        current_shell = chamber.pop(0)
        shells -= 1
        if ecooldown == 0:
            dummy_choices = ["self", "enemy", "ability"]
        else:
            dummy_choices = ["self", "enemy"]
        dummy_choice = random.choice(dummy_choices)
        if dummy_choice in ["self", "enemy"]:
            print(f"They choose to shoot {dummy_choice}.")
        else:
            print("They used their ability.")
        time.sleep(1)
        # --- ENEMY SHOOTS SELF ---
        if dummy_choice == "self":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                ehp -= 1
                lives -= 1
                if ehp == 0:
                    print("they die haha :D")
                    return "enemy_dead"
        # --- ENEMY SHOOTS PLAYER ---
        elif dummy_choice == "enemy":
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print(f"<< {current_shell} >>")
            if current_shell == "live":
                print("<< BAM >>")
                ecooldown = 0
                print("(their cooldown was reset)")
                hp -= 1
                lives -= 1
                if hp == 0:
                    print("you die haha :D")
                    return "player_dead"
            time.sleep(1)
            # Enemy forced self-shot
            if not chamber:
              # reload here
              shells = 24
              lives = 6
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
                    lives -= 1
                    if ehp == 0:
                        print("they die haha :D")
                        time.sleep(2)
                        return "enemy_dead"
        # --- ENEMY SPIN ABILITY ---
        elif dummy_choice == "ability":
            ecooldown = 1
            print("They used their Spin!")
            print("Spinning chamber...")
            time.sleep(1)
            print("Ejecting current shell...")
            time.sleep(1)
            if current_shell == "live":
                lives -= 1
            else:
                blanks -= 1
            # 50/50 flip of NEXT shell
            if len(chamber) > 0:
                if random.random() > 0.5:
                    chamber[0] = "live" if chamber[0] == "blank" else "blank"
                    if chamber[0] == "live":
                        lives += 1
                        blanks -= 1
                    else:
                        blanks += 1
                        lives -= 1
            print("Chamber spun.")
        time.sleep(1.5)
        if shells <= 0:
          print("RELOADING...")
          time.sleep(1.5)
          shells = 24
          lives = 6
          blanks = shells - lives
          chamber = ["live"] * lives + ["blank"] * blanks
          random.shuffle(chamber)
while True:
  result = doi_test_fight()
  print("\n"*40)
  if money == 0 and result == "enemy_dead":
    print("First round bonus!")
    rounds += 1
    money += 1095763
  elif result == "player_dead":
    print("You lost so no money haha")
  elif result == "enemy_dead":
    print("MONEY x2!")
    rounds += 1
    money *= 2
  print(f"MONEY: !!!!{{$${money}$$}}!!!!")
  choice = input("Wanna keep gambling? \ny/n\n").strip().lower()
  if choice in["y", "yes"]:
    print("Thaaaaat's the spirit!")
  elif choice in["n", "no"]:
    print("Hmph. Be that way. I'm sure that you'll! Be! BACK!")
    time.sleep(2)
    sys.exit()
  else:
    print("INVALID! So that automatically means! That! YOU! KEEP! GaaaaaMBLING!")
  time.sleep(1.5)