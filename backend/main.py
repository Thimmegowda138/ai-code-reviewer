from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/review")
async def review_code(request: CodeRequest):

    code = request.code

    review = []

    if "password" in code:
        review.append("- Hardcoded password detected")

    if "eval(" in code:
        review.append("- Avoid using eval()")

    review.append("- Improve variable naming")
    review.append("- Add proper error handling")

    return {
        "review": "\n".join(review)
    }