from flask import Flask, request

app = Flask(__name__)

usd = 11380.7 # 1 USD = 11380.7 UZS

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
        "converted": int(request.args.get('amount', 0)) / usd, 
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
        "currency": "UZS", 
        "converted": int(request.args.get('amount', 0)) * usd, 
        "convertedCurrency": "USD" 
    }
    

if __name__ == '__main__':
    app.run()    