import gradio as gr
from PIL import Image
import zhipuai
from zhipuai import ZhipuAI
import os

name_refer = {
    "a": "马踏飞燕",
    "b": "仪礼简",
    "c": "人头形器口彩陶瓶",
    "d": "东罗马神人纹鎏金银盘"
}

client = ZhipuAI(api_key = "c075c10b0d98a821e49af2ba4b5b1424.xk4AlAwO9oUiOEyw")

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
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, "Artifacts", relic)
    img_path = os.path.join(path, "pic.jpg")
    intro_path = os.path.join(path, "intro.txt")
    
    try:
        image = Image.open(img_path, "r")
        intro = open(intro_path, "r", encoding="UTF-8").read()
    except:
        print(f"Failed to open File with argument relic_id = {relic} with path = {img_path, intro_path}")
        image = None
        intro = ""
    global situation
    situation = relic
    
    def func():
        global history
        prompt = f"""
你是一个人工智能助手。现在，你将被提供一份关于文物“{name_refer[relic]}”的简介。
{intro}
请根据接下来的提问，结合这一份简介作出回答。"""
        history = [
            {"role":"user", "content": prompt}
        ] # Clear the original history, ready for a new relic.
        # Note that this is not finished, and should be done with a find-tuned prompt.
        return image, intro
    return func

def LLM_Reply(question: str) -> str:
    """
    Main AI Function, provided to return the answer to the user question.

    Parameters:
    ----------
    question : str
        An arbitrary string, provided by user, and is thus not controllable.
    
    Return value:
    ----------
    answer : str
        A string, produced by ZhipuAI API (https://maas.aminer.cn/pricing). This should be the answer to the input.
    """
    history.append(
        {"role":"user", "content":question}
    )
    response = client.chat.completions.create(
        model = "glm-3-turbo",
        messages = history,
    )
    answer = response.choices[0].message.content
    history.append(
        {"role":"assistant", "content":answer}
    )
    """ ADD # TO DEBUG, DEL TO UNDO
    print(answer)
    print(history)
    #"""
    return answer # It seems that 'answer' needs a modification

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
        with gr.Group():
            chatbot = gr.Chatbot(height=300)
            question=gr.Textbox(label = "问题",
                            placeholder = "如果您有问题，可以在此进一步输入！",
                            interactive = True)
            def respond(message, chat_history):
                bot_message = LLM_Reply(message)
                chat_history.append((message, bot_message))
                return "", chat_history
            question.submit(respond, [question, chatbot], [question, chatbot])
            with gr.Row():
                sbmt = gr.Button(value = "提交")
                clear = gr.ClearButton([chatbot, question])
        with gr.Group():
            imagew = gr.Image()
            with gr.Row():
                Button_A=gr.Button(name_refer["a"])
                Button_B=gr.Button(name_refer["b"])
                Button_C=gr.Button(name_refer["c"])
                Button_D=gr.Button(name_refer["d"])
            introduction = gr.Textbox(label="introduction")
    
    Button_A.click(fn=greet('a'),inputs=[],outputs=[imagew,introduction])
    Button_B.click(fn=greet('b'),inputs=[],outputs=[imagew,introduction])
    Button_C.click(fn=greet('c'),inputs=[],outputs=[imagew,introduction])
    Button_D.click(fn=greet('d'),inputs=[],outputs=[imagew,introduction])
    sbmt.click( fn = respond,
                inputs = [question, chatbot],
                outputs = [question, chatbot])  # abreviation for 'SUBMIT', in case of conflict

if __name__ == "__main__":
    demo.launch()
########################  MAIN  ########################
