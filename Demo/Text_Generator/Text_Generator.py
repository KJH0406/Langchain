import streamlit as st
import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

# 환경 변수 설정
os.environ["OPENAI_API_KEY"] = "sk"  # 실제 OpenAI API 키로 변경 필요

# 페이지 설정
st.set_page_config(page_title="이메일 작성 봇", page_icon="🤖")
st.header("이메일 작성에 활용할 정보를 입력해주세요.")

# 입력 함수들
def getEmailSituation():
    return st.text_input(label="상황", placeholder="예: 회의 취소 알림")

def getEmailPurpose():
    return st.text_input(label="목적", placeholder="예: 이번 주 금요일 예정된 회의를 취소하려고 합니다.")

def getEmailDetails():
    return st.text_area(label="상세 내용", placeholder="상세 내용을 입력해주세요")

def getAuthor():
    return st.text_input(label="작성자", placeholder="예: 홍길동")

def getEmailTone():
    return st.selectbox(label="이메일 톤", options=["정중한", "친근한", "공식적인", "비공식적인"])

def getRecipient():
    return st.text_input(label="수신자", placeholder="예: 팀원, 고객, 상사")

# 사용자 입력 받기
situation = getEmailSituation()
purpose = getEmailPurpose()
details = getEmailDetails()
author = getAuthor()
tone = getEmailTone()
recipient = getRecipient()

# 텍스트 변환 작업을 위한 템플릿 정의
query_template = """
메일을 작성해주세요.
상황, 목적, 이메일 내용, 이메일 톤, 수신자의 내용을 참고하여, 설명을 구체적으로 해주세요.
글의 첫 문단은 가장 먼저 상황에 대해서 작성해주세요.

상황: {situation}
목적: {purpose}
이메일 내용: {details}
작성자: {author}
이메일 톤: {tone}
수신자: {recipient}
"""

# 프롬프트템플릿 인스턴스 생성
prompt = PromptTemplate(
    input_variables=["situation", "purpose", "details", "author", "tone", "recipient"],
    template=query_template,
)

# 언어 모델을 호출
def loadLanguageModel():
    return ChatOpenAI(temperature=.7, model_name='gpt-4')
    # 온도(temperature)값의 범위는 0에서 무한대, 일반적으로 0.5 ~ 1.0 사이의 값을 주로 사용(기본 값은 0.7)
    # 정보성 글일때는 낮은 온도를 사용하고 창의성이 필요한 경우에는 높은 온도로 설정하여 사용

# 버튼 생성 및 결과 표시
if st.button("이메일 작성", type='secondary', help="버튼을 누르면 이메일이 생성됩니다."):
    if all([situation, purpose, details, author, tone, recipient]):
        llm = loadLanguageModel()
        prompt_with_email = prompt.format(situation=situation, purpose=purpose, details=details, author=author, tone=tone, recipient=recipient)
        formatted_email = llm.predict(prompt_with_email)
        st.markdown("### 작성된 이메일:")
        st.write(formatted_email)
    else:
        st.warning("모든 필드를 입력해주세요.")
