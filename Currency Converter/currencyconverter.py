import requests
from pyfiglet import Figlet
from dotenv import load_dotenv
import os 

f = Figlet(font='slant')
load_dotenv()

api_key = os.getenv("RAPID_API_KEY")
api_host = os.getenv("RAPID_API_HOST")

def print_title():
    print(f.renderText('Currency Converter'))

def convert_currency(money_amount, currency_from, currency_to):
	url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"
	querystring = {"have":currency_from,"want":currency_to,"amount":money_amount}
	headers = {
		"X-RapidAPI-Key": api_key,
		"X-RapidAPI-Host": api_host
	}
	print("Converting amount...")
	response = requests.request("GET", url, headers=headers, params=querystring)
	return response.json()["new_amount"]
 
def get_user_parameters():
    money_amount = input("Enter the amount of money you want to convert: ")
    currency_from = input("Enter the currency you want to convert from: ")
    currency_to = input("Enter the currency you want to convert to: ")
    
    return money_amount, currency_from, currency_to
 
if __name__ == "__main__":
	print_title()
	money_amount, currency_from, currency_to = get_user_parameters()
	converted_amount = convert_currency(money_amount, currency_from, currency_to)
	print(f'Converted amount: {converted_amount} {currency_to}')
