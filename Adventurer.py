from item import Item
class Adventurer:
    def __init__(self):
        self.inventory = []
        self.skill = 5
        self.will = 5


    def get_inv(self):
        """TODO: Returns the adventurer's inventory."""
        return self.inventory


    def get_skill(self):
        """TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        total_skill=self.skill
        for item in self.inventory:
            total_skill+=item.get_skill()
        return total_skill

    def get_will(self):
       total_will=self.will
       for item in self.inventory:
           total_will+=item.get_will()
       return total_will


    def take(self, item):
        """TODO: Adds an item to the adventurer's inventory."""
        self.inventory.append(item)

    def check_self(self):
        """TODO: Shows adventurer stats and all item stats."""
        print("You are an adventurer, with a SKILL of {} and a WILL of {}.".format(self.skill,self.will))
        print("You are carrying:")

        if self.inventory:
            for item in self.inventory:
                item.get_info()
        else:
            print("Nothing")

        print("With your items, you have a SKILL level of {} and a WILL power of {}".format(self.get_skill(),self.get_will()))

if __name__=="__main__":

    player=Adventurer()
    player.check_self()
    item1=Item("shield for flowers","shield",10,40)
    item2=Item("shield for smth","smth",20,80)
    player.take(item1)
    player.take(item2)
    player.check_self()


