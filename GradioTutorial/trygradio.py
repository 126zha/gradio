import gradio as gr
from PIL import Image

title="博物馆小助手"

description = "点击按钮，向AI提关于该文物的问题"

situation = ''

def greet(relic):
    #print(relic)
    try:
        image = Image.open(f"GradioTutorial/Artifacts/{relic}/pic.jpg")
        intro = open(f"GradioTutorial/Artifacts/{relic}/intro.txt", "r").read()
    except:
        print(f"Failed to open File with argument relic = {relic}.")
        image = None
        intro = ""
    global situation
    situation = relic
    def func():
        return image, intro
    return func

def ai(question):
    question = list(question)
    #for i in question:
     #   if i == '时':
      #      word= 1
    if situation== 'a':
        return "ss"
    if situation== 'b':
        return 'ee'
    if situation=='c':
        return 'ev'
    if situation=='d':
        return 'dd'

def clear_input():
    return "",""

with gr.Blocks() as demo:
    gr.Markdown("# 博物馆小助手")
    gr.Markdown("点击按钮，向AI提关于该文物的问题")
    with gr.Row():
        a=gr.Button("马踏飞燕")
        b=gr.Button("b")
        c=gr.Button("c")
        d=gr.Button("d")
    imagew = gr.Image()
    introduction = gr.Textbox(label="introduction")
    with gr.Column():
        question=gr.Textbox(label="question")
        answer= gr.Textbox(label="answer")
    with gr.Row():
        submit=gr.Button("submit")
        clear=gr.Button("clear")
    
    
    
    submit.click(fn=ai,inputs=question,outputs=answer)
    clear.click(fn=clear_input,inputs=[],outputs=[question,answer])
    a.click(fn=greet('a'),inputs=[],outputs=[imagew,introduction])
    b.click(fn=greet('b'),inputs=[],outputs=[imagew,introduction])
    c.click(fn=greet('c'),inputs=[],outputs=[imagew,introduction])
    d.click(fn=greet('d'),inputs=[],outputs=[imagew,introduction])
demo.launch()