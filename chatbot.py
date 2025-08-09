import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY="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"

#Step1: Upload pdf file
st.header("AskFromPDF")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a file and start asking questions",type="pdf")

#Step2: Convert the file into chunks

# Extract the text
if file is not None:
    pdf_reader= PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
        #st.write(text)

# Break it into chunks
    text_splitter=RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks= text_splitter.split_text(text)
    #st.write(chunks)

    # Step3: Generate Embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    #Step4: Store in Vector Store  - FAISS
    vector_store = FAISS.from_texts(chunks,embeddings)

    #Step5: Get user questions
    user_question= st.text_input("Type your question here")

    #Step6: Do similarity search
    if user_question:
        match= vector_store.similarity_search(user_question)
        #st.write(match)

        #define llm
        llm =ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0.2,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )
        #Step7: Output the results
        chain=load_qa_chain(llm,chain_type="stuff")
        response=chain.run(input_documents=match, question=user_question)
        st.write(response)