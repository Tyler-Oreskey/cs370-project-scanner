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
    alexa = Helper(name='Alexa')

    while True:
        upc_code = scan_upc_code()
        res = get_req(BASE_URL + '/product/upc/' + upc_code)
        #if the item is not in data base
        if res.status_code < 200 or res.status_code > 299:
            alexa.say_this("This item is not reckognized. Would you like to add this item to the database?", feedback=True)
            answer = alexa.listen_for_command(feedback=True)
            if answer.startswith('yes') or answer.startswith('yeah'):
                while True:
                    alexa.say_this("What is the name of the product you would like to add?", feedback=True)
                    item_to_add = alexa.listen_for_command(feedback=True)
                    alexa.say_this("The item you would like to add is " + item_to_add + "is that correct?", feedback=True)
                    answer = alexa.listen_for_command(feedback=True)
                    if answer.startswith('yes') or answer.startswith('yeah'):
                        break
                payload = {'name': item_to_add, 'upcCode': upc_code}
                posted = post_req(BASE_URL + '/product', payload)
                if res == None: return

                if res.status_code < 200 or res.status_code > 299:
                    print('Post request failed with status code: ', res.status_code, '\n', 'message: ', res.text)
                    return
        else:
            #print/speak the name of the object
            alexa.say_this("Your item is " + res.json()[0].name, feedback=True)
        alexa.say_this("Would you like to scan another item?", feedback=True)
        answer = alexa.listen_for_command(feedback=True)
        if answer.startswith('no'):
            break

'''
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

'''

if __name__ == '__main__':
    main()