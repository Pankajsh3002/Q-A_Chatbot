# Q&A Chatbot 

🔗 **Live Application:** [askquery-chatbot.streamlit.app](https://askquery-chatbot.streamlit.app/)

A clean, interactive web application built with **Streamlit** and powered by **LangChain** and **Google Gemini** models. This app allows users to choose their preferred Gemini model, tune inference configurations (temperature and output token limits) dynamically, and ask questions through a form-batch interface.

## Features  

- **Interactive UI:** Dynamic settings sidebar built with Streamlit.
- **Model Flexibility:** Toggle seamlessly between different Gemini models (`Gemini 3.1 Flash-Lite`, `Gemini 2.5 Flash`, `Gemini 2.0 Flash`).
- **Real-time Parameters Tuning:** Sliders to customize `Temperature` and `Max Tokens`.
- **Form Batching:** Integrated form submission button to prevent accidental API requests while typing.
- **Robust Orchestration:** Powered by LangChain's Expression Language (LCEL) using prompt templates and structured output string parsers.

---

## Tech Stack

- **Frontend Interface:** Streamlit
- **LLM Orchestration:** LangChain Core & LangChain Google GenAI Integration
- **Inference Models:** Google Gemini Architecture

---

## Getting Started (Local Setup)

Follow these steps to set up the project sandbox on your local Windows system.

### 1. Clone the Repository
```bash
git clone [https://github.com/Pankajsh3002/Q-A_Chatbot.git](https://github.com/Pankajsh3002/Q-A_Chatbot.git)
cd Q-A_Chatbot