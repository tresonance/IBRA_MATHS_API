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

#cmd = "docker exec -it my-math-tle-container  cat /manim/geometry.hpp | grep '#define BACKGROUND_CHOSEN_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3"
cmd = "cat /Users/ibrahimatraore/COURSES/ONLY_BOARD/board-ext-geometry.hpp | grep '#define EXTERN_BACKGROUND_CHOSEN_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3"
execution = subprocess.Popen([ cmd ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, err = execution.communicate(b"get background color")
rc = execution.returncode 
print("output: ", output.decode())
global BACKGROUND_CHOSEN_COLOR
BACKGROUND_CHOSEN_COLOR = output.decode()
BACKGROUND_CHOSEN_COLOR = BACKGROUND_CHOSEN_COLOR.strip()
#BACKGROUND_CHOSEN_COLOR = str( BACKGROUND_CHOSEN_COLOR )
# THE TITLE OF THIS LESSON:
TOP_MENU_LECON_TITLE_FROM_MANIM_PYTHON_FILE = "EQ PARAM DROITE"

print("\n::::::BACKGROUND_CHOSEN_COLOR:%s" % BACKGROUND_CHOSEN_COLOR )

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

AXE_MIN_VAL, AXE_MAX_VAL , AXE_STEP= 0, 3, 0.5

MIN_UVRANGE, MAX_UVRANGE = -1.5, 1.6

ANGLE_PHI_IN_RADIAN, ANGLE_THETA_IN_RADIAN, ANGLE_GAMMA_IN_RADIAN = 2*PI/5, PI/5, 0, 

X_LENGTH, Y_LENGTH, Z_LENGTH = 5, 5, 5

UNITAIRE_VECTOR_CIRCLE_RADIUS = 0.1

AXES_NAME_FONT_SIZE, AXES_NAME_COLOR = 105, YELLOW

OFFSET_VALUE = 6

dir1_x, dir1_y, dir1_z = 1, -1, 1

LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z = -2, 3, 1

# ............................................................................. #
#
#                             VIDEO 1
#
# .............................................................................. #
class Equation_Parametrique_Line_1(ThreeDScene):
    CONFIG = {
            "x_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "y_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "z_range":[AXE_MIN_VAL, AXE_MAX_VAL, AXE_STEP],
            "x_length": X_LENGTH,
            "y_length": Y_LENGTH,
            "z_length": Z_LENGTH,
            "color": YELLOW
        }
    

    def construct(self):
       
        font_size=30
   
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            self.camera.background_color = BLACK
        elif BACKGROUND_CHOSEN_COLOR == 'WHITE':
            self.camera.background_color = WHITE
        elif BACKGROUND_CHOSEN_COLOR == 'CYAN':
            self.camera.background_color = TEAL_B
        elif BACKGROUND_CHOSEN_COLOR == 'GREY':
            self.camera.background_color = GREY_B
        elif BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'SILVER':
            self.camera.background_color = SILVER
        elif BACKGROUND_CHOSEN_COLOR == 'MAROON':
            self.camera.background_color = MAROON_E
        elif BACKGROUND_CHOSEN_COLOR == 'OLIVE':
            self.camera.background_color = OLIVE
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'MAGENTA':
            self.camera.background_color = MAGENTA
        elif BACKGROUND_CHOSEN_COLOR == 'TRANSPARENT':
            self.camera.background_color = TRANSPARENT
        elif BACKGROUND_CHOSEN_COLOR == 'ORANGE':
            self.camera.background_color = ORANGE
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE
        elif BACKGROUND_CHOSEN_COLOR == 'BROWN':
            self.camera.background_color = BROWN
        else:
            print( "BACKGROUND_CHOSEN_COLOR:%s" % BACKGROUND_CHOSEN_COLOR )
            print("len : " , len(BACKGROUND_CHOSEN_COLOR))
            raise Exception("Unable to identify this background color in MANIM Scrpt scene1\n")

        myfont_size=130
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
        #  
        ##############################
        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))
        
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
        
     

        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            x_label, y_label, z_label
        )
        
        ###################################
        # LINE
        ###################################
        def func(t):
            pos = axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)
            return [
                pos[0] + dir1_x * t , 
                pos[1] + dir1_y * t, 
                pos[2] + dir1_z * t
            ]

        func = ParametricFunction(func, t_range = np.array([-0.3, 1.3]), fill_opacity=0).set_color(RED)
       
        point_A_rond = dot.copy().set_radius(dot.get_radius() + 1).set_color(TEAL_B)
        
        point_A_rond_name = MathTex(r"\text{A}", font_size=myfont_size, color=WHITE).scale(0.4).move_to( axes.coords_to_point(0, 3.5, 0.9) )
        point_A_rond.move_to(axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z))
        self.add(func.scale(3))

        point_A_rond_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        
        #self.add_fixed_in_frame_mobjects( point_A_name)
        point_O_origine_name = MathTex(r"\text{O}", font_size=myfont_size, color=YELLOW).scale(0.3).move_to( axes.coords_to_point(0, 0.1, -0.25) )
        point_O_origine_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        

        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            FadeIn( point_A_rond ), FadeIn( point_A_rond_name ), FadeIn( point_O_origine_name )
        )

        self.wait(DURATION_TO_PROCESS_TIMELINE) 


# ............................................................................. #
#
#                             VIDEO 2
#
# .............................................................................. #
class Equation_Parametrique_Line_2(ThreeDScene):
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
        elif BACKGROUND_CHOSEN_COLOR == 'RED':
            self.camera.background_color = RED
        elif BACKGROUND_CHOSEN_COLOR == 'GREEN':
            self.camera.background_color = GREEN
        elif BACKGROUND_CHOSEN_COLOR == 'YELLOW':
            self.camera.background_color = YELLOW
        elif BACKGROUND_CHOSEN_COLOR == 'BLUE':
            self.camera.background_color = BLUE
        elif BACKGROUND_CHOSEN_COLOR == 'PURPLE':
            self.camera.background_color = PURPLE
        else:
            print( BACKGROUND_CHOSEN_COLOR )
            print("len : " , len(BACKGROUND_CHOSEN_COLOR))
            raise Exception("Unable to identify this background color in MANIM Scrpt Scene\n")
     
        

        myfont_size=130
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
        #  
        ##############################
        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))
        
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(MAROON_B)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
     

        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            x_label, y_label, z_label
        )
        
        ###################################
        # LINE
        ###################################
        def func(t):
            pos = axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)
            return [
                pos[0] + dir1_x * t , 
                pos[1] + dir1_y * t, 
                pos[2] + dir1_z * t
            ]
        
        func = ParametricFunction(func, t_range = np.array([-0.3, 1.3]), fill_opacity=0).set_color(RED)
        start_pos = axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)
        next_pos = axes.coords_to_point( start_pos[0] + dir1_x, start_pos[1] + dir1_y, start_pos[2] + dir1_z)
        #next_pos = axes.coords_to_point(LINE_CHOSEN_POINT_X + dir1_x, LINE_CHOSEN_POINT_Y + dir1_y, LINE_CHOSEN_POINT_Z + dir1_z)

        vecteur_directeur = Arrow( 
            start_pos ,
            (  start_pos[0] + 1.6*dir1_x,  start_pos[1] + 1.6*dir1_y,  start_pos[2] + 1.6*dir1_z ) ,
            color=YELLOW, tip_shape=ArrowTriangleTip,
            stroke_width=8, buff=0.25
        )

        myfont_size=130
        vecteur_directeur_name = MathTex("\\vec{u}", font_size=myfont_size, color=YELLOW).move_to( 0.5*(vecteur_directeur.get_end() + vecteur_directeur.get_start() ) + np.array([0, 1, 1]) )
        line_name = MathTex("( \\Delta )", font_size=int(0.5*myfont_size) , color=RED).move_to(vecteur_directeur.get_start() + np.array([-1, 3.1, -1]))
        point_A_rond = dot.copy().set_radius(dot.get_radius() + 2).set_color(TEAL_B).move_to(axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z))
        
        point_A_rond_name = MathTex(r"\text{A}", font_size=myfont_size, color=WHITE).scale(0.4).move_to( axes.coords_to_point(0, 3.5, 0.9) )
        point_A_rond.move_to(axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z))
        self.add(func.scale(3))

        vecteur_directeur_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        line_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        point_A_rond_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        
        #self.add_fixed_in_frame_mobjects(vecteur_directeur_name, line_name)
        point_O_origine_name = MathTex(r"\text{O}", font_size=myfont_size, color=YELLOW).scale(0.3).move_to( axes.coords_to_point(0, 0.1, -0.25) )
        point_O_origine_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            Write( vecteur_directeur ),
            FadeIn( point_A_rond ), FadeIn( point_A_rond_name ), FadeIn( point_O_origine_name )
        )

        self.add( vecteur_directeur_name, line_name )
        self.wait(DURATION_TO_PROCESS_TIMELINE)


# ............................................................................. #
#
#                             VIDEO 3
#
# .............................................................................. #

class Equation_Parametrique_Line_3(ThreeDScene):
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
        #  
        ##############################
        # 3D variant of the Dot() object
        dot = Dot3D(radius=UNITAIRE_VECTOR_CIRCLE_RADIUS).set_fill(YELLOW).move_to(np.around(axes.coords_to_point(0, 0, 0), 2))
        
        #self.add_fixed_in_frame_mobjects( plane )

        # one dot for each direction
        #############################
        #  CIRCLE
        #############################
        upDot = dot.copy().set_color(MAROON_B)
        rightDot = dot.copy().set_color(BLUE)
        outDot = dot.copy().set_color(GREEN)

        if BACKGROUND_CHOSEN_COLOR == 'WHITE':  
            pass 
        
        if BACKGROUND_CHOSEN_COLOR == 'BLACK':
            pass
        
     

        #self.add( axes,   plane )
        group = VGroup(
            axes, 
            x_label, y_label, z_label
        )
        
        ###################################
        # LINE
        ###################################
        def func(t):
            pos = axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)
            return [
                pos[0] + dir1_x * t , 
                pos[1] + dir1_y * t, 
                pos[2] + dir1_z * t
            ]

        func = ParametricFunction(func, t_range = np.array([-0.3, 1.3]), fill_opacity=0).set_color(RED)
        start_pos = axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)
        next_pos = axes.coords_to_point( start_pos[0] + dir1_x, start_pos[1] + dir1_y, start_pos[2] + dir1_z)
        #next_pos = axes.coords_to_point(LINE_CHOSEN_POINT_X + dir1_x, LINE_CHOSEN_POINT_Y + dir1_y, LINE_CHOSEN_POINT_Z + dir1_z)
        vecteur_to_line = DashedVMobject(Arrow( 
            axes.get_origin() ,
            axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z)  
        ), num_dashes=12).set_color(TEAL_C)

        vecteur_directeur = Arrow( 
            start_pos ,
            (  start_pos[0] + 1.6*dir1_x,  start_pos[1] + 1.6*dir1_y,  start_pos[2] + 1.6*dir1_z ) ,
            color=YELLOW, tip_shape=ArrowTriangleTip,
            stroke_width=8, buff=0.25
        )

        myfont_size=130
        vecteur_directeur_name = MathTex("\\vec{u}", font_size=myfont_size, color=YELLOW).move_to( 0.5*(vecteur_directeur.get_end() + vecteur_directeur.get_start() ) + np.array([0, 1, 1]) )
        line_name = MathTex("( \\Delta )", font_size=int(0.5*myfont_size) , color=RED).move_to(vecteur_directeur.get_start() + np.array([-1, 3.1, -1]))
        point_A_rond = dot.copy().set_radius(dot.get_radius() + 2).set_color(TEAL_B).move_to(axes.coords_to_point(LINE_CHOSEN_POINT_X, LINE_CHOSEN_POINT_Y, LINE_CHOSEN_POINT_Z))
        point_A_rond_name = MathTex(r"\text{A}", font_size=myfont_size, color=WHITE).scale(0.4).move_to( axes.coords_to_point(0, 3.5, 0.9) )
        self.add(func.scale(3))

        vecteur_directeur_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        line_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        
        point_A_rond_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        #self.add_fixed_in_frame_mobjects(vecteur_directeur_name, line_name)
        point_O_origine_name = MathTex(r"\text{O}", font_size=myfont_size, color=YELLOW).scale(0.3).move_to( axes.coords_to_point(0, 0.1, -0.25) )
        point_O_origine_name.scale(2).rotate(-3*PI/2,axis=X_AXIS).rotate(PI/2, axis=Z_AXIS)
        
        self.play(
            FadeIn( group ),
            upDot.animate.shift(UP),
            rightDot.animate.shift(RIGHT),
            outDot.animate.shift(OUT),
            Write( vecteur_directeur ),
            FadeIn( point_A_rond ), FadeIn( point_A_rond_name ), FadeIn( point_O_origine_name )
        )

        myfont_size = 40
        application1 = MathTex("\\text{EXERCICE}", font_size=myfont_size, color=RED).move_to(9.96*RIGHT+2*UP)
        application2 = MathTex("\\text{Determiner  l'équation  paramétrique  de la droite }", font_size=myfont_size - 10, color=WHITE).next_to(application1, DOWN)
        application3 = MathTex("\\text{passant par les points }", "\\text{A(3,4,2)}", "\\text{ et de vecteur directeur }", font_size=myfont_size - 10, color=WHITE).next_to(application2, DOWN)
        application4 = MathTex( "\\vec{u}(1, -1, 1) }", font_size=myfont_size - 13, color=WHITE).next_to(application3, DOWN)

        application3.set_color_by_tex_to_color_map({
            "A(3,4,2)": YELLOW,
            "{u}": YELLOW
        })

        application4.set_color_by_tex_to_color_map({
            "(1, -1, 1)": YELLOW
        })
        
        group_exo = VGroup(application1, application2, application3,  application4 ).shift(0.5*LEFT)
        box = SurroundingRectangle(group_exo, color=YELLOW, buff=MED_LARGE_BUFF)
        exercice = VGroup(group_exo, box).scale(0.8)


        self.add_fixed_in_frame_mobjects( exercice )

        self.add( vecteur_to_line, vecteur_directeur_name, line_name )
        self.wait(DURATION_TO_PROCESS_TIMELINE)
