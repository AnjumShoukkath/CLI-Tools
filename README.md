# CLI Calculator & Web Scraper Tool
This is a simple Python CLI application built with Typer.
It has two main features:
    - **Calculator** – perform basic arithmetic (add, subtract, multiply, divide)
    - **Web Scraper** – fetch and display all visible text from a given URL

# To run the file
 `pip install -r requirements.txt`
 `python main.py <command> [options]`
 `python main.py <command> --help`

 ## Calculator
 ```
 # Addition
 python main.py calc add 10 5

 # Subtraction
 python main.py calc subtract 20 7

 # Multiplication
 python main.py calc multiply 3 6

 # Division
 python main.py calc divide 10 2

 ```

 ## Web Scraper
 `python main.py scrape https://en.wikipedia.org/wiki/MCP`
