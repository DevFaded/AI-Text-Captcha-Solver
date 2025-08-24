import time
from PIL import Image
import google.generativeai as genai #gpt didnt work for me some reason idk

genai.configure(api_key="AIzaSyAE7H4JuCJnySo8jCck_LTlN0k3gOQkfCU")

#this works but is NOT accurate i made this because i felt like it lolll
def solve(path):
    image = Image.open(path)
    prompt = ("You are an OCR assistant. Extract and return ONLY the exact characters shown in this CAPTCHA image.")
    start = time.time()
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([prompt, image])
    elapsed = time.time() - start
    return response.text.strip(), elapsed

text, duration = solve("captcha.png")
print(text, f"- {duration:.2f}s")
