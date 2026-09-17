import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool 

load_dotenv()
api_key= os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Langchain AI Chatbot", page_icon="", layout="wide")
st.title("Langchain AI Chatbot")
if not api_key:
    st.error("Create a .env file with GROQ_API_KEY")
    st.stop()
temperature = st.sidebar.slider("Temperature", 0.0,1.0,0.2,0.1)
llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key= api_key,
    temperature=temperature
)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
if "messages" not in st.session_state:
    st.session_state.messages=[]
def calculator(expr):
    try:
        return str(eval(expr,{"__builtins__":()}))
    except Exception as e:
        return str(e)
calc_tool = Tool(
    name= "Calculator",
    func= calculator,
    description= "Math Calculator"
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant"),
    MessagesPlaceholder (variable_name="history"),
    ("human", "{question}")
])

parser = StrOutputParser()
for role,msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)
question = st.chat_input("ask Anything....")
if question:
    st.session_state.messages.append(("user", question))
    with st.chat_message("user"):
        st.markdown(question)
    if question.lower().startswith("calculate"):
        answer = calc_tool.run(question.replace("calculate","",1).strip())
    else:
        chain = prompt| llm | parser
        answer = chain.invoke({
            "history": st.session_state.memory.chat_memory.messages,
            "question":question
        })
        st.session_state.memory.chat_memory.add_user_message(question)
        st.session_state.memory.chat_memory.add_ai_message(answer)
        st.session_state.messages.append(("assistant", answer))
        with st.chat_message("assistant"):
            st.markdown(answer)
if st.sidebar.button("Clear Chat"):
    st.session_state.messages=[]
    st.session_state.memory.clear()
    st.rerun()
    