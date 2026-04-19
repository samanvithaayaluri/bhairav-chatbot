from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os

app = Flask(__name__)

# ✅ 1. Get the key and verify it's not empty
API_KEY = os.environ.get("GEMINI_API_KEY")

# ✅ 2. Initialize the client
# If API_KEY is None, this will still initialize, but the first call will fail.
client = genai.Client(api_key=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Check if the user even sent a message
    data = request.json
    if not data:
        return jsonify({"reply": "No data received! 🐾"})
        
    user_input = data.get("message")
    
    # Check if the API key is missing from Render's environment
    if not API_KEY:
        print("CRITICAL ERROR: GEMINI_API_KEY environment variable is NOT SET!", flush=True)
        return jsonify({"reply": "System Error: My API Key is missing in Render. Please add it!"})

    if not user_input:
        return jsonify({"reply": "I'm listening! What's on your mind? 🐾"})

    try:
        # ✅ 3. Using the stable Gemini 1.5 Flash (most reliable for free tier)
        # You can change this to "gemini-3-flash" once we verify the connection works.
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are Bhairav 🐶, a friendly and smart pet care assistant. "
                    "Help users with adoption guidance, pet care tips, and emotional support. "
                    "Use simple English, keep a warm tone, and give practical advice."
                )
            ),
            contents=user_input
        )
        
        # Return the AI's response text
        return jsonify({"reply": response.text})
        
    except Exception as e:
        # ✅ 4. The 'flush=True' makes this appear in Render Logs immediately
        print(f"Bhairav Error Details: {str(e)}", flush=True) 
        
        # ✅ 5. Temporarily sending the ACTUAL error to the chat window for debugging
        return jsonify({"reply": f"Doggie Brain Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # debug=False is better for Render production
    app.run(debug=False, host='0.0.0.0', port=port)





















# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai

# app = Flask(__name__)

# genai.configure(api_key="AIzaSyAwJMtY4PdkBzlPHZVV_q9HbNX73S91dAM")

# model = genai.GenerativeModel("gemini-3-flash-001")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     try:
#         context = (
#     "You are Bhairav 🐶, a friendly and smart pet care assistant who helps users with adoption guidance, pet care tips, and emotional support. "
#     "Your tone should be warm, helpful, and reassuring — like a caring companion. "
#     "Give responses that are clear and informative, moderately detailed, but avoid being too dramatic or overly wordy. "
#     "No storytelling or excessive exclamations. Focus on practical, useful advice in a friendly tone."
#     "Dont use complicated english,keep the language simple"
#     "Start by introducing yourself in a kind way: for example, 'Hi! I'm Bhairav, your pet care assistant.' "
#     "After that, don't repeat the greeting. Just answer the user's questions helpfully and kindly."
     
# )

#         response = model.generate_content([context, user_input])
#         return jsonify({"reply": response.text})
#     except Exception as e:
#         return jsonify({"reply": f"Error: {str(e)}"})

# if __name__ == "__main__":
#     import os
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)




