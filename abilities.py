# Class and functions relating to the ability pane and ability dock
# Abilities are stored in both the abilities model and in the character object

import sys
import time
from functools import partial
import random

from character import *

from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QSize,

)

from PyQt5.QtWidgets import (
    QWidget,
    QDockWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTableView,
    QHeaderView,
)

from PyQt5.QtGui import (
    QFont,
)

from character import Character
from utils import set_font

random.seed(time.time())


class TableModel(QAbstractTableModel):
    """Model used to store the characters abilities. Accessed by other widgets in the abilities pane to change the abilities
    data. Separate from the abilities table stored in the character object."""

    def __init__(self, data):
        super().__init__()
        self.data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self.data[index.row()][index.column()]
            if index.column() == 2 and isinstance(value, int):
                if value >= 0:
                    return f"(+{value})"
                else:
                    return f"({value})"
            return value

        if role == Qt.FontRole:

            if index.column() == 0:
                return QFont('Ariel', 24, 400)

            if index.column() == 1:
                return QFont('Ariel', 20)

            if index.column() == 2:
                return QFont('Ariel', 16)

        if role == Qt.TextAlignmentRole:

            if index.column() == 0:
                return Qt.AlignVCenter | Qt.AlignLeft

            if index.column() == 1 or index.column() == 2:
                return Qt.AlignVCenter | Qt.AlignRight

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0])


class AbilitiesTableView(QTableView):
    """Table View used to display abilities from the abilities model."""

    def __init__(self):
        super(AbilitiesTableView, self).__init__()

        self.verticalHeader().hide()
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(60)
        self.horizontalHeader().hide()
        self.setShowGrid(False)


class AbilitiesPane(QWidget):
    """Central widget on the abilities dock. Holds the abilities table, buttons for rolling
    and swapping abilities, and various settings."""

    def __init__(self, character):
        super().__init__()

        self.character = character

        self.layout = QVBoxLayout()

        self.data = character.ability_scores

        # Create model and view for holding ability names, scores, and modifiers
        self.abilities_view = AbilitiesTableView()
        self.abilities_model = TableModel(self.data)
        self.abilities_view.setModel(self.abilities_model)
        self.abilities_view.resizeColumnsToContents()
        self.abilities_view.setColumnWidth(1, 40)
        self.abilities_view.setColumnWidth(2, 50)
        self.abilities_view.setFocusPolicy(Qt.NoFocus)
        self.layout.addWidget(self.abilities_view)

        # Creates button for re-rolling abilities
        self.roll_abilities_button = QPushButton("Re-roll!")
        set_font(self.roll_abilities_button, 12, bold=True)
        self.roll_abilities_button.setCheckable(False)
        self.roll_abilities_button.clicked.connect(self.roll_abilities_button_clicked)
        self.layout.addWidget(self.roll_abilities_button)

        # Creates buttons for swapping ability scores
        # Requires two ability scores to be currently selected on the abilities table
        self.swap_button = QPushButton("Swap!")
        set_font(self.swap_button, 12, bold=True)
        self.swap_button.setCheckable(False)
        self.swap_button.clicked.connect(self.swap_button_clicked)
        self.layout.addWidget(self.swap_button)

        # Set size and layout of abilities pane
        self.setLayout(self.layout)
        self.setFocusPolicy(Qt.NoFocus)
        self.setMaximumSize(QSize(200, 450))

    def roll_abilities_button_clicked(self):
        """Uses 4d6 and add the 3 highest rolls method to generate scores, then refreshes score"""
        # TODO: add additional methods for rolling abilities with setting selector in the abilities pave

        ability_scores = []

        for _ in range(6):
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            ability_scores.append(sum(rolls))

        for index, ability in enumerate(self.abilities_model.data):
            ability[1] = ability_scores[index]

        self.refresh_abilities()

    def swap_button_clicked(self):
        """If two scores are selected in the abilities table, they are swapped; otherwise no effect"""

        selected_indexes = self.abilities_view.selectedIndexes()

        if len(selected_indexes) != 2:
            return

        ability_score1 = self.abilities_model.data[selected_indexes[0].row()][1]
        ability_score2 = self.abilities_model.data[selected_indexes[1].row()][1]
        self.abilities_model.data[selected_indexes[0].row()][1] = ability_score2
        self.abilities_model.data[selected_indexes[1].row()][1] = ability_score1

        self.refresh_abilities()

    def refresh_abilities(self):
        """Calculates ability modifiers, refreshes ability scores and modifiers on the abilities table,
        then calls update_abilities method to store the abilities in the character object"""

        self.calculate_ability_modifiers()
        index1 = self.abilities_model.index(0, 0)
        index2 = self.abilities_model.index(len(self.abilities_model.data), len(self.abilities_model.data[0]))
        self.abilities_model.dataChanged.emit(index1, index2)
        self.character.update_abilities(self.abilities_model.data)

    def calculate_ability_modifiers(self):
        for ability in self.abilities_model.data:
            ability[2] = (ability[1] // 2) - 5


class AbilitiesDock(QDockWidget):
    """Dock containing character's basic ability scores."""

    def __init__(self, character):
        super().__init__()
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setWindowTitle("Ability Scores")
        self.abilities_pane = AbilitiesPane(character)
        self.setWidget(self.abilities_pane)


