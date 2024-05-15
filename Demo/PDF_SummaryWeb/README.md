# 0. Summary

    💡 PyPDF와 스트림릿(streamlit)을 활용하여 PDF 요약 웹사이트 구현

<br>

# 1. Display

    - LLM에 PDF파일 요약 요청
    - query = "업로드된 PDF 파일의 내용을 약 15 문장으로 요약해주세요."

<br>

## 1-1. gpt-3.5-turbo-16k 결과

![PDF-1](https://github.com/KJH0406/Langchain_study/assets/109582129/569d1329-aa64-4660-b013-240465f25fb9)

<br>

## 1-2. gpt-4 결과

![PDF-2](https://github.com/KJH0406/Langchain_study/assets/109582129/3877e2a4-3ddc-4975-b8e9-2fe997b0809d)

<br>

# 2. Setting

|                 |                                                     |
| --------------- | --------------------------------------------------- |
| Library         | langchain, streamlit, PyPDF2, sentence-transformers |
| Language Model  | gpt-3.5-turbo-16k, gpt-4                            |
| Embedding Model | all-MiniLM-L6-v2                                    |
| Vector Database | FAISS                                               |
|                 |                                                     |

<br>

# 3. Issues

- Jupyter 내의 Download as 기능을 찾지 못했음
  - Python 변환은 Home에서 터미널 생성 후 해당 파일이 있는 위치까지 이동(cd)
    ```python
    cd Demo/PDF_SummaryWeb
    ```
  - 해당 파일이 위치한 곳에서 아래 코드를 통해 변환 파일 생성
    ```python
    jupyter nbconvert --to script PDF_SummaryWeb.ipynb
    ```

<br>

- Scripts 위치 찾지 못했음

  - 위와 마찬가지로, 해당 파일이 위치한 곳의 터미널에서 아래 코드를 통해 streamlit 실행

    ```python
    streamlit run PDF_SummaryWeb.py
    ```

<br>

- streamlit 실행 시, NameError: name 'get_ipython' is not defined 라는 에러 발생 - Streamlit 환경에서 `pip` 명령어 직접 실행하여 생기는 에러임. 따라서, 이전에 했던 것처럼 **라이브러리 설치했던 부분들을 모두 주석 처리** 해주어야함!

          ```python
          # !pip install langchain
          # !pip install streamlit
          # !pip install PyPDF2
          # !pip install sentence-transformers
          ```

  <br>

- 성능 비교를 위한 llm 모델 수정
  - gpt-3.5-turbo-16k ⇒ gpt-4 => gpt-3.5-turbo-16k

<br>

- 파일 크기가 큰 문서 요약 결과도 확인하기 위해 쿼리에서 요약 문장 조건 수정

        [기존] query = "업로드된 PDF 파일의 내용을 약 3~5문장으로 요약해주세요."
        [변경] query = "업로드된 PDF 파일의 내용을 약 15문장으로 요약해주세요."
