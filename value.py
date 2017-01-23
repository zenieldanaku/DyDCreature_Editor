from pygame import font
from azoe.widgets import BaseWidget


class Value (BaseWidget):
    hasMouseOver = False
    img_uns = None
    img_sel = None
    img_dis = None

    def __init__(self, value, center):
        super().__init__()
        self.value = value
        self.render()

        self.image = self.img_uns
        self.rect = self.image.get_rect(center=center)

    def __repr__(self):
        return str(self.value)

    def on_mouse_in(self):
        self.hasMouseOver = True

    def on_mouse_out(self):
        self.hasMouseOver = False

    def on_mouse_down(self, button):
        if button == 4:
            self.value += 1
        elif button == 5:
            self.value -= 1
        self.render()

    def render(self):
        fuente_n = font.SysFont('Verdana', 16)
        fuente_b = font.SysFont('Verdana', 16, bold=True)
        blanco = 255, 255, 255
        gris = 125, 125, 125
        negro = 0, 0, 0

        value = self.value
        self.img_uns = fuente_n.render(str(value), 1, negro, blanco)
        self.img_sel = fuente_b.render(str(value), 1, negro, blanco)
        self.img_dis = fuente_n.render(str(value), 1, gris, blanco)

    def update(self):
        if self.hasMouseOver:
            self.image = self.img_sel
        else:
            self.image = self.img_uns
