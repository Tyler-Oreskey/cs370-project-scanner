import requests;
import os;
from dotenv import load_dotenv

# load .env variables
load_dotenv()

BASE_URL = os.getenv('BASE_URL')

# scan and return upc code
def scan_upc_code():
    return input('Scan a barcode: ')

# handle get requests
def get_req(url):
    res = None

    try: res = requests.get(url)
    except Exception as e: print('Get request failure: ', e)
    finally: return res

# handle post requests 
def post_req(url, payload):
    res = None

    try: res = requests.post(url, json=payload)
    except Exception as e: print('Post request failure: ', e)
    finally: return res

def main():
    #get request example
    res = get_req(BASE_URL + '/product/upc/' + scan_upc_code())

    if res == None: return
    
    if res.status_code < 200 or res.status_code > 299:
        print('Get request failed with status code: ', res.status_code, '\n', 'message: ', res.text)
        return
    
    print(res.json())
    
    #post request example
    payload = { 'name': 'Cheerios', 'upcCode': scan_upc_code() }

    res = post_req(BASE_URL + '/product', payload)

    if res == None: return
    
    if res.status_code < 200 or res.status_code > 299:
        print('Post request failed with status code: ', res.status_code, '\n', 'message: ', res.text)
        return
    
    print(res.json())


if __name__ == '__main__':
    main()