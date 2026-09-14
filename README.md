# Python Examples

This repository contains Python example programs for learning and demonstrating core programming concepts. Most examples are based on topics from Tony Gaddis' *Starting Out with Python* and are organized by chapter. The repository also includes separate Jupyter notebooks for introductory **pandas** and **Matplotlib** examples.

## Repository Structure

```text
Python_Examples_BA/
├── Chapter_02/        # Variables, input/output, strings, formatting, basic math
├── Chapter_03/        # Decision structures and conditional expressions
├── Chapter_04/        # Loops, repetition, validation, and turtle graphics
├── Chapter_05/        # Functions, arguments, modules, random numbers, and math
├── Chapter_06/        # Files, records, CSV/JSON, and exception handling
├── Chapter_07/        # Lists, tuples, list processing, and charts
├── Chapter_08/        # Strings, slicing, tokenizing, validation, and CSV data
├── Chapter_09/        # Dictionaries, sets, comprehensions, JSON, and pickle
├── pd_examples/       # pandas examples in a Jupyter notebook
├── plt_examples/      # Matplotlib examples in a Jupyter notebook
├── requirements.txt   # Python package dependencies
└── README.md
```

The chapter folders contain small, focused Python scripts together with supporting data files where needed.

Examples include:

- `Chapter_02/simple_math.py`
- `Chapter_03/loan_qualifier.py`
- `Chapter_04/for_loop_with_break.py`
- `Chapter_05/args_kwargs.py`
- `Chapter_06/read_write_three_formats.py`
- `Chapter_07/bar_chart1.py`
- `Chapter_08/validate_password.py`
- `Chapter_09/dictionary_comprehension.py`

## Additional Examples

### pandas

The `pd_examples/` folder contains `pd_examples.ipynb`, an introductory pandas notebook covering topics such as:

- creating `Series` and `DataFrame` objects
- inspecting DataFrames with `info()`, `shape`, and `describe()`
- adding and selecting columns
- slicing, sorting, and filtering rows
- using `loc`, `iloc`, `isin()`, and `query()`
- calculating descriptive statistics
- grouping and aggregating data with `groupby()`
- reading and writing CSV, JSON, and Excel data
- creating simple plots from pandas DataFrames

The folder also contains generated example files such as `output.csv`, `output.json`, and `output.xlsx`.

### Matplotlib

The `plt_examples/` folder contains `plt_examples.ipynb`, which demonstrates common plotting techniques with Matplotlib, including:

- line plots
- multiple lines and legends
- axis labels, titles, and limits
- horizontal and vertical reference lines
- bar and horizontal bar charts
- histograms
- scatter plots
- pie charts
- plotting NumPy-generated data
- saving a figure to a file

The notebook includes `quad.png` as an example generated plot.

## Getting Started

### Requirements

Use a recent Python 3 version. The main third-party packages used by this repository are listed in `requirements.txt`:

- `matplotlib`
- `numpy`
- `pandas`

For the Jupyter notebooks, you also need a notebook environment such as Jupyter Notebook, JupyterLab, or an IDE with Jupyter support.

Some pandas Excel examples may additionally require `openpyxl`.

### Clone the Repository

```bash
git clone https://github.com/rtelesko/Python_Examples_BA.git
cd Python_Examples_BA
```

### Create a Virtual Environment

Creating a virtual environment is recommended:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If you want to run the notebooks from Jupyter and work with Excel files, you can also install:

```bash
python -m pip install jupyter openpyxl
```

## Running the Examples

Run a Python example from the repository root, for example:

```bash
python Chapter_02/simple_math.py
```

You can also change into a chapter folder first:

```bash
cd Chapter_02
python simple_math.py
```

For examples that read local `.txt`, `.csv`, `.json`, or `.dat` files, running the script from its chapter directory is often the simplest option because many examples use relative file paths.

To open a notebook with Jupyter Notebook:

```bash
jupyter notebook pd_examples/pd_examples.ipynb
```

or:

```bash
jupyter notebook plt_examples/plt_examples.ipynb
```

## Purpose

This repository is intended for:

- students learning Python programming fundamentals
- learners following along with chapter-based examples
- instructors looking for small teaching examples
- introductory practice with pandas and Matplotlib

The examples are intentionally small so that individual concepts can be run, inspected, and modified independently.

## Reference

- Tony Gaddis, *Starting Out with Python*, Pearson.

## Contributing

This repository is primarily intended for educational use. Improvements to comments, explanations, examples, or supporting material are welcome.

## License / Educational Use

The repository is intended for educational and personal use. Some example programs are based on or adapted from material associated with *Starting Out with Python* and are provided as learning examples.
