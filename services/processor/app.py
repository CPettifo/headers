from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HeaderInfo(BaseModel):
    ip: str
    user_agent: str

def process_header(info):
    # for now return junk data
    return {
        "ip": info["ip"],
        "country": "Ugunda",
        "user_agent": info["user_agent"]
    }

@app.post("/process")
async def process(header: HeaderInfo):
    processed = process_header(header.dict())
    print("Processed:", processed)
    return {"status": "ok", "data": processed}