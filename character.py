# Classes relating to character data

from pprint import pprint

MAX_LEVEL = 3

ABILITIES_INIT = [
            ["STR", 10, 0],
            ["DEX", 10, 0],
            ["CON", 10, 0],
            ["INT", 10, 0],
            ["WIS", 10, 0],
            ["CHA", 10, 0],
]

CLASSES = {
    "Barbarian": (3, ("Path of the Berserker", "Path of the Totem Warrior")),
    "Bard": (3, ("College of Lore", "College of Valor")),
    "Cleric": (1,
               ("Domain of Knowledge",
                "Domain of Life",
                "Domain of Light",
                "Domain of Nature",
                "Domain of Tempest",
                "Domain of Trickery",
                "Domain of War",)
               ),
    "Druid": (2, ("Circle of the Land", "Circle of the Moon")),
    "Fighter": (3, ("Champion", "Battle Master", "Eldritch Knight")),
    "Monk": (3, ("Way of the Open Hand", "Way of Shadow", "Way of the Four Elements")),
    "Paladin": (3, ("Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance")),
    "Ranger": (3, ("Hunter", "Beast Master")),
    "Rogue": (3, ("Thief", "Assassin", "Arcane Trickster")),
    "Sorcerer": (1, ("Draconic Bloodline", "Wild Magic")),
    "Warlock": (1, ("Patron: the Archfey", "Patron: the Fiend", "Patron: the Great Old One")),
    "Wizard": (2,
               ("School of Abjuration",
                "School of Conjuration",
                "School of Divination",
                "School of Enchantment",
                "School of Evocation",
                "School of Illusion",
                "School of Necromancy",
                "School of Transmutation")
               ),
}

RACES = {
    "Dwarf": ("Hill Dwarf", "Mountain Dwarf"),
    "Elf": ("High Elf", "Wood Elf"),
    "Halfling": ("Lightfoot", "Stout"),
    "Human": ("Standard Rules", "Feat Rules"),
    "Dragonborn": ("Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"),
    "Gnome": ("Forest Gnome", "Rock Gnome"),
    "Half-Elf": (),
    "Half-Orc": (),
    "Tiefling": (),
}

BACKGROUNDS = (
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Sailor",
    "Soldier",
    "Urchin",
)

ALIGNMENTS = (
    "True Neutral",
    "Neutral Good",
    "Neutral Evil",
    "Lawful Good",
    "Lawful Neutral",
    "Lawful Evil",
    "Chaotic Good",
    "Chaotic Neutral",
    "Chaotic Evil",
)


class Character:
    """Object containing all the character's information"""
    def __init__(self):
        self.ability_scores = list(ABILITIES_INIT)
        self.name = ""
        self.level = 1
        self._class = "Barbarian"
        self.subclass = CLASSES[self._class][1][0]
        self.race = "Human"
        self.subrace = RACES[self.race][0]
        self.background = BACKGROUNDS[0]
        self.alignment = ALIGNMENTS[0]

    def update_abilities(self, ability_scores):
        self.ability_scores = ability_scores

    def print_character(self):          #TODO: remove
        """For debugging purposes"""
        pprint(self.ability_scores)
        print(self.name)
        print(self._class)
        print(self.subclass)
        print(self.race)
        print(self.subrace)
        print(self.background)
        print(f"Level: {self.level}")
        print("-" * 30)
        print()

    @staticmethod
    def get_max_subclass_length():
        all_subclasses = set().union(*[set(CLASSES[sub][1]) for sub in CLASSES])
        return len(max(all_subclasses, key=len))

