import streamlit as st
import requests
import json

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("error:", response.text)

# Create Streamlit interface
st.title("Code Generator App")

# Create a text input for the prompt
prompt = st.text_area("Enter your Prompt", height=4)

# Check if the user has entered a prompt
if prompt:
    # Call your generate_response function with the entered prompt
    response = generate_response(prompt)

    # Display the generated response
    st.text("Generated Response:")
    st.text(response)
