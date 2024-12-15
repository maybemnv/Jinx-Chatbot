from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure the Gemini API key
genai.configure(api_key="AIzaSyDNDJHLxWRBFlxhqbFlbn0ATjqq-it6Sbg")

# Chat histories stored in memory
chat_histories = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chats', methods=['GET'])
def get_chats():
    """Fetch all available chats."""
    chats = [{'id': chat_id, 'name': f'Chat {chat_id}'} for chat_id in chat_histories.keys()]
    return jsonify({'chats': chats})

@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    """Fetch the chat history for a specific chat."""
    chat_id = request.args.get('chat_id')
    if not chat_id:
        return jsonify({'status': 'error', 'message': 'Chat ID is required'}), 400
    chat_id = int(chat_id)
    history = chat_histories.get(chat_id, [])
    return jsonify({'messages': history})

@app.route('/new_chat', methods=['POST'])
def new_chat():
    """Create a new chat."""
    data = request.get_json()
    chat_name = data.get('chat_name', 'New Chat')
    new_id = max(chat_histories.keys(), default=0) + 1
    chat_histories[new_id] = []
    return jsonify({'status': 'success', 'chat_id': new_id, 'chat_name': chat_name})

@app.route('/delete_chat', methods=['POST'])
def delete_chat():
    """Delete a specific chat."""
    data = request.get_json()
    chat_id = data.get('chat_id')
    if not chat_id:
        return jsonify({'status': 'error', 'message': 'Chat ID is required'}), 400
    chat_id = int(chat_id)
    chat_histories.pop(chat_id, None)
    return jsonify({'status': 'success', 'message': f'Chat {chat_id} deleted successfully.'})

@app.route('/get_ai_response', methods=['POST'])
def get_ai_response():
    """Fetch AI-generated response using Gemini API."""
    data = request.get_json()
    chat_id = data.get('chat_id')
    user_message = data.get('message')

    if not chat_id or not user_message:
        return jsonify({'status': 'error', 'message': 'Chat ID and message are required'}), 400
    
    chat_id = int(chat_id)

    try:
        # Call the Gemini API for a response
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_message)
        ai_response = response.text if response.text else "No response received from AI."
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    # Update chat history
    chat_histories.setdefault(chat_id, []).append({'role': 'You', 'content': user_message})
    chat_histories[chat_id].append({'role': 'AI', 'content': ai_response})

    return jsonify({'ai_response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
