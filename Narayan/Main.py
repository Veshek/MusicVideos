from manim import *

class Narayan(Scene):

    def construct(self):
        shape = Sector(color=GOLD_B,
                       fill_color=GOLD_B,
                       fill_opacity=1,
                       angle=360 * DEGREES)
        self.play(Create(shape,
                               lag_ratio=0,
                               rate_func=lambda t: linear(1 - t),
                               run_time= 4 * 2))

    def lyrics(self):
        self.play()
