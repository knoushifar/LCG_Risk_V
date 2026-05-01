# LCG Risk Visualization / Linear Congruential Generator

This project implements a simple **Linear Congruential Generator (LCG)** in Python.

An LCG is a pseudo-random number generator based on the recurrence relation:

```
X(n+1) = (aX(n) + c) mod m
```

Where:

* `m` is the modulus
* `a` is the multiplier
* `c` is the increment
* `X0` is the seed value

---

## Features

* Clean implementation of an infinite LCG generator
* Example usage through `main.py`
* Basic input validation
* Simple and beginner-friendly Python structure
* Fully implemented in RISC-V assembly through 'LCG.s'
* Suitable for learning pseudo-random number generation

---

## Project Structure

```
LCG_Risk_V/
├── main.py
├── lcg.py
├── README.md
├──LCG.s
└── .gitignore
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/LCG_Risk_V.git
cd LCG_Risk_V
```

Run the program:

```bash
python main.py
```

---

## Example Output

```
Linear Congruential Generator Output:
----------------------------------------
01: 11
02: 12
03: 2
04: 0
...
```

---

## Why This Project Matters

This project demonstrates understanding of:

* Python generators
* Hands-on low-level programming
* Mathematical recurrence relations
* Pseudo-random number generation
* Clean code organization
* Basic software documentation

---

## Future Improvements

Possible improvements include:

* Adding command-line arguments
* Visualizing the generated sequence
* Detecting repetition cycles
* Comparing different LCG parameter choices
* Adding unit tests with `pytest`

---
