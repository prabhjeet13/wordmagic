from TTmodel import translate_text

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hompage():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translates():
    try:
        data = request.json
        text = data.get('text')
        target_lang = data.get('target_lang')

        if not text or not target_lang:
            return jsonify({"error": "Missing 'text' or 'target_lang' in request"}), 400

        translated_text = translate_text(text,target_lang)
        return jsonify({"translated_text": translated_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000,debug=True)