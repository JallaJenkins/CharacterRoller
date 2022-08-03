# Personal info pane for holding basic character date, other than abilities
# Data is also stored in the character object
# Data other than name and level are displayed in combo boxes for ease of selection.
# Data on options for the combo boxes in held in character file

# TODO: Remove all calls to character.print_character
# TODO: Add mechanism for user to lock any selection

from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QSize,

)

from PyQt5.QtWidgets import (
    QWidget,
    QDockWidget,
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QSpinBox,
    QLabel,
    QTableView,
    QHeaderView,
    QLineEdit,
    QComboBox,
)

from PyQt5.QtGui import (
    QPalette,
    QColor,
)

from character import *
from abilities import *
from utils import set_font


FONT_SIZE = 14


class TitleLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        set_font(self, FONT_SIZE, bold=True)
        qss = """QLabel {
                    color: white;
                    background-image: url(./cob_a.jpg);
                    }"""
        # TODO: optimize image settings & size
        self.setStyleSheet(qss)


class NameBox(QLineEdit):
    def __init__(self, character, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.character = character

        set_font(self, FONT_SIZE, bold=True)
        self.setReadOnly(True)
        self.setPlaceholderText("What's your name?")
        self.returnPressed.connect(self.text_entered)

    def mouseDoubleClickEvent(self, e):
        if self.isReadOnly():
            self.setReadOnly(False)
            self.setSelection(0, len(self.text()))
        else:
            self.text_entered()

    def text_entered(self):
        self.character.name = self.text()
        self.setReadOnly(True)
        self.clearFocus()
        self.character.print_character()


class ClassBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.addItems(CLASSES)
        self.update_class_view()

    def update_class_view(self):
        self.setCurrentText(self.character._class)


class SubclassBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.update_available_subclasses()
        self.setMinimumContentsLength(Character.get_max_subclass_length())
        self.update_subclass_view()

    def update_available_subclasses(self):
        """Updates list of subclasses available when the user selects a new class"""
        self.clear()
        _class = self.character._class
        available_subclass_level = CLASSES[_class]["Subclass Level"]
        if self.character.level < available_subclass_level:
            self.addItem("No subclass available")
            return

        available_subclasses = CLASSES[_class]["Subclasses"]
        for subclass in available_subclasses:
            self.addItem(subclass)

    def update_subclass_view(self):
        self.setCurrentText(self.character.subclass)


class RaceBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.addItems(RACES)
        self.update_race_view()

    def update_race_view(self):
        self.setCurrentText(self.character.race)


class SubraceBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.update_available_subraces()
        self.update_subrace_view()

    def update_available_subraces(self):
        """Updates available subraces when user selects a new race"""
        self.clear()
        current_race = self.character.race
        available_subraces = RACES[current_race]
        if not available_subraces:
            self.addItem("No subrace available")
            return

        for subrace in available_subraces:
            self.addItem(subrace)

    def update_subrace_view(self):
        self.setCurrentText(self.character.subrace)


class LevelBox(QSpinBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.setMinimum(1)
        self.setMaximum(3)
        self.lineEdit().setReadOnly(True)

        palette = self.lineEdit().palette()
        palette.setColor(QPalette.Highlight, QColor(Qt.transparent))
        palette.setColor(QPalette.HighlightedText, QColor(Qt.black))
        self.lineEdit().setPalette(palette)

        self.update_level_box()

    def update_level_box(self):
        self.setValue(self.character.level)


class BackgroundBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.addItems(BACKGROUNDS)
        self.update_background_box()

    def update_background_box(self):
        self.setCurrentText(self.character.background)


class AlignmentBox(QComboBox):
    def __init__(self, character):
        super().__init__()

        self.character = character
        set_font(self, FONT_SIZE, bold=True)
        self.addItems(ALIGNMENTS)
        self.update_alignment_box()

    def update_alignment_box(self):
        self.setCurrentText(self.character.alignment)


class PersonalPane(QWidget):
    """Central widget for the personal info dock"""

    def __init__(self, character):
        super().__init__()

        self.character = character
        self.layout = QGridLayout()

        self.title = TitleLabel(" Character Roller")
        self.layout.addWidget(self.title, 0, 0)

        label = QLabel("Class/Subclass: ")
        set_font(label, FONT_SIZE)
        self.layout.addWidget(label, 0, 1)

        self.class_box = ClassBox(character)
        self.class_box.currentTextChanged.connect(self.handle_class_changed)
        self.layout.addWidget(self.class_box, 0, 2)

        self.subclass_box = SubclassBox(character)
        self.subclass_box.currentTextChanged.connect(self.handle_subclass_changed)
        self.layout.addWidget(self.subclass_box, 0, 3)

        self.name_box = NameBox(character)
        self.layout.addWidget(self.name_box, 1, 0)

        label = QLabel("Race/Subrace: ")
        set_font(label, FONT_SIZE)
        self.layout.addWidget(label, 1, 1)

        self.race_box = RaceBox(character)
        self.race_box.currentTextChanged.connect(self.handle_race_changed)
        self.layout.addWidget(self.race_box, 1, 2)

        self.subrace_box = SubraceBox(character)
        self.subrace_box.currentTextChanged.connect(self.handle_subrace_changed)
        self.layout.addWidget(self.subrace_box)

        alignment_layout = QHBoxLayout()

        label = QLabel("Level: ")
        set_font(label, FONT_SIZE)
        alignment_layout.addWidget(label)

        self.level_box = LevelBox(character)
        self.level_box.valueChanged.connect(self.handle_level_changed)
        alignment_layout.addWidget(self.level_box)

        label = QLabel()
        qss = """QLabel {
                            color: white;
                            background-image: url(./cob_a.jpg);
                            }"""
        label.setStyleSheet(qss)
        alignment_layout.addWidget(label)

        alignment_layout.setStretch(2, 1)
        self.layout.addLayout(alignment_layout, 2, 0)

        label = QLabel("Background: ")
        set_font(label, FONT_SIZE)
        self.layout.addWidget(label, 2, 1)

        self.background_box = BackgroundBox(character)
        self.background_box.currentTextChanged.connect(self.handle_background_changed)
        self.layout.addWidget(self.background_box, 2, 2)

        alignment_layout = QHBoxLayout()

        label = QLabel("Alignment: ")
        set_font(label, FONT_SIZE)
        alignment_layout.addWidget(label)

        self.alignment_box = AlignmentBox(character)
        self.alignment_box.currentTextChanged.connect(self.handle_alignment_changed)
        alignment_layout.addWidget(self.alignment_box)

        alignment_layout.setStretch(1, 1)
        self.layout.addLayout(alignment_layout, 2, 3)

        self.setLayout(self.layout)

    def handle_class_changed(self, _class):
        self.character._class = _class
        self.subclass_box.update_available_subclasses()

    def handle_subclass_changed(self, subclass):
        self.character.subclass = subclass
        self.character.print_character()

    def handle_race_changed(self, race):
        self.character.race = race
        self.subrace_box.update_available_subraces()

    def handle_subrace_changed(self, subrace):
        self.character.subrace = subrace
        self.character.print_character()

    def handle_background_changed(self, background):
        self.character.background = background
        self.character.print_character()

    def handle_alignment_changed(self, alignment):
        self.character.alignment = alignment
        self.character.print_character()

    def handle_level_changed(self, level):
        self.character.level = level
        self.subclass_box.update_available_subclasses()
        self.character.print_character()


class PersonalInfoDock(QDockWidget):
    """Dock containing character's basic personal info such as class, race, and alignment."""
    def __init__(self, character):
        super().__init__()

        self.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.setWindowTitle("Personal Information")
        self.personal_pane = PersonalPane(character)
        self.setWidget(self.personal_pane)
