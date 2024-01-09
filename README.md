# streamlit_learn
 learn streamlit


테스트환경 : python 3.11.7
support version 3.8 to 3.12.

가상환경 만들기
python -m venv .venv

활성화 명령
# Windows command prompt
.venv\Scripts\activate.bat
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS and Linux
source .venv/bin/activate
비활성화 명령
deactivate

windows PowerShell error
Get-ExecutionPolicy
(RemoteSigned) 여야함
Set-ExecutionPolicy RemoteSigned




install

pip install streamlit

requirements.txt 만들기
pip freeze > requirements.txt


test 해보기
streamlit hello
python -m streamlit hello


로컬이 아닌 코드를 실행 할 수도 있다.
python -m streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py








Documentation
https://docs.streamlit.io/get-started



https://streamlit.io/

templite

https://github.com/MarcSkovMadsen/awesome-streamlit