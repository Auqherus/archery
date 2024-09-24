def main():
    class Archer:
        def __init__(self, name, health, num_arrows):  # it's done
            self.name = name
            self.health = health
            self.num_arrows = num_arrows

        def get_shot(self):  # it's done

            if self.health > 0:
                self.health -= 1
            if self.health <= 0:
                raise ValueError(f"{self.name} is dead")

        def shoot(self, target):  # working on it

            if self.num_arrows > 0:
                self.num_arrows -= 1
                # print(self.num_arrows)
                print(f"{target.name} shot {self.name}")
                target.get_shot()
            else:
                raise ValueError(f"{self.name} can't shoot")

        # don't touch below this line

        def get_status(self):
            return self.name, self.health, self.num_arrows

        def print_status(self):
            print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

        # Creating example archers

    archer1 = Archer("Robin", 5, 3)
    archer2 = Archer("Marian", 5, 2)

    # Showing initial status
    archer1.print_status()
    archer2.print_status()

    # Shooting simulation
    archer1.shoot(archer2)  # Robin shoot Marian
    archer2.shoot(archer1)  # Marian shoot Robin

    # Showing results after shooting
    archer1.print_status()
    archer2.print_status()


main()


