from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# 1. Configuration
genai.configure(api_key="AIzaSyAwJMtY4PdkBzlPHZVV_q9HbNX73S91dAM")

# 2. Model Initialization (Modern 2026 Method)
# Using gemini-3-flash with system instructions for a consistent persona
model = genai.GenerativeModel(
    model_name="gemini-3-flash",
    system_instruction=(
        "You are Bhairav 🐶, a friendly and smart pet care assistant. "
        "Help users with adoption guidance, pet care tips, and emotional support. "
        "Use simple English, keep a warm tone, and give practical advice. "
        "Introduce yourself as Bhairav in the first message, then just answer helpfully."
    )
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    
    if not user_input:
        return jsonify({"reply": "I didn't hear anything! Woof?"})

    try:
        # The system instruction is already handled in the model object
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        # Logs the error for debugging on Render
        print(f"Chat Error: {e}")
        return jsonify({"reply": "Bhairav is taking a quick nap. Please try again in a moment! 🐾"})

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




