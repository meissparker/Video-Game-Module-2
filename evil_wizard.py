# Base Character class

import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        power = self.attack_power * (random.randint(1,2)) # Randomizing the attack power
        opponent.health -= power
        print(f"{self.name} attacks {opponent.name} for {power} damage!")
        print(f'{opponent.name} health: {opponent.health}/{opponent.max_health}')
        if opponent.health <= 0:
            print(f"\n{opponent.name} has been defeated by {self.name}!\n")

    def display_stats(self, opponent):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print(f"{opponent.name}'s Stats - Health: {opponent.health}/{opponent.max_health}, Attack Power: {opponent.attack_power}\n")
        battle(self, opponent) # I called the battle function in the display function to ensure 
                                #the player was not being penalized for viewing their stats.

    def heal(self): # Healing Mechanic
        if self.health < self.max_health:
            self.health += 5
            print(f'You have recovered some health! Health: {self.health}/{self.max_health}\n')
        elif (self.health) == (self.max_health):
            print("Health is full\n")


        

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)


    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Rage  2. Made of Stone\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 3
            opponent.health -= (new_power)
            print(f'''Your fury gives you incredible strength! Attack Power: {new_power}''')
        elif choice == 2:
            print('''\nThe wizard attacks but his spells are no use against solid stone!''')
            battle(self, opponent)
        else:
            print('''Invalid Choice. The wizard gets a free shot. Choose (1 or 2) next time!''')


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)


    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Avada Kedavra    2. Aura\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 4
            opponent.health -= (new_power)
            print(f"You cast a deadly spell! Attack Power: {new_power}\n")
        elif choice == 2:
            if self.health < self.max_health:
                self.health += 15
                print(f'Your aura has a dramatic healing effect! Health: {self.health}/{self.max_health}\n')
            elif (self.health) == (self.max_health):
                print("Your health is full. Aura has no effect.\n")
            else:
                print('Invalid Choice, The wizard gets a free shot. Choose (1 or 2) next time!\n')

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Double Shot  2. Evade\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 2
            opponent.health -= (new_power)
            print(f"You shoot double arrows! Attack Power: {new_power}\n")
        elif choice == 2:
            print('\nThe wizard attacks but you jump out of the way!')
            battle(self, opponent)
        else:
            print('Invalid Choice, The wizard gets a free shot. Choose (1 or 2) next time!\n')

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)


    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Holy Strike   2. Intercession\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 2
            opponent.health -= (new_power)
            print(f"Your sword flashes in righteous anger! Attack Power: {new_power}\n")
        elif choice == 2:
            if self.health < self.max_health:
                self.health += 25
                print(f'Heaven has heard your prayers! Health: {self.health}/{self.max_health}\n')
            elif (self.health) == (self.max_health):
                print("Your health is full. Intercession has no effect.\n")
            else:
                print('Invalid Choice, The wizard gets a free shot. Choose (1 or 2) next time!\n')

# Goblin class (inherits from Character)
class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Poison Fang   2. Conceal\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 3
            opponent.health -= (new_power)
            print(f"You sink your venomous teeth deep into the dark wizard's arm! Attack Power: {new_power}\n")
        elif choice == 2:
            print('\nThe wizard attacks but you hide yourself in the undergrowth!')
            battle(self, opponent)
        else:
            print('Invalid Choice, The wizard gets a free shot. Choose (1 or 2) next time!')

# Vampire class (inherits from Character)
class Vampire(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)


    def special_ability(self, opponent):
        print("\nSpecial Abilities: 1. Thirst for blood    2. Flight\n")
        choice = int(input("Choose a special ability: (select 1 or 2) "))
        if choice == 1:
            new_power = self.attack_power * 3
            opponent.health -= (new_power)
            print(f"You suck the wizard's blood! Attack Power: {new_power}\n")
        elif choice == 2:
            print("\nThe wizard attacks but you turn into a bat and fly out of his reach!")
            battle(self, opponent)
        else:
            print('Invalid Choice, The wizard gets a free shot. Choose (1 or 2) next time!')

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def regenerate(self):
        if self.health < self.max_health: # I made this conditional formatting to ensure the wizard did not go above 150 health.
            self.health += 5
            print(f"\n{self.name} regenerates 5 health! Wizard's current health: {self.health}/{self.max_health}")
       



def create_character():
    print("\nChoose your character class:\n")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    print("5. Goblin")
    print("6. Vampire")


    class_choice = input("\nEnter the number of your class choice: ")
    name = input("\nEnter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3': #Archer Class
        return Archer(name)
    elif class_choice == '4': #Paladin Class
        return Paladin(name)
    elif class_choice == '5': # Goblin Class
        return Goblin(name)
    elif class_choice == '6': # Vampire Class
        return Vampire(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability") #Each character has 2 options once special ability is chosen.
        print("3. Heal")
        print("4. View Stats")
        print("5. Quit Game")

        choice = input("\nChoose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats(wizard) # I modified display stats so that the player could see the wizard's stats as well.
        elif choice == '5':
            quit = input("Are you sure you want to quit? Y/N ").upper() # I added an option for quitting the game.
            if quit == 'Y':
                break

            elif quit == 'N':
                battle(player, wizard)
            else:
                print('Invalid Choice, returning to battle.')
                battle(player, wizard)
        else:
            print("\nInvalid choice. Free shot for the wizard. Do better next time.\n")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"\nThe dark wizard has triumphed over {player.name}!\n")
            break

    if wizard.health <= 0:
        print(f"\n{wizard.name} has been defeated by {player.name}!\n")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()