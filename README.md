# Driving-using-motion-recogniton

[Paper](https://ieeexplore.ieee.org/document/9063804) about the project.

Youtube video of project:

<https://youtu.be/F8jHWu5fUM0>

<b>Program to drive cars in games like GTA V using motion recognition.</b>

<b>Formulation:</b>

Calculate slope between centers of fists, if negative : turn-right else turn left.

Calculate distance between centres of fists and convert to speed. If distance is zero, apply brake.

<img src="https://github.com/TanayKarve/Driving-using-motion-recogniton/blob/master/hands.jpg" width=300 height=250>


Patent pending.

TODO: Implement hand localisation using Faster RCNN for accurate and robust results.


Used Pyvjoy for joystick interface and UCR for XBOX 360 controller emulation.

<b>External libraries</b>

Pyvjoy: <https://github.com/tidzo/pyvjoy>

UCR: <https://autohotkey.com/boards/viewtopic.php?t=12249>
