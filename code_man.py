import streamlit as st 
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
st.markdown("<head> <title> Code Refractor </title></head>",unsafe_allow_html=True)
st.markdown("<h1 align=center>Code Refractor</h>",unsafe_allow_html=True)
# api_key=st.text_input("Enter OpeaAI Api key")
os.environ["OPENAI_API_KEY"]="sk"+"-2zRGrin2jnTtR31xl"+"Fh8T3BlbkFJJjEy9F8"+"clkdlN2l7KIap"


def generate_code(original_code,lang):
    prompt="""
I want to act as Expert in Manuplating the code in {lang} programming languages. I will provide a code . your task is to complete modify the identifiers ( variables, function ,parameters,etc..) names in the provided code. Also add the normal comments but not much. Also modify the test cases and generate it your own according to code problem.

    {original_code}

    """
    Final_prompt=PromptTemplate(template=prompt,input_variables=["original_code","lang"])
    llm=ChatOpenAI(temperature=0.8,model="gpt-3.5-turbo-16k")
    llm_agent=LLMChain(
        llm=llm,
        prompt=Final_prompt,
        verbose=True
    )
    res=llm_agent.predict(original_code=original_code,lang=lang)
    return res


lang=st.selectbox("Select a Programing Language",["C","C++","Java","python","Javascript","html"])


input_code=st.text_area("Enter your code:",height=500)
# output_section=col2.text_area("Refracted Code",height=500)
submit_btn=st.button("Submit")
spinner=st.empty()
alert=st.success("Click Submit Button")
if submit_btn:
    alert.success("Code on the Way.....")
output_code=""
if input_code != "": 
    output_code=generate_code(input_code,lang)

if output_code!="":
    alert.success("Here is your Code...")
    st.caption("Refracted Code:")
    code=st.code(body=output_code,language=lang.lower())
st.markdown("<footer> by Anonymous</footer>",unsafe_allow_html=True)
