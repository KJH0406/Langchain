# 0. Summary

    💡 RAG 기반의 독립형 질문 챗봇 구현

<br>

# 1. Display

     query = chat_input("질문을 입력해주세요.") => "줄거리를 설명해줘"

## 1-1. gpt-3.5-turbo-16k-0613 결과

    간단하게 요약한 결과 출력

![QnA-1](https://github.com/KJH0406/Langchain_study/assets/109582129/1ad5675e-3d8b-4e2b-9a74-ef75fc3ced43)

<br>

## 1-2. gpt-4 결과

    gpt-3.5-turbo-16k-0613 보다는 상세한 줄거리 결과 출력

![QnA-2](https://github.com/KJH0406/Langchain_study/assets/109582129/a299c723-5c50-4b9b-96b5-ae34e6546de0)

<br>

# 2. Setting

|                 |                               |
| --------------- | ----------------------------- |
| Library         | langchain, streamlit, PyPDF2  |
| Language Model  | gpt-3.5-turbo-16k-0613, gpt-4 |
| Embedding Model | all-MiniLM-L6-v2              |
| Vector Database | FAISS                         |
|                 |                               |

<br>

# 3. Issues

- 파일 위치, 스트림릿 실행 과정은 전과 동

<br>

- 성능 비교를 위한 llm 모델 수정
  - gpt-3.5-turbo-16k-0613 ⇒ gpt-4 => gpt-3.5-turbo-16k-0613
