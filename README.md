# Cross River Problem - AI Solution

This project is a Python implementation of the classic **Cross River Puzzle** using **Depth-Limited Search (DLS)**. The goal is to safely transfer all characters across the river according to the puzzle rules.

## Characters
- Father
- Mother
- Son
- Daughter
- Police
- Thief

## Rules
1. Only certain characters can drive the boat: father, mother, police.
2. Son cannot stay with mother without father; daughter cannot stay with father without mother.
3. Thief cannot be alone with others without police.

## Features
- Depth-Limited Search (DLS) implementation.
- Generates all valid states and prevents invalid moves.
- Visualizes the path of transfers step by step.
- Shows characters on the boat and the sides of the river.
- Configurable maximum search depth.

## How to Run
```bash
python main.py
