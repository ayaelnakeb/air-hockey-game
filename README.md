# air -hockey-
Pygame module must be installed prior to running airHockey.py
Read the instructions below to install pygame.

--------------------------
    
Windows Installation :
	
	py -m pip install pygame --user

Mac & Debian/Ubuntu/Mint Installation:

	sudo apt-get update && sudo apt-get install python3-pygame

Mac Compiling from Source:

	brew install mercurial
	
	brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi
	python3.5 -m venv anenv
	. ./anenv/bin/activate
	pip install hg+http://bitbucket.org/pygame/pygame

*Note : If running into errors installing pygame on Mac with the first method, please refer to the buliding from source code method

**Note : Some installations of Linux may require running pygame code with Python2 instead of Python3 


Intro Air Hockey
-----------------

Description: 
-------------
This project is a simulation of the Air Hockey game. We have used the 
pygame module for the implementing this game. It has a striker for the 
player, a computer that runs on its own and a puck that is pursued by 
both the striker throughout the game. The objective of the game is to 
make as many goals as you can in three minutes. The one who scores the 
most wins!

Design: 
Classes: 

1. Class Background: 
	This class instantiates a background for the display. Here the back
	ground is the image of an air hockey table. 
	It has no methods 
2. Class Scores: 
	This class is designed to display scores on the hockey table 
	during a game. 
	Methods: 
	def scoreUpdate:
	this method updates the scores during the game
3. Class Timer: 
	this class keeps track of the time during the game. Eacj game 
	lasts for three minutes. It has an update method. 
4. Class Puck: 
	This is class that deals with puck of the game. It has all its 
	relevant variables like angles, speeds, scores instantiated in the 
	init function. 
	Methods: 
	def calcNewPos: 
		Caluclates the new position of the puck for every frame 
	def update: 
		this updates the position of the puck using the calcNewPos 
		method
		It also handles the odd movements of the puck when it 
		collides with the edges of the display. 
	def courtHalf: 
		This keeps track of which half of the court the puck is on
5. Class Player: 
	This class deals with the interaction of the player in the game. It 
	allows the player to move his striker with the aid of the mouse 
	controller. It also handles the collisions with puck. 
	Methods: 
	def start: 
		places the player in the correct half of the court 
	def moveMouse: 
		helps the player to use the mouse as a controller in the 
		game 
	def update: 
		updates the position of the player. It also handles the 
		odd parts like interaction with the walls and obstructing 
		movement into the computers half 
6. Class Comp: 
	This class deals with the interaction of the computer striker in the 
	game. The computer follows the movement of the puck and tries to 
	score in the on the player's half
 	Methods: 
	def start: 
		places the computer in the correct half of the court
	def calculateNewPos: 
		this method is the logic behind the computer method to 
		follow the puck. It uses basic trigometry. 
	def update: 
		this updates the position of the computer. It also handles the 
		odd interaction of the computer with the edges of the 
		screen 

Testing and Modfications needed:
-------------------------------
We have tried our code numerous times are there still are a lot of issues with the
collision between sprites. The collisions could be made more realistic using
physics momemtum laws. For now we have used basic trigonometry and vector math to
define the movement of the puck after collisions.


