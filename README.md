<h1 style="border:2px solid; text-align:center;color:blue">API_MATHS</h1>

<h4><p style="color:orange">DESCRIPTION:</p> This is boards application for maths vido course</h4>

<h4 style="color:orange">Arborescence</h4>
<div><img src="imgs/arborescence.png" /><br/>As you can see, i have symbolic link to link the created library ../SFE_SFML_IMGUI_LIBS/create_unique_library/libsfe_movie_bin.so<br/>We can notice that the rpositoy is compose of Python scipts[aka MANIM] directory, C++ scripts and Dockerfile</div>

<h4 style="color:orange">Why this arborecence ?</h4>
<ol>
<li>
	<h4>Dockerfile</h4>
	<span>Inside the Dockerfile, we load Manim docker image because to generate video mp4 with Manim python script, we will work inside dockr container. So make sure your docker engine has started.</span>
	<pre>load your docker manim image[If it does not yet exists]<br/>docker build . -t manim_image </pre>
	<pre>REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
manim_image   latest    b4e1b47b59a2   11 seconds ago   2.24GB</pre>
</li>
<li><h4>MANIM directory (python scripts to build mp4 vido)</h4></h4>
<ol><li>Create your manim scene. You have some exampleinside  python script:intros_videos.py - c1_eq_parametique_droite.py - c2_eq_paramerique_plan.py ...</br></br></li>
<li>Shell Script tu run python script inde container and generate mp4 video:
<pre>source run_manim_script my_manim_python_scene_file.py</pre>
example:<pre>source MANIM/run_manim_script.sh MANIM/c1_eq_parametrique_droite.py  OR    source run.sh MANIM_DIR/mypython_script.py </pre>
<div><img src="imgs/conteneur.png" /></div>
i you can see the script has three scenes, so i choose to run the first(aka 1).
<br/>The script run inside container and after i get the mp4 file with sharing volumes with the host, so i open it: <pre>open MANIM/media/videos/c1_eq_parametrique_droite/720p30/Equation_Parametrique_Line_1.mp4</pre>
<div><img src="imgs/mp4.png"/></div><br/>
</li>
<li>Save your mp4 files to DiskE
<pre>source run.sh save</pre><pre>

It will save the new generated scene, which lies inside shared directory called media 
(shared directory between host and docker, because here MANIM runs his script inside docker)
into DiskE and at the same time 
export the DiskE path (Exemple export VOLUME_VIDEOS_PHYSICS_PATH=/Volumes/DiskE/VIDEOS-Tle-Physics-mp4/dynamic/) into 
~/.bashrc file (because if we export simply, the variable will be lost after)

So, while running c++, it will load dynamically all mp4 files  from thate expoted variable.
No need to set manually , mp4 files names (as in old days)</pre>
</li>
<li>OTHERS OPTIONS
<pre>To build manim image[IF NOT YET EXISTS]source run.sh build</pre>

<pre>To stop and remove the container: source run.sh down</pre>
</li>
<li>USEFULL INFO: Paremetrage
<pre>Please, set these Macro used by the following class in board-ext-geometry.hpp
	#define EXTERN_BACKGROUND_CHOSEN_COLOR BLACK
	#define EXTERN_MENU_SHAPE_COLOR BLACK 
	#define EXTERN_SCREEN_STROKE_COLOR WHITE</pre>
	<pre>I remove Imgui from this API so , do not set IMGUI MACROS</pre>
</li>
</ol>
</li>
</ol>



### DOCUMENTATION AND USEFULS LINKS:
manim: https://docs.manim.community/en/stable/index.html

### HOW TO RUN THIS SOTWARE
````
-+- TEST MODE or REAL COURSE MODE (MACRO aka #define):

*=> To simply test a mp4 file : 
do not mount /Volume/DiskE, the script 
is so intelligent to detect it

*=> If you need real mode course, 
because the course mp4 file are inside /Volume/DiskE, simply mount the DiskE into your PC

------

*=> NUM_RENDER_WINDOWS: the macro which indicates the number of windows to open (default is 3), this macro is inside ONLY_BOARD/board-gpu.hpp 
````

```
>> THE MENU:

```
 Shortcuts: SFE-MOVIES-MENU
	.... Space - Play / pause 
	.... S - Stop 
	.... R - Reset 
	.... H - Hide / show user controls and mouse cursor
	.... F - Toggle fullscreen 
	.... I - Log media info and current state 
	.... Alt + V - Select next video stream 
	.... Alt + A - Select next audio stream 
	.... Alt + S - Select next subtitle stream 
	.... Alt + P - Music Volume + 
	.... Alt + M - Music Volume - 
    .... [No Shortcut for timeline]:simply click inside and move mouse cursor
```

######  DES LIENS UTILS:
###### [Physic-Maths] https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/

###### site Maths Myriam: https://www.annales2maths.com/e3c2-2019-2020/

###### https://docs.manim.community/en/stable/tutorials/quickstart.html#transforming-a-square-into-a-circle


###### https://azarzadavila-manim.readthedocs.io/en/latest/geometry.html#rectangle


###### class definition: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html

###### Youtube: https://www.youtube.com/watch?v=MOv6yN7b2aI&list=PLWOlLjdyZm2NQD1YZmEPB0dwbd0yKINAT&index=1

###### convert to gif 
https://www.zamzar.com/uploadComplete.php?session=5111fb3e3738c3a399ab6b6d77266e98&tcs=Z85

###### AnimatedGIFS: code source origin:
    https://github.com/SFML/SFML/wiki/Source:-Animated-GIF


###### Imgui-SFML: 
	https://github.com/SFML/imgui-sfml
