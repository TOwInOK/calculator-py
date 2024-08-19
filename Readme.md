# Python calculator lib

## What's the point of the test?
- How long does it take to run the system from 0?
- Just a test of how bad Python is.

**Note:** Yes... it's very bad.

## Explain
- Let's start by getting rid of the manual use of venv.
    - Use poetry instead, like rust way!
- use __init__ as a mod in rust

- There's no type of error? Let's add with result package

- Stop using run with file!
    - Use module instead 
        - poetry run python -m folder.file.module (module if needed)
        #### Example 
        - normal
            - poetry run python -m scripts.main 
        - test
            - poetry run python -m unittest tests\calculator.py 

## What we get
- Normal toml file about project
- Lock file for lib (with hashes)
- Rust-like file arrangement