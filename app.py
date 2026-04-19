from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os

app = Flask(__name__)

# 1. Securely fetch your new API Key from Render
API_KEY = os.environ.get("GOOGLE_API_KEY")

# 2. Initialize the modern 2026 Client
client = genai.Client(api_key=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    
    if not user_input:
        return jsonify({"reply": "I'm listening! What's up? 🐾"})

    try:
        # 3. Upgrade to Gemini 3 Flash (The 2026 Standard)
        # This model is faster, smarter, and replaces the old 1.5/2.0 series
        response = client.models.generate_content(
            model="gemini-3-flash", 
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are Bhairav 🐶, a friendly and smart pet care assistant for a pet adoption site. "
                    "Help users with adoption advice, pet care tips, and emotional support. "
                    "Use simple English, keep a warm tone, and be very helpful. "
                    "If people ask about adopting, encourage them to look at the available pets on the site!"
                )
            ),
            contents=user_input
        )
        
        return jsonify({"reply": response.text})
        
    except Exception as e:
        # Logs the error to Render for you
        print(f"Bhairav Error: {e}", flush=True) 
        return jsonify({"reply": "I'm having a quick dognap. Please try again in a second! 🐾"})

if __name__ == "__main__":
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




