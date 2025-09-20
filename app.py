from google import genai
import streamlit as st

advisor=genai.Client(api_key="AIzaSyCqF-F8bfJMvIxj8DUcjJM1HVr-NMh6JJE")
st.title("AI Carrier Advisor")
name=st.text_input("What is Your Name:")
age=st.text_input("What is Your Age:")
qualification=st.text_input("What is Your Qualification:")
experience=st.text_input("What is Your Experience:")
interest=st.text_input("Which Field You will be intrested:")
skills=st.text_input("What are the skills you have:")
languages=st.text_input("What are the languages yu konw:")
location=st.text_input("waht is Your Preffered Location:")
prompt=f"""You are Expert Carrier Advisor,based on the User input ,give Carrier advice.

name:{name},
age:{age},
qualification:{qualification},
experience;{experience},
interest:{interest},
skills:{skills},
languages:{languages},
"""

if st.button("SUBMIT"):
    response=advisor.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    st.write(response.text)
