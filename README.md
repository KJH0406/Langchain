# LangChain Service Develop

![logo](https://github.com/KJH0406/Langchain/assets/109582129/c46040bb-0b2d-4775-be36-1b5adbbf4cee)

<br>

# Demo Projects

| Name                                                                                             | Description                                                             |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| [Conversation_Chatbot](https://github.com/KJH0406/Langchain/tree/main/Demo/Conversation_Chatbot) | RAG 기반의 대화형 챗봇 구현                                             |
| [QnA_Chatbot](https://github.com/KJH0406/Langchain/tree/main/Demo/QnA_Chatbot)                   | RAG 기반의 독립형 질문 챗봇 구현                                        |
| [PDF_SummaryWeb](https://github.com/KJH0406/Langchain/tree/main/Demo/PDF_SummaryWeb)             | PyPDF와 스트림릿(streamlit)을 활용하여 PDF 요약 웹사이트 구현           |
| [RAG_Chatbot](https://github.com/KJH0406/Langchain/tree/main/Demo/RAG_Chatbot)                   | Chat-GPT 모델과 랭체인(Langchain)을 활용하여 RAG 기반 챗봇 구현         |
| [Simple_Chatbot](https://github.com/KJH0406/Langchain/tree/main/Demo/Simpe_Chatbot)              | Chat-GPT 모델과 스트림릿(streamlit)을 활용하여 웹앱 기반 기초 챗봇 구현 |

<br>

# 기본 환경 설정(MAC)

1. 아나콘다 설치

   64-Bit Graphical Installer 설치 (윈도우 동일)

   [Installing on macOS — Anaconda documentation](https://docs.anaconda.com/free/anaconda/install/mac-os/)

2. 가상환경 생성

   터미널에서 아래 코드 입력

   ```
   conda create -n llm python=3.8
   ```

3. 가상환경 생성 확인 및 활성화(터미널 왼쪽에 llm 표시 = 활성화)

   ```
   conda env list
   conda activate llm
   ```

4. 주피터 노트북 설치

   ```
   pip install ipykernel

   *mac에서는 pip install notebook 해줬음.
   ```

5. 가상환경에 커널 연결

   ```
   python -m ipykernel install --user --name llm --display-name "llm"
   ```

6. 주피터 노트북 접속

   ```
   jupyter notebook
   ```
