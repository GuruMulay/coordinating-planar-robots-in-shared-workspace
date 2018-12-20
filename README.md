README:

$ python initialDisplay.py && octave kinematics_r1.m && octave kinematics_r2.m && python gui.py 

OR

1. python initialDisplay.py: 
	Draw a shape: rectangle or circle.
	This script will record the rectangle or circle and descretize it.

2. octave kinematics\_r1.m  and octave kinematics\_r2.m
	Performs inverse kinematics to find arm posistions and joint angles to weld the shapes using tooltips.

3. python gui.py
	Displays the simulated positions of robots' tooltips required for welding the shape.

## Warning:
There are many bugs and corner cases yet to be handled! Also, there is a huge scope for code reuse and code cleanup.

## Demos:

Click to watch demo 1:

[![Click to watch demo 1](/media/demo1_1.png)](https://youtu.be/n__4ONsruzI)


Click to watch demo 2:

[![Click to watch demo 2](/media/demo2_1.png)](https://youtu.be/Ocnn4p4AvOU)


Click to watch demo 3:

[![Click to watch demo 3](/media/demo3_1.png)](https://youtu.be/CooqHyeg5ms)
