# HackerRank 3rd Semester Portfolio

## Introduction

This repository contains beginner-friendly Python solutions to five HackerRank
programming problems as part of a 3rd Semester programming portfolio. Each
solution includes the HackerRank function and a standalone command-line
program that reads input from standard input.

- **Programming language:** Python 3
- **HackerRank profile:** [Add your HackerRank Profile URL]

## Repository structure

```text
HackerRank-3rdSem-Portfolio/
├── Diagonal-Difference/
│   └── solution.py
├── Dynamic-Array/
│   └── solution.py
├── Time-Conversion/
│   └── solution.py
├── Compare-the-Triplets/
│   └── solution.py
├── Sparse-Arrays/
│   └── solution.py
└── README.md
```

## Problem summary

| Problem | Main topic | Time complexity | Auxiliary space complexity |
|---|---|---:|---:|
| Diagonal Difference | Matrices and diagonal traversal | O(N) | O(1) |
| Dynamic Array | Lists, XOR, and query processing | Expected O(Q) | O(N + Q) |
| Time Conversion | String processing and conditionals | O(1) | O(1) |
| Compare the Triplets | Lists and element-wise comparison | O(1) | O(1) |
| Sparse Arrays | Dictionaries and frequency counting | Expected O(N + Q) | O(N + Q) |

For Dynamic Array, the auxiliary space includes the sequences and returned
answers. For Sparse Arrays, it includes the frequency dictionary and returned
answers.

## Algorithmic concepts

- **Diagonal Difference:** Traverse the square matrix once, accumulating its
  primary and secondary diagonal sums, then return their absolute difference.
- **Dynamic Array:** Store values in one of `N` lists. XOR `x` with the last
  answer to select a list; type-2 queries also record the selected value.
- **Time Conversion:** Handle the special `12 AM` and `12 PM` cases, adjust
  other PM hours, and preserve the minutes and seconds.
- **Compare the Triplets:** Compare corresponding scores and increment the
  score of whoever has the larger value.
- **Sparse Arrays:** Count each input string in a dictionary and look up the
  frequency of every query.

## Run a solution

Run commands from the repository root with Python 3 installed. Each program
accepts input in the corresponding HackerRank format.

```powershell
python .\Diagonal-Difference\solution.py
python .\Dynamic-Array\solution.py
python .\Time-Conversion\solution.py
python .\Compare-the-Triplets\solution.py
python .\Sparse-Arrays\solution.py
```

Enter or pipe the problem's input after starting a command. For example:

```powershell
@"
3
11 2 4
4 5 6
10 8 -12
"@ | python .\Diagonal-Difference\solution.py
```

## HackerRank accepted submission screenshots

Add screenshots of accepted HackerRank submissions here when available.

- [ ] Diagonal Difference: `screenshots/diagonal-difference-accepted.png` (add later)
- [ ] Dynamic Array: `screenshots/dynamic-array-accepted.png` (add later)
- [ ] Time Conversion: `screenshots/time-conversion-accepted.png` (add later)
- [ ] Compare the Triplets: `screenshots/compare-the-triplets-accepted.png` (add later)
- [ ] Sparse Arrays: `screenshots/sparse-arrays-accepted.png` (add later)

No submission screenshots are included yet.

## HackerRank skill badge screenshots

Add genuine HackerRank skill badge screenshots here when available.

- [ ] Skill badge screenshot: `screenshots/hackerrank-skill-badge.png` (add later)

No skill badge screenshots or achievements are claimed here.

## Portfolio target

The target for this portfolio is to earn a minimum **3-star HackerRank
badge**. This is a goal, not a claim that the badge has already been earned.
