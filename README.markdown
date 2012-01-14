Subdivision Toy
===============

A little subdivision toy using python. By clicking on a square, you can subdivide it. By subdividing many, you can create pictures (no this is not trying to compete with a real painting package).

I just happen to like the way these look, and think that interesting things can be done with it - like render out the tree as a tree too, and compare them, use subdivision to analyse an image (ooh look, computer vision stuff). Right now - it just creates these images.

Requirements
------------
Python - 2.7+
Pygame

Usage
-----
Grab this source, then run python pygame_subdiv.py. You can start it with a single file parameter to load a saved file - two such file are provided as examples. Yes they are large - they are python pickles of the object tree without any optimisation. Feel free to send me a push request with improvements (please do resave/convert the sample files if you do).

Left click divides a square, middle button undivides it (watch out - this could undo many levels of work).
Keys (work in the window, not the console):
s - save the current tree - either as the file provided as an argument when it started, or the default test.tree (feel free to add a real file dialog for saving Loading).
l - load a tree (using the default filename - test.tree)
c - Clear the current tree to start again
q - quit - the same as closing the window

There are no unit tests for it, it is really just a bit of play. Have fun with it.

Note - the width/height is set to a power of 2. It doesn't have to be, but rounding errors will start to make gaps at the edges. I have experimented with using the python Decimal module and other techniques for floating point (simple doubles will still have enough error that you'd see it), but sticking to powers of 2 will work and keep it clear - each subdivision is a division by two.

I like the way the code to find the right square for the mouse pointer works. I am not so keen on the render square generation. I am sure there are may improvements that can be made to it.

License
-------
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Subdivision Toy</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Danny Staple</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
This program is free software. It comes without any warranty, to the extent permitted by applicable law.
