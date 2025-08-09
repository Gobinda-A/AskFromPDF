# 📄 AskFromPDF

**AskFromPDF** is an AI-powered document assistant that lets you **upload a PDF and instantly ask questions** about its contents.  
It uses **OpenAI’s API** to generate embeddings, stores them in a **FAISS** vector database for efficient semantic search, and employs a **Large Language Model (LLM)** to deliver accurate answers.

---

## 🚀 Features
- **Upload any PDF** file through a Streamlit web app.  
- **Ask natural language questions** and get instant answers from the document.  
- **Semantic search** powered by embeddings — understands meaning, not just keywords.  
- **Fast retrieval** using FAISS vector store.  
- **Simple, interactive UI** with Streamlit.

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **Streamlit** – Web app interface  
- **PyPDF2** – PDF text extraction  
- **LangChain** – Orchestration of LLMs, embeddings, and vector stores  
- **OpenAI API** – Generating embeddings & answering questions  
- **FAISS** – High-performance vector search library  

---

## 📚 Key Python Libraries
| Library | Purpose |
|---------|---------|
| `streamlit` | Interactive web application |
| `PyPDF2` | Extract text from PDFs |
| `langchain_text_splitters` | Break long text into manageable chunks |
| `langchain.embeddings.openai` | Create vector embeddings using OpenAI |
| `langchain.vectorstores.FAISS` | Store and search embeddings |
| `langchain_community.chat_models` | Access OpenAI’s ChatGPT models |
| `langchain.chains.question_answering` | Build Q&A logic over documents |

---

## 🧠 High-Level Concept
1. **Upload & Extract** – The user uploads a PDF; text is extracted page-by-page.  
2. **Chunking** – The text is split into overlapping chunks for better context retention.  
3. **Embeddings** – Each chunk is converted into a numerical vector using OpenAI’s `text-embedding` model.  
4. **Vector Store** – Vectors are stored in FAISS for fast similarity search.  
5. **Query** – User enters a question; it is also embedded and compared to stored vectors.  
6. **Retrieve & Answer** – The most relevant chunks are passed to an LLM (ChatGPT) to generate a natural language answer.

---

## 📂 Project Structure
