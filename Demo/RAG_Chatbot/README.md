# 1.Display

## 1-1. gpt-3.5-turbo 모델을 사용하여 생성된 결과

    쿼리(질문)에 대하여 유사도 검색을 수행하여 적절한 답변을 생성하였음

![RAG-none](https://github.com/KJH0406/Langchain_study/assets/109582129/eb0c3274-60a4-4491-b8d8-78fdede76ac3)

<br>

## 1-2. gpt-4 모델을 사용하여 생성된 결과

    기존 gpt-3.5-turbo 모델보다 조금 더 상세하게 답변이 생성되는 것 같음

![RAG-4](https://github.com/KJH0406/Langchain_study/assets/109582129/2152d4e8-8f7d-4827-82ac-d1159090b2c2)

<br>

## 1-3. AI.txt에 담겨있는 내용과는 완전히 다른 질문을 한 결과

    유사도가 매우 낮은 질문에 대해서는 답변 불가능

![RAG-3](https://github.com/KJH0406/Langchain_study/assets/109582129/8f9c10a0-671e-43b3-898b-473e1bc02280)

<br>

# 2. Setting

|                 |                                                                  |
| --------------- | ---------------------------------------------------------------- |
| Library         | langchain, openai, unstructured, sentence-transformers, chromadb |
| Language Model  | gpt-3.5-turbo, gpt-4                                             |
| Embedding Model | all-MiniLM-L6-v2                                                 |
| Vector Database | chroma                                                           |
|                 |                                                                  |

<br>

# 3.Issues

- 성능 비교를 위한 llm 모델 수정 및 복구
  - gpt-3-turbo ⇒ gpt-4 => gpt-3-turbo
