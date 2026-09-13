# Sequence Alignment Tool


## <img width="978" height="729" alt="Capture 2" src="https://github.com/user-attachments/assets/bc0d98c5-0f61-41ba-ba7e-def7c1f4fb4a" />
 How to Run

 <img width="402" height="566" alt="Capture2" src="https://github.com/user-attachments/assets/67d13d54-48bc-4f38-9fcf-a86ee70cf45c" />

A simple Python-based tool for comparing two DNA sequences using two popular sequence alignment algorithms.

I built this project to understand how **pairwise sequence alignment and dynamic programming** work in bioinformatics.

##  What can it do?

You can:

* Enter two DNA sequences
* Choose between **Global** and **Local alignment**
* Set your own match, mismatch and gap scores
* See the final alignment
* Get alignment statistics
* View the scoring matrix as a heatmap 📊

## Algorithms Used

### 1. Needleman-Wunsch

Used for **global alignment**, meaning it tries to align the sequences from beginning to end.

### 2. Smith-Waterman

Used for **local alignment**, meaning it looks for the best matching region between the sequences.

##  Example

For example, the tool can compare:

```text
Sequence 1: GTCAGATCA
Sequence 2: GT-AG--CA
```

and give results such as:

```text
Alignment score: 12

Alignment Statistics:
Alignment length : 9
Matches          : 6
Mismatches       : 0
Gaps             : 3
Identity         : 66.67%
```

It also generates a **scoring matrix heatmap** so the alignment process can be visualized.

##  Built With

* Python
* Dynamic Programming
* Matplotlib

## Project Structure

```text
sequence_alignment_tool/
│
├── main.py
├── alignment.py
├── alignment_stats.py
├── visualization.py
├── requirements.txt
└── README.md
```


First install the required libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

Follow the instructions shown in the terminal.

## 🎯 Why I Made This

This is one of my bioinformatics projects while learning **computational biology and programming**. I wanted to understand what actually happens behind sequence alignment tools instead of only using ready-made tools.

More projects coming soon! 🧬💻

