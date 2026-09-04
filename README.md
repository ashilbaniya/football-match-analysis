
# Football Match Analysis

This project is an assistive path for people who do not know much about football and are enthusiastic about learning it. It analyzes the different movements going around the pitch and interprets it so that the viewers can understand it properly without any confusion.


## Features

- Player Detection and Tracking - Tracks unique players and where they are on the pitch
- Ball Detection and Tracking - Tracks where the football is and its trajectory
- Referee Detection - Can differ referee from players
- Team Detection - Can differ between teams
- Player Speed and their Distance Covered - It estimates the player speed and calculates their whole distance covered throughout the clip


## Technologies Used

YOLO - For detecting objects

OpenCV - For processing videos and images

Python - For primary coding


## Demonstration


https://github.com/user-attachments/assets/b6c19e9b-dede-4aca-a606-2a9e4840ee38


## How to Run the Program

Python must be installed in your program.

Third party modules (as in requirements.txt) should be installed in a Python Virtual Environment.

Code Editors such as Virtual Studio Code (or the terminal) must be used to run the code.

Path of a football video should be given as input in the terminal as a command line argument.

You also need to provide the file path to where you want to save the output as a command line argument.

>Here's an example:

- Open up a Code editor or a terminal and go to the directory where the **project.py** file and its relevant modules are.

- Then in the command line, type 'python project.py -r **input_file_name** -w **output_file_name**'

- This will enable the program to take **input_file_name** as an input for detection and analysis.

- The AI model will then predict the players, their movements, and ball acquisition and save the results in **output_file_name**.

- The results can be seen in output_videos/**output_file_name**.

- You can type 'python project.py -h' for more information.


## Credits & References

- Tutorial: [Football Analysis with Python, YOLO and OpenCV](https://www.youtube.com/watch?v=neBZ6huolkg) — by [Code In a Jiffy](https://www.youtube.com/@codeinajiffy). Thank you Jiffy!
- Dataset used to train the yolov5mu model: [From Roboflow](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1)
- Thank you everyone in our Group (Group-A) for making this project successful!
