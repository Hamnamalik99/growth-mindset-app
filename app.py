# import streamlit as st

# st.title("Mera Pehla Streamlit App")  # Title
# st.write("Assalamualaikum! Yeh mera pehla Streamlit app hai.")  # Text






# import streamlit as st
# import random

# # App ka Title
# st.title("🚀 Growth Mindset Challenge")

# # User ka Naam Input
# name = st.text_input("Apna Naam Likhein:")

# if name:
#     st.write(f"Salam {name}, Growth Mindset ka safar shuru karein! 🌟")

# # Motivational Quotes
# quotes = [
#     "Ghaltiyan sab se behtareen teachers hain.",
#     "Mehnat wo chaabi hai jo success ka darwaza kholti hai.",
#     "Har challenge ek naya mauqa hai kuch seekhne ka.",
#     "Bar bar koshish karna hi asli kamiyabi hai.",
# ]

# # Button to Show Random Quote
# if st.button("Mujhe Ek Motivational Quote Dikhayein!"):
#     st.success(random.choice(quotes))





# st.header("📊 Apni Growth Mindset Progress Check Karein")
# effort = st.slider("Aap kitni mehnat kar rahe hain? (1-10)", 1, 10, 5)
# learning = st.slider("Aap naye skills kitne seekh rahe hain? (1-10)", 1, 10, 5)

# st.write(f"🚀 Aapka Mehnat Score: {effort}/10")
# st.write(f"📚 Aapka Learning Score: {learning}/10")










# import streamlit as st
# import random
# import pandas as pd

# # Session State for User Data
# if "users" not in st.session_state:
#     st.session_state.users = {}

# # App Title
# st.title("🚀 Growth Mindset Interactive Web App")

# # User Input Section
# st.sidebar.header("👤 Aapki Information")
# name = st.sidebar.text_input("Apna Naam Likhein:")
# goal = st.sidebar.text_input("Aap ka Learning Goal Kya Hai?")
# learning_style = st.sidebar.selectbox(
#     "Aap ka Learning Style Kya Hai?", ["Visual", "Reading/Writing", "Hands-on", "Listening"]
# )

# if name:
#     if name not in st.session_state.users:
#         st.session_state.users[name] = {"effort": 5, "learning": 5, "feedback": ""}
    
#     st.write(f"🌟 Salam, {name}! Aapka Goal: **{goal}**")

#     # Motivational Quotes Section
#     st.subheader("💡 Aaj Ka Inspirational Quote")
#     quotes = [
#         "Ghaltiyan sab se behtareen teachers hain.",
#         "Mehnat wo chaabi hai jo success ka darwaza kholti hai.",
#         "Har challenge ek naya mauqa hai kuch seekhne ka.",
#         "Bar bar koshish karna hi asli kamiyabi hai.",
#     ]
    
#     if st.button("🚀 Mujhe Ek Motivational Quote Dikhayein!"):
#         st.success(random.choice(quotes))

#     # Self-Assessment Progress Tracker
#     st.subheader("📊 Apni Growth Mindset Progress Check Karein")
#     st.session_state.users[name]["effort"] = st.slider("Aap kitni mehnat kar rahe hain? (1-10)", 1, 10, st.session_state.users[name]["effort"])
#     st.session_state.users[name]["learning"] = st.slider("Aap naye skills kitne seekh rahe hain? (1-10)", 1, 10, st.session_state.users[name]["learning"])

#     # Feedback System
#     st.subheader("📝 Apna Feedback Dein")
#     st.session_state.users[name]["feedback"] = st.text_area("Growth mindset ke baare mein aap kya sochte hain?", value=st.session_state.users[name]["feedback"])

#     if st.button("Feedback Submit Karein"):
#         st.success("Shukriya! Aapka feedback save kar liya gaya hai. 🎉")

#     # Leaderboard (Top Learners)
#     st.subheader("🏆 Top Learners Leaderboard")
#     df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
#     df = df.sort_values(by=["effort", "learning"], ascending=False)
#     st.table(df)

#     # Progress Graph
#     st.subheader("📈 Learning Progress Chart")
#     st.line_chart(df[["effort", "learning"]])

#     # Learning Style Display
#     st.info(f"🧠 Aap ka learning style hai: **{learning_style}**")













import streamlit as st
import random
import pandas as pd

# Initialize Session State for User Data
if "users" not in st.session_state:
    st.session_state.users = {}

# App Title
st.title("🚀 Growth Mindset Interactive Web App")

# Sidebar - User Input
st.sidebar.header("👤 Your Information")
name = st.sidebar.text_input("Enter Your Name:", value="")  # Default empty
goal = st.sidebar.text_input("What is Your Learning Goal?")
learning_style = st.sidebar.selectbox(
    "What is Your Preferred Learning Style?",
    ["Visual", "Reading/Writing", "Hands-on", "Listening"]
)

# Check if user entered a name
if name.strip():  # Ensure name is not empty
    if name not in st.session_state.users:
        st.session_state.users[name] = {"Effort Level": 5, "Learning Progress": 5, "Feedback": ""}

    # Welcome Message
    st.markdown(f"### 🌟 Welcome, {name}! Your Goal: **{goal if goal else 'Not Set'}**")

    # Motivational Quotes Section
    st.subheader("💡 Today's Inspirational Quote")
    quotes = [
        "Mistakes are the best teachers.",
        "Effort is the key that unlocks success.",
        "Every challenge is a new learning opportunity.",
        "Success comes from persistent effort."
    ]
    
    if st.button("🚀 Show Me a Motivational Quote!"):
        st.success(random.choice(quotes))

    # Self-Assessment Progress Tracker
    st.subheader("📊 Growth Mindset Progress Tracker")
    st.session_state.users[name]["Effort Level"] = st.slider(
        "How much effort are you putting in? (1-10)",
        1, 10, st.session_state.users[name]["Effort Level"]
    )
    st.session_state.users[name]["Learning Progress"] = st.slider(
        "How much are you improving your skills? (1-10)",
        1, 10, st.session_state.users[name]["Learning Progress"]
    )

    # Feedback System
    st.subheader("📝 Share Your Thoughts")
    st.session_state.users[name]["Feedback"] = st.text_area(
        "What do you think about the growth mindset?",
        value=st.session_state.users[name]["Feedback"]
    )

    if st.button("Submit Feedback"):
        st.success("Thank you! Your feedback has been saved. 🎉")

    # Leaderboard (Top Learners)
    st.subheader("🏆 Top Learners Leaderboard")
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df = df.sort_values(by=["Effort Level", "Learning Progress"], ascending=False)
    st.table(df)

    # Learning Progress Chart
    st.subheader("📈 Learning Progress Chart")
    st.line_chart(df[["Effort Level", "Learning Progress"]])

    # Display Learning Style
    st.info(f"🧠 Your preferred learning style: **{learning_style}**")  
else:
    st.warning("Please enter your name in the sidebar to continue.")