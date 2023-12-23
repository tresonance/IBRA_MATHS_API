from manim import *

import numpy as np
import random
import subprocess
import re 

from intros_videos import USE_DEFAULT_MANIM_CONFIG, CONFIG_MANIM_BACKGROUND

from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip


# SET BACKGROUND COLOR (get this color from extern/geometry.cpp which has been copied from host to container by ./run.sh)

cmd = "cat /manim/geometry.hpp | grep '#define BACKGROUND_CHOSEN_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3"
execution = subprocess.Popen([ cmd ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
output, err = execution.communicate(b"get background color")
rc = execution.returncode 
BACKGROUND_CHOSEN_COLOR = output.decode()
BACKGROUND_CHOSEN_COLOR = re.sub("\n", "", BACKGROUND_CHOSEN_COLOR).strip()

# THE TITLE OF THIS LESSON:
TOP_MENU_LECON_TITLE_FROM_MANIM_PYTHON_FILE = "EQ PARAM PLAN"

#print("\n::::::BACKGROUND_CHOSEN_COLOR:::::: ", BACKGROUND_CHOSEN_COLOR)
BACKGROUND_CHOSEN_COLOR = 'BLACK'

DEMONSTRATION_SIZE = 22

LECON_TITLE=25

# https://www.melomaths.fr/static/main/pdfs/TmatCh02combinatoire-denombrement-prof.pdf

############################
#
DURATION_TO_PROCESS_TIMELINE = 5*60
#
#############################

DEMONSTRATION_SIZE = 22

LECON_TITLE=25
##############################################################################
# Video 1:  Introduction au cercle trigo : valeur sin, cos, tan
##############################################################################

AXE_MIN_VAL, AXE_MAX_VAL , AXE_STEP= 0, 3, 0.5

MIN_UVRANGE, MAX_UVRANGE = -1.5, 1.6

ANGLE_PHI_IN_RADIAN, ANGLE_THETA_IN_RADIAN, ANGLE_GAMMA_IN_RADIAN = 2*PI/5, PI/5, 0, 

X_LENGTH, Y_LENGTH, Z_LENGTH = 5, 5, 5

UNITAIRE_VECTOR_CIRCLE_RADIUS = 0.1

AXES_NAME_FONT_SIZE, AXES_NAME_COLOR = 105, YELLOW

OFFSET_VALUE = 6

dir1_x, dir1_y, dir1_z = 1, 1, 0
dir2_x, dir2_y, dir2_z = 0, 0, 1
PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z = 3, 4, 2

# ............................................................................. #
#
#                             VIDEO 1
#
# .............................................................................. #
class Equation_Parametrique_Plan_1(ThreeDScene):
    CONFIG = {
            "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "x_length": X_LENGTH,
            "y_length": Y_LENGTH,
            "z_length": Z_LENGTH,
            "color": YELLOW,
        }

    def construct(self):
       
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

     
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
             (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane = Surface(
            lambda u, v: axes.c2p(*self.surf(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        plane_line = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)


        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            plane, 
            dot, 
            x_label, y_label, z_label
        )
        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT)
        )

        self.wait(DURATION_TO_PROCESS_TIMELINE)
       
    def surf(self, u, v):
        return [
            PLAN_CHOSEN_POINT_X + dir1_x * u + dir2_x * v, 
            PLAN_CHOSEN_POINT_Y + dir1_y * u + dir2_y * v, 
            PLAN_CHOSEN_POINT_Z - dir1_z * u + dir2_z * v
        ]


# ............................................................................. #
#
#                             VIDEO 2
#
# .............................................................................. #    
class Equation_Parametrique_Plan_2(ThreeDScene):
    CONFIG = {
        "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "x_length": X_LENGTH,
        "y_length": Y_LENGTH,
        "z_length": Z_LENGTH,
        "color": YELLOW,
    }

    def construct(self):
        
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

        
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
                (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane = Surface(
            lambda u, v: axes.c2p(*self.surf(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        dot_position = plane_dot.get_center()
        #plane_line = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        vecteur_line_to_plane = DashedVMobject(Arrow( 
            start=axes.get_origin() ,
            end= dot_position
        ), num_dashes=12).set_color(TEAL_C)

        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)


        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            plane, 
            dot, 
            x_label, y_label, z_label
        )
        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT)
        )

        ### Coordinate A(x_A, y_A)
        myfont_size = 40
        point_A = MathTex(r"A")
        text_A_coordinate_3D = MobjectMatrix([[ MathTex(r"x_A", font_size=myfont_size) ], [ MathTex(r"y_A", font_size=myfont_size) ], [ MathTex(r"z_A", font_size=myfont_size) ]]).scale(0.5).set_shade_in_3d(True)
        #text_A_coordinate_3D.rotate(PI/2,axis=RIGHT)

        application1 = MarkupText('<span foreground="white"  >EXERCICE</span>', font_size=font_size, color=RED).move_to(9.5*RIGHT+2*UP)
        application2 = MarkupText('<span>Determiner l\'équation parametrique du plan (P)  </span>', font_size=font_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MarkupText('<span>passant par les points A(3,4,2). B(4, 5, 2)</span>', font_size=font_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MarkupText('<span> et C(3,4,3) </span>', font_size=font_size - 13, color=WHITE).next_to(application3, DOWN)
        
        group_exo = VGroup(application1, application2, application3, application4)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects(text_A_coordinate_3D, point_A)
        point_A.move_to(axes.coords_to_point(PLAN_CHOSEN_POINT_X , 0.5*PLAN_CHOSEN_POINT_Y, 1.5*PLAN_CHOSEN_POINT_Z))
        text_A_coordinate_3D.next_to(point_A)

        
        self.wait(2) 
        self.add(vecteur_line_to_plane)
        self.play(
         Write(point_A), Write(text_A_coordinate_3D) 
        )
        self.wait(DURATION_TO_PROCESS_TIMELINE)

       
       
        
    def surf(self, u, v):
        return [
            PLAN_CHOSEN_POINT_X + dir1_x * u + dir2_x * v, 
            PLAN_CHOSEN_POINT_Y + dir1_y * u + dir2_y * v, 
            PLAN_CHOSEN_POINT_Z - dir1_z * u + dir2_z * v
        ]

# ............................................................................. #
#
#                             VIDEO 3
#
# .............................................................................. #
            
class Equation_Parametrique_Plan_3(ThreeDScene):
    CONFIG = {
        "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "x_length": X_LENGTH,
        "y_length": Y_LENGTH,
        "z_length": Z_LENGTH,
        "color": YELLOW,
    }

    def construct(self):
        
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

        
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
                (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane = Surface(
            lambda u, v: axes.c2p(*self.surf(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        myfont_size = 40
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        
        dot_position = plane_dot.get_center()
        #vecteur_line_to_plane = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        vecteur_line_to_plane = DashedVMobject(Arrow( 
            start=axes.get_origin() ,
            end= dot_position
        ), num_dashes=12).set_color(TEAL_C)

        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)

        plane_vector_dir_1_name = MathTex("\\vec{u}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_1.get_end() + np.array([1, 0, 0]) )
        plane_vector_dir_1_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        plane_vector_dir_2_name = MathTex("\\vec{v}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_2.get_end() + np.array([-1, 0, 0]) )
        plane_vector_dir_2_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)


        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            plane, 
            dot, 
            x_label, y_label, z_label
        )

        ### Coordinate A(x_A, y_A)
        myfont_size = 40
        point_A = MathTex(r"A")
        #text_A_coordinate_3D = MobjectMatrix([[ MathTex(r"x_A", font_size=myfont_size) ], [ MathTex(r"y_A", font_size=myfont_size) ], [ MathTex(r"z_A", font_size=myfont_size) ]]).scale(0.5).set_shade_in_3d(True)
        #text_A_coordinate_3D.rotate(PI/2,axis=RIGHT)

        application1 = MathTex("\\text{EXERCICE}", font_size=myfont_size, color=RED).move_to(9.96*RIGHT+2*UP)
        application2 = MathTex("\\text{Determiner  l\' équation  paramétrique  du  plan   }", font_size=myfont_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MathTex("\\text{passant par les points }", "\\text{A(3, 4, 2) }", "\\text{, }" "\\text{B(4, 5, 2)}", font_size=myfont_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MathTex("\\text{et }",  "\\text{C(3, 4, 3)}", font_size=myfont_size - 13, color=WHITE).next_to(application3, DOWN)
        
        application3.set_color_by_tex_to_color_map({
            "A(3, 4, 2) ": YELLOW,
            "B(4, 5, 2)": YELLOW
        })

        application4.set_color_by_tex_to_color_map({
            "C(3, 4, 3)": YELLOW
        })

        group_exo = VGroup(application1, application2, application3, application4).shift(LEFT)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects( point_A, exercice)
        #point_A.move_to(axes.coords_to_point(PLAN_CHOSEN_POINT_X , 0.5*PLAN_CHOSEN_POINT_Y, 1.5*PLAN_CHOSEN_POINT_Z))
        point_A.move_to(  axes.coords_to_point(1.1*PLAN_CHOSEN_POINT_X , 0.6*PLAN_CHOSEN_POINT_Y, 0.5*PLAN_CHOSEN_POINT_Z) )
        #text_A_coordinate_3D.next_to(point_A)

        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            FadeIn(plane_dot), Write(point_A), GrowArrow(plane_vector_dir_1), GrowArrow(plane_vector_dir_2)
        )

        self.add( plane_vector_dir_1_name, plane_vector_dir_2_name, vecteur_line_to_plane,  exercice  )
        self.wait(DURATION_TO_PROCESS_TIMELINE)
            
    def surf(self, u, v):
        return [
            PLAN_CHOSEN_POINT_X + dir1_x * u + dir2_x * v, 
            PLAN_CHOSEN_POINT_Y + dir1_y * u + dir2_y * v, 
            PLAN_CHOSEN_POINT_Z - dir1_z * u + dir2_z * v
        ]


# ............................................................................. #
#
#                             VIDEO 4
#
# .............................................................................. #
            
class Equation_Cartesienne_Plan_4(ThreeDScene):
    CONFIG = {
        "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "x_length": X_LENGTH,
        "y_length": Y_LENGTH,
        "z_length": Z_LENGTH,
        "color": YELLOW,
    }

    def construct(self):
        
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

        # ... 
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
                (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane = Surface(
            lambda u, v: axes.c2p(*self.surf(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        myfont_size = 40
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        
        dot_position = plane_dot.get_center()
        #vecteur_line_to_plane = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        vecteur_line_to_plane = DashedVMobject(Arrow( 
            start=axes.get_origin() ,
            end= dot_position
        ), num_dashes=12).set_color(TEAL_C)

        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)

        plane_vector_dir_1_name = MathTex("\\vec{u}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_1.get_end() + np.array([1, 0, 0]) )
        plane_vector_dir_1_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        plane_vector_dir_2_name = MathTex("\\vec{v}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_2.get_end() + np.array([-1, 0, 0]) )
        plane_vector_dir_2_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        normalized = lambda v:  np.array(v) / np.sqrt(np.sum(np.array(v)**2))
        normalized_dir1 = normalized([dir1_x, dir1_y, dir1_z])
        normalized_dir2 = normalized([dir2_x, dir2_y, dir2_z])

        croos_vector_dir1_dir2 = np.cross([
                normalized_dir1[0],
                normalized_dir1[1],
                normalized_dir1[2]
        ],  
        [
                normalized_dir2[0],
                normalized_dir2[1],
                normalized_dir2[2]
        ])
        
        croos_vector_dir1_dir2_direction = normalized([
            croos_vector_dir1_dir2[0],
            croos_vector_dir1_dir2[1],
            croos_vector_dir1_dir2[2],
        ])

        #croos_vector_dir1_dir2_direction=croos_vector_dir1_dir2

        ###################################
        #  CROSS VECTOR
        ###################################
        pos = [ dot_position[0], dot_position[1], dot_position[2]  ]
        def func(t):
           
            return [
                pos[0] + croos_vector_dir1_dir2_direction[0] * t , 
                pos[1] + croos_vector_dir1_dir2_direction[1] * t, 
                pos[2] + croos_vector_dir1_dir2_direction[2] * t
            ]
        T_RANGE = [0.5, 1.2]
        func = ParametricFunction(func, t_range = np.array(T_RANGE), fill_opacity=0).set_color(LIGHT_GREY)
        #self.add(func.scale(3))
        vecteur_normal = Arrow( 
           start=(  pos[0] + T_RANGE[0]*croos_vector_dir1_dir2_direction[0],  
              pos[1] + T_RANGE[0]*croos_vector_dir1_dir2_direction[1], 
              pos[2] + T_RANGE[0]*croos_vector_dir1_dir2_direction[2] 
           )
              ,
            end=(  
              pos[0] + T_RANGE[-1]*croos_vector_dir1_dir2_direction[0],  
              pos[1] + T_RANGE[-1]*croos_vector_dir1_dir2_direction[1], 
              pos[2] + T_RANGE[-1]*croos_vector_dir1_dir2_direction[2] 
            ), 
            color=YELLOW, tip_shape=ArrowTriangleTip,
            stroke_width=12, buff=0.5
        )
        #croos_vector_dir1_dir2_end_point = croos_vector_dir1_dir2_direction + 0.001*plane_dot.get_center()
        #plane_vector_croos_product = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point( croos_vector_dir1_dir2_end_point[0], croos_vector_dir1_dir2_end_point[1], croos_vector_dir1_dir2_end_point[2]), color=RED_E)
        plane_vector_normal_name = MathTex("\\vec{w}", font_size=myfont_size - 15, color=YELLOW)
        plane_vector_normal_name.scale(5).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)


        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            plane, 
            dot, 
            x_label, y_label, z_label
        )

        ### Coordinate A(x_A, y_A)
       
        point_A = MathTex(r"A")
        #text_A_coordinate_3D = MobjectMatrix([[ MathTex(r"x_A", font_size=myfont_size) ], [ MathTex(r"y_A", font_size=myfont_size) ], [ MathTex(r"z_A", font_size=myfont_size) ]]).scale(0.5).set_shade_in_3d(True)
        #text_A_coordinate_3D.rotate(PI/2,axis=RIGHT)

        application1 = MathTex("\\text{EXERCICE}", font_size=myfont_size, color=RED).move_to(9.96*RIGHT+2*UP)
        application2 = MathTex("\\text{Determiner  l\' équation  cartesienne  du  plan   }", font_size=myfont_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MathTex("\\text{passant par les points }", "\\text{A(3, 4, 2) }", "\\text{, }" "\\text{B(4, 5, 2)}", font_size=myfont_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MathTex("\\text{et }",  "\\text{C(3, 4, 3)}", font_size=myfont_size - 13, color=WHITE).next_to(application3, DOWN)
        
        application3.set_color_by_tex_to_color_map({
            "A(3, 4, 2) ": YELLOW,
            "B(4, 5, 2)": YELLOW
        })

        application4.set_color_by_tex_to_color_map({
            "C(3, 4, 3)": YELLOW
        })

        group_exo = VGroup(application1, application2, application3, application4).shift(LEFT)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects( point_A,  exercice)
        point_A.move_to(  axes.coords_to_point(1.1*PLAN_CHOSEN_POINT_X , 0.6*PLAN_CHOSEN_POINT_Y, 0.5*PLAN_CHOSEN_POINT_Z) )
        end_point = np.array(
            [
              pos[0] + 0.5*croos_vector_dir1_dir2_direction[0],  
              pos[1] + 0.5*croos_vector_dir1_dir2_direction[1], 
              pos[2] + 0.5*croos_vector_dir1_dir2_direction[2]
            ]
        ) + np.array([0, -0.5, 1])

        pos_A = point_A.get_center()
        plane_vector_normal_name.move_to(  axes.coords_to_point(pos_A[0], pos_A[1], pos_A[2]) + np.array([-3.2, 0, 0])   )
        #text_A_coordinate_3D.next_to(point_A)

        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            FadeIn(plane_dot), Write(point_A), GrowArrow(plane_vector_dir_1), GrowArrow(plane_vector_dir_2)
        )

        self.add( plane_vector_dir_1_name, plane_vector_dir_2_name, plane_vector_normal_name,  exercice  )
        self.add(func.scale(3),  vecteur_normal)
        self.wait(DURATION_TO_PROCESS_TIMELINE)

       
            
    def surf(self, u, v):
        return [
            PLAN_CHOSEN_POINT_X + dir1_x * u + dir2_x * v, 
            PLAN_CHOSEN_POINT_Y + dir1_y * u + dir2_y * v, 
            PLAN_CHOSEN_POINT_Z - dir1_z * u + dir2_z * v
        ]


# ............................................................................. #
#
#                             VIDEO 5
#
# .............................................................................. #
            
class Intersection_Plan_Droite_5(ThreeDScene):
    CONFIG = {
        "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "x_length": X_LENGTH,
        "y_length": Y_LENGTH,
        "z_length": Z_LENGTH,
        "color": YELLOW,
    }

    def construct(self):
        
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

        # ... 
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
                (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane = Surface(
            lambda u, v: axes.c2p(*self.surf(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        myfont_size = 40
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        
        dot_position = plane_dot.get_center()
        #vecteur_line_to_plane = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        vecteur_line_to_plane = DashedVMobject(Arrow( 
            start=axes.get_origin() ,
            end= dot_position
        ), num_dashes=12).set_color(TEAL_C)

        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)

        plane_vector_dir_1_name = MathTex("\\vec{u}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_1.get_end() + np.array([1, 0, 0]) )
        plane_vector_dir_1_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        plane_vector_dir_2_name = MathTex("\\vec{v}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_2.get_end() + np.array([-1, 0, 0]) )
        plane_vector_dir_2_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        #normalized = lambda v:  np.array(v) / np.sqrt(np.sum(np.array(v)**2))
        #normalized_dir1 = normalized([dir1_x, dir1_y, dir1_z])
        #normalized_dir2 = normalized([dir2_x, dir2_y, dir2_z])

        #croos_vector_dir1_dir2 = np.cross([
        #        normalized_dir1[0],
        #        normalized_dir1[1],
        #        normalized_dir1[2]
        #],  
        #[
        #        normalized_dir2[0],
        #        normalized_dir2[1],
        #        normalized_dir2[2]
        #])
        
        #croos_vector_dir1_dir2_direction = normalized([
        #    croos_vector_dir1_dir2[0],
        #    croos_vector_dir1_dir2[1],
        #    croos_vector_dir1_dir2[2],
        #])

        #croos_vector_dir1_dir2_direction=croos_vector_dir1_dir2

        ###################################
        #  LINE INTERSECT
        ###################################
        line_chosen_pos = [ 3, 2.7, 0  ]
        pos = axes.coords_to_point( line_chosen_pos[0], line_chosen_pos[1], line_chosen_pos[2] )

        line_intesect_dir_x, line_intesect_dir_y, line_intesect_dir_z = -0.9, 2, 0.5
        def func(t):
           
            return [
                pos[0] + line_intesect_dir_x * t , 
                pos[1] + line_intesect_dir_y * t, 
                pos[2] + line_intesect_dir_z * t
            ]
        
        T_RANGE = [0.2, 1]
        T_DASHED_RANGE = [2.5, 3]
        func1 = ParametricFunction(func, t_range = np.array(T_RANGE), fill_opacity=0).set_color(TEAL_C)
        vecteur_directeur_line_intersect = Arrow( 
            start=pos ,
            end= np.array([
                pos[0] + line_intesect_dir_x * 0.43*T_RANGE[-1] , 
                pos[1] + line_intesect_dir_y * 0.43*T_RANGE[-1], 
                pos[2] + line_intesect_dir_z * 0.43*T_RANGE[-1]
            ])
        ).scale(1.5).set_color(PURPLE)
        
        func2 = ParametricFunction(func, t_range = np.array(T_DASHED_RANGE), fill_opacity=0, dt=2).set_color(TEAL_C)
        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            plane, 
            dot, 
            x_label, y_label, z_label
        )

        ### Coordinate A(x_A, y_A)
       
        point_A = MathTex(r"A")
        point_K_name = MathTex(r"K", color=ORANGE)
        dot_point_K =  Dot(radius=2*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=pos, color=YELLOW)
        #text_A_coordinate_3D = MobjectMatrix([[ MathTex(r"x_A", font_size=myfont_size) ], [ MathTex(r"y_A", font_size=myfont_size) ], [ MathTex(r"z_A", font_size=myfont_size) ]]).scale(0.5).set_shade_in_3d(True)
        #text_A_coordinate_3D.rotate(PI/2,axis=RIGHT)

        application1 = MathTex("\\text{EXERCICE}", font_size=myfont_size, color=RED).move_to(9.96*RIGHT+2*UP)
        application2 = MathTex("\\text{Determiner  les coordonnées du point d\'intersection P entre   }", font_size=myfont_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MathTex("\\text{le plan }" , "\\text{(P) }", "\\text{passant par les points }", "\\text{A(3, 4, 2) }", "\\text{, }" "\\text{B(4, 5, 2)}", font_size=myfont_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MathTex("\\text{et }",  "\\text{C(3, 4, 3)", "\\text{ et la droite", "\\text{(D)}" ,"\\text{passant }" , font_size=myfont_size - 13, color=WHITE).next_to(application3, DOWN)
        application5 = MathTex("\\text{par le point }", "\\text{E(3, 2.7, 0) }", "\\text{ et de vecteur directeur }", "\\vec{V}","\\text{(-0.9, 2, 0.5)}", font_size=myfont_size - 13, color=WHITE).next_to(application4, DOWN)
        
        application3.set_color_by_tex_to_color_map({
            "A(3, 4, 2) ": YELLOW,
            "B(4, 5, 2)": YELLOW,
            "(P)":YELLOW
        })

        application4.set_color_by_tex_to_color_map({
            "C(3, 4, 3)": YELLOW,
            "(D)": TEAL_B
        })

        application5.set_color_by_tex_to_color_map({
            "E(3, 2.7, 0)": TEAL_B,
            "{V}": TEAL_B,
            "(-0.9, 2, 0.5)": TEAL_B
        })


        group_exo = VGroup(application1, application2, application3, application4, application5).shift(LEFT)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects( point_A,  exercice)
        point_A.move_to(  axes.coords_to_point(1.1*PLAN_CHOSEN_POINT_X , 0.6*PLAN_CHOSEN_POINT_Y, 0.5*PLAN_CHOSEN_POINT_Z) )
        point_K_name.rotate(PI/2,axis=RIGHT).move_to( dot_point_K.get_center() )
        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            FadeIn(plane_dot), Write(point_A), GrowArrow(plane_vector_dir_1), GrowArrow(plane_vector_dir_2)
        )

        self.add( plane_vector_dir_1_name, plane_vector_dir_2_name,  exercice  )
        self.add(func1.scale(3), func2.scale(3), dot_point_K, point_K_name, vecteur_directeur_line_intersect )
        self.wait(DURATION_TO_PROCESS_TIMELINE)

       
            
    def surf(self, u, v):
        return [
            PLAN_CHOSEN_POINT_X + dir1_x * u + dir2_x * v, 
            PLAN_CHOSEN_POINT_Y + dir1_y * u + dir2_y * v, 
            PLAN_CHOSEN_POINT_Z - dir1_z * u + dir2_z * v
        ]


# ............................................................................. #
#
#                             VIDEO 6
#
# .............................................................................. #
MIN2_UVRANGE, MAX2_UVRANGE = -2.1, 1.9
dir1_1_x, dir1_1_y, dir1_1_z = 1, 1, 0
dir1_2_x, dir1_2_y, dir1_2_z = 0, 0, 1
PLAN1_CHOSEN_POINT_X, PLAN1_CHOSEN_POINT_Y, PLAN1_CHOSEN_POINT_Z = 3, 4, 2

dir2_1_x, dir2_1_y, dir2_1_z = -1, 0, 0
dir2_2_x, dir2_2_y, dir2_2_z = 0.2, 2, 0.2
PLAN2_CHOSEN_POINT_X, PLAN2_CHOSEN_POINT_Y, PLAN2_CHOSEN_POINT_Z = 0, 0 , 0

class Intersection_Plan_Plan_6(ThreeDScene):
    CONFIG = {
        "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
        "x_length": X_LENGTH,
        "y_length": Y_LENGTH,
        "z_length": Z_LENGTH,
        "color": YELLOW,
    }

    def construct(self):
        
        font_size=30
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        if BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE

        # ... 
        self.set_camera_orientation(frame_center=-6*LEFT - UP)
        self.move_camera(phi=ANGLE_PHI_IN_RADIAN, theta=ANGLE_THETA_IN_RADIAN, gamma=ANGLE_GAMMA_IN_RADIAN, distance = 1200,  zoom=0.5, run_time=1.5)
        axes = ThreeDAxes(**self.CONFIG)#.add_coordinates()#.move_to(-LEFT + 2*DOWN)
        
        ############################
        #    LABELS
        #############################
        x_label = axes.get_x_axis_label(Tex("x",font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(self.CONFIG["x_length"] + OFFSET_VALUE, 0, 0), 2)))
        y_label = axes.get_y_axis_label(Tex("y", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, self.CONFIG["y_length"] + OFFSET_VALUE, 0), 2)))
        z_label = axes.get_z_axis_label(Tex("z", font_size=AXES_NAME_FONT_SIZE, fill_color=AXES_NAME_COLOR).move_to(np.around(axes.coords_to_point(0, 0, self.CONFIG["z_length"] + OFFSET_VALUE), 2)))

        ##############################
        #  VECTOR
        ##############################
        vector1 = Arrow( 
            np.array([PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z])  , 
            (dir1_x, dir1_y, dir1_z)
        ).set_color(RED)

        vector2 = Arrow( 
            [PLAN_CHOSEN_POINT_X, PLAN_CHOSEN_POINT_Y, PLAN_CHOSEN_POINT_Z]  ,
                (dir2_x, dir2_y, dir2_z)
        ).set_color(YELLOW)

        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))

        ##############################
        # PLANE
        ##############################
        plane1 = Surface(
            lambda u, v: axes.c2p(*self.surf_p1(u, v)),
            u_range=[MIN_UVRANGE, MAX_UVRANGE],
            v_range=[MIN_UVRANGE, MAX_UVRANGE],
            resolution=8,
        ).set_opacity(0.5)


        plane2 = Surface(
            lambda u, v: axes.c2p(*self.surf_p2(u, v)),
            u_range=[MIN2_UVRANGE, MAX2_UVRANGE],
            v_range=[MIN2_UVRANGE, MAX2_UVRANGE],
            checkerboard_colors=[RED, GREEN],
             fill_opacity=1,
            resolution=8,
        ).set_opacity(0.5)
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(RED)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
        ##################################
        # INSIDE THE  PLANE
        ##################################
        myfont_size = 40
        plane_dot = Dot(radius=3*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=axes.coords_to_point(3, 4, 1.9), color=GREEN)
        
        dot_position = plane_dot.get_center()
        #vecteur_line_to_plane = Arrow(start=axes.coords_to_point(0,0,0), end=axes.coords_to_point(3,4,1.9), color=YELLOW)
        vecteur_line_to_plane = DashedVMobject(Arrow( 
            start=axes.get_origin() ,
            end= dot_position
        ), num_dashes=12).set_color(TEAL_C)

        plane_vector_dir_1 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(4, 5, 1.9), color=PURPLE_C)
        plane_vector_dir_2 = Arrow(start=plane_dot.get_center() , end=axes.coords_to_point(3, 4, 2.9), color=RED_E)

        plane_vector_dir_1_name = MathTex("\\vec{u_1}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_1.get_end() + np.array([1, 0, 0]) )
        plane_vector_dir_1_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        plane_vector_dir_2_name = MathTex("\\vec{v_1}", font_size=myfont_size, color=YELLOW).move_to( plane_vector_dir_2.get_end() + np.array([-1, 0, 0]) )
        plane_vector_dir_2_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)

        #normalized = lambda v:  np.array(v) / np.sqrt(np.sum(np.array(v)**2))
        #normalized_dir1 = normalized([dir1_x, dir1_y, dir1_z])
        #normalized_dir2 = normalized([dir2_x, dir2_y, dir2_z])

        #croos_vector_dir1_dir2 = np.cross([
        #        normalized_dir1[0],
        #        normalized_dir1[1],
        #        normalized_dir1[2]
        #],  
        #[
        #        normalized_dir2[0],
        #        normalized_dir2[1],
        #        normalized_dir2[2]
        #])
        
        #croos_vector_dir1_dir2_direction = normalized([
        #    croos_vector_dir1_dir2[0],
        #    croos_vector_dir1_dir2[1],
        #    croos_vector_dir1_dir2[2],
        #])

        #croos_vector_dir1_dir2_direction=croos_vector_dir1_dir2

        ###################################
        #  LINE INTERSECT
        ###################################
        line_chosen_pos = [ 3, 2.7, 0  ]
        pos = axes.coords_to_point( line_chosen_pos[0], line_chosen_pos[1], line_chosen_pos[2] )

        line_intesect_dir_x, line_intesect_dir_y, line_intesect_dir_z = -0.9, 2, 0.5
        def func(t):
           
            return [
                pos[0] + line_intesect_dir_x * t , 
                pos[1] + line_intesect_dir_y * t, 
                pos[2] + line_intesect_dir_z * t
            ]
        
        T_RANGE = [0.2, 1]
        T_DASHED_RANGE = [2.5, 3]
        func1 = ParametricFunction(func, t_range = np.array(T_RANGE), fill_opacity=0).set_color(TEAL_C)
        vecteur_directeur_line_intersect = Arrow( 
            start=pos ,
            end= np.array([
                pos[0] + line_intesect_dir_x * 0.4*T_RANGE[-1] , 
                pos[1] + line_intesect_dir_y * 0.4*T_RANGE[-1], 
                pos[2] + line_intesect_dir_z * 0.4*T_RANGE[-1]
            ])
        ).set_color(YELLOW)
        
       
        group = VGroup(
            axes, 
            plane1, plane2,
            dot, 
            x_label, y_label, z_label
        )

        ### Coordinate A(x_A, y_A)
       
        point_A = MathTex(r"\vec{A_1}")
        point_K_name = MathTex(r"K", color=ORANGE)
        dot_point_K =  Dot(radius=2*UNITAIRE_VECTOR_CIRCLE_RADIUS, point=pos, color=YELLOW)
        #text_A_coordinate_3D = MobjectMatrix([[ MathTex(r"x_A", font_size=myfont_size) ], [ MathTex(r"y_A", font_size=myfont_size) ], [ MathTex(r"z_A", font_size=myfont_size) ]]).scale(0.5).set_shade_in_3d(True)
        #text_A_coordinate_3D.rotate(PI/2,axis=RIGHT)

        application1 = MathTex("\\text{EXERCICE}", font_size=myfont_size, color=RED).move_to(9.96*RIGHT+2*UP)
        application2 = MathTex("\\text{Determiner  l\'equation de la droite (D) qui est l\'intersection  entre   }", font_size=myfont_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MathTex("\\text{d\'une part le plan }", "\\text{(P1)}" , "\\text{passant par le point }", font_size=myfont_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MathTex("\\text{A}_1", "\\text{(3, 4, 2)}", "\\text{ et de vecteurs }", font_size=myfont_size - 10, color=WHITE).next_to(application3, DOWN)
        application5 = MathTex( "\\text{directeurs }", "\\vec{U_1}", "\\text{(1, 1, 0)}", "\\text{ et }", "\\vec{V_1}", "\\text{(0, 0, 1)}" , font_size=myfont_size - 13, color=WHITE).next_to(application4,  DOWN)
        application6 = MathTex( "\\text{ et d\'autre part le plan }" "\\text{(P2)}", "\\text{ contenant le point }",  "\\text{O}", "\\text{(0, 0, 0)}", font_size=myfont_size - 13, color=WHITE).next_to(application5,  DOWN)
        application7 = MathTex("\\text{ et dont deux vecteurs directeurs sont }", "\\vec{U_2}","\\text{(0.2, 2, 0.2)}","\\text{ et }" ,"\\vec{V_2}", "\\text{(-1, 0, 0)}", font_size=myfont_size - 13, color=WHITE).next_to(application6,  DOWN)
        
        application2.set_color_by_tex_to_color_map({
            "(D°": RED
        })

        application3.set_color_by_tex_to_color_map({
            "(P1)": YELLOW,
        })

        application4.set_color_by_tex_to_color_map({
            "{A}_1": YELLOW,
            "(3, 4, 2)": YELLOW
        })

        application5.set_color_by_tex_to_color_map({
            "{U_1}":YELLOW,
            "(1, 1, 0)":YELLOW,
            "{V_1}": YELLOW,
            "(0, 0, 1)": YELLOW
         })

        application6.set_color_by_tex_to_color_map({
            '(P2)': TEAL_A,
            "{O}": TEAL_A,
            "(0, 0, 0)":  TEAL_A,
        })

        application7.set_color_by_tex_to_color_map({
            "{U_2}": TEAL_B,
            "(0.2, 2, 0.2)": TEAL_B,
            "{V_2}": TEAL_B,
            "(-1, 0, 0)": TEAL_B
        })


        group_exo = VGroup(application1, application2, application3, application4, application5, application6, application7).shift(LEFT)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects( point_A,  exercice)
        point_A.move_to(  axes.coords_to_point(1.1*PLAN_CHOSEN_POINT_X , 0.6*PLAN_CHOSEN_POINT_Y, 0.5*PLAN_CHOSEN_POINT_Z) )
        point_K_name.rotate(PI/2,axis=RIGHT).move_to( dot_point_K.get_center() )
        
        ###################################
        # VIDEOS 1
        ###################################
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            FadeIn(plane_dot), Write(point_A), GrowArrow(plane_vector_dir_1), GrowArrow(plane_vector_dir_2)
        )

        self.add( plane_vector_dir_1_name, plane_vector_dir_2_name,  exercice  )
        #self.add(dot_point_K, point_K_name )
        self.wait(DURATION_TO_PROCESS_TIMELINE)

       
            
    def surf_p1(self, u, v):
        return [
            PLAN1_CHOSEN_POINT_X + dir1_1_x * u + dir1_2_x * v, 
            PLAN1_CHOSEN_POINT_Y + dir1_1_y * u + dir1_2_y * v, 
            PLAN1_CHOSEN_POINT_Z - dir1_1_z * u + dir1_2_z * v
        ]

    def surf_p2(self, u, v):
        return [
            PLAN2_CHOSEN_POINT_X + dir2_1_x * u + dir2_2_x * v, 
            PLAN2_CHOSEN_POINT_Y + dir2_1_y * u + dir2_2_y * v, 
            PLAN2_CHOSEN_POINT_Z - dir2_1_z * u + dir2_2_z * v
        ]

           

        

        
       
       
      

        
         
