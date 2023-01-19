# safe_cracker_puzzle_50_solver
brute forcing a puzzle a friend gifted me

## Background
A friend gifted me a safe cracker puzzle.

![image](https://user-images.githubusercontent.com/15304023/213350864-8a8a0c39-99c2-4612-b914-51bc3fbd5be7.png)
(image credit: Mathematica Stack Exchange https://i.stack.imgur.com/zgdCY.jpg)

It has 4 wheels that you can spin, controlling 9 wings of numbers. When you spin a wheel, it changes the visibility of numbers behind that wheel.

The goal of this puzzle is to spin the wheels such that each column individually sums up to 50.

## The plan
Simulate this puzzle in python, so that I can brute force it by checking every possible combination of wheel positions- until I find a solution.

## Outcome
Success!

![image](https://user-images.githubusercontent.com/15304023/213351569-e9feb5f9-95af-4b9d-8f15-0f0c721c78ff.png)
(photo I took of my solved puzzle)

Wasn't too bad to code. I could have done things cleaner using recursion or building a single function to spin the wheels, but I wanted to have fun with this and not go overboard on code design.

