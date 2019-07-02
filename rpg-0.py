from heroclass import hero, goblin

# class Hero():
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
# captain = Hero(10,5)

# class Goblin(Hero):
#     def __init__(self, health, power)
#         self.health = health
#         self.power = power
# luetenant = Goblin(6,2)


def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    captain = hero(hero_health, hero_power)
    luetenant = goblin(goblin_health, goblin_power)
    



    while luetenant.alive() and captain.alive():

    # while goblin_health > 0 and hero_health > 0:
        print("You have %d health and %d power." % (captain.health, captain.power))
        print("The luetenant has %d health and %d power." % (luetenant.health, luetenant.power))
        print()
        print("What do you want to do?")
        print("1. fight luetenant")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            captain.attack(luetenant)
            print("You do %d damage to the luetenant." % captain.power)
            if luetenant.health <= 0:
                print("The luetenant is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if luetenant.health > 0:
            # Goblin attacks hero
            luetenant.attack(captain)
            print("The goblin does %d damage to you." % luetenant.power)
            if captain.health <= 0:
                print("You are dead.")

main()
