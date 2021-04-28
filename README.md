##Description
This was a quick project to show some code to my 7yo child and also play with some math with him.

It is intended to calculate days and hours from birthdate to current date (though in practice it could be any two dates).
Of course the code could me much shorter for that with proper libraries, but the goal was to write the code with the child (_watching_) to solve the calculation. It assumes both dates at 0:00 hour to simplify input.

Leap years are not 100% correctly accounted for. The code defines any year divisible by 4 as a leap year, but in reality it should exclude the ones divisible by 100 but not by 400 (so 1700, 1800, 1900, 2100...). As long as both dates are between two of those exceptions, the code works - which is good enough considering how close we are to midway between 1900 and 2100. Note that 2000 was a leap year since it is divisible by 400.

In my other repos there is similar code developed in C for a University exercise.
