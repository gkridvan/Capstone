import streamlit as st
import pandas as pd
from langchain.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain.chains import LLMChain
import difflib

@st.cache_resource
def load_csv():
    df = pd.read_csv("articles.csv")  
    return df

@st.cache_resource
def load_model():
    return OllamaLLM(model='llama2')

df = load_csv()
model = load_model()

human_template = ChatMessagePromptTemplate.from_template("User: {question}", role="user")
chat_prompt = ChatPromptTemplate.from_messages([human_template])

chain = LLMChain(prompt=chat_prompt, llm=model)

st.title("Botino")
st.write("Ask something!")

user_input = st.text_input("User:", "")

chat_container = st.container()

if st.button("Gönder"):
    if user_input:
        with chat_container:
            st.chat_message("user").write(user_input)

        response = chain.run(question=user_input)  

        with chat_container:
            st.chat_message("assistant").write(f"Botino: {response}")  

        best_matches = difflib.get_close_matches(user_input, df['Title'], n=4, cutoff=0.3)

        if best_matches:
            with chat_container:
                st.chat_message("assistant").write("Here are some related news articles:")

            for match in best_matches:
                matched_row = df[df['Title'] == match].iloc[0]

                news_title = matched_row['Title']
                news_image_url = matched_row['Image URL']
                news_slug = matched_row['Slug']
                news_ID = matched_row['ID']
                news_link = f"https://www.rtbf.be/article/{news_slug}-{news_ID}"

                with chat_container:
                    st.chat_message("assistant").markdown(f"""
                        <div style="display: flex; align-items: center; margin-top: 10px;">
                            <a href="{news_link}" target="_blank" style="text-decoration: none;">
                                <img src="{news_image_url}" alt="{news_title}" style="width: 100px; height: 100px; margin-right: 10px;">
                                <span style="font-size: 16px; font-weight: bold; color: #0066cc;">{news_title}</span>
                            </a>
                        </div>
                    """, unsafe_allow_html=True)
            
        else:
            with chat_container:
                st.chat_message("assistant").write("No matching news found. Please try again.")

    else:
        with chat_container:
            st.chat_message("assistant").write("I didn't get it. Could you please clarify?")
