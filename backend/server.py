from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator.calculator import add

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate_string():
    print('Request received /calculate')
    
    if not request.json:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    data = request.json
    print('Data:', data)
    numbers = data.get('numbers', '')

    try:
        result = add(numbers)
        print('calculation result:', result)
        return jsonify({'result': result})
    except ValueError as e:
        print('Calculation error:', str(e))
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)