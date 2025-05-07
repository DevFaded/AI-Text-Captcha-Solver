import time
from PIL import Image
from google import genai #gpt didnt work for me some reason idk

client = genai.Client(api_key="api")

#this works but is NOT accurate i made this because i felt like it lolll
def solve(path):
    image = Image.open(path)
    prompt = ("You are a OCR assistant. Extract and return only the exact characters shown in this CAPTCHA image, without any extra formatting or commentary.")
    start = time.time()
    response = client.models.generate_content(model="gemini-2.0-flash", contents=[image, prompt])
    elapsed = time.time() - start
    return response.text.strip(), elapsed

text, duration = solve("captcha.png")
print(text, f"- {duration:.2f}")
