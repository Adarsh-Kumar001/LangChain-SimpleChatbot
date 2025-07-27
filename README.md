
This project is a simple **Question Answering app** built using **Streamlit**, **LangChain** and **Google Gemini API**. It takes user input then sends it to Gemini using LangChain and displays the response in a web interface using streamlit.

---

## Environment Setup

### 1️⃣ Create and activate a virtual environment
```bash
python -m venv myvenv
myvenv\Scripts\activate

#Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install --upgrade --quiet langchain-google-genai pillow
pip install streamlit
pip install python-dotenv

```
.env contains :
GOOGLE_API_KEY=
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT="geminiChatbotApp"

To run:
streamlit run gemini_app_qa.py
