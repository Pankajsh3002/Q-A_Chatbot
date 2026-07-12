import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please to the user queries"),
        ("user","Question: {question}"),
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    
    ## Model Initialization
    llm = ChatGoogleGenerativeAI(
        model=llm, 
        google_api_key=api_key, 
        temperature=temperature, 
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer=chain.invoke({"question": question})

    return answer



## Title
st.title("Q&A Chatbot")

## Sidebar setting 

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")


## Dropdown for model selection

model_mapping = {
    # "Gemini 3.5 Flash (Recommended)": "gemini-3.5-flash",
    "Gemini 3.1 Flash-Lite": "gemini-3.1-flash-lite",
    "Gemini 2.5 Flash": "gemini-2.5-flash",
    "Gemini 2.0 Flash": "gemini-2.0-flash"
}



selected_model_name = st.sidebar.selectbox("Select Model", list(model_mapping.keys()))
llm_string = model_mapping[selected_model_name]


## Adjust model setting in sidebar
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


## Mian Interface for user input

st.write("Ask any question and get an answer from the chatbot!")

with st.form(key="chatbot_form"):
    user_input = st.text_input("Enter your question here:", placeholder="Type your question here...")
    
    # 2. Add the form submit button
    submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        if not user_input.strip():
            st.warning("Please type a question before submitting.")
        elif not api_key:
            st.error("Please enter your Google API Key in the sidebar.")
        else:
            with st.spinner("Generating response..."):
                try:
                    # Pass the corrected model string identifier
                    response = generate_response(user_input, api_key, llm_string, temperature, max_tokens)
                    st.success("Response generated!")
                    st.write("**Answer:**")
                    st.write(response)
                except Exception as e:
                    st.error(f"Failed to fetch response: {e}")