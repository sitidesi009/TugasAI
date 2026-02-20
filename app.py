from flask import Flask, render_template, request, jsonify
from google import genai
import json
import re

app = Flask(__name__)

# 🔥 TEMPORARY: Hardcode dulu biar pasti jalan
client = genai.Client(api_key="AIzaSyAaih4MiUWeAbakLBu-xVEMt6l4hktLSfw")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/proses_ai', methods=['POST'])
def proses_ai():
    try:
        data = request.get_json()

        game = data.get('game')
        players = data.get('players')
        playtime = data.get('playtime')

        prompt = f"""
Kamu adalah Game Monetization Analyst.

Analisis game berikut:

Nama Game: {game}
Jumlah Pemain: {players}
Rata-rata Durasi Main: {playtime} menit

Berikan 3 strategi monetisasi dalam format JSON valid seperti ini:

[
  {{
    "strategi": "Nama Strategi",
    "deskripsi": "Penjelasan singkat",
    "estimasi_dampak": "Rendah / Sedang / Tinggi",
    "skor_potensi": 8.5,
    "estimasi_conversion_rate": 0.05
  }}
]

Keterangan:
- skor_potensi dari 1–10
- estimasi_conversion_rate dalam bentuk desimal (contoh 0.05 = 5%)

JANGAN tambahkan teks apapun selain JSON.
"""

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        raw_text = response.text.strip()

        # Bersihkan jika AI menambahkan ```json
        cleaned = re.sub(r"```json|```", "", raw_text).strip()

        parsed_json = json.loads(cleaned)

        return jsonify(parsed_json)

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)