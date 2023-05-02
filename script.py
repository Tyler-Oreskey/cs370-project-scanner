import requests;
import os;
from dotenv import load_dotenv
from PyHelper2 import Helper

# load .env variables
load_dotenv()

BASE_URL = os.getenv('BASE_URL')

talking_class = Helper(name = "Item Scanner", path = '/home/tpores/Desktop/say_this.mp3')

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

    talking_class.say_hello()

    while True:

        talking_class.say_this("Ok, Please scan an item.")

        upc_code = scan_upc_code()
        res = get_req(BASE_URL + '/product/upc/' + upc_code)

        #if the item is not in data base
        if res == None: return

        if res.status_code == 404:
            talking_class.say_this("Ok, this item is not recognized. Would you like to add this item to the database?", feedback=True)
            answer = talking_class.listen_for_command(feedback=True)
            if answer.startswith('yes') or answer.startswith('yeah'):
                while True:
                    talking_class.say_this("Ok, What is the name of the product you would like to add?", feedback=True)
                    item_to_add = talking_class.listen_for_command(feedback=True)
                    talking_class.say_this("Ok, the item you would like to add is " + item_to_add + ", is that correct?", feedback=True)
                    answer = talking_class.listen_for_command(feedback=True)
                    if answer.startswith('yes') or answer.startswith('yeah'):
                        break
                payload = {'name': item_to_add, 'upcCode': upc_code}
                posted = post_req(BASE_URL + '/product', payload)
                if posted == None: return

                if posted.status_code < 200 or posted.status_code > 299 :
                    print('Post request failed with status code: ', posted.status_code, '\n', 'message: ', posted.text)
                    talking_class.say_this("hm. Sorry there was a problem adding that item.")
                    continue

                talking_class.say_this("Ok, your item was succesfully added!")

        elif res.status_code < 200 or res.status_code > 299 :
            print('Get request failed with status code: ', res.status_code, '\n', 'message: ', res.text)
            return

        else:
            # print/speak the name of the objects
            # what exactly does res.json() return? 
            talking_class.say_this("Ok, your item is " + res.json()[0]['name'], feedback=True)

        talking_class.say_this("Would you like to scan another item?", feedback=True)
        answer = talking_class.listen_for_command(feedback=True)
        if answer.startswith('no'):
            talking_class.say_this("Ok, Goodbye!")
            break

if __name__ == '__main__':
    main()