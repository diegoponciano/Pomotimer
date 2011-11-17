The project
=============

Pomotimer is a simple project I put together to learn python and Qt. I decided to use pyside for the Qt bindings.


Contributing
--------------

If you want to contribute, just fork it away =)
If you have any ideas on what to add/improve, or want to request some feature, just open an Issue, I'll be glad to discuss it.
Just so you know, I'm a python noob, the code may not look very 'pythonic', but I'm totally open to criticism.


ToDo-s
--------------

Although it started as a experimental project, I have plans to have it fully and beautifully working (and package it for distribution for the main desktop OSes) =)
Amongst the few things lacking, there are:

* Short (5 min.) and long (15 min.) pauses when a pomodoro finishes
* A ring-bell sound when a pomodoro finishes
* Options to change these timings
* Integration with desktop notifications
* Option to configure a ticking sound
* Etc (I'll keep adding as I remember/discover)

I'm planning to add some of these things before packaging a public distribution.


Testing
--------------

To run the tests, from the root of the project:

    $ python test/test_suite.py

As I stated, I'm a noob, some of the tests are not passing, and I have some difficult in testing other things, don't know if they are necessary, and if they are, how to test them =/.
