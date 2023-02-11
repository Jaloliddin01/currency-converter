from flask import Flask, request
import requests
from json import loads

app = Flask(__name__)

usd = float()

def set_currency():
    data = requests.get('https://nbu.uz/uz/exchange-rates/json/').text
    # print(type(data))
    # print(data)
    # print(type(loads(data)[-1]))
    global usd
    usd = float(loads(data)[-1]['nbu_buy_price'])


@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    return { 
        "amount": int(request.args.get('amount', 0)), 
        "currency": "UZS", 
        "converted": round(int(request.args.get('amount', 0)) / usd, 2), 
        "convertedCurrency": "USD" 
    }
    

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    return { 
        "amount": int(request.args.get('amount', 0)), 
        "currency": "USD", 
        "converted": int(request.args.get('amount', 0)) * usd, 
        "convertedCurrency": "UZS" 
    }
    

if __name__ == '__main__':
    set_currency()
    app.run(debug=True)    