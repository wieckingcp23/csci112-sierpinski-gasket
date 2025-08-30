# Gasket

**Type:** Course Work  
**Institution:** Randolph-Macon College  
**Course:** CSCI 112 Data Structures  
**Date:** 3 May 2019  
**Grade:** 40/40

---

## Description
Recursive implementation of the Sierpiński gasket (triangle) rendered using the EzGraphics package.

This repository contains my final lab submission for CSCI 112. It demonstrates recursion and simple graphical rendering.

---

## Prerequisite: EzGraphics

This project depends on the EzGraphics package, which is not included here.

Download and instructions: https://www.ezgraphics.org/Software/Download

Install after downloading `ezgraphics-2.2.tar.gz`:

**Linux**
```bash
python3 -m pip install ~/Downloads/ezgraphics-2.2.tar.gz
# or
pip3 install ~/Downloads/ezgraphics-2.2.tar.gz
```
**macOS**
```bash
python3 -m pip install ~/Downloads/ezgraphics-2.2.tar.gz
# If using Anaconda:
~/anaconda/bin/pip3 install ~/Downloads/ezgraphics-2.2.tar.gz
```
**Windows (PowerShell)**
```powershell
Copy code
py -m pip install "$env:USERPROFILE\Downloads\ezgraphics-2.2.tar.gz"
# If using Anaconda:
C:\Anaconda3\Scripts\pip3 install "$env:USERPROFILE\Downloads\ezgraphics-2.2.tar.gz"
```
**Tip: Do not commit EzGraphics files to this repository.**

## Requirements
- Python 3.x
- EzGraphics installed system-wide (see above)

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/wieckingcp23/gasket.git
cd gasket
```
2. Ensure EzGraphics is installed as shown above.
3. Run:
```bash
Copy code
python gasket.py
```
### Example Output
Running the program draws a Sierpiński gasket as a recursive triangular fractal.

## Repository Contents
- gasket.py — Recursive Sierpiński gasket program
- README.md — This document

## Notes
- This project was completed as an academic exercise and is not actively maintained.
- EzGraphics is third-party course material. It remains the property of its respective copyright holder.

### Academic Use Disclaimer
This repository is an archived academic project completed as part of coursework at [Randolph-Macon College](http://catalog.rmc.edu/academic-regulations/academic-integrity/).  
It is provided **for portfolio and reference purposes only**.  

If you are a current student, do not copy or submit this work as your own.  
Course assignments may have changed since this project was completed, and instructors actively use plagiarism detection tools.  

I encourage you to use this repository only as a learning reference.
---