import requests


def get_bitcoin_price():
    endpoint = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd,gbp,eur',
        'include_24hr_change': 'true'
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        btc_data = data['bitcoin']

        print("Bitcoin Price:")
        print(f"USD: ${btc_data['usd']:,.2f}")
        print(f"GBP: £{btc_data['gbp']:,.2f}")
        print(f"EUR: €{btc_data['eur']:,.2f}")
        print(f"\n24h Change: {btc_data['usd_24h_change']:.2f}%")

    except requests.exceptions.ConnectionError:
        print("Connection Error: Can't reach the API")
        print("Check your internet connection or try a different network")
    except requests.exceptions.Timeout:
        print("Timeout Error: Request took too long")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_bitcoin_price()