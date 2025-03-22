from flask import Flask, render_template, request, jsonify
import random
import google.generativeai as genai

genai.configure(api_key="AIzaSyDolEs78y3Nfrgn6wFFNLCbqgluCpiPtoA") 

app = Flask(_name_)

EMOTIONS = ["Happy", "Sad", "Angry", "Fear", "Neutral"]

def get_random_emotion():
    return random.choice(EMOTIONS)

def get_gemini_response(emotion):
    model = genai.GenerativeModel("gemini-1.5-pro")
    system_instruction = (
        f"The user is feeling {emotion}. Respond in a supportive and friendly way."
    )
    response = model.generate_content(system_instruction)
    return response.text if response else "I'm here to help! 😊"
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    audio_path = "uploaded_audio.wav"
    audio_file.save(audio_path)

    detected_emotion = get_random_emotion()

    chatbot_response = get_gemini_response(detected_emotion)

    return jsonify({"emotion": detected_emotion, "response": chatbot_response})

if _name_ == '_main_':
    app.run(debug=True)