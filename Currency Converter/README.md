## Currency Converter

This is a simple python script that uses the [RapidAPI](https://rapidapi.com/) to convert one currency to another. The script uses the `requests` library to make an API call and the `pyfiglet` library to print the title in an ASCII art font. The API key and host are stored in a `.env` file and loaded using the `dotenv` library.

### Prerequisites

* You will need to have Python3 installed on your machine.
* You will also need to create an account on [RapidAPI](https://rapidapi.com/).

### Usage

1. Clone the repository.
2. Create a `.env` file in the same directory as the script and add the following lines:

```bash
RAPID_API_KEY=<your RapidAPI key>
RAPID_API_HOST=currency-converter-by-api-ninjas.p.rapidapi.com
```

3. Run the script using `python currency_converter.py`.
4. Enter the amount of money you want to convert, the currency you want to convert from, and the currency you want to convert to.

## Built With

* [Python3](https://www.python.org/) - Programming language used
* [Requests](https://docs.python-requests.org/en/master/) - Package used to make API calls
* [PyFiglet](https://pypi.org/project/pyfiglet/) - Package used to generate ASCII art text
* [Dotenv](https://pypi.org/project/python-dotenv/) - Package used to store and manage environment variables
