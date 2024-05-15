# 1.Display

![simple_chatbot](https://github.com/KJH0406/Langchain_study/assets/109582129/abe9f0a0-05e0-4fa3-bf6e-752e42dc7c39)

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

# 3.Issues

- llm 모델 수정
  - gpt-4-0314 ⇒ gpt-4

 <br>

- Jupyter 내의 Download as 기능을 찾지 못했음

  - Python 변환은 Home에서 터미널 생성 후 아래 코드를 통해 변환 파일 생성
    ```python
    jupyter nbconvert --to script Simple_Chatbot.ipynb
    ```

<br>

- Scripts 위치 찾지 못했음

  - 위와 마찬가지로, Home에서 터미널 생성 후 아래 코드를 통해 streamlit 실행

    ```python
    streamlit run Simple_Chatbot.py
    ```
