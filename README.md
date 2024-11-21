# SOKOBAN-like game with Procedural Content Generation

The game was implemented using Python3, with the Python library **arcade**.

The intent is to procedurally generate Sokoban levels using artificial agents.

This project was initially developed as the final project developed under the discipline 
**MAC5784 - Artificial Intelligence in Computer Games (2024)**, ministered by professor Flavio Soares Correa da Silva and
professor Ricardo Nakamura at the University of São Paulo (IME - USP).

## Player Mechanics
* Move UP, DOWN, LEFT, or RIGHT using W, S, A, D, or keyboard directionals
* Press R to redo the last movement
* Press ESC to reset the current level

## Artificial Agents
Agents are anything that perceives its **Environment** through **Sensors** and acts in the environment by **Actuators** [1]

The description of two categories of artificial agents and their implementation in this project are shown below.
### Purely Rational Agent
An Agent in this category has a single objective and acts alone (without more agents).
The agent simply follows the definition of artificial agents, sensing the environment and acting on it.

This project uses a Solver, in which it "walks" in a level and tests if it has a valid solution.
Its objective is to solve the level, given a limit of movements. The environment is the Level and its characteristics.

It also returns the set of movements to solve the tested level.

### Social Agents
Social agents has more than one objective, and involves two or more agents in the environment interacting with each other.

The project implements two social agents:
* Constructor: Agent that moves in the environment and interacts constructing impassable blocks and boxes.
* Destructor: Agent that moves in the environment, interacts destructing impassable blocks or boxed, and adds goal blocks.

Both agents are influenced by the game **Difficulty**, which is adjusted by player interactions and completion time 
of the last completed level.

Each agent's action has a **Chance** to occur. The chance is calculated using a **Genetic Algorithm**, in which calculate
individual's fitness, considering the number of blocks and whether the level is completable (using the Solver).

## Game Narrative
The game intends to be an Educational Game focused on raising awareness about sustainable consumption, related to goal 12
of the UN's 17 Goals of Sustainable Development [2].

Given the game's scope, it is only possible to address some goal targets. So, the project focuses on the Target 12.5 [3]:
* By 2030, substantially reduce waste generation through prevention, reduction, recycling, and reuse

The player's objective is to clean all the trash in the city and recycle it.
The narrative is drawn from the visual art of game elements and the player's interactions with the environment.

## Limitations
This project is ongoing and needs to address several limitations for its completion.

### Content Limitations
At this moment, the procedurally generated levels lack complexity and reliability. Most levels have fewer blocks than intended for the environment's size and difficulty.

Some procedural generator parameters need to be adjusted, as well as constants related to the number of interactions in the genetic algorithm and evaluation weights. 

All of these elements consider and relate to the time spent generating a level, which is a technical limitation that needs to be addressed.

### Narrative Limitations
The game lacks UI. It has no menu, mechanics tutorial, points, etc.

As a serious game, the game lacks elements of the serious intent to raise awareness about sustainable consumption.

It is planned to be implemented Lore Items or Collectibles for the user to read about the game's intentions related to
the ONU Sustainable Development Goals. 
Additionally, it is planned to add an animation of the Social Agents developing the level and talking with each other and
with the users.

### Technical Limitations
The project needs better programming practices. This issue is mainly due to the latest commits, which were less carefully developed due to the project's deadline.
These problems relate to commented code, code duplication, and different levels of code abstraction in the same method.

Another problem is the time spent to procedurally generate a new level. The generation uses the Solver to test levels
playability, which its process falls on the curse of dimensionality. 
Additionally, fitness calculation involves generating a level and testing its playability, causing significant delays.

## Credits and References

[1] - Russell, Stuart J. (Stuart Jonathan), 1962-. Artificial Intelligence : a Modern Approach. Upper Saddle River, N.J. :Prentice Hall, 2010.

[2] - https://sdgs.un.org/goals

[3] - https://sdgs.un.org/goals/goal12

"Littered Dungeon" by Tianmaru licensed CC0:<br>
https://opengameart.org/content/littered-dungeon

"Recycle Items Set" by Clint Bellanger licensed CC-BY 3.0, OGA-BY 3.0:<br>
https://opengameart.org/content/recycle-items-set
