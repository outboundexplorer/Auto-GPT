from flask import Flask, jsonify

app = Flask(__name__)
print("Starting Flask app")
print(__name__)
@app.route('/embeddings')
def embeddings():
    # Replace this with the actual function to create OpenAI embeddings
    sample_data = {"embedding": [0.1, 0.2, 0.3, 0.4]}
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
