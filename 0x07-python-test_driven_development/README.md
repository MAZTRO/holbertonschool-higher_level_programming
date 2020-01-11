# Test-driven development.
## Project 0x07. Python
Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved so that the tests pass. This is opposed to software development that allows software to be added that is not proven to meet requirements.

#### Some info that you need to consider:
 - Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
 - The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
 - We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
 - Don’t trust the user, always think about all possible edge cases

## Learning Objectives.
 - What’s an interactive test
 - Why tests are important
 - How to write Docstrings to create tests
 - How to write documentation for each module and function
 - What are the basic option flags to create tests
 - How to find edge cases

## Requirements.
#### Python Scripts:
 - All your files should end with a new line
 - The first line of all your files should be exactly #!/usr/bin/python3
 - A README.md file, at the root of the folder of the project, is mandatory
 - Your code should use the PEP 8 style (version 1.7.*)
 - All your files must be executable
 - The length of your files will be tested using wc

#### Python Test Cases:
 - All your files should end with a new line
 - All your test files should be inside a folder tests
 - All your test files should be text files (extension: .txt)
 - All your tests should be executed by using this command: python3 -m doctest ./tests/*
 - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 - All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
 - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Authors:
[Jonatan Mazo](https://github.com/MAZTRO)
