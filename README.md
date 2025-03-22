# Emotion-Aware Chatbot for Mental Health Support

## Overview
This project is designed to recognize human emotions from voice input and provide meaningful chatbot responses based on the detected emotion. The system processes speech, extracts features, identifies emotions, and generates responses to support users' mental well-being.

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Speech Processing:** pyaudio, pydub, librosa
- **Emotion Analysis:** Wav2Vec2 (for feature extraction)
- **Chatbot Framework:** Gemini API

## System Workflow
1. **Voice Input**
   - The user speaks into the microphone.
   - The system records audio using **pyaudio** and processes it with **pydub**.
   - Noise reduction is applied using **librosa**.

2. **Emotion Analysis**
   - The **Wav2Vec2 model** is used to extract meaningful speech features.
   - These features capture variations in tone, pitch, and intensity.

3. **Emotion Prediction**
   - The extracted features are analyzed and categorized into emotions like **happy, sad, fearful, disgusted, or surprised**.
   - A rule-based approach is used for classification.

4. **Chatbot Response**
   - The chatbot, powered by **Gemini API**, generates appropriate responses.
   - The responses are adjusted based on the user's detected emotion.

## How to Run the Project Locally

### Prerequisites
Ensure you have Python installed. 
### Step 1: Install Dependencies
Navigate to the project folder and install the required Python libraries:
```bash
pip install flask pyaudio pydub librosa transformers google-generativeai

Step 2: Run the Flask Server
Start the backend server by running:
python app.py
If everything is set up correctly, you should see:
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
Step 3: Open the Web Interface
Open your browser and go to http://127.0.0.1:5000/

Speak into the microphone and interact with the chatbot!


Future Enhancements:

-Improve emotion classification using a trained ML model.

-Expand chatbot responses for a better conversation flow.

-Deploy as a mobile or web application.


