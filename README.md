<h1 style="border:2px solid; text-align:center;color:blue">API_MATHS</h1>

<h4><p style="color:orange">DESCRIPTION:</p> This is boards application for maths video course</h4>

<h4 style="color:orange">Arborescence</h4>
<div><img src="imgs/arborescence.png" /><br/>As you can see, i have symbolic link to link the created library ../SFE_SFML_IMGUI_LIBS/create_unique_library/libsfe_movie_bin.so<br/>We can notice that the rpositoy is compose of Python scipts[aka MANIM] directory, C++ scripts and Dockerfile</div>

<h4 style="color:orange">Why this arborecence ?</h4>
<ol>
<!-- ........................... -->
<li>
	<h4>Dockerfile</h4>
	<span>Inside the Dockerfile, we load Manim docker image because to generate video mp4 with Manim python script, we will work inside dockr container. So make sure your docker engine has started.</span>
	<pre>load your docker manim image[If it does not yet exists]<br/>docker build . -t manim_image </pre>
	<pre>REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
manim_image   latest    b4e1b47b59a2   11 seconds ago   2.24GB</pre>
</li>
<!-- ........................... -->
<li><h4>MANIM directory (python scripts to build mp4 video)</h4></h4>
	<ol>
		<li style="border 1px solid">Create your manim scene. You have some example of manim  python script:intros_videos.py - c1_eq_parametique_droite.py - c2_eq_paramerique_plan.py ...</br></br>
		</li>
		<li style="border 1px solid">  Shell Script tu run python script inde container and generate mp4 video:
			<pre>source run_manim_script my_manim_python_scene_file.py</pre>
			example:<pre>source MANIM/run_manim_script.sh MANIM/c1_eq_parametrique_droite.py  OR    source run.sh MANIM_DIR/mypython_script.py </pre>
			<div><img src="imgs/conteneur.png" /></div>
			you can see the script has three scenes, so i choose to run the first(aka 1).
			<br/>The script run inside container and after i get the mp4 file with sharing volumes with the host (here host "media" directory), so i open it: <pre>open MANIM/media/videos/c1_eq_parametrique_droite/720p30/Equation_Parametrique_Line_1.mp4</pre>
			<div><img src="imgs/mp4.png"/></div><br/>
		</li>
		<li style="border 1px solid">Save your mp4 files to DiskE
			<pre>source run.sh save</pre><pre>
			It will save the new generated scene, which lies inside shared directory called media 
			(shared directory between host and docker, because here MANIM runs his script inside docker) into DiskE</pre>
		</li>
		<li style="border 1px solid">LETS'S RESUME ALL POSSIBLES MENUS<br/>
			<ol>
				<li>To Stop and remove manim current container[maths or physic or chemistry]Container<pre>source run.sh down</pre></li>
				<li>To build current manim image [for maths or physic or chemistry If it is not yet done]<pre>source run.sh build</pre></li>
				<li>To set symbolik link wih library[If it is not yet done]: SFE_SFML_IMGUI_LIBS/create_unique_library/libsfe_movie_bin.so <pre>source run.sh symlib OR source run.sh symlink_lib</pre></li>
				<li>To run your python script to generate mp4 video scene:<pre>source run.sh myscript.py</pre></li>
				<li>To save generated mp4 files to DiskE.Alog will show you where it has been saved<pre>source run.sh save</pre></li>
				<li>To set the symbolik link with ONLY_BOARD(because the API needs some class and methods from ONL_YBOARD)<pre>source run.sh symlink_ob OR source run.sh symb_ob</pre>ob stands for Only Board</li>
				<li>To run makefile: make re <pre>source run.sh make</pre></li>
				<li>To run make clean,fclean,re<pre>source run.sh makec</pre></li>
				<li>To clean and fclean with Makefile: make fclean && make clean<pre>source make clean</pre></li>
			</ol>
		</li>
		<li style="border 1px solid">HOW TO INEGRATE MP4 generated video to the API ? <br/>
			<ol>
				<li>DiskE Reperory where we have saved mp4 files according to topic(maths, physic,chemistry and school class level<br/>
					<ol>
						<li>
							<pre>
							[Command to list repositoris with absolute path]:<br/>find "$(readlink -f .)" -maxdepth 1 -mindepth 1 -type d | grep VIDEOS
							<pre></pre>
							+> +> +> /Volumes/DiskE/INTROS_OUTROS_VIDEOS
							<pre></pre>
							+> +> +> /Volumes/DiskE/MY_CHANELS_VIDEOS_ICONS
							<pre></pre>
							+> +> +> /Volumes/DiskE/ONLINE_VIDEOS
							<pre></pre>
							+> +> +> /Volumes/DiskE/QUICTIME-PLAYER-VIDEOS
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-1ere-Chemistry-mp4 [script option "save" will save chemistry class 1ere here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-1ere-Maths-mp4 [script option "save" will save Maths 1ere videos here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-1ere-Physic-mp4 [script option "save" will save Physic 1ere videos here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-Intro-mp4 [script option "save" will save videos intro here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-Tle-Chemistry-mp4 [script option "save" Chemistry for level Tle here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS-Tle-Maths-mp4 [script option "save" Maths for Terminal level here]
							<pre></pre>
							/+> +> +> Volumes/DiskE/VIDEOS-Tle-Physics-mp4 [script option "save" Physics for Tle here]
							<pre></pre>
							+> +> +> /Volumes/DiskE/VIDEOS_MONTAGE
							</pre>
						</li>
					</ol><br/></br>
				</li>
				<li><pre></pre></li>
				<li>[STEP 1] Go To ONLY_BOARD/board-ext-geometry.hpp, and set thos MACROS
					<pre>
						#define  MATHS_VIDEO_INDEX 0 //0:intro, 1: first viedo, 2: second video, ...5<br/>
						#define  PHYSICS_VIDEO_INDEX 1 //0:intro, 1: first viedo, 2: second video, ...5<br/>
						#define CHEMISTRY_VIDEO_INDEX 0 //0:intro, 1: first viedo, 2: second video, ...5<br/>
						#define PROGRAMMING_VIDEO_INDEX 0 //0:intro, 1: first viedo, 2: second video, ...5<br/>
						//#define CODING_VIDEO_INDEX 0 //0:intro, 1: first viedo, 2: second video, ...5<br/>
						#define  MATHS_MUSIC_INDEX 0  //[0, 1] because i have only two music
					</pre>
				</li>
					<li>[STEP 2] mount DiskE andG o to ONLY_BOARD/board-ext-geometry.cpp and add your videos to list <pre>const char *EXT_MP4_[MATHS|PHYSIC|CHEMISTRY|PROGRAMMING]_FILES_ARRAY_FROM___BOARD_EXT_GEOMETRY_CPP[]={ }</pre>
					<pre>You can also add your music in this array: <br/>const char *EXT_MP3_FILES_ARRAY[] =  { }</pre>
					<img src="imgs/mp4_arrays.png"/><br/>
					<img src="imgs/mp3_arrays.png"/><br/>
				</li>
				<li>[STEP 3]: Go to API_MATHS/main.cpp to instanciate your media files(video and/or  music)<br/>Your media files class can have three instance, so if 
					<ol>
						<li>
							You are working on maths domain(this is the default). So inside the API_MATHS/main.cpp instanciate your class
							<pre> ext::AnimatedSFE_MOVIES anim_movies;
		ext::AnimatedSFE_MOVIES mymusic = ext::AnimatedSFE_MOVIES(MATHS_MUSIC_INDEX);
							</pre>Feel free to instance more han one class if you have many mp4 videos to display inside differents boards<br/>
							so you will need to declare like:
							<pre>ext::AnimatedSFE_MOVIES anim_movies1,anim_movies2;</pre>
						</li>
						<li>
							You're working on Physics, so set your media files like that
							<pre>ext::AnimatedSFE_MOVIES anim_movies("physic");
		ext::AnimatedSFE_MOVIES mymusic = ext::AnimatedSFE_MOVIES(MATHS_MUSIC_INDEX);</pre>Feel free to instance more han one class if you have many mp4 videos to display inside differents boards</br>so you will need to declare like:
							<pre>ext::AnimatedSFE_MOVIES anim_movies1("physic",0),anim_movies2("physic",1);<br/>the first argument is the domain, and the second is the mp4_files index from your mp4 files array:EXT_MP4_[MATHS|PHYSIC|CHEMISTRY|PROGRAMMING]_FILES_ARRAY_FROM___BOARD_EXT_GEOMETRY_CPP[] you fill from ONLY_BOARD/board-ext-geometry.cpp</pre>
						</li>
						<li>
							You're working on Chemistry, so set your media files like that
							<pre>ext::AnimatedSFE_MOVIES anim_movies("chemistry");
		ext::AnimatedSFE_MOVIES mymusic = ext::AnimatedSFE_MOVIES(MATHS_MUSIC_INDEX);</pre>Feel free to instance more han one class if you have many mp4 videos to display inside differents boards</br>so you will need to declare like:
							<pre>ext::AnimatedSFE_MOVIES anim_movies1("chemistry",0),anim_movies2("chemistry",1);<br/>the first argument is the domain, and the second is the mp4_files index from your mp4 files array:EXT_MP4_[MATHS|PHYSIC|CHEMISTRY|PROGRAMMING]_FILES_ARRAY_FROM___BOARD_EXT_GEOMETRY_CPP[] you fill from ONLY_BOARD/board-ext-geometry.cpp</pre>
						</li>
						<li>
							You're working on Programming, so set your media files like that
							<pre>ext::AnimatedSFE_MOVIES anim_movies("programming");
		ext::AnimatedSFE_MOVIES mymusic = ext::AnimatedSFE_MOVIES(MATHS_MUSIC_INDEX);</pre>Feel free to instance more han one class if you have many mp4 videos to display inside differents boards</br>so you will need to declare like:
							<pre>ext::AnimatedSFE_MOVIES anim_movies1("programming",0),anim_movies2("programming",1);<br/>the first argument is the domain, and the second is the mp4_files index from your mp4 files array:EXT_MP4_[MATHS|PHYSIC|CHEMISTRY|PROGRAMMING]_FILES_ARRAY_FROM___BOARD_EXT_GEOMETRY_CPP[] you fill from ONLY_BOARD/board-ext-geometry.cpp</pre>
						</li>
					</ol>
				</li>
			</ol>
		</li>
		<li style="border 1px solid">USEFULL INFO: Paremetrage
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
