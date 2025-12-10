from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import openai
import base64
import os

app = FastAPI()

# Mount the static folder to serve index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize OpenAI (It will look for OPENAI_API_KEY in environment variables)
client = openai.OpenAI()

def encode_image(image_file):
    return base64.b64encode(image_file).decode('utf-8')

@app.get("/")
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # 1. Read and encode the image
    contents = await file.read()
    base64_image = encode_image(contents)

    # 2. Send to GPT-4o
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Using mini to save costs, it has vision!
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Is this a picture of a hotdog? Answer strictly with 'Hotdog' or 'Not hotdog'."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )

    # 3. Return the answer
    return {"result": response.choices[0].message.content}
