def set_font(widget, size, bold=False):
    font = widget.font()
    font.setPointSize(size)
    if bold:
        font.setBold(True)
    widget.setFont(font)
    return font


def calculate_ability_modifier(ability: int) -> int:
    """Return the proper ability modifer for a given ability score"""
    return (ability // 2) - 5
