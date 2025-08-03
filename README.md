# 🧠 Reflection Agent Tweet Generator with LangGraph

This project implements a **Reflection Agent** using [LangGraph](https://github.com/langchain-ai/langgraph), designed to generate high-quality and context-aware tweets. The agent is capable of iteratively refining its outputs using structured reflection loops to improve clarity, engagement, and originality.

## 🚀 Features

- ✍️ Generates concise, engaging tweets on various topics
- 🔁 Uses a reflection loop to improve tweet quality
- 🧠 Human-in-the-Loop (HITL) mechanism allows users to review, reject, or approve tweets for better control and satisfaction
- 🧩 Modular design with LangGraph for flexibility and extensibility
- 🔌 Easy to plug in your own prompt templates, models, or evaluators

## 📌 Use Cases

- Personal branding / thought leadership automation  
- Content creation for X (formerly Twitter)  
- Experimentation with reflection-style agents  
- NLP education and LangGraph demos  

## 🛠️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph)  
- OpenAI API / LLM of your choice  
- Python 3.11+  
- LangChain 

## 🧠 Agent Architecture

The agent follows a **reflect-think-write** loop:
1. **Generator Node**: creates an initial draft of a tweet.
2. **Critic Node**: critiques the draft based on style, clarity, or engagement.
3. **human feedback**: after 2 iterations user decides when to regenerate the tweet or finish.
4. **Final Output Node**: outputs the polished tweet.

---------------------------------------------------------------------------------


## 🚀 Getting Started

Follow these steps to set up and run the project:

### 1. Install Python 3.11 or higher  
Ensure you have **Python 3.11+** installed on your system.  
You can check your version with:

```bash
python --version
```
2. Install dependencies
Use pip to install all required packages:

```bash
pip install -r requirements.txt
```
3. Set up environment variables
Create a .env file in the root directory and configure the necessary environment variables.

💡 Example:
---- .env.example ----

4. Run the Tweet Generator
Start the generator with:

```bash
python workflow.py
```

5. Enable Tracing with LangSmith
LangSmith helps trace and debug your agents effectively.
Check out the:

[tracing](https://docs.smith.langchain.com/concepts/tracing).

6. (Optional) Use LangGraph Studio
You can launch an interactive development studio for LangGraph using:

```bash
langgraph dev
```

