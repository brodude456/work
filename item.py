class Item:
    def __init__(self, name, short, skill_bonus, will_bonus):

        self.name=name
        self.shortname=short
        self.skill_bonus=skill_bonus
        self.will_bonus=will_bonus



    def get_name(self):
        return self.name


    def get_short(self):
        """TODO: Returns an item's short name."""
        return self.shortname

    def get_info(self):
        """TODO: Prints information about the item."""
        print(self.name)
        print("Grants a bonus of {} to SKILL.".format(self.skill_bonus))
        print("Grants a bonus of {} to WILL.".format(self.will_bonus))


    def get_skill(self):
        """TODO: Returns the item's skill bonus."""
        return self.skill_bonus
    def get_will(self):
        """TODO: Returns the item's will bonus."""
        return self.will_bonus
