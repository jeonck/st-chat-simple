from openai import OpenAI
import streamlit as st

with st.sidebar:
    st.markdown("# OpenAI API Key First!")
    openai_api_key = st.text_input("", placeholder="openai_api_key", key="chatbot_api_key", type="password")
    "[Create OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("🤖 ChatGPT")
# st.caption("Using ChatGPT")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please input your OpenAI API key in the sidebar.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
