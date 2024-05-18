# 0. Summary

    💡 RAG기반의 대화형 챗봇 구현

<br>

# 1. Display

    query = 이력서(resume)를 업로드하고 해당 지원자에 대한 설명 요청

<br>

![기록1](https://github.com/KJH0406/Langchain_study/assets/109582129/dd4329da-3c44-42ff-83d6-50b1b28793b6)

<br>

    추가적으로, 책 관련 PDF 파일의 내용 요약도 실행해보았음.

![localhost_8501_ (2)](https://github.com/KJH0406/Langchain_study/assets/109582129/4b153424-ad70-4f0f-8b18-f25fd67b7d89)

<br>

# 2. Setting

|                 |                                                 |
| --------------- | ----------------------------------------------- |
| Library         | langchain, streamlit, streamlit_chat, faiss-cpu |
| Language Model  | gpt-4                                           |
| Embedding Model | -                                               |
| Vector Database | FAISS                                           |
|                 |                                                 |

<br>

# 3. Issues

- 데이터 세트가 커질 수록 확실히 탐색과 처리가 느려지는 것이 체감되었음.

<br>

- 프로젝트 명이 깨져서 보이는 것으로 보아, PDF 데이터를 txt로 변환하는 과정에서 형식이나 구조가 잘못 변형되었던 것 같음.
