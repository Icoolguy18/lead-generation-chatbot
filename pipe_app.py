from flask import Flask, render_template, request, jsonify
from pipeline import AppLogic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure "templates/index.html" exists

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input', '')

    app_logic = AppLogic()
    answer = app_logic.execute(user_input)  # Make sure execute() returns data

    if answer is None:
        answer = "No response generated."

    response = answer
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
