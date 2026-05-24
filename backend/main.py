from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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

# Review logic
def review_code(code: str):

    review = []

    # Security checks
    if "password =" in code:
        review.append("- Hardcoded password detected")

    if "eval(" in code:
        review.append("- Avoid using eval()")

    if "os.system(" in code:
        review.append("- Avoid using os.system()")

    # Performance checks
    if "for i in range" in code and "for j in range" in code:
        review.append("- Avoid unnecessary nested loops")

    # General suggestions
    review.append("- Improve variable naming")
    review.append("- Add proper error handling")

    # If no major issues
    if len(review) == 2:
        review.insert(0, "- Code received successfully")

    return "\n".join(review)

# Home API
@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer Running"
    }

# Review API
@app.post("/review")
def review(data: CodeRequest):

    result = review_code(data.code)

    return {
        "review": result
    }