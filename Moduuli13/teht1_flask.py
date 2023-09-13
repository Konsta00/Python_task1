from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(num):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
        
        if is_prime:
            return is_prime
        else:
            return is_prime
        
@app.route('/prime/<int:num>', methods=['GET'])
def check_prime(num):
    is_prime_result = is_prime(num)
    res_data = {
        'Number': num,
        'isPrime': is_prime_result
    }
    return jsonify(res_data)

if __name__ == '__main__':
    app.run(debug=True)
    
