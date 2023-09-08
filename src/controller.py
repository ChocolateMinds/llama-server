from flask import Flask, request, jsonify
from load_model import model

app = Flask(__name__)

@app.route('/invoke_model', methods=['POST'])
def invoke_model():
    data = request.json
    prompt = data.get('prompt', '')
    answer:str = model(prompt)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
