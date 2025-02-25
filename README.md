## Inspiration:

I have always been passionate about hockey and the thrill of competitive sports. This project was born out of my love for the game and a desire to create a challenging simulation where you can play against a dynamic AI opponent. The game leverages predictive modeling for the AI, allowing it to anticipate the puck’s trajectory and react in real time, making for an exciting and fast-paced match.

-------------------------


## Features
Real-Time Gameplay: Experience the fast-paced action of air hockey with continuously moving puck and responsive player controls.
Intelligent AI Opponent: The computer-controlled striker uses a predictive heuristic to anticipate and intercept the puck.
Score Tracking and Timer: Keep track of the scores and a countdown timer that limits the game to three minutes.
Dynamic Collision Handling: Realistic puck collisions with walls and strikers are handled using vector mathematics.
Optional Sound Effects: Basic sound generation enhances the immersive experience.

-------------------------

## Technologies Used
This project leverages a range of technologies to bring the Air Hockey simulation to life:

**Python 3:** The primary programming language used for implementing game logic and AI.
**Pygame:** A set of Python modules designed for writing video games; it handles graphics, input, and sound, providing a framework for building the game.
**NumPy:** Utilized for generating sound effects by creating and manipulating numerical arrays representing audio samples.
**Git & GitHub:** Version control tools used for managing the codebase and collaborating on the project.
**Predictive Modeling:** A heuristic-based approach used in the AI opponent to anticipate the puck’s movement and dynamically adjust its position.

-------------------------


### Prerequisites

Make sure Python 3 is installed on your system.

### Installing Pygame

#### Windows:

`   bashCopypy -m pip install pygame --user   `

#### Mac & Debian/Ubuntu/Mint:

`   bashCopysudo apt-get update && sudo apt-get install python3-pygame   `

#### Mac – Compiling from Source (if needed):

`bashCopybrew install mercurial `

`brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi  `

`python3 -m venv anenv  `

`source anenv/bin/activate  `

`pip install hg+http://bitbucket.org/pygame/pygame   `

_Note: If you encounter issues installing pygame on Mac using the first method, please refer to the building from source instructions above. Some Linux installations may require running pygame with Python 2 instead of Python 3._

Running the Game
----------------

1.  **Clone or Download the Repository:**Ensure that the following files are in the same directory:
    
    *   airHockey.py
        
    *   classes.py
        
    *   Image assets: table.png, puck.png, player.png, comp.png
        
    *   Font files: digital-7.ttf, TESLA.ttf
        
2.   `anenv/bin/activate `
    
3.   `python3 airHockey.py ` The game window will open. Use your mouse to control the player's striker and compete against the AI opponent!!
