# This file contains all the functionality for the main statistics pane
# Includes all basic character stats, saving throws, skills, and primary racial and class abilities
# Roughly analogous to the first page of the official D&D 5e character sheet

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
    QGroupBox,
    QCheckBox,
    QRadioButton,
    QStyledItemDelegate,
    QItemDelegate,
    QStyleOptionViewItem, QHeaderView, QTableView,
)

from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QModelIndex,
    QAbstractItemModel,
    QEvent,
)

import utils
from pprint import pprint


# class SkillSaveRow(QWidget):
#     def __init__(self, text):
#         super(SkillSaveRow, self).__init__()
#         self.layout = QHBoxLayout
#         self.skillsave = QRadioButton(text)
#         self.modifier = 0
#         self.modifier_label = "+0"
#         self.layout.addWidget(self.skillsave)
#         self.layout.addWidget(self.modifier_label)


class SavingThrowsModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def data(self, index, role):
        value = self.data[index.row()][index.column()]

        if role == Qt.DisplayRole:

            if index.column() == 0:
                return ""

            if index.column() == 1:
                return f" {value}"

            if index.column() == 2:
                return value

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0])

    def update_saving_throws_view(self):
        index1 = self.index(0, 0)
        index2 = self.index(len(self.data), len(self.data[0]))
        self.dataChanged.emit(index1, index2)


class SavingThrowsView(QTableView):
    def __init__(self):
        super(SavingThrowsView, self).__init__()

        self.verticalHeader().hide()
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        # self.verticalHeader().setDefaultSectionSize(60)
        self.horizontalHeader().hide()
        self.setShowGrid(False)

        # delegate = RadioButtonDelegate()
        # self.setItemDelegateForColumn(0, delegate)


class SavingThrowCheckBox(QCheckBox):
    def __init__(self, model, row, character):
        super().__init__()

        self.row = row
        self.model = model
        self.character = character

    def saving_throw_checkbox_clicked(self, state):
        self.model.data[self.row][0] = bool(state)
        self.character.update_actual_saving_throws()
        self.model.update_saving_throws_view()


class SavingThrowsBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Saving Throws")
        # self.strength_label = QLabel("Strength")
        # self.dexterity_label = QLabel("Dexterity")
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.strength_label)
        # self.layout.addWidget(self.dexterity_label)
        # self.setLayout(self.layout)

        self.layout = QVBoxLayout()
        self.data = character.saving_throws
        pprint(self.data)

        self.tablemodel = SavingThrowsModel(self.data)
        self.tableview = SavingThrowsView()
        self.tableview.setModel(self.tablemodel)

        self.checkboxes = []
        for row in range(self.tablemodel.rowCount(0)):
            checkbox = SavingThrowCheckBox(self.tablemodel, row, character)
            checkbox.stateChanged.connect(checkbox.saving_throw_checkbox_clicked)
            self.checkboxes.append(checkbox)

            checkbox_layout = QVBoxLayout()
            checkbox_layout.setAlignment(Qt.AlignHCenter)
            checkbox_layout.addWidget(checkbox)
            checkbox_pane = QWidget()
            checkbox_pane.setLayout(checkbox_layout)
            self.tableview.setIndexWidget(self.tablemodel.index(row, 0), checkbox_pane)

        self.tableview.setColumnWidth(0, 40)
        self.tableview.setColumnWidth(1, 150)
        self.tableview.resizeRowsToContents()
        self.layout.addWidget(self.tableview)
        self.setLayout(self.layout)


class ProficiencyBonusBox(QGroupBox):
    def __init__(self, character):
        super(ProficiencyBonusBox, self).__init__("Proficiency Bonus")
        self.statlabel = QLabel()
        self.update_proficiencybonusbox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_proficiencybonusbox(self, character):
        character.proficiency_bonus = character.get_proficiency_bonus()
        self.statlabel.setText(f"+{character.proficiency_bonus}")


class ArmorClassBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Armor Class")
        self.statlabel = QLabel()
        self.update_armorclassbox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_armorclassbox(self, character):
        self.statlabel.setText(str(character.armorclass))


class HitPointsBox(QGroupBox):
    #TODO: add randomization feature to hit points??
    def __init__(self, character):
        super().__init__("Hit Points")
        self.statlabel = QLabel()
        self.update_hitpointsbox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_hitpointsbox(self, character):
        character.calculate_hit_points()
        self.statlabel.setText(f"{character.hitpoints}/{character.hitpoints}")


class InitiativeBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Initiative")
        self.statlabel = QLabel()
        self.update_intiativebox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_intiativebox(self, character):
        character.calculate_initiative()
        self.statlabel.setText(str(character.initiative))


class SpeedBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Speed")
        self.statlabel = QLabel()
        self.update_speedbox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_speedbox(self, character):
        character.update_speed()
        self.statlabel.setText(f"{character.speed}'")


class HitDiceBox(QGroupBox):
    def __init__(self, character):
        super().__init__("Hit Dice")
        self.statlabel = QLabel()
        self.update_hitdicebox(character)
        StatisticsTab.constructStatBox(self, self.statlabel)

    def update_hitdicebox(self, character):
        character.update_hitdie()
        self.statlabel.setText(f"{character.level}d{character.hitdie}")

# Saving throws

# Skills

# Passive Skills


# Attacks

# Equipment


class StatisticsTab(QWidget):
    """This tab contains the character's core stats and saving throw and skill modifiers."""
    def __init__(self, character):
        super().__init__()

        self.character = character
        self.layout = QHBoxLayout()
        self.sublayout_left = QVBoxLayout()
        self.sublayout_right = QVBoxLayout()
        self.topright_layout = QGridLayout()

        for column in range(3):
            self.topright_layout.setColumnStretch(column, 1)

        self.savingthrowsbox = SavingThrowsBox(character)
        self.sublayout_left.addWidget(self.savingthrowsbox)

        self.proficiencybox = ProficiencyBonusBox(character)
        self.topright_layout.addWidget(self.proficiencybox, 0, 0)

        self.armorclassbox = ArmorClassBox(character)
        self.topright_layout.addWidget(self.armorclassbox, 0, 1)

        self.hitpointsbox = HitPointsBox(character)
        self.topright_layout.addWidget(self.hitpointsbox, 0, 2)

        self.initiativebox = InitiativeBox(character)
        self.topright_layout.addWidget(self.initiativebox, 1, 0)

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

    def refresh_statistics_tab(self):
        self.proficiencybox.update_proficiencybonusbox(self.character)
        self.armorclassbox.update_armorclassbox(self.character)
        self.hitdicebox.update_hitdicebox(self.character)
        self.hitpointsbox.update_hitpointsbox(self.character)
        self.initiativebox.update_intiativebox(self.character)
        self.speedbox.update_speedbox(self.character)

    @staticmethod
    def constructStatBox(statbox, statlabel):
        """Used to formate single stat display boxes (passed as 'statbox').
         Centres the label (passed as 'statlabel') within the box."""
        statbox.setAlignment(Qt.AlignHCenter)
        statbox.layout = QHBoxLayout()
        statbox.layout.setAlignment(Qt.AlignHCenter)
        statbox.layout.addWidget(statlabel)
        statbox.setLayout(statbox.layout)