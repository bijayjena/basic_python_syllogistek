from abc import ABC, abstractmethod


class soldier(ABC):
    def gather(self):
        print("Gather")

    @abstractmethod
    def attack(self):
        pass


class refillable(ABC):
    @abstractmethod
    def refill(self):
        pass


class timebasedrefill(refillable):
    def refill(self):
        print("Time based refill")


class weaponbasederfill(refillable):
    def refill(self):
        print("Weapon based refill")


class heal(ABC):
    @abstractmethod
    def healing(self):
        pass


class selfhealing(heal):
    def healing(self):
        print("Character heals itself")


class externalhealing(heal):
    def healing(self):
        print("Character heals from external sources")


class archer(soldier):
    def attack(self):
        print("Archer attack")

    def refill(self):
        return timebasedrefill().refill()

    def healing(self):
        return selfhealing().healing()


class spearsman(soldier):
    def attack(self):
        print("Spearsman attack")

    def healing(self):
        return externalhealing().healing()


class swordsman(soldier):
    def attack(self):
        print("Swordsman attack")

    def healing(self):
        return selfhealing().healing()


class gunman(soldier):
    def attack(self):
        print("Gun Man attack")

    def refill(self):
        return weaponbasederfill().refill()

    def healing(self):
        return externalhealing().healing()


a = archer()
a.gather()
a.attack()
a.refill()
a.healing()
s1 = swordsman()
s1.gather()
s1.attack()
s1.healing()
s2 = spearsman()
s2.gather()
s2.attack()
s2.healing()
g = gunman()
g.gather()
g.attack()
g.refill()
g.healing()