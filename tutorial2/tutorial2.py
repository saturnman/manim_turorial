import numpy as np

from manimlib.imports import *


class MCat(SVGMobject):
    CONFIG = {
        "file_name" : "mcat.svg",
        "stroke_width" : 2,
        "fill_opacity" : 0,
        "height" : 0.5,
    }

class DropNeedle(GraphScene):
    CONFIG = {
        "x_min": -1.5,
        "x_max": 1.5,
        "y_min": -1.0,
        "y_max": 1.0,
        "graph_origin": ORIGIN
    }
    def get_needles(self):
        result = []
        for _ in range(0,50):
            center = (np.random.random()*2-1,np.random.random()*2-1)
            angle = np.random.random()*2*PI
            result.append((center[0]+2*np.cos(angle),center[1]+2*np.sin(angle),center[0]-2*np.cos(angle),center[1]-2*np.sin(angle)))
        return result
    def construct(self):
        self.setup_axes()
        needles = self.get_needles()
        for needle in needles:
            line = Line(np.array((needle[0],needle[1],0.)),np.array((needle[2],needle[3],0.)))
            line.set_color(BLUE_D)
            self.play(ShowCreation(line))

class SquareToCircle(Scene):
    def construct(self):
        #self.setup_axes()
        circle = Circle()
        square = Square()
        text = TextMobject("This is a square").scale(2)
        text.next_to(square)
        text.set_color(GREEN)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        self.play(ShowCreation(square),ShowCreation(text))
        self.play(Write(text))
        self.play(square.move_to,DOWN,rate_func=linear,run_time=2)
        self.play(Transform(square, circle))
        self.play(circle.flip,RIGHT,rate_func=linear,run_time=2)
        self.play(FadeOut(square))

class ThreeDSurface(ParametricSurface):

    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [BLUE_D]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,x**2 - y**2])

class Test(ThreeDScene):

    def construct(self):
        sphere = ParametricSurface(
        lambda u, v: np.array([
            1.5*np.cos(u)*np.cos(v),
            1.5*np.cos(u)*np.sin(v),
            1.5*np.sin(u)
        ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
        resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        axes = ThreeDAxes()
        self.add(axes)
        self.play(Write(sphere),run_time=2)
        self.wait()

class TutorialBasicAnimation(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes()
        polygon = Polygon(np.array((-1.,0.,0.)),np.array((1.,0.,0.)),np.array((2.,1.,0.)),np.array((1.,1.,0.)))
        svgImage = SVGMobject("mcat.svg")
        svgImageScale = svgImage.copy().scale(3)
        
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(ShowCreation(graph),run_time=2)
        
        #self.add(svgImage)
        self.play(ShowCreation(polygon))
        #self.play(ShowCreation(svgImage))
        self.play(Transform(svgImage,svgImageScale))

        self.wait()
        #svgImage.move_to(DOWN)
        self.play(
            svgImage.move_to, DOWN,
            rate_func=there_and_back,
            run_time=3,
        )

        #self.wait()
        #
        self.wait()
        #self.play(Rotate(svgImage,PI/2,IN))
        self.play(Rotate(svgImage,PI/2,np.array((0.,1.,-1.))))
        #self.remove(svgImage)
        self.wait()
        self.play(FadeOut(svgImage))

    def dummy(self):
        pass
