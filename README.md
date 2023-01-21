# safe_cracker_puzzle_50_solver
brute forcing a puzzle a friend gifted me

## Background
A friend gifted me a safe cracker puzzle.

![image](https://user-images.githubusercontent.com/15304023/213882297-de624e22-b9e0-4de4-8a4e-7827a98239b9.png)

It has 4 wheels that you can spin, controlling 9 rings of numbers. When you spin a wheel, it spins 2 rings of numbers (or only 1 in the case of the top wheel), and also changes the visibility of numbers on the ring behind that wheel.

The goal of this puzzle is to spin the wheels such that each column individually sums up to 50.

## The plan
Simulate this puzzle in python, so that I can brute force it by checking every possible combination of wheel positions- until I find a solution.

## Outcome
Success!

![image](https://user-images.githubusercontent.com/15304023/213351947-8c8600a2-092c-4a7b-b3d1-635cb10e1cf4.png)
(photo I took of my solved puzzle)

Wasn't too bad to code. I could have done things cleaner using recursion or building a single function to spin the wheels, but I wanted to have fun with this and not go overboard on code design.

