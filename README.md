---

# 🤖 AI Agent Terminal App

This is a terminal-based **AI Agent application** that allows users to ask natural language questions and receive intelligent answers using the **LLaMA3-8B model** via **Groq API**, orchestrated using **LangGraph** and **LangChain**.

---

## ✨ Features

* Conversational AI powered by LLaMA3-8B (via Groq).
* LangGraph-based reasoning with tool support.
* Lightweight terminal interface (`python main.py`).
* Modular and easy to extend (custom tools, memory, agents).

---

## 🧰 Technologies Used

* Python
* LangGraph
* LangChain
* Groq API (LLaMA3-8B)
* Tool integrations: Search and Calculator

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```

### 2. (Optional) Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**If you don’t have `requirements.txt`, run:**

```bash
pip install langgraph langchain langchain-community python-dotenv groq
```

### 4. Set Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
```

Or export in terminal:

```bash
export GROQ_API_KEY=your_groq_api_key     # Mac/Linux
set GROQ_API_KEY=your_groq_api_key        # Windows CMD
```

---

### 5. Run the Application

```bash
python main.py
```

Example output:

```
❓ Ask something: who is the current president of the US?
⚙️ Running AI Agent...

✅ Done!
🤖 Response: As of 2024, the President of the United States is Joe Biden.
```

---

## 📁 File Structure

```
.
├── main.py             # Entry point to run the agent
├── agent_graph.py      # LangGraph setup and agent definition
├── tools.py            # Tool implementations (e.g., search, calculator)
├── .env                # Environment variables (GROQ_API_KEY)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📸 Terminal Screenshot

<img width="800" alt="terminal-output" src="https://github.com/user-attachments/assets/a1ae891d-f0d3-4905-a238-bbf8b21fe5bc" />

---

## ⚠️ Notes

* You may face rate limits using Groq's free API key. Consider a paid plan for production use.
* Ensure you're using Python 3.9+ and have `langchain-community` installed (required by latest LangChain versions).
* Works entirely in terminal—no browser needed!

---

## 🧑‍💻 Author

Built by [Your Name](https://github.com/your-username) as part of the [LangGraph AI Agent course](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph).

---

## 📄 License

This project is open-source and free to use for educational or experimental purposes.

---
