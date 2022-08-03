from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

import utils


class SavingThrowsBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Saving Throws")
        self.strength_label = QLabel("Strength")
        self.dexterity_label = QLabel("Dexterity")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.strength_label)
        self.layout.addWidget(self.dexterity_label)
        self.setLayout(self.layout)


class ProficiencyBonusBox(QGroupBox):
    def __init__(self, character):
        super(ProficiencyBonusBox, self).__init__("Proficiency Bonus")
        self.stat = character.proficiency_bonus
        self.statlabel = QLabel(f"+{self.stat}")
        StatisticsPane.constructStatBox(self, self.statlabel)


class ArmorClassBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Armor Class")
        self.stat = character.armorclass
        self.statlabel = QLabel(str(self.stat))
        StatisticsPane.constructStatBox(self, self.statlabel)


class HitPointsBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Hit Points")
        self.stat = character.hitpoints
        self.statlabel = QLabel(f"{self.stat}/{self.stat}")
        StatisticsPane.constructStatBox(self, self.statlabel)


class InitiativeBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Initiative")
        self.stat = character.initiative
        self.statlabel = QLabel(f"+{self.stat}")
        StatisticsPane.constructStatBox(self, self.statlabel)


class SpeedBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Speed")
        self.stat = character.speed
        self.statlabel = QLabel(f"{self.stat}'")
        StatisticsPane.constructStatBox(self, self.statlabel)


class HitDiceBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Hit Dice")
        self.stat = character.hitdice
        self.statlabel = QLabel(f"{character.level}d{self.stat}")
        StatisticsPane.constructStatBox(self, self.statlabel)


# Saving throws

# Skills

# Passive Skills


# Attacks

# Equipment


class StatisticsPane(QWidget):
    def __init__(self, character):
        super().__init__()

        self.layout = QHBoxLayout()
        self.sublayout_left = QVBoxLayout()
        self.sublayout_right = QVBoxLayout()
        self.topright_layout = QGridLayout()

        for column in range(3):
            self.topright_layout.setColumnStretch(column, 1)

        self.savingthrowsbox = SavingThrowsBox(character)
        self.sublayout_left.addWidget(self.savingthrowsbox)

        self.proficiency_label = ProficiencyBonusBox(character)
        self.topright_layout.addWidget(self.proficiency_label, 0, 0)

        self.armorclassbox = ArmorClassBox(character)
        self.topright_layout.addWidget(self.armorclassbox, 0, 1)

        self.hitpointsbox = HitPointsBox(character)
        self.topright_layout.addWidget(self.hitpointsbox, 0, 2)

        self.initativebox = InitiativeBox(character)
        self.topright_layout.addWidget(self.initativebox, 1, 0)

        self.speedbox = SpeedBox(character)
        self.topright_layout.addWidget(self.speedbox, 1, 1)

        self.hitdicebox = HitDiceBox(character)
        self.topright_layout.addWidget(self.hitdicebox, 1, 2)

        # qss = ".ProficiencyLabel {border-style: groove; border-width: 1px}"
        # self.setStyleSheet(qss)
        utils.set_font(self, 14)
        self.layout.addLayout(self.sublayout_left)
        self.sublayout_right.addLayout(self.topright_layout)
        self.layout.addLayout(self.sublayout_right)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 1)
        self.setLayout(self.layout)

    @staticmethod
    def constructStatBox(statbox, statlabel):
        """Used to formate single stat display boxes (passed as 'statbox').
         Centres the label (passed as 'statlabel') within the box."""
        statbox.setAlignment(Qt.AlignHCenter)
        statbox.layout = QHBoxLayout()
        statbox.layout.setAlignment(Qt.AlignHCenter)
        statbox.layout.addWidget(statlabel)
        statbox.setLayout(statbox.layout)