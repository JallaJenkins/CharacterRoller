from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget, QTabWidget,
)

from statistics_tab import *


class DetailsTabs(QTabWidget):
    """Central area for holding three tabbed pages with character details:
        Tab 1) basic states and abilities,
        Tab 2) further background and more advanced abilities, and
        Tab 3) spells."""

    def __init__(self, character):
        super().__init__()

        self.statistics_pane = StatisticsPane(character)
        self.addTab(self.statistics_pane, "&Stats")





