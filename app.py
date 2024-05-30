import gradio as gr
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDVchcLAOKYfv_Cmz-qp2WQjJ8jM7SMNxI"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def verify(user_prompt):
    response = chat.send_message(f"""I heard news stating that {user_prompt}. Can you cross-reference it with sites on Google to let me know about it? Do NOT provide me references!! Just tell me if it's right or wrong and give me a brief description, around 25 words about it.""")
    return response.text

iface = gr.Interface(
    fn=verify,
    inputs="text",
    outputs="text",
    title="Verify Prompt",
    description="Enter a prompt and press enter to get verification result."
)

iface.launch()
