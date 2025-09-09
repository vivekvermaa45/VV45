import streamlit as st

import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBMPfIT7DpxTBRqrnNyV2LY8mC-YuhDhQs") # <- Replace with your actual key!

# Function to get response from Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Set the page title and icon
st.set_page_config(page_title="My AI Assistant", page_icon="🤖")
st.title("🤖 My Personal AI Assistant")

# Create a sidebar for navigation
page = st.sidebar.selectbox("Choose a Module", ["Summary Creator", "Language Enhancer", "Schedule Maker", "My Portfolio"])

# Module 1: Summary Creator
if page == "Summary Creator":
    st.header("📝 Summary Creator")
    user_input = st.text_area("Paste your long text here:", height=200)
    if st.button("Summarize!"):
        if user_input:
            prompt = f"Summarize the following text in about 100 words:\n\n{user_input}"
            summary = get_gemini_response(prompt)
            st.success(summary)
        else:
            st.warning("Please enter some text to summarize.")



# Module 2: Language Enhancer
elif page == "Language Enhancer":
    st.header("✨ Language Enhancer")
    user_input = st.text_area("Paste your rough text here:", height=200)
    if st.button("Enhance!"):
            if user_input:
                prompt = f"Rewrite the following text to be more professional, clear, and polished for a business setting. Do not change its core meaning:\n\n{user_input}"
                enhanced_text = get_gemini_response(prompt)
                st.success(enhanced_text)
            else:
                st.warning("Please enter some text to enhance.")


# Module 3: Schedule Maker
elif page == "Schedule Maker":
    st.header("📅 Daily Schedule Maker")
    user_input = st.text_input("Describe your day in a sentence (e.g., 'I need to gym for 1 hr, work for 3 hours, and lunch at 1 pm'):")
    if st.button("Make Schedule!"):
        if user_input:
            prompt = f"Create a structured time-based schedule for the following tasks: {user_input}. Format it as a clear list with estimated times."
            schedule = get_gemini_response(prompt)
            st.info(schedule)
        else:
            st.warning("Please describe your day.")

# Module 4: Portfolio Page
elif page == "My Portfolio":
    st.header("👨‍💻 My Portfolio")
    st.subheader("Vivek Verma")
    st.write("""
    **Data Scientist & AI Enthusiast**
    
    This is my personal AI assistant project, showcasing my skills in Python, NLP, and building applications with LLMs.
    
    **Skills:** Python, Data Analysis, Machine Learning, LLMs
    
    **GitHub:** https://github.com/vivekvermaa45
    
    **Email:** vivekvermafzd460@gmail.com
    """)
    # You can add more details here later


