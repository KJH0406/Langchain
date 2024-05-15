#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!pip install langchain


# In[2]:


#!pip install streamlit


# In[6]:


#!pip install openai


# In[7]:


# 필요한 라이브러리 설치 후, streamlit 실행 시 오류 발생 방지를 위해 설치 코드 주석 처리


# In[5]:


import streamlit as st # 스트림릿
from langchain.chat_models import ChatOpenAI
st.set_page_config(page_title="🦜🔗 Ask anything! ")
st.title('🦜🔗 Ask anything! ')

import os
os.environ["OPENAI_API_KEY"] = "sk-"  #openai 키 입력

def generate_response(input_text):  #llm이 답변 생성
    llm = ChatOpenAI(temperature=0,  # 창의성 0으로 설정 
                 model_name='gpt-4',  # 모델명
                )
    st.info(llm.predict(input_text))

with st.form('Question'):
    text = st.text_area('Enter your question:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('Send')
    generate_response(text)

