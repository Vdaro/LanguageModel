# load the large language model file
from llama_cpp import Llama

#
import streamlit as st


def prompting(_prompt):
    # create a text prompt
    prompt = " Q : " + str(_prompt) + " A : "
    # generate a response ( takes several seconds )
    output = LLM(prompt)
    # display the response
    #    print(output["choices"][0]["text"])
    st.write(output["choices"][0]["text"])


st.title("💬 Chatbot")
prompt = str(st.chat_input("Write your message"))

# with st.sidebar:
with st.chat_message("assistant"):
    LLM = Llama(model_path="./llama-2-7b.Q4_K_M.gguf")
#    LLM.max_new_token = 512
    prompting(prompt)
# st.button('Execute', on_click=prompting(prompt))


