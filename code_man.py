import streamlit as st 
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
st.markdown("<h1 align=center>Code Refractor</h>",unsafe_allow_html=True)
# api_key=st.text_input("Enter OpeaAI Api key")
os.environ["OPENAI_API_KEY"]="sk-"+"4Igq3BJ1vzdI4dfizaga"+"T3BlbkFJwYKy5mJsczVygMZqnplz"


def generate_code(original_code):
    prompt="""change the given code to another code with same functionality but change in the variable names and identifiers names
    note the varaible name and function name should change and rephrase it and also change the position of code snippet like changing the position of functions and more.
    example:
    in given code:
    def swap()
    def partition()
    in response code:
    def partition()
    def swap()
    Note: 
    - you should add the comments with 2 to 4 words by your own,just mention when it important to required.
    - rewrite the code with less line if possible
    - you should change the test case with according to problem by your own
    example:
    num[]=[5,1,10,4,7];
    then change to 
    numArray[]=[4,10,1,55,2];
    

    {original_code}

    """
    Final_prompt=PromptTemplate(template=prompt,input_variables=["original_code"])
    llm=ChatOpenAI(temperature=0.7,model="gpt-3.5-turbo-16k")
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
