import re
import streamlit as st
st.set_page_config(page_title="Password Strength Checker by Salman Ali", page_icon="😀", layout="centered")
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color #4CAF50; color: black; font-size: 16px; }
    .stButton button:hover { background-color: #45a049;}
    </style>
    """, unsafe_allow_html=True)
st.title("Password Strength Generator")
st.write("Enter your password below to check its security level.")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password)>=8:
        score += 1
    else:
        feedback.append("Password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include **at least one number (0-9) **,")
    
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("Include **at least one special character (!@#$%^&*)**,")
    if score == 4:
        st.success("**Strong Password** - Your password is secure.")
    elif score == 3 :
        st.info("**Moderate Password** - Consider improving security by adding more feature")
    else:
        st.error("**week Password** - Follow the suggestion below to strength it.")
    if feedback:
        with st.expander("**Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password it strong")

if st.button("Check Strenght"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password firt!")
st.markdown("<div class='footer'>Created by Mr. Salman Ali", unsafe_allow_html=True)
