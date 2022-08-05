# Classes relating to character data

from pprint import pprint

MAX_LEVEL = 3

INIT_CLASS = "Barbarian"
INIT_SUBCLASS = "No Subclass Available"
INIT_RACE = "Human"
INIT_SUBRACE = "Standard Rules"
INIT_ARMORCLASS = 10
INIT_INITIATIVE = 0
INIT_SPEED = 30
INIT_HITDIE = 12


INIT_ABILITIES = [
    # (Abbreviation, Initial score, Initial modifier)
            ["STR", 10, 0],
            ["DEX", 10, 0],
            ["CON", 10, 0],
            ["INT", 10, 0],
            ["WIS", 10, 0],
            ["CHA", 10, 0],
]


CLASSES = {
    # (Class name: Subclass selection level, Subclasses list, Hit dice)
    "Barbarian":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Path of the Berserker",
                    "Path of the Totem Warrior",
                ),
            "Hit Die": 12,
        },
    "Bard":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "College of Lore",
                    "College of Valor",
                ),
            "Hit Die": 8,
        },
    "Cleric":
        {
            "Subclass Level": 1,
            "Subclasses":
                (
                    "Domain of Knowledge",
                    "Domain of Life",
                    "Domain of Light",
                    "Domain of Nature",
                    "Domain of Tempest",
                    "Domain of Trickery",
                    "Domain of War",
                ),
            "Hit Die": 8,
        },
    "Druid":
        {
            "Subclass Level": 2,
            "Subclasses":
                (
                    "Circle of the Land",
                    "Circle of the Moon",
                ),
            "Hit Die": 8,
        },
    "Fighter":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Champion",
                    "Battle Master",
                    "Eldritch Knight",
                ),
            "Hit Die": 10,
        },
    "Monk":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Way of the Open Hand",
                    "Way of Shadow",
                    "Way of the Four Elements"
                ),
            "Hit Die": 8,
        },
    "Paladin":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Oath of Devotion",
                    "Oath of the Ancients",
                    "Oath of Vengeance",
                ),
            "Hit Die": 10,
        },
    "Ranger":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Hunter",
                    "Beast Master",
                ),
            "Hit Die": 10,
        },
    "Rogue":
        {
            "Subclass Level": 3,
            "Subclasses":
                (
                    "Thief",
                    "Assassin",
                    "Arcane Trickster",
                ),
            "Hit Die": 8,
        },
    "Sorcerer":
        {
            "Subclass Level": 1,
            "Subclasses":
                (
                    "Draconic Bloodline",
                    "Wild Magic",
                ),
            "Hit Die": 6,
        },
    "Warlock":
        {
            "Subclass Level": 1,
            "Subclasses":
                (
                    "Patron: the Archfey",
                    "Patron: the Fiend",
                    "Patron: the Great Old One",
                ),
            "Hit Die": 8,
        },
    "Wizard":
        {
            "Subclass Level": 2,
            "Subclasses":
                (
                    "School of Abjuration",
                    "School of Conjuration",
                    "School of Divination",
                    "School of Enchantment",
                    "School of Evocation",
                    "School of Illusion",
                    "School of Necromancy",
                    "School of Transmutation"),
            "Hit Die": 6,
               },
}

# CLASSES = {
#     # (Class name: Subclass selection level, Subclasses list, Hit dice)
#     "Barbarian": (3, ("Path of the Berserker", "Path of the Totem Warrior"), 12),
#     "Bard": (3, ("College of Lore", "College of Valor"), 8),
#     "Cleric": (1,
#                ("Domain of Knowledge",
#                 "Domain of Life",
#                 "Domain of Light",
#                 "Domain of Nature",
#                 "Domain of Tempest",
#                 "Domain of Trickery",
#                 "Domain of War",),
#                8
#                ),
#     "Druid": (2, ("Circle of the Land", "Circle of the Moon"), 8),
#     "Fighter": (3, ("Champion", "Battle Master", "Eldritch Knight"), 10),
#     "Monk": (3, ("Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"), 8),
#     "Paladin": (3, ("Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"), 10),
#     "Ranger": (3, ("Hunter", "Beast Master"), 10),
#     "Rogue": (3, ("Thief", "Assassin", "Arcane Trickster"), 8),
#     "Sorcerer": (1, ("Draconic Bloodline", "Wild Magic"), 6),
#     "Warlock": (1, ("Patron: the Archfey", "Patron: the Fiend", "Patron: the Great Old One"), 8),
#     "Wizard": (2,
#                ("School of Abjuration",
#                 "School of Conjuration",
#                 "School of Divination",
#                 "School of Enchantment",
#                 "School of Evocation",
#                 "School of Illusion",
#                 "School of Necromancy",
#                 "School of Transmutation"),
#                6
#                ),
# }

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

SAVING_THROWS = (
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
)

SKILLS = {
    "Acrobatics",
    "Animal Handling",
    "Arcana",
    "Athletics",
    "Deception",
    "History",
    "Insight",
    "Intimidation",
    "Investigation",
    "Medicine",
    "Nature",
    "Perception",
    "Performance",
    "Persuasion",
    "Religion",
    "Slight of Hand",
    "Stealth",
    "Survival",
}


class Character:
    """Object containing all the character's information"""
    def __init__(self):
        self.ability_scores = list(INIT_ABILITIES)
        self.name = ""
        self.level = 1
        self.character_class = INIT_CLASS
        self.subclass = INIT_SUBCLASS
        self.race = INIT_RACE
        self.subrace = INIT_SUBRACE
        self.background = BACKGROUNDS[0]
        self.alignment = ALIGNMENTS[0]
        self.proficiency_bonus = self.calculate_proficiency_bonus()
        self.armorclass = INIT_ARMORCLASS
        self.initiative = INIT_INITIATIVE
        self.speed = INIT_SPEED
        self.hitdie = INIT_HITDIE
        self.hitpoints = self.calculate_hit_points()

    def update_ability_scores(self, new_scores: list):
        """Replaces scores in ability_scores with the scores provided in new_scores"""
        for index, ability in enumerate(self.ability_scores):
            ability[1] = new_scores[index]
        self.calculate_ability_modifiers()

    def swap_ability_scores(self, ability_index1: int, ability_index2: int):
        """Swaps scores in items at ability_index1 and ability_index2 in the ability_scores list"""
        ability_score1 = self.ability_scores[ability_index1][1]
        ability_score2 = self.ability_scores[ability_index2][1]
        self.ability_scores[ability_index1][1] = ability_score2
        self.ability_scores[ability_index2][1] = ability_score1
        self.calculate_ability_modifiers()

    def calculate_ability_modifiers(self):
        for ability in self.ability_scores:
            ability[2] = (ability[1] // 2) - 5

    def calculate_proficiency_bonus(self):
        return (self.level // 4) + 2

    def update_hitdie(self):
        self.hitdie = CLASSES[self.character_class]["Hit Die"]

    def calculate_hit_points(self):
        return self._process_hit_points(self.level)

    def _process_hit_points(self, level):
        if level <= 1:
            return self.hitdie
        else:
            return ((self.hitdie // 2) + 1) + self._process_hit_points(level - 1)

    def calculate_speed(self):
        pass

    def print_character(self):          #TODO: remove
        """For debugging purposes"""
        pprint(self.ability_scores)
        print(self.name)
        print(self.character_class)
        print(self.subclass)
        print(self.race)
        print(self.subrace)
        print(self.background)
        print(f"Level: {self.level}")
        print(f"Prof bonus: {self.proficiency_bonus}")
        print(f"Hit Dice: 1d{self.hitdie}")
        print("-" * 30)
        print()

    @staticmethod
    def get_max_subclass_length():
        all_subclasses = set().union(*[set(CLASSES[sub]["Subclasses"]) for sub in CLASSES])
        return len(max(all_subclasses, key=len))

