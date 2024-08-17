from fastapi import FastAPI, UploadFile, File
import json
from dotenv import load_dotenv
from apis.rag import initialize_rag
load_dotenv()

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Service is running."}

@app.post("/answer-questions/")
async def answer_questions(questions_file: UploadFile = File(...), content_file: UploadFile = File(...)):
    # Read and parse the uploaded files
    questions_data = await questions_file.read()
    content_data = await content_file.read()

    questions = json.loads(questions_data)
    content = content_data.decode('utf-8')

    # Initialize the RAG chain with the content
    rag_chain = initialize_rag(content)

    # Generate answers for each question
    responses = {}
    for q in questions:
        question = q["question"]
        answer = rag_chain.run(question)
        responses[question] = answer

    return responses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
