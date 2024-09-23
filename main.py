def main():
    class Archer:
        def __init__(self, name, health, num_arrows):  # it's done
            self.name = name
            self.health = health
            self.num_arrows = num_arrows

        def get_shot(self):  # it's done

            if self.health > 0:
                self.health -= 1
            raise ValueError(f"{self.name} is dead")

        def shoot(self, target):  # working on it

            archer = Archer(self.name, self.health, self.num_arrows)

            if archer.num_arrows > 0:
                archer.num_arrows -= 1
                print(f"{archer.name} shot {archer.name}")
                self.get_shot()
            raise ValueError(f"{self.name} can't shoot")

        # don't touch below this line

        def get_status(self):
            return self.name, self.health, self.num_arrows

        def print_status(self):
            print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

main()


