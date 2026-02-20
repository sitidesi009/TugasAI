from google import genai

client = genai.Client(api_key="AIzaSyAaih4MiUWeAbakLBu-xVEMt6l4hktLSfw")

for m in client.models.list():
    print(m.name)