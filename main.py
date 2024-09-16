from fastapi import FastAPI, Request
app = FastAPI()
@app.post("/arr")
async def arr(req: Request):
    body = await req.json()
    return body