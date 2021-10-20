import requests

# you can p print to see nice JSON. pretty print!


def get_bitcoin_conversions():
    try:
        response = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
        # print(response.status_code) # 200 codes represent successful request
        response.raise_for_status() # raise an exception for 400 or 500 code
        data = response.json()
        return data

    except Exception as e:
        print(e)
        print('There was an error making the request.')


def extract_bitcoin_USD(data):
    return data['bpi']['USD']['rate_float']


def get_bitcoin_conversion_USD():
    data = get_bitcoin_conversions()
    rate = extract_bitcoin_USD(data)
    return rate


def calculate_bitcoin_rate(bitcoin_number):
    rate = get_bitcoin_conversion_USD()
    calculation = rate * bitcoin_number
    return calculation


def get_bitcoin_number():
    while True:
        number_of_bitcoin = input('How many bitcoins? : ')
        # not ideal since it doesn't accept decimal
        if number_of_bitcoin.isnumeric() == False:
            print('Enter a number, no text.')
        else:
            return number_of_bitcoin


def main():
    bitcoin_number = get_bitcoin_number()
    bitcoin_number_float = float(bitcoin_number)

    bitcoin_to_USD = calculate_bitcoin_rate(bitcoin_number_float)

    print(f'You have ${bitcoin_to_USD:.2f} in bitcoin.')

    # bpi = data['fact'] # it is now a python dictionary so can treat it as such



if __name__ == '__main__':
    main()


