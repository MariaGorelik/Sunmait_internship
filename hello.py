from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import uvicorn

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")


class PredictRequest(BaseModel):
    text: str


@app.get("/ping")
async def ping():
    return {"message": "server is working"}


@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        input_ids = tokenizer(request.text, return_tensors="pt").input_ids
        outputs = model.generate(input_ids)
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
