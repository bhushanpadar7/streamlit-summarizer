import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app
def main():
    st.title("Text Summarization with Generative AI")
    st.write("Enter your text below:")

    user_input = st.text_area("Input Text", "")
    
    if st.button("Generate Summary"):
        if user_input:
            # Generate the summary
            summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            st.write("Generated Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

if __name__ == '__main__':
    main()
