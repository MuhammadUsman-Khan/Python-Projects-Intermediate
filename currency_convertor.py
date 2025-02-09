import requests

def get_currency(amount, from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['conversion_rates'].get(to_currency)
        if conversion_rate:
            converted_amount = conversion_rate * amount
            print(f"{amount} {from_currency} is {converted_amount} {to_currency}")

        else:
            print("Invalid Target Currency!")

    else:
        print("Failed to retrieve data!")


def main():
    api_key = "*******************"
    from_currency = input("Enter base currency (e.g: USD): ").upper()
    to_currency = input("Enter target currency (e.g: EUR): ").upper()
    amount = float(input("Enter amount: "))
    get_currency(amount, from_currency, to_currency, api_key)
        


if __name__ == "__main__":
    main()