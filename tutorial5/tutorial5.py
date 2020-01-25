import numpy as np

from manimlib.imports import *
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

class BasicElementDemo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)
        axes = ThreeDAxes()
        self.add(axes)
        sphere = ParametricSurface(
        lambda u, v: np.array([
            1.5*np.cos(u)*np.cos(v),
            1.5*np.cos(u)*np.sin(v),
            1.5*np.sin(u)
        ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
        resolution=(15, 32)).scale(2)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.add(axes)
        self.play(Write(sphere),run_time=2)
        self.wait() 

class TestAxes(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)
        axes = ThreeDAxes()
        self.add(axes)
        #self.move_camera(-0.25*PI,0.25*PI)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait()

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
        self.begin_ambient_camera_rotation()
        #self.play(Write(sphere),run_time=2)
        self.move_camera(PI/3)
        self.wait()

        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

class ThreeCutDemo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.25*PI, 0.35*PI, 120.,0.)
        axes = ThreeDAxes()
        self.add(axes)
        vect = ORIGIN
        face = Square(
            side_length=10.0,
            shade_in_3d=True,
            fill_opacity=0.3,
            color=YELLOW
        )
        xPlane = ValueTracker(3.0)
        cutCurve=ParametricFunction(
                lambda u : np.array([
                u,
                3.0,
                u**2-3.0**2
            ]),color=RED,t_min=-5.0,t_max=5.0,
            )
        cutCurve.set_shade_in_3d(True)
        #face.flip()
        face.shift(5.0 * IN )
        #face.move_to(UP*3.0)
        face.apply_matrix(z_to_vector(UP))
        surface = ThreeDSurface()
        #self.play(ShowCreation(surface))
        def updateCurve(curve):
            curValue = xPlane.get_value()
            newCurve=ParametricFunction(
                lambda u : np.array([
                u,
                curValue,
                u**2-curValue**2
            ]),color=RED,t_min=-5.0,t_max=5.0,
            )
            curve.become(newCurve)
        cutCurve.add_updater(updateCurve) 

        face.add_updater(lambda f:f.move_to(UP*(xPlane.get_value())))

        self.add(face)
        self.add(cutCurve)
        self.add(surface)
        self.play(xPlane.increment_value,-5.0,rate_func=linear,run_time=2.0)
        self.begin_ambient_camera_rotation()
        self.move_camera(PI/3)
        self.wait(2)


class ThreeDTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.25*PI, 0.35*PI, 120.,0.)
        axes = ThreeDAxes()
        self.add(axes)
        movingAxes = ThreeDAxes()
        self.add(movingAxes)

        xLabel = TextMobject("x",color=RED).scale(2)
        xLabel.move_to(RIGHT*3)
        yLabel = TextMobject("y",color=RED).scale(2)
        yLabel.move_to(UP*3)
        yLabel.rotate(PI/2)
        zLabel = TextMobject("z",color=RED).scale(2)
        zLabel.move_to(OUT*3)
        self.add(xLabel)
        self.add(yLabel)
        self.add(zLabel)
        #surface = ThreeDSurface()
        #self.play(ShowCreation(surface))

        d = Dot(np.array([0,0,0]), color = YELLOW)
        self.play(ShowCreation(d))


        self.wait()
        xArrow = Arrow(LEFT*3,RIGHT*3,color=PINK)
        self.add(xArrow)
        movingXAxisData = np.array((1.,0.,0.))
        movingYAxisData = np.array((0.,1.,0.))
        movingZAxisData = np.array((0.,0.,1.))
        #self.move_camera(0.25*np.pi, 0.35*np.pi)
        #self.begin_ambient_camera_rotation()
        self.play(Rotate(zLabel,PI/2,RIGHT))
        self.play(Rotate(xLabel,-PI/2,RIGHT))
        self.play(Rotate(yLabel,PI/2,UP))
        #rotation_matrix
        self.play(Rotate(movingAxes,PI/4,Z_AXIS))
        self.play(Rotate(movingAxes,PI/4,np.array((1.,1.,0.))))
        self.play(Rotate(movingAxes,PI/4,np.array((1.,-1.,np.sqrt(2.0)))))
        self.wait()
        #self.play(Rotate)

        rot1Matrix = rotation_matrix(PI/4,Z_AXIS)
        [movingXAxisData,movingYAxisData,movingZAxisData] = map(lambda vector:np.dot(rot1Matrix,vector),[movingXAxisData,movingYAxisData,movingZAxisData])
        rot2Matrix = rotation_matrix(PI/4,movingXAxisData)
        [movingXAxisData,movingYAxisData,movingZAxisData] = map(lambda vector:np.dot(rot2Matrix,vector),[movingXAxisData,movingYAxisData,movingZAxisData])
        rot3Matrix = rotation_matrix(PI/4,movingZAxisData)
        print(movingZAxisData)
        [movingXAxisData,movingYAxisData,movingZAxisData] = map(lambda vector:np.dot(rot3Matrix,vector),[movingXAxisData,movingYAxisData,movingZAxisData])
        
        resultArrow = Arrow(ORIGIN,movingXAxisData*3,color=GREEN)
        self.add(resultArrow)
        #rot2Matrix = rotation_matrix(PI/4,arrowData)
        #arrowData = np.dot(arrowData,rot2Matrix)

        self.move_camera(PI/3)
        self.wait()