from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure a chave de API da OpenAI
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    chat_history = request.form['chat_history']

    # Chamar a API GPT-3.5-Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente de chat que fala como um usuário."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": chat_history}
        ]
    )

    assistant_response = response.choices[0].message['content']

    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
