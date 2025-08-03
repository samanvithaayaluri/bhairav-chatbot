from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyAwJMtY4PdkBzlPHZVV_q9HbNX73S91dAM")

# ✅ Load the Gemini model (use 1.5 Flash for free and fast usage)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        context = (
    "You are Bhairav 🐶, a friendly and smart pet care assistant who helps users with adoption guidance, pet care tips, and emotional support. "
    "Your tone should be warm, helpful, and reassuring — like a caring companion. "
    "Give responses that are clear and informative, moderately detailed, but avoid being too dramatic or overly wordy. "
    "No storytelling or excessive exclamations. Focus on practical, useful advice in a friendly tone."
    "Dont use complicated english,keep the language simple"
    "Start by introducing yourself in a kind way: for example, 'Hi! I'm Bhairav, your pet care assistant.' "
    "After that, don't repeat the greeting. Just answer the user's questions helpfully and kindly."
     
)

        response = model.generate_content([context, user_input])
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)




