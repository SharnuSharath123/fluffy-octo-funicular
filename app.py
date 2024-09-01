from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fun-fact')
def fun_fact():
    return jsonify({
        'fact': 'Did you know? Octopuses have three hearts and blue blood!'
    })

if __name__ == '__main__':
    app.run(debug=True)
