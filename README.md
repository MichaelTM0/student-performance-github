# Student Performance Analyzer

A command-line Python tool that loads a class gradebook from a CSV file and analyzes student performance: individual averages, class rankings, subject averages, passing rates, and which students need extra help.

## Features

- **Student lookup**: view a student's grade in one subject or their overall average
- **Rankings**: list students from highest to lowest average, or lowest to highest
- **Class averages**: overall class average or the average for a single subject
- **Passing percentage**: share of students at or above the passing grade (70 by default)
- **Students needing help**: everyone below passing, with their averages
- **Save or exit**: save the gradebook to a new CSV, or quit without saving

## Requirements

- Python 3.6 or newer
- No external packages; it uses only Python's built-in `csv` module

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MichaelTM0/student-performance-analyzer.git
   cd student-performance-analyzer
   ```

2. Make sure a `students.csv` file is in the same folder (a sample is included).

3. Run the program:

   ```bash
   python students_performance.py
   ```

## CSV Format

The program expects a `students.csv` file with a header row and these columns:

```csv
name,math,science,english
Alice,92,88,95
Bob,65,70,58
Carla,78,82,74
Dev,55,60,62
```

If `students.csv` isn't found, the program starts with an empty gradebook.

## Usage

When the program starts, it shows a menu:

```
==================================================
1. Average grade
2. Highest student
3. Lowest student
4. Class average
5. Passing percentage
6. Students needing help
7. Save and exit
8. Exit without saving
Choose one of the eight available options (1-8):
```

Example output for option 2 (Highest student):

```
Students sorted by average, highest to lowest:
  Alice: 91.67
  Carla: 78.00
  Bob: 64.33
  Dev: 59.00
```

Example output for option 6 (Students needing help):

```
Students below passing who may need help:
  Bob: 64.33
  Dev: 59.00
```

## Configuration

Two constants at the top of `students_performance.py` control the program's settings:

```python
PASSING_GRADE = 70.0
SUBJECTS = ["math", "science", "english"]
```

To change the passing grade, edit `PASSING_GRADE`. To track another subject, add it to `SUBJECTS` and add a matching column to the CSV; averages adjust automatically.

## How It Works

- Each CSV row is loaded as a dictionary using `csv.DictReader`, with column headers as keys.
- A single helper function, `calculate_average()`, computes each student's average across all subjects, and every feature reuses it.
- Rankings use Python's built-in `sorted()` with `calculate_average` as the sort key.
- Saving writes the gradebook to `New_student.csv` with `csv.DictWriter`.

## Future Improvements

- Add, edit, and remove students from within the program
- Handle missing or invalid grades without crashing
- Letter grades (A–F) alongside numeric averages
- Export reports or charts of class performance

## What I Learned

- Working with CSV data as dictionaries (keys and values)
- Writing reusable helper functions instead of repeating logic (DRY)
- Sorting complex data with `sorted()` and a `key` function
- Using constants for program settings
- Debugging syntax, runtime, and logic errors

## Author

**Michael Murchie**

- GitHub: [@MichaelTM0](https://github.com/MichaelTM0)
- LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
