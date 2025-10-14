from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

class FreeTelegramBridge:
    def __init__(self):
        self.telegram_url = "https://api.telegram.org/bot"
    
    def forward_request(self, bot_token, method, data):
        """Проксирование запроса к Telegram API"""
        url = f"{self.telegram_url}{bot_token}/{method}"
        try:
            response = requests.post(url, json=data, timeout=10)
            return response.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}

bridge = FreeTelegramBridge()

@app.route('/telegram/<bot_token>/<method>', methods=['POST'])
def telegram_proxy(bot_token, method):
    """HTTP прокси для Telegram API"""
    data = request.get_json() or {}
    result = bridge.forward_request(bot_token, method, data)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "service": "telegram_bridge"})

@app.route('/')
def home():
    return "🚀 Free Telegram Bridge Active"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
