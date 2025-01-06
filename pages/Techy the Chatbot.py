import streamlit as st
import openai

# -----------------------------
# 1. Configuration & Setup
# -----------------------------
st.set_page_config(page_title="TechLaunch Chatbot - Techy", layout="centered")

# Provide your OpenAI API key here or retrieve it from st.secrets / environment variables
openai.api_key = st.secrets["KEY"]

# Initial system message: set the context and style of Techy
SYSTEM_PROMPT = """\
You are Techy, an AI assistant for the TechLaunch program. \
You are helpful, friendly, and knowledgeable about the TechLaunch curriculum, structure, \
and any other details regarding the course. You only answer questions about TechLaunch.
If the user asks something unrelated to TechLaunch, politely respond that you can only assist \
with TechLaunch-related inquiries.


Course Overview:		
This course is designed to get students from zero programming knowledge to intermediate Python scripting.		
In addition to gaining technical and critical thinking skills, students will complete this course with a portfolio of projects to boost their college and internship/job applications.		
		
Who is this course for:		
- High-school seniors looking to boost their profile for college applications		
- College students looking to develop technical skills and profile for internship/job applications		
- High-schoolers curious about programming in general		
- Business-oriented individuals looking to leverage technology for business			
		
		
Course Takeaways:		
- Develop "problem-solving" skills through coding		
- Gain a deep understanding of coding fundamentals		
- Achieve intermediate "Python functional programming" level		
- Learn how to leverage AI to 10X learning speed and project management		
- Complete portfolio of Python projects hosted online		
		
Requirements:		
No previous programming knowledge required		
BYO Laptop		
		
Main Projects:		
Data Analysis		
Process Automation		
Agentic Artificial Intelligence		
		
		
		
		
Learning Path:		
		
Session #1	Intro to Programming and Python	
Why should I learn Python?		
Scripting Vs Coding		
Variables, Methods, Inputs, Outputs		
Commenting		
Integers, Strings, Lists (Basic data types)		
Conditional Statements		
Mini project #1 -  Simple Calculator / to-do list app		
		
Session #2	The power of algorithms 	
First session recap		
What is an algortihm?		
For Loops and While Loops		
Python Dictionaries (intermediate data types)		
Functions		
Mini project #2 - Message Decryption		
		
Session #3	Thinking like a Programmer	
First and second session recap		
Input-process-output mindset		
Divide and Conquer		
Pattern Recognition and algorithmic thinking		
Team project - Python Scavenger Hunt		
		
Session #4	Storytelling through Code	
Recap		
What does open-source mean?		
Leveraging other peoples' code		
Popular python packages		
Intro to the best Python tool you will ever learn		
ChatGPT for programmers		
Main Projects 1st step - Create the portfolio		
		
Session #5	Data Analysis	
Recap		
What is data?		
Intro to Pandas and Dataframes		
Code with structure using Jupyter Notebooks		
Intro to statistics (Average, Median, Min, Max)		
Aggregating data using groupby		
		
Session #6	Visualizing Data	
Recap		
Tables Vs Charts		
Intro to Plotly		
Main Project #1 - Supermaket Sales analysis dashboard		
		
Session #7	Automate Anything	
Recap - Complete Project #1		
What in an API?		
Tramsferring data between systems		
Main Project #2 - Process Automation		
		
Session #8	Python for the Future	
Recap - Complete Project #2		
What is a Large Language Model?		
Main Project #3 - Build custom AI chatbot		
		
Session #9	Next Steps	
Recap - Complete Project #3		
Complete Portfolio		
Paths for programming		
		
		



"""

# -----------------------------
# 2. Initialize Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]





st.info("Large Language Models (Artificial Intelligence systems like ChatGPT) are changing the world."
        " Using **Python** we can create our own custom chatbots and give them special instructions."
        " Chat with Techy, an AI chatbot created to answer any question on **TechLaunch** :rocket:")

if st.button("Clear Chat"):
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    st.rerun()

# -----------------------------
# 3. Display Past Messages
# -----------------------------
st.subheader("**:blue[Techy]** ")
st.write("Your TechLaunch Chatbot")

for msg in st.session_state["messages"][1:]:  # skip the system prompt in display
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])


# -----------------------------
# 4. Capture User Input
# -----------------------------
user_input = st.chat_input("Ask Techy anything about TechLaunch...")

if user_input:
    # Display user message in chat
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # -----------------------------
    # 5. Get OpenAI Response
    # -----------------------------
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=st.session_state["messages"],
        temperature=0.7,  # adjust as needed for more/less creative responses
    )

    # Extract Assistant's reply
    assistant_reply = response.choices[0].message["content"]

    # Display Assistant message in chat
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.write(assistant_reply)
