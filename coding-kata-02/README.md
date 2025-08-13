# Coding Kata 02

## Overview
The purpose of this coding kata is to develop proficiency in the tasks listed below. It assumes you have `git`, `python`, `docker`, and a code editor installed. 

## Covered Topics
* Create a repository in a Git-based version control system like GitHub
* Create a branch using GitHub's UI
* Clone and check out a branch using `git`
* Install dependencies into a virtual environment
* Write a CI pipeline in YAML
* Push changes from a local branch to a remote branch
* Write a simple Python script
* Format a Python script using a tool
* Lint a Python script for issues
* Conduct a static security scan
* Create and run Unit Tests on a Python script

## Step-by-Step

**Step 1.** Login to [GitHub](https://github.com/) and create a new repository.
* Set yourself as the owner
* Name it whatever you want
* Set the visibility to public
* Add a README
* Add a Python-based `.gitignore`
* Add an MIT license

**Step 2.** Within a Linux-based environment (e.g., Windows Subsystem for Linux), open a CLI-based shell. Next, clone your repository using `git`, change directories to it using `cd`, and then, checkout the branch you created using `git`. In the example below, `cyberphor` is a GitHub username while `peacefield` is the name of a repository.  You should also install any dependencies into a virtual environment
```bash
git clone https://github.com/cyberphor/peacefield
cd peacefield
git checkout -b vf/unittests
python -m venv .venv
pip install black pylint
```

Before moving on, verify you're on the correct branch by running the command below.
```bash
git branch
``` 

**Step 3.** Create a directory called `.github` that contains another directory called `workflows`. Then, create a file called `ci-pipeline.yml` under `.github/workflows`. Add the content below to the `ci-pipeline.yml` file.
```yaml
# Set the pipeline name.
name: Continuous Integration

# Set pipeline execution criteria.
on:
  push

# Define all jobs within the pipeline.
jobs:
  # Define the test job.
  formatting:
    name: formatting
    runs-on: ubuntu-latest
    steps:

      # Install Python.
      - name: python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      # Install Python dependencies.
      - name: pip
        run: python -m pip install black

      # Download the source code.
      - name: clone
        uses: actions/checkout@v4

      # Conduct a QA test.
      - name: black
        run: black --diff --color --check .

  linting:
    name: linting
    runs-on: ubuntu-latest
    steps:

      # Install Python.
      - name: python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      # Install Python dependencies.
      - name: pip
        run: python -m pip install pylint

      # Download the source code.
      - name: clone
        uses: actions/checkout@v4

      # Conduct a static linting.
      - name: pylint
        run: pylint --ignore=tests .

  # Define the unittest job.
  unittests:
    name: unittests
    runs-on: ubuntu-latest
    steps:

      # Install Python.
      - name: python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      # Download the source code.
      - name: clone
        uses: actions/checkout@v4

      # Conduct a QA test.
      - name: unittests
        run: python -m unittest

  # Define the pre-build-scan job.
  pre-build-scan:
    name: pre-build-scan
    needs: 
      - formatting
      - linting
      - unittests
    runs-on: ubuntu-latest
    container:
      image: semgrep/semgrep

    steps:
      # Download the source code.
      - name: clone
        uses: actions/checkout@v4
      
      # Conduct a SAST scan.
      - name: semgrep
        run: semgrep scan --config auto
```

**Step 4.** Commit the changes made to the local branch to the remote branch of your repository using the commands below. Review the pipeline results in the GitLab UI, but do not take action on them yet.
```bash
git add -A
git commit -m "Added a CI pipeline"
git push
```

**Step 5.** Open your code editor from within your current working directory (this should be the same folder as the repository you downloaded). Write a simple Python script called `main.py` that has functions that you can test indepdently of each other. Deliberately write some formatting and logical errors in your code for testing purposes.  Below is an example. 
```python
def function_one(num_one: int, num_two: int) -> int:
    """
    This function takes two numbers and returns their sum.
    """
    return num_one * num_two

def function_two(num_one, num_two):
    return num_one+num_two

def function_three(num_one: int, num_two: int) -> int:
    """This function generates the sum of two integers.

    Args:
        num_one (int): The first integer to sum.
        num_two (int): The second integer to sum.

    Raises:
        TypeError: If either num_one or num_two is not an integer.

    Returns:
        int: The sum of num_one and num_two.
    """
    if not isinstance(num_one, int):
        raise TypeError("num_one must be an integer")
    if not isinstance(num_two, int):
        raise TypeError("num_two must be an integer")
    return num_one + num_two
```

**Step 6.** Once you confirm your code (doesn't) work, commit the changes you've made and review the pipeline results in the GitLab UI. Note that three of the build steps will fail at this point. 
```bash
git add -A
git commit -m "Added a backend"
git push
```

**Step 7.** Fix your formatting issues in the python file using black.  Run the following in the terminal to auto-format your code.  You can usually also setup your IDE to do this for you.  Then, commit the changes you've made and review the pipeline results in the GitLab UI.
```bash
black main.py
```

**Step 8.** Fix your code quality issues, as discovered by pylint. You can run pylint locally again on the directory to see what the issues are. Then, commit the changes you've made and review the pipeline results in the GitLab UI. 
```bash
pylint --ignore=tests .
```

**Step 9.** Create your unittests.  Create a new folder called `tests`.  Inside of there, create two new files:  `__init__.py` and `test_main.py`.  Write unittests for your `main.py` inside of the `test_main.py` file that validate the correctness of those functions.  Once your unit tests are written, run the command below to run the unittests and verify the results.  Fix any logical or test errors.  Then, commit the changes you've made and review the pipeline results in the GitLab UI.
```bash
python -m unittest
```

```python
from main import *
import unittest

class TestMain(unittest.TestCase):
    def test_function_one(self):
        self.assertEqual(function_one(2, 3), 5)
        self.assertEqual(function_one(-1, 1), 0)
        self.assertEqual(function_one(0, 0), 0)

    def test_function_two(self):
        self.assertEqual(function_two(2, 3), 5)
        self.assertEqual(function_two(-1, 1), 0)
        self.assertEqual(function_two(0, 0), 0)

    def test_function_three(self):
        self.assertEqual(function_three(2, 3), 5)
        self.assertEqual(function_three(-1, 1), 0)
        self.assertEqual(function_three(0, 0), 0)
        with self.assertRaises(TypeError):
            function_three(2, "3")
        with self.assertRaises(TypeError):
            function_three("2", 3)
```

**Step 10.** Relax! Great job!
