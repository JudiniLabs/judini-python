from judini.codegpt.chat import Completion
import streamlit as st


st.set_page_config(page_title="CodeGPT Chat", layout="wide")
st.title("CodeGPT Chat")

if "codegpt_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = None

if "agent_id" not in st.session_state:
    st.session_state["agent_id"] = None

if "messages" not in st.session_state:
    st.session_state["messages"] = []

CODEGPT_API_KEY = st.sidebar.text_input("CodeGPT API Key", type="password", value=st.session_state.get("codegpt_api_key"))
if not CODEGPT_API_KEY:
    st.sidebar.info("Please enter your CodeGPT API key.")
    st.stop()
AGENT_ID = st.sidebar.text_input("Agent ID", value=st.session_state.get("agent_id"))
if not AGENT_ID:
    st.sidebar.info("Please enter an Agent ID.")
    st.stop()
enable_stream = st.sidebar.checkbox("Enable Stream", value=True)
if st.sidebar.button("Clear message history"):
    st.session_state["messages"] = []
    st.rerun()

completion = Completion(api_key=CODEGPT_API_KEY)


for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_query := st.chat_input("How can I help you?"):
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        st.session_state["messages"].append({"role": "user", "content": user_query})
        msgs = st.session_state["messages"]
        ai_response = ""
        if enable_stream:
            message_placeholder = st.empty()
            with st.spinner("Wait for it..."):
                response = completion.create(AGENT_ID, msgs, stream=True)
            for chunk in response:
                ai_response += chunk
                message_placeholder.markdown(ai_response)
                
        else:
            with st.spinner("Wait for it..."):
                ai_response = completion.create(AGENT_ID, msgs, stream=False)
                st.markdown(ai_response)
        st.session_state["messages"].append({"role": "assistant", "content": ai_response})