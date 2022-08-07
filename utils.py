def set_font(widget, size, bold=False):
    font = widget.font()
    font.setPointSize(size)
    if bold:
        font.setBold(True)
    widget.setFont(font)
    return font

