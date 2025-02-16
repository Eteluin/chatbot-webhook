from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Загружаем модель RuGPT-3
chatbot = pipeline("text-generation", model="sberbank-ai/rugpt3large")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_message = data["queryResult"]["queryText"]
    
    # Генерация ответа с помощью модели
    response = chatbot(user_message, max_length=50)[0]["generated_text"]
    
    return jsonify({
        "fulfillmentText": response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
