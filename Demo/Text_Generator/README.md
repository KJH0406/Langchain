# 0. Summary

    💡 chat-gpt 모델과 스트림릿(streamlit)을 활용하여 텍스트 생성 봇 구현(이메일 작성을 예제로 구현)

<br>

# 1. Display

![localhost_8502_ (3)](https://github.com/KJH0406/Langchain/assets/109582129/a15371ad-f636-47fd-b375-830de529d7d5)

<br>

# 2. Setting

|                 |                              |
| --------------- | ---------------------------- |
| Library         | langchain, openai, streamlit |
| Language Model  | gpt-4                        |
| Embedding Model | -                            |
| Vector Database | -                            |
|                 |                              |

<br>

# 3. Issues

- OpenAI LLM 모델 호출 방식 변경

  - 기존

    ```python
    from langchain.llms import OpenAI

    def loadLanguageModel():
        return OpenAI(temperature=.7, model_name='gpt-4')
    ```

  - 변경 후

    ```python
    from langchain.chat_models import ChatOpenAI

    def loadLanguageModel():
        return ChatOpenAI(temperature=.7, model_name='gpt-4')
    ```

 <br>

- 더 다양한 구현을 위해서 입력 함수 및 query_template 수정
- **query_template을 더 고도화 할 수록 원하는 상황 맥락에 맞추어, 더 높은 정확도로 출력됨.**

  - 기존

    ```python
      def getTextInfo():
          input_text = st.text_area(label="메일 입력", label_visibility='collapsed', placeholder="메일 내용을 입력해주세요", key="input_text")
          return input_text

          input_text = getTextInfo()

      query_template = """
          메일을 작성해주세요.
          아래는 이메일입니다:
          이메일 내용: {email}
      """
    ```

  - 변경 후

    ```python
     # 상황
     def getEmailSituation():
         return st.text_input(label="상황", placeholder="예: 회의 취소 알림")
     # 목적
     def getEmailPurpose():
         return st.text_input(label="목적", placeholder="예: 이번 주 금요일 예정된 회의를 취소하려고 합니다.")
     # 상세 내용
     def getEmailDetails():
         return st.text_area(label="상세 내용", placeholder="상세 내용을 입력해주세요")
     # 작성자
     def getAuthor():
         return st.text_input(label="작성자", placeholder="예: 홍길동")
     # 이메일 톤 - selectbox 사용, 옵션에 사용하고 싶은 톤 추가 가능
     def getEmailTone():
         return st.selectbox(label="이메일 톤", options=["정중한", "친근한", "공식적인", "비공식적인"])
     # 수신자
     def getRecipient():
         return st.text_input(label="수신자", placeholder="예: 팀원, 고객, 상사")

     situation = getEmailSituation()
     purpose = getEmailPurpose()
     details = getEmailDetails()
     author = getAuthor()
     tone = getEmailTone()
     recipient = getRecipient()


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

    ```
