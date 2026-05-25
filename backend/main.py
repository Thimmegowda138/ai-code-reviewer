from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class CodeRequest(BaseModel):
    code: str

# Home route
@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer Running"
    }

# Review route
@app.post("/review")
async def review(request: CodeRequest):

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