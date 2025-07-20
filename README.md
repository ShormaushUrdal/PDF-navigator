# 📚 PDF Navigator

A simple Streamlit application that allows you to understand the contents of PDF documents.

---

**🚧 Project Status: Under Improvement**

## ✨ Features

* **PDF Processing:** Loads and processes text from a PDF file.
* **Vector Embeddings:** Uses Google's `gemini-embedding-001` to create numerical representations (vectors) of your document's text.
* **Vector Storage:** Stores and indexes the document vectors using **FAISS** (Facebook AI Similarity Search) for quick retrieval.
* **Q&A with LLMs:** Leverages the fast and powerful **Llama3** model via the **Groq API** to answer questions.
* **Context-Aware Answers:** The LLM is strictly instructed to answer questions *only* based on the context provided from the PDF, preventing hallucinations or fabricated answers.
* **Source Verification:** Displays the exact text chunks from the PDF that were used to generate the answer.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

* Python 3.8 or newer

### 2. Clone the Repository


### 3. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install them using pip:
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

You need API keys from Google and Groq for this project to work. You can also change the LLM model for the embedding and the response generation.

1.  Create a file named `.env` in the root of your project directory.
2.  Add your API keys to this file:
    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    ```
3.  You can get your keys from:
    * **Google AI Studio:** [https://ai.google.dev/](https://ai.google.dev/)
    * **Groq Console:** [https://console.groq.com/keys](https://console.groq.com/keys)

### 6. Add Your PDF

1.  Create a folder named `data` in the root of your project directory.
2.  Place the PDF you want to study inside this folder and name it `xyz.pdf`.
    * Alternatively, you can change the hardcoded path in the code on this line: `st.session_state.loader = PyPDFLoader("data/xyz.pdf")`.



### Running the App

Once the setup is complete, run the following command in your terminal (assuming your Python script is named `app.py`):

```bash
streamlit run app.py
```

Your web browser should automatically open a new tab with the running Streamlit application.

### Using the App

The user interface is simple and straightforward:

1.  **Embed the Document:** First, you must process and embed your PDF. Click the **"Documents Embedding"** button. This will load the PDF, split it into chunks, and create a vector store. You only need to do this once per session.
2.  **Wait for Confirmation:** A message "Vector Store is up and running" will appear to let you know the process is complete.
3.  **Ask a Question:** Type your question about the PDF content into the text input field labeled "Enter your question from the PDF".
4.  **Get the Answer:** The application will process your question, find the relevant context from the document, and generate an answer. The answer will be displayed on the screen.
5.  **Verify the Context:** Below the answer, you can click on the **"Document Similarity Search"** expander to see the exact pieces of text from the PDF that the AI used to formulate its response. This is great for verification and deeper understanding.

---