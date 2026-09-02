import streamlit as st

st.set_page_config(
    page_title="Hello Amitaa",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Minimalistic Dark Aesthetic CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Inter:wght@300;400&display=swap');

/* Streamlit defaults hide */
#MainMenu, header, footer,
div[data-testid="stToolbar"],
div[data-testid="stDecoration"],
div[data-testid="stStatusWidget"] {
    display: none !important;
}

/* App Background */
html, body, .stApp {
    background-color: #0d0d0d !important;
    color: #eee9df !important;
}

/* Center Container */
.block-container {
    max-width: 480px !important;
    padding-top: 9rem !important;
    padding-bottom: 4rem !important;
    margin: 0 auto !important;
    text-align: center !important;
}

/* Minimalist Typography */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 400;
    color: #eee9df;
    margin-bottom: 0.6rem;
    line-height: 1.2;
}

.sub-title {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 300;
    color: #9a948a;
    letter-spacing: 0.03em;
    margin-bottom: 2.2rem;
}

.caption-text {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #858078;
    font-size: 1.1rem;
    margin-top: 1rem;
}

/* Centered Rounded Buttons */
div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
    margin: 0.6rem 0;
}

div[data-testid="stButton"] > button {
    background: transparent !important;
    color: #e8e2d8 !important;
    border: 1px solid #3d3932 !important;
    border-radius: 999px !important;
    padding: 0.65rem 2rem !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 300 !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
    max-width: 320px !important;
}

div[data-testid="stButton"] > button:hover {
    border-color: #eee9df !important;
    background: rgba(255, 255, 255, 0.05) !important;
}
</style>
""", unsafe_allow_html=True)

# State Management
if "step" not in st.session_state:
    st.session_state.step = 1
if "choice" not in st.session_state:
    st.session_state.choice = None

# Screen 1: Hello
if st.session_state.step == 1:
    st.markdown('<div class="main-title">Hello Amitaa</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Only tiny question...</div>', unsafe_allow_html=True)
    
    if st.button("Ask me →"):
        st.session_state.step = 2
        st.rerun()

# Screen 2: Question & Choices
elif st.session_state.step == 2:
    st.markdown('<div class="main-title" style="font-size: 2.1rem;">Should I make another one..??</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Pick one</div>', unsafe_allow_html=True)

    if st.button("Something like you"):
        st.session_state.choice = "Something like you"
        st.session_state.step = 3
        st.rerun()

    if st.button("Another portrait"):
        st.session_state.choice = "Another portrait"
        st.session_state.step = 3
        st.rerun()

    if st.button("Or may be...!!"):
        st.session_state.choice = "Or may be...!!"
        st.session_state.step = 3
        st.rerun()

# Screen 3: Final Hello
elif st.session_state.step == 3:
    st.markdown('<div class="main-title">Helloo :)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">Noted: <i>{st.session_state.choice}</i></div>', unsafe_allow_html=True)
    st.markdown('<div class="caption-text">— Dhananjay</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start again"):
        st.session_state.step = 2
        st.session_state.choice = None
        st.rerun()