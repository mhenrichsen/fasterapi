from fastapi import FastAPI, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
import uvicorn
from PIL import Image
import io
import model as m

app = FastAPI()


#
@app.get("/iris")
async def flower(s_length, s_width, p_length, p_width):
    res = m.predict(s_length, s_width, p_length, p_width)
    return JSONResponse({"result": res})

@app.post("/image")
async def upload_image(file: bytes = File(...), text: str = Form(...)):
    image = Image.open(io.BytesIO(file))
    print(text)
    image.save('img.png')
    print(file)
    return {"file_size": len(file),
            "text": text}

@app.get("/")
async def home():
    return RedirectResponse("/docs")

app.add_middleware(CORSMiddleware, allow_origins=["*"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
