from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.schema import Document

# Function to initialize LangChain RAG with a FAISS vector store
def initialize_rag(content: str):
    # Convert content into a list of documents
    documents = [Document(page_content=doc) for doc in content.split('\n')]
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()

    # Create the FAISS index
    vector_store = FAISS.from_documents(documents, embeddings)
    
    # Initialize the RAG chain
    llm = OpenAI(model_name="gpt-3.5-turbo")
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())
    
    return rag_chain