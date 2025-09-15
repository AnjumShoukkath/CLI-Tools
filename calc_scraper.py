import typer
from enum import Enum
import requests
from bs4 import BeautifulSoup

app = typer.Typer()

class Command(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

@app.command()
def calc(cmd: Command, val1: float, val2: float):
    match cmd:
        case Command.add:
            sum = val1 + val2
            print(sum)

        case Command.subtract:
            dif = val1-val2
            print(dif)

        case Command.divide:
            if val2 == 0:
                print("Not possible")
            else: 
                quo = val1/val2
                print(quo)
        case Command.multiply:
            pro = val1*val2
            print(pro)

@app.command()
def scrape(url: str):
    try:
        headers = {
            "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0 Safari/537.36")
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)

        if text:
            print(text)
        else:
            print(("No visible text"))

    except requests.exceptions.RequestException as e:
        print(e)
        

if __name__ == "__main__":
    app()