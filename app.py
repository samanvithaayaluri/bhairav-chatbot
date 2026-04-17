from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os

app = Flask(__name__)

# ✅ SECURE: Fetch the API key from the environment variable you created
# Make sure the name matches exactly what you typed in Render (e.g., GEMINI_API_KEY)
API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize the Gemini 3 Client
client = genai.Client(api_key=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    if not user_input:
        return jsonify({"reply": "I'm listening! What's on your mind? 🐾"})

    try:
        # Modern 2026 API call with System Instructions
        response = client.models.generate_content(
            model="gemini-3-flash", 
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
        # This prints the specific error to your Render logs for debugging
        print(f"Bhairav Error: {e}") 
        return jsonify({"reply": "I'm having a bit of trouble connecting to my doggie brain. Check my logs!"})

if __name__ == "__main__":
    # Render provides the PORT via environment variables
    port = int(os.environ.get("PORT", 5000))
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




