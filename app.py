from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the constant to return
CONSTANT_VALUE = "The input was 1"

@app.route('/check_input', methods=['POST'])
def check_input():
    print(request.json['input'])
    # Check if the request data is JSON and contains 'input' field
    if not request.json or 'input' not in request.json:
        return jsonify({"error": "Bad request, 'input' field is required"}), 400

    try:
        user_input = int(request.json['input'])
    except ValueError:
        return jsonify({"error": "Invalid input, must be an integer"}), 400

    if user_input == 1:
        return jsonify({"message": CONSTANT_VALUE}), 200
    else:
        return jsonify({"error": "Input must be 1"}), 400

if __name__ == '__main__':
    app.run(debug=True)
