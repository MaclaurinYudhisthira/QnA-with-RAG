# QnA-with-RAG

## Setup env
- python3 -m pip install virtualenv
- python3 -m venv myenv
- source myenv/bin/activate

## Dependency Installation
- pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai langchain-chroma bs4
- pip install openai==0.28
- pip install fastapi uvicorn
- pip install -r requirements.txt

## Setting env
- create a file at QnA-with-RAG/app/.env
refer QnA-with-RAG/example.env for adding your open-api-key

## Running and Testing
- cd QnA-with-RAG/app/
- uvicorn main:app --reload
- Open http://localhost:8000/docs and test the apis


