# Red-Nosed Reports

This repository contains a solution for **Day 2: Red-Nosed Reports** from Advent of Code 2024.

## 📋 About the Problem

The challenge involves analyzing security reports (lists of numbers) and determining which ones are considered "safe". A report is safe if it meets one of the following criteria:

- **Strictly increasing** OR **strictly decreasing**
- The differences between consecutive numbers must be in the range of **1 to 3** (in absolute value)

## 🛠️ Solution

The Python code (`orange_test.py`) implements the following operations:

1. **Data reading**: Reads the `data.txt` file containing the reports
2. **Safety analysis**: For each report, checks if it's strictly increasing or decreasing and if differences between consecutive numbers are within the allowed range
3. **Counting**: Counts how many reports are considered safe

## 📊 Result

The solution found **631 safe reports** in the provided data.

## 🚀 How to Use

```bash
python main.py
```
