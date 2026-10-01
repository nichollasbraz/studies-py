# título
# campo de mensagem (input)
# quando o usuário enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar a mensagem para a IA responder
    # mostrar a resposta da IA

# streamlit e openai

import streamlit as st
from openai import OpenAI

modelAI = OpenAI(api_key="AQ.Ab8RN6K5_vxVz8fvvKfx0IlJHLNpx72WvYfgY7r9ZdV1767c1A",
                base_url="https://generativelanguage.googleapis.com/v1beta")

st.write("## Chatbot de IA")

if "msgLst" not in st.session_state:
    st.session_state["msgLst"] = []

msgUser = st.chat_input("Escreva sua mensagem aqui")

for msg in st.session_state["msgLst"]:
    whoSent = msg["role"]
    msgSent = msg["content"]

    st.chat_message(whoSent).write(msgSent)

if msgUser:
    st.chat_message("user").write(f"**Você perguntou**: {msgUser}")

    msg = {
        "role": "user",
        "content": msgUser
    }

    st.session_state["msgLst"].append(msg)

    answerAI = modelAI.chat.completions.create(
        messages=st.session_state["msgLst"],
        model="gemini-flash-lite-latest"
    )
    msgAI = f"**Assistente respondeu**: {answerAI.choices[0].message.content}"
    
    st.chat_message("assistant").write(msgAI)

    msg_2 = {
        "role": "assistant",
        "content": msgAI
    }

    st.session_state["msgLst"].append(msg_2)

print(msgUser)
