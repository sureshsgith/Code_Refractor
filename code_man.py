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


def generate_code(original_code):
    prompt="""
    Rewrite the given code by changing variable and identifier names while maintaining the same functionality. Also, rephrase and change the position of the code snippet, including the functions.
Example:
Given code=
def swap():
def partition():

Response code=
def partition():
def swap():

Note:

Add comments (2 to 4 words) .
Optimize the code by reducing the number of lines if possible.
Modify the test case according to the problem.
Example:
Given test case:
num[]=[5,1,10,4,7];

Updated test case:
numArray[]=[4,10,1,55,2];

Include fewer comments for better understanding.

    {original_code}

    """
    Final_prompt=PromptTemplate(template=prompt,input_variables=["original_code"])
    llm=ChatOpenAI(temperature=0.8,model="gpt-3.5-turbo-16k")
    llm_agent=LLMChain(
        llm=llm,
        prompt=Final_prompt,
        verbose=True
    )
    res=llm_agent.predict(original_code=original_code)
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
    output_code=generate_code(input_code)

if output_code!="":
    alert.success("Here is your Code...")
    st.caption("Refracted Code:")
    code=st.code(body=output_code,language=lang.lower())
st.markdown("<footer> by Suresh Rathod</footer>",unsafe_allow_html=True)
