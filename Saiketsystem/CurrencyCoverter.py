import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://openexchangerates.org/api/latest.json"

def get_exchange_rates():
    try:
        response = requests.get(f"{BASE_URL}?app_id={API_KEY}")
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch exchange rates.")
        return None


def currency_converter():
    rates = get_exchange_rates()
    if not rates:
        return

    print("\nAvailable currencies include: USD, EUR, GBP, INR, JPY, AUD\n")

    base_currency = input("Enter base currency: ").upper()
    target_currency = input("Enter target currency: ").upper()

    if base_currency not in rates or target_currency not in rates:
        print("Invalid currency code.")
        return

    try:
        amount = float(input("Enter amount to convert: "))
        if amount < 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    # Conversion logic
    usd_amount = amount / rates[base_currency]
    converted_amount = usd_amount * rates[target_currency]

    print(f"\n{amount} {base_currency} = {converted_amount:.2f} {target_currency}")


print("💱 Welcome to the Currency Converter")
currency_converter()
