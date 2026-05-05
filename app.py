import streamlit as st
import random

st.set_page_config(layout="wide")

# CSS: Centers text and button, fixes hover/active visibility
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu, header, footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        margin: 0;
        background: #0f172a;
        overflow: hidden;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    /* Fixed Container for vertical/horizontal centering */
    .fixed-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        max-width: 900px;
        text-align: center;
        z-index: 9999;
    }

    .title {
        color: #ff4d6d;
        font-size: 60px; 
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
    }

    .subtitle {
        color: #e2e8f0;
        font-size: 28px;
        margin-bottom: 40px;
        text-align: center;
    }

    div[data-testid="stNumberInput"] {
        margin: 0 auto !important;
        width: 60% !important;
    }
    
    div[data-testid="stNumberInput"] label {
        display: none;
    }

    input {
        background-color: #111827 !important;
        color: white !important;
        border: 2px solid #7c3aed !important;
        border-radius: 12px !important;
        height: 60px !important;
        text-align: center !important;
        font-size: 24px !important;
    }

    /* CENTER THE SUBMIT BUTTON */
    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }

    .stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Fixed Button visibility and pressing states */
    .stButton > button {
        width: 300px !important; 
        height: 70px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        margin-top: 25px !important;
        border: none !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    /* Maintain visibility and appearance when hovering or clicking */
    .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
        background-color: #ff758f !important;
        color: white !important;
        border: none !important;
        outline: none !important;
        box-shadow: 0px 4px 15px rgba(255, 77, 109, 0.4) !important;
    }

    /* CENTER THE RESULT MESSAGE */
    .result {
        margin-top: 35px;
        color: #fbbf24;
        font-size: 26px;
        font-weight: bold;
        width: 100%;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# State initialization
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.message = ""

# Layout
st.markdown('<div class="fixed-container">', unsafe_allow_html=True)

st.markdown('<div class="title">GUESS THE NUMBER GAME</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I\'m thinking of a number between 1 and 100.</div>', unsafe_allow_html=True)

with st.form(key='game_form', clear_on_submit=False):
    guess = st.number_input("", min_value=1, max_value=100, step=1)
    submit = st.form_submit_button("Submit Guess")
    
    if submit:
        if guess < st.session_state.number:
            st.session_state.message = "Too Low! ↑"
        elif guess > st.session_state.number:
            st.session_state.message = "Too High! ↓"
        else:
            st.session_state.message = f"🎉 Correct! It was {st.session_state.number}"
            st.session_state.number = random.randint(1, 100)

st.markdown(f'<div class="result">{st.session_state.message}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)