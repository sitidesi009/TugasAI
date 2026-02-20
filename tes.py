from google import genai

client = genai.Client(api_key="AIzaSyAaih4MiUWeAbakLBu-xVEMt6l4hktLSfw")

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Halo, jawab singkat."
)

print(response.text)