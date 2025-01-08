import streamlit as st

st.set_page_config(layout="wide")

st.title(":blue[TechLaunch] :blue[507] :rocket:")
st.write("Python Coding for College & Internships")

st.divider()

# ==========

st.write("**:blue[Overview]**")
st.write("This course is designed to get students from **:red[zero]** programming knowledge to intermediate Python scripting.")
st.write("In addition to gaining technical and critical thinking skills, students will complete this course with a **portfolio of projects** to boost their college and internship/job applications.")

st.write("**:green[No coding experience required!]**")

st.divider()
# ===========

st.write("**:blue[FAQs]**")


col1, col2, col3 = st.columns([7,1,7])

with col1:
    with st.expander("**Why take this course**"):
        st.write('You may have heard this famous line of common wisdom: "Is not what you know, is who you know that matters".')
        st.write("As a general rule for business and life, having good connections is key for success.")
        st.write('Nevertheless, at some point in your journey you will be required to prove your value. In the words of the same common wisdom: "There is no free lunch".')
        st.write("Having a deep and practical understanding of technology will make you worthy of your network, as someone who isn't just calling to get a problem solved, but rather designing and developing solutions for yourself and others.")
        st.write("Today's top college and job recruiters are looking for leaders who can identify problems and take action, not only point out where the problems are.")
        st.write("Technology gives you the power to be a problem-solver.")


with col3:
    with st.expander("**Who is this course for**"):
        st.write("- High-school seniors looking to boost their profile for college applications")
        st.write("- College students looking to develop technical skills for internship/job applications")
        st.write("- Students curious about programming in general")

# ==========

col1, col2, col3 = st.columns([7,1,7])


with col1:
    with st.expander("**Why Python**"):
        st.write("Python is versatile, beginner-friendly, and widely used in fields like data science, web development, and AI.")
        st.write("Its extensive libraries, strong community, and high demand by employers make it a top choice for anyone looking to stay relevant and adaptable in tech.")
        st.write("Learning Python gives you access to a broad range of career paths and ensures your skills remain relevant across industries.")


with col3:
    with st.expander("**Course Takeaways**"):
        st.write("- Complete portfolio of Python projects hosted online")
        st.write('- Develop "problem-solving" skills through coding')
        st.write('- Achieve intermediate "Python functional programming" level')


# ======

st.divider()

st.write("**:blue[Learning Path]**")
st.markdown("")

sessions = {
    "1 - Intro to Programming and Python": ["Why should I learn Python?","Scripting Vs Coding","Variables, Methods, Inputs, Outputs","Commenting","Integers, Strings, Lists (Basic data types)","Conditional Statements","Mini project #1 - Simple Calculator / to-do list app"],
    "2 - The Power of Algorithms": ["First session recap","What is an algorithm?","For Loops and While Loops", "Python Dictionaries (intermediate data types)", "Functions","Mini project #2 - Message Decryption"],
    "3 - Thinking like a Programmer": ["First and second session recap","Input-process-output mindset","Divide and Conquer","Pattern Recognition and algorithmic thinking","Team project - Python Scavenger Hunt"],
    "4 - Storytelling through Code": ["Recap","What does open-source mean?","Leveraging other peoples' code","Popular python packages","Intro to the best Python tool you will ever learn","ChatGPT for programmers","Main Projects 1st step - Create the portfolio"],
    "5 - Data Analysis": ["Recap","What is data?","Intro to Pandas and Dataframes","Code with structure using Jupyter Notebooks","Intro to statistics (Average, Median, Min, Max)","Aggregating data using groupby"],
    "6 - Visualizing Data": ["Recap","Tables Vs Charts","Intro to Plotly","Main Project #1 - Supermarket Sales analysis dashboard"],
    "7 - Automate Anything": ["Recap - Complete Project #1","What is an API?","Transferring data between systems","Main Project #2 - Process Automation"],
    "8 - Python for the Future": ["Recap - Complete Project #2","What is a Large Language Model?","Main Project #3 - Build custom AI chatbot"],
    "9 - Next Steps": ["Recap - Complete Project #3","Complete Portfolio","Paths for programming"]
}

session_name = st.selectbox('Select a Session:', list(sessions.keys()))


for x in sessions[session_name]:
    st.write(f" - {x}")


st.divider()

st.info(":arrow_upper_left:  Check out some of the projects we will code througout the sessions!")

# =====
