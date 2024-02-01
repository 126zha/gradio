# Museum Introduction WEB UI
The project is a simple demo of the application of AI in the field of museum introduction. The purpose of this demo is to demonstrate the potential use of LLM in the introduction to the relics whilst no introducer is available.
## How To Use
write before,we should open the file gradio so that we can get the way to the pictures. if we open "GradioTutorial" we will find chatbot run correctly but cannot find the picture.
1. Download Python3. It may take a while.
2. Prepare required package: Download Gradio and ZhipuAI by
```shell
pip install gradio==4.16.0
pip install zhipuai==2.0.1
```
3. run 
```shell
python3 trygradio.py
```
1. Wait until message "Running on local URL:  http://127.0.0.1:7860" is shown, then open the URL in a browser. E.g. Firefox, Chrome. Notice that the WEB UI should be used whilst the Internet connection is established.
2. Maybe after we use open to the function launch we can get a new way to reach the web.
## WEB UI Introduction
Click the button to display the according information and picture of the relic. The AI will provide basic information. If further information is required, ask AI in the 'Question' Box, the AI will soon reply.
