# 🎥 AskTube – Ask Anything About YouTube Videos  

AskTube is an **AI-powered RAG (Retrieval-Augmented Generation) app** that lets you interactively **query YouTube videos**.  
It fetches transcripts, splits them into chunks, generates embeddings using Google Gemini and stores them in FAISS for efficient retrieval, and uses **Google Gemini** to generate accurate, grounded answers — without hallucinations.  

---
## 🎥 Demo

[![AskTube Demo](assets/Asktube.gif)](https://www.youtube.com/watch?v=MwR6mTB0Qh8 "AskTube Demo")







## ✨ Features  

✅ **YouTube Transcript Fetching** – Extracts transcript (if available) directly from videos  
✅ **Chunking & Embedding** – Splits transcript into smaller chunks for better retrieval  
✅ **Vector Search with FAISS** – Stores embeddings and retrieves the most relevant context  
✅ **Google Gemini Integration** – Provides high-quality, context-grounded answers  
✅ **Streamlit UI** – Simple and interactive user interface  

---

## 🚀 How It Works  

1. Enter a **YouTube Video URL** in the Streamlit app.  
2. The transcript is **fetched and split** into chunks.  
3. Chunks are stored in a **FAISS vector database**.  
4. When you ask a question, the app **retrieves relevant transcript parts**.  
5. **Gemini LLM** answers *only from the transcript context*, avoiding hallucinations.  

---

## 🧪 Demonstration  

For demonstration, we asked the following questions:  

- ❓ *What is this video about?*  
- ❓ *How does GenAI work?*  
- ❓ *What are the applications of GenAI?*  
- ❓ *What is a heart transplant?*  

The app successfully provided **accurate answers for questions covered in the video transcript** (such as how GenAI works and its applications).  
<img width="300" height="300" alt="Screenshot 2025-09-05 235428" src="https://github.com/user-attachments/assets/79440577-f43f-4169-8564-4a8012b8745d" />
<img width="300" height="300" alt="Screenshot 2025-09-05 235220" src="https://github.com/user-attachments/assets/af91ba03-338c-4d0c-8cb5-49e28e3ffc21" />





When asked about **topics not mentioned in the video** (like heart transplant), the model **did not hallucinate** — it simply responded that the information was not available in the transcript.  





<img width="400" height="400" alt="Screenshot 2025-09-06 000215" src="https://github.com/user-attachments/assets/52d61f70-19a5-4f98-a886-52469fc163ea" />





This clearly demonstrates the **main advantage of RAG**: answers remain grounded in real content rather than AI’s imagination.  
 

---

## 🛠️ Tech Stack  

- **Python** 🐍  
- **Streamlit** – UI Framework  
- **LangChain** – Orchestration  
- **FAISS** – Vector Database  
- **Google Gemini (Generative AI)** – LLM & Embeddings  
- **YouTube Transcript API** – Transcript fetching  

---

## ⚡ Installation & Setup  

Clone the repository:  

```bash

git clone https://github.com/omraut31/AskTube-ask-anything-about-YouTube-videos-.git
cd AskTube-ask-anything-about-YouTube-videos-
```
Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file in the project root and add your Google API Key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Run the Streamlit app:
```
streamlit run app.py
```
## 📌 Usage

Paste a YouTube video link into the input field.
Ask any question related to the video.
Get precise answers, grounded only in the transcript.
---
## 🌟 Why AskTube?
Unlike standard LLMs that may hallucinate, AskTube uses RAG to ensure answers come only from the actual video transcript.
This makes it highly trustworthy for learning, research, and content summarization.
