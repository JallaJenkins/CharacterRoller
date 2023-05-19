# Classes relating to character data

from pprint import pprint
# from copy import deepcopy
from class_data import *
from race_data import *
from background_data import *

MAX_LEVEL = 3

INIT_CLASS = sorted(CLASSES)[0]
INIT_SUBCLASS = "No Subclass Available" if CLASSES[INIT_CLASS]["Subclass Level"] > 1 \
    else CLASSES[INIT_CLASS]["Subclasses"][0]
INIT_RACE = "Human"
INIT_SUBRACE = RACES[INIT_RACE]["Subraces"][0]
INIT_BACKGROUND = sorted(BACKGROUNDS)[0]
INIT_ARMORCLASS = 10
INIT_INITIATIVE = 0
INIT_SPEED = 30
INIT_HITDIE = 12

INIT_ABILITIES_RAW = [
    # (Abbreviation, Initial score, Initial modifier)
    ["STR", 10],
    ["DEX", 10],
    ["CON", 10],
    ["INT", 10],
    ["WIS", 10],
    ["CHA", 10],
]

INIT_ABILITIES = [
    # (Abbreviation, Initial score, Initial modifier)
    ["STR", 10, 0],
    ["DEX", 10, 0],
    ["CON", 10, 0],
    ["INT", 10, 0],
    ["WIS", 10, 0],
    ["CHA", 10, 0],
]

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

INIT_SAVING_THROWS_RAW = [
    ["Strength", 0],
    ["Dexterity", 0],
    ["Constitution", 0],
    ["Intelligence", 0],
    ["Wisdom", 0],
    ["Charisma", 0],
]

INIT_SAVING_THROWS = [
    [False, "Strength", 0],
    [False, "Dexterity", 0],
    [False, "Constitution", 0],
    [False, "Intelligence", 0],
    [False, "Wisdom", 0],
    [False, "Charisma", 0],
]

INIT_SKILLS_RAW = [
    ["Acrobatics", 0],
    ["Animal Handling", 0],
    ["Arcana", 0],
    ["Athletics", 0],
    ["Deception", 0],
    ["History", 0],
    ["Insight", 0],
    ["Intimidation", 0],
    ["Investigation", 0],
    ["Medicine", 0],
    ["Nature", 0],
    ["Perception", 0],
    ["Performance", 0],
    ["Persuasion", 0],
    ["Religion", 0],
    ["Slight of Hand", 0],
    ["Stealth", 0],
    ["Survival", 0],
]

INIT_SKILLS = [
    [False, "Acrobatics", 0, 1],
    [False, "Animal Handling", 0],
    [False, "Arcana", 0],
    [False, "Athletics", 0],
    [False, "Deception", 0],
    [False, "History", 0],
    [False, "Insight", 0],
    [False, "Intimidation", 0],
    [False, "Investigation", 0],
    [False, "Medicine", 0],
    [False, "Nature", 0],
    [False, "Perception", 0],
    [False, "Performance", 0],
    [False, "Persuasion", 0],
    [False, "Religion", 0],
    [False, "Slight of Hand", 0],
    [False, "Stealth", 0],
    [False, "Survival", 0],
]


class Character:
    """Object containing all the character's information"""
    def __init__(self):

        self.name = ""
        self.level = 1
        self.character_class = INIT_CLASS
        self.subclass = INIT_SUBCLASS
        self.race = INIT_RACE
        self.subrace = INIT_SUBRACE
        self.background = INIT_BACKGROUND
        self.alignment = ALIGNMENTS[0]
        self.proficiency_bonus = self.get_proficiency_bonus()
        self.hitdie = INIT_HITDIE

        self.ability_scores_raw = INIT_ABILITIES_RAW
        self.ability_scores = INIT_ABILITIES

        self.saving_throws_raw = INIT_SAVING_THROWS_RAW
        self.saving_throws = INIT_SAVING_THROWS

        self.skills_raw = INIT_SKILLS_RAW
        self.skills = INIT_SKILLS

        self.armorclass_raw = INIT_ARMORCLASS
        self.armorclass = INIT_ARMORCLASS
        # self.initiative_raw = INIT_INITIATIVE
        self.initiative = INIT_INITIATIVE
        self.speed_raw = INIT_SPEED
        self.speed = INIT_SPEED
        self.hitpoints_raw = self.calculate_hit_points()
        self.hitpoints = self.calculate_hit_points()

    # Ability score helper functions
    def replace_ability_scores(self, new_scores: list):
        """Replaces scores in ability_scores with the scores provided in new_scores"""
        for index, ability in enumerate(self.ability_scores_raw):
            ability[1] = new_scores[index]
        self.update_actual_ability_scores()

    def swap_ability_scores(self, ability_index1: int, ability_index2: int):
        """Swaps scores in items at ability_index1 and ability_index2 in the ability_scores_raw list then
        updates ability_scores"""
        ability_score1 = self.ability_scores_raw[ability_index1][1]
        ability_score2 = self.ability_scores_raw[ability_index2][1]
        self.ability_scores_raw[ability_index1][1] = ability_score2
        self.ability_scores_raw[ability_index2][1] = ability_score1
        self.update_actual_ability_scores()

    def calculate_ability_modifiers(self):
        for ability in self.ability_scores:
            ability[2] = (ability[1] // 2) - 5

    def get_ability_modifier(self, ability_abbreviation):
        for ability in self.ability_scores:
            if ability[0] == ability_abbreviation:
                return ability[2]

        return None

    def update_actual_ability_scores(self):
        # Read in raw scores to ability_scores
        for index, ability_score in enumerate(self.ability_scores):
            ability_score[1] = self.ability_scores_raw[index][1]

        # Add class modifiers
        ability_modifiers = CLASSES[self.character_class]["Modifiers"].get("Abilities")
        if ability_modifiers:
            for ability_modifier in ability_modifiers:
                for ability_score in self.ability_scores:
                    if ability_score[0] == ability_modifier:
                        ability_score[1] += ability_modifiers[ability_modifier]

        # Update ability modifiers
        self.calculate_ability_modifiers()

        # # Update saving throws
        self.update_actual_saving_throws()

    # Saving throw helper functions
    def update_actual_saving_throws(self):
        # Read in raw scores to saving_throws
        for index, saving_throw in enumerate(self.saving_throws):
            saving_throw[2] = self.saving_throws_raw[index][1]

        # Adjust for proficiency bonuses
        for saving_throw in self.saving_throws:
            if saving_throw[0]:
                saving_throw[2] += self.proficiency_bonus

        # Adjust for ability modifiers
        for index, ability_score in enumerate(self.ability_scores):
            self.saving_throws[index][2] += ability_score[2]

        # pprint(self.saving_throws)   #TODO: Remove once function is working

    def update_actual_skills(self):
        # Read in raw scores to skills
        for index, skill, in enumerate(self.skills):
            skill[2] = self.skills_raw[index][1]

        # Adjust for proficiency bonus
        for skill in self.skills:
            if skill[0]:
                skill[2] += self.proficiency_bonus

        # Adjust for ability modifiers:


    def get_proficiency_bonus(self):
        return (self.level // 4) + 2

    def update_hitdie(self):
        self.hitdie = CLASSES[self.character_class]["Hit Die"]

    def calculate_hit_points(self):
        base_hit_points = self._process_hit_points(self.level)
        hit_points_modifier = self.get_ability_modifier("CON") * self.level
        self.hitpoints = base_hit_points + hit_points_modifier

    def _process_hit_points(self, level):
        if level <= 1:
            return self.hitdie
        else:
            return ((self.hitdie // 2) + 1) + self._process_hit_points(level - 1)

    def update_speed(self):
        self.speed_raw = RACES[self.race]["Speed"]
        self.calculate_speed()

    def calculate_speed(self):
        # TODO: Dwarves do not get speed reduction from heavy armor
        self.speed = self.speed_raw

    def calculate_initiative(self):
        self.initiative = self.get_ability_modifier("DEX")

    def print_character(self):          #TODO: remove
        """For debugging purposes"""
        pprint(self.ability_scores)
        pprint(self.skills)
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

