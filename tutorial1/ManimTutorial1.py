from manimlib.imports import *
import numpy as np
class TutorialShapes(Scene):
    def construct(self):
        line = Line(LEFT,ORIGIN)
        dot = Dot(ORIGIN,buff = 0.1) #buffer
        circle = Circle()
        square = Square()
        square.move_to(LEFT)
        rectangle  = Rectangle()
        rectangle.set_width(2)
        rectangle.set_height(1)
        polygon = Polygon(np.array((-1.,0.,0.)),np.array((1.,0.,0.)),np.array((2.,1.,0.)),np.array((1.,1.,0.)))
        arc = Arc(0,PI/2).scale(2)
        arrow = Arrow().scale(1.5)
        vector = Vector().scale(1.5)
        vector.move_to(DR)
        doubleArrow = DoubleArrow().scale(1.5)
        doubleArrow.move_to(UR)
        tex=TexMobject("\\frac{d}{dx}f(x)g(x)").set_color(RED)
        tex.move_to(UP)
        text = TextMobject("Hello")
        text.move_to(DOWN)
        self.add(line)
        self.add(dot)
        self.add(circle)
        self.add(square)
        self.add(rectangle)
        self.add(polygon)
        self.add(arc)
        self.add(arrow)
        self.add(vector)
        self.add(doubleArrow)
        self.add(tex)
        self.add(text)

class MyScene(Scene):
    def construct(self):
        pass