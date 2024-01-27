import gradio as gr
from PIL import Image
import zhipuai

name_refer = {
    "a": "马踏飞燕",
    "b": "TestNameB",
    "c": "TestNameC",
    "d": "TestNameD"
}

zhipuai.api_key = "c075c10b0d98a821e49af2ba4b5b1424.xk4AlAwO9oUiOEyw"

history = []

title="博物馆小助手"

description = "点击按钮，向AI提关于该文物的问题"

situation = ''

def greet(relic: str):
    """The function should return a function, in which the image and introduction to the relic will be provided.
    
    Parameters:
    ----------
    relic : str
        A modified string transmitted from Gradio.Button. If this attribute cannot open file, 'None' will be returned for image, and an empty string will be returned for intro.
    
    Return Value:
    ----------
    A function. The function will return a tuple in format (image, introduction).
    """
    try:
        image = Image.open(f"GradioTutorial/Artifacts/{relic}/pic.jpg")
        intro = open(f"GradioTutorial/Artifacts/{relic}/intro.txt", "r").read()
    except:
        print(f"Failed to open File with argument relic_id = {relic}.")
        image = None
        intro = ""
    global situation
    situation = relic
    
    def func():
        global history
        prompt = f"""
        你是一个人工智能助手。现在，你将被提供一份关于{name_refer[relic]}的简介。
        {intro}
        请根据接下来的提问，结合这一份简介作出回答。
        """
        history = [
            {"role":"user", "content": prompt}
        ] # Clear the original history, ready for a new relic.
        # Note that this is not finished, and should be done with a find-tuned prompt.
        return image, intro
    return func

def ai(question: str) -> str:
    """
    A todo function, will be used to interact with AI,
    """
    history.append(
        {"role":"user", "content":question}
    )
    response = zhipuai.model_api.invoke(
        model = "glm-3-turbo",
        prompt = history,
        temperature = 0.,
    )
    answer = response['data']['choices'][0]['content']
    history.append(
        {"role":"AI", "content":answer}
    )
    print(history)
    return str(answer)# It seems that 'answer' needs a modification

def clear_input():
    """
    Clear the input and output of AI.

    Parameters:
    ----------
    No Parameters.

    Return Value:
    ----------
    A tuple with two empty string elements. The two strings will be returned to question block and answer block in Gradio Module to erase the content.
    """
    return "",""

########################  MAIN  ########################
with gr.Blocks() as demo:
    gr.Markdown("# 博物馆小助手")
    gr.Markdown("点击按钮，向AI提关于该文物的问题")
    with gr.Row():
        a=gr.Button("a")
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
########################  MAIN  ########################