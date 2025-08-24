# Coding Kata 02

## Overview
The purpose of this coding kata is to develop proficiency in the tasks listed below. It assumes you have `git`, `python`, and a code editor installed. 

## Covered Topics
* Create a repository in a Git-based version control system like GitHub
* Create a branch using GitHub's UI
* Clone and check out a branch using `git`
* Install dependencies into a virtual environment
* Write a simple Python script
* Use pre-commit hooks to validate code quality before committing

## Step-by-Step

**Step 1.** Login to [GitHub](https://github.com/) and create a new repository.
* Set yourself as the owner
* Name it whatever you want
* Set the visibility to public
* Add a README
* Add a Python-based `.gitignore`
* Add an MIT license

**Step 2.** Within a Linux-based environment (e.g., Windows Subsystem for Linux), open a CLI-based shell. Next, clone your repository using `git`, change directories to it using `cd`, and then, checkout the branch you created using `git`. In the example below, `cyberphor` is a GitHub username while `peacefield` is the name of a repository.  You should also install any dependencies into a virtual environment.

```bash
git clone https://github.com/cyberphor/peacefield
cd peacefield
git checkout -b vf/unittests
python -m venv .venv
pip install black pylint precommit
```

Before moving on, verify you're on the correct branch by running the command below.
```bash
git branch
``` 

**Step 3.** Open your code editor from within your current working directory (this should be the same folder as the repository you downloaded). Write a simple Python script called `main.py` that has functions that you can test indepdently of each other. Deliberately write some formatting and logical errors in your code for testing purposes.  Below is an example. 
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

**Step 4.**
Pre-commit hooks allow us to validate that our code will pass specific tests prior to committing our changes into the repository.  This helps keep our commit history clean and avoids the commit messages like "fixes linter errors" or "code quality fixes".  Create a new file called `.pre-commit-config.yaml` that has the content below.  This file will dictate how which pre-commit hooks are run.

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/pylint
    rev: v3.2.3
    hooks:
      - id: pylint
```

Inspect the yaml file.  Which current tools are we using as our pre-commit hooks?

**Step 5.**
Install and run the pre-commit hooks using the following commands.  Note that anytime the pre-commit file changes, the new packages need to be installed.  You can then do a manual test by running the second command.

```bash
pre-commit install
pre-commit run --all-files
```

Inspect the output.  What do you notice about the tests?  Did any of them pass or fail?  Try running the pre-commit hooks again.  Did `black` pass the second time?  What about pylint?  Do not fix the pylint errors yet.

**Step 6.** Try making a commit.  Notice that the pre-commit hooks run and pylint should fail again.  Now try fixing the pylint errors and then committing.  Did the commit work this time?
```bash
git add -A
git commit -m "Added a backend"
```

This is just a small sample of pre-commit hooks.  Try finding a pre-commit hook that does static security analysis or fixes `import` statement ordering and adding that to your pre-commit config.  Remember to install the hooks after updating the config.

**Step 7.** Relax! Great job!
