import gradio as gr
from PIL import Image

title="博物馆小助手"

description = "点击按钮，向AI提关于该文物的问题"

image_patha = "GradioTutorial/Artifacts/A/pic.jpg"
image_pathb = "GradioTutorial/Artifacts/B/pic.jpg"
image_pathc = "GradioTutorial/Artifacts/C/pic.jpg"
image_pathd = "GradioTutorial/Artifacts/D/pic.jpg"


situation = ''


def greeta ():
    image=Image.open(image_patha)
    a1='马踏飞燕' #介绍
    global situation
    situation = 'a'
    return image,a1
def greetb ():
    image=Image.open(image_pathb)
    b1='av'
    global situation
    situation = 'b'
    return image,b1
def greetc ():
    image=Image.open(image_pathc)
    c1='gv'
    global situation
    situation = 'c'
    return image,c1
def greetd ():
    image=Image.open(image_pathd)
    d1='vev'
    global situation
    situation = 'd'
    return image,d1
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
    a.click(fn=greeta,inputs=[],outputs=[imagew,introduction])
    b.click(fn=greetb,inputs=[],outputs=[imagew,introduction])
    c.click(fn=greetc,inputs=[],outputs=[imagew,introduction])
    d.click(fn=greetd,inputs=[],outputs=[imagew,introduction])
demo.launch()