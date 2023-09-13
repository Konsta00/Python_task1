import requests

def get_prime_value(num):
    base_url =f'http://127.0.0.1:5000/prime/{num}'  
    res = requests.get(base_url)
    print(res.json())

if __name__ == '__main__':
    num = int(input('Check if number is a prime number: '))
    get_prime_value(num)