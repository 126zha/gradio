# Museum Introduction WEB UI
The project is a simple demo of the application of AI in the field of museum introduction. The purpose of this demo is to demonstrate the potential use of LLM in the introduction to the relics whilst no introducer is available.
## How To Use
1. Download Python3. It may take a while.
2. Prepare required package: Download Gradio and ZhipuAI by
```shell
pip install gradio==4.16.0
pip install zhipuai==2.0.1
```
3. run 
```shell
python3 museum-introduction.py
```
under the folder "Museum-Introduction"

4. Wait until message "Running on local URL:  http://127.0.0.1:7860" is shown, then open the URL in a browser. E.g. Firefox, Chrome. Notice that the WEB UI should be used whilst the Internet connection is established.

**Or:**

You may firstly run "install.bat", then run "run.bat" to launch the WEB UI, both of which are under the folder "gradio-main"
## WEB UI Introduction
Click the button to display the according information and picture of the relic. The AI will provide basic information. If further information is required, ask AI in the 'Question' Box, the AI will soon reply.
