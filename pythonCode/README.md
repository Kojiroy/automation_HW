The code for this was written in Python using the pyads and opencv libraries. I tried using ADS on other languages like C# and C++, but I ended up sticking to Python because I wanted to use a camera in my example and I have the most experience doing so in Python. 

## Overview
The program uses a camera and detects if there was motion detected. If there was, the program sends a command to the PLC via ADS and turns on the ESTOP. The program keeps the ESTOP for 10 seconds, before making the PLC go into IDLE state, requiring a human to manually turn the controller back on via the HMI. By default, the UI shows the pressure and the state that the program is in.

For full transparency, the motion detection library was only slightly modified by me and was based on a github repo called Motion-Detection-OpenCV. I implemented the ADS communication and the state machine logic for the program.