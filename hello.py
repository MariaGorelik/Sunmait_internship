from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

class PredictRequest(BaseModel):
    text: str

@app.get("/ping")
async def ping():
    return {"message": "server is working"}

@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        if request.text[-1] != '.':
            request.text += '.'
        input_ids = tokenizer(request.text, return_tensors="pt").input_ids
        outputs = model.generate(input_ids)
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)