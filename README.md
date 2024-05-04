## Overview
- Basic UI
    - The colored status textbox on the top left indicates what state the main loop is in. It can be in five possible states: IDLING, PUMPING, E_STOPPED, LEAK, and MALFUNC (short for malfunctioned). If the program gets into E_STOPPED, LEAK, or MALFUNC, the textbox should turn red. Else, the textbox should be green, indicating that things are nominal. 
    - If the user clicks on the E_STOP button on the top right, both the pump controllers and the pumps themselves would be forced off. The only way to re-enable the pumps is to click the reset button on its right. Once the reset button is clicked and the user verifies that things are nominal again, the program will go back to idle and wait for the user to start the pump controller again.
    - A leak, E-STOP, or broken pump status would make the pumps and their controllers shut down.
- General Page
    - The general page has all of the essential buttons and information that users will need for the majority of the time. The Start/Stop toggle switch will turn the controller on and off. This is there in case the user needs to disable the controller and  
- Analysis Page
    - Uses a historized symbol of nPressure so that we can keep track of the pressure over the past 10,000 seconds. This can be extended for real-world implementation. 
    - Pausing the trend graph will let you see the individual data points, and clicking the data points will tell you the pressure value and time it was captured (to the milliseconds).
To simulate the pump and pump sensor, I created a simple function block called FB_SimulatedIO, which increases the global variable "nPressure" by 0.01 if "bPump" is true and decreases it by 0.001 if it's false. There numbers are likely exaggerated from what would occur in real life, but this was done to test for edge cases more frequently. This does also mean that some of the safety features like leak detection and pump malfunctioning are untuned, but fine-tuned parameters for these features should be found through practice anyway.

Within the code, I purposely decentralized the pump controller from the pump relays because I wanted to make the code modular for various types of controllers. I hope I made this apparent with my implementation of both the simple pump controller and the PID pump controller.

## What I Did Well

## Challenges
The largest challenge for this assignment was the limitation of using a Desktop Windows computer. Although I have access to multiple computers, most of them run Linux and my daily driver has been a Macbook for the past year. I tried getting a virtual machine working on these computers, but it was very slow and hard to work with. Even when I borrowed a friend's Window's laptop, I couldn't get TwinCat running on the machine because it didn't have Hyper-V support since it was running Windows 11 Home Edition. Fortunately, I was able to get TwinCAT running natively on a Desktop computer, but this option didn't give me much time to work on the assignment because I'm on-campus for most of the week.

Another challenge was the learning curve for many of the widgets in TwinCAT. Some of the commonly used widgets would have tons of documentation online and work as expected on the first try, but other widgets were harder to integrate and debug. For example, I tried getting a line graph to monitor the pressure over time, but I couldn't get the data to display on the graph. I tried following different tutorials, reading the documentation, and messing around with different inputs to no avail. 

I also faced difficulties trying to get the HMI to update correctly. For instance, something that I spent a while on was making sure that the colors changed when an action happened. This turned out to be more difficult that I anticipated because there are many ways to set the background color of widgets, and I wanted to be as consistent in my implementation as possible. That's why I ended up using Themes and classNames for each of the primary colors, Javascript for reading and setting PLC variables to give me more flexibility, and structured language to change the colors of the widgets because the UI is intuitive and easy to use. Even with this approach, I still have some bugs like the Status Textbox starting out Red rather than green, which only changes to green after a reset.

## What I would do Differently
