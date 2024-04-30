from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'OK'})

if __name__ == '__main__':
    app.run(debug=True)