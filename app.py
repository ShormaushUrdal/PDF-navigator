import streamlit as st
import asyncio
import os
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("Study with your PDF")

llm = ChatGroq(groq_api_key=groq_api_key, 
               model_name="llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
"""
Answer the question based on the following context only.
If you don't know the answer, just say that you don't know.
Do not try to make up an answer.
If the question is not related to the context, politely respond 
that you are tuned to only answer questions that are related 
to the context.
<context>
{context}
</context>
Questions:{input}
"""
)

prompt1 = st.text_input("Enter your question from the PDF")

def vector_embedding():
    if "vectors" in st.session_state:
        return
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    # edit this for your own pdf file path
    st.session_state.loader = PyPDFLoader("data/xyz.pdf")
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(
    st.session_state.docs) 
    st.session_state.vectorstore = FAISS.from_documents(st.session_state.final_documents, 
                                                        st.session_state.embeddings)

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store is up and running")

import time

if prompt1:
    start = time.process_time()    
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectorstore.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input" : prompt1})
    print("Response time : ", time.process_time() - start)
    st.write(response["answer"])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------")
