import time
import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# CONFIGURATION & PERSONALIZATION
# Replace these values with your girlfriend's name and your personal message!
# ==============================================================================
GIRL_NAME = "AMODING ANNA GRACE"
YOUR_LOVE_MESSAGE = (
    "From the moment you entered my life, everything became brighter, kinder, "
    "and infinitely more beautiful. You are my home, my favorite dream, and "
    "my greatest blessing. I love you more than words could ever say."
)
SECOND_MESSAGE = (
    "No matter where life takes us, my heart will always choose you, "
    "today, tomorrow, and for all eternity. ❤️"
)

# Optional romantic background audio URL (Royalty-free ambient romance track)
# You can replace this link with any direct mp3 link of your choice!
AUDIO_URL = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=piano-moment-114476.mp3"

# Set Streamlit Page Configuration
st.set_page_config(
    page_title=f"For {GIRL_NAME} ❤️",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================================================================
# CUSTOM CSS & ANIMATIONS
# Hides standard Streamlit elements and applies dark romantic styling
# ==============================================================================
st.markdown(
    f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Great+Vibes&family=Montserrat:wght@300;400;500&display=swap');

    /* Hide standard Streamlit header, footer, and menu */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none !important;}}
    div[data-testid="stToolbar"] {{visibility: hidden !important;}}
    div[data-testid="stDecoration"] {{display: none !important;}}

    /* Fullscreen romantic gradient background */
    .stApp {{
        background: radial-gradient(circle at center, #2b0818 0%, #12030a 60%, #050104 100%);
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        overflow-x: hidden;
    }}

    /* Global Container */
    .main-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 2rem 1rem;
        min-height: 80vh;
    }}

    /* Floating ambient stars/sparkles */
    .bg-sparkles {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #ffb3c6, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40px 70px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(1.5px 1.5px at 90px 40px, #ff4d6d, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 160px 120px, #ffb3c6, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 200px 200px;
        opacity: 0.35;
        animation: sparkleAnim 12s infinite linear;
    }}

    @keyframes sparkleAnim {{
        0% {{ transform: translateY(0); }}
        100% {{ transform: translateY(-200px); }}
    }}

    /* Girl's Name Title */
    .girl-name {{
        font-family: 'Great Vibes', cursive;
        font-size: clamp(3.5rem, 8vw, 6.5rem);
        color: #fff0f5;
        text-shadow: 0 0 15px #ff4d6d, 0 0 35px #ff0055, 0 0 60px #ff0055;
        margin-bottom: 0.5rem;
        animation: fadeInDown 2s ease-out;
        letter-spacing: 2px;
    }}

    /* Subtitle */
    .subtitle {{
        font-family: 'Cinzel', serif;
        font-size: clamp(0.9rem, 2.5vw, 1.3rem);
        letter-spacing: 4px;
        color: #ffb3c6;
        text-transform: uppercase;
        margin-bottom: 2.5rem;
        opacity: 0.85;
        animation: fadeIn 3s ease-out;
    }}

    /* Heartbeat animation container */
    .heart-glow-box {{
        margin: 1.5rem auto;
        display: inline-block;
        animation: heartbeat 1.8s infinite ease-in-out;
    }}

    .glowing-heart {{
        font-size: clamp(4rem, 10vw, 6rem);
        color: #ff1744;
        text-shadow: 0 0 20px #ff1744, 0 0 40px #ff4d6d, 0 0 80px #ff0055;
        filter: drop-shadow(0 0 15px rgba(255, 23, 68, 0.8));
    }}

    /* Romantic Love Message Card */
    .message-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 179, 198, 0.2);
        box-shadow: 0 8px 32px 0 rgba(255, 0, 85, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        max-width: 750px;
        margin: 2rem auto;
        animation: fadeInUp 1.5s ease-out;
    }}

    .message-text {{
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(1.1rem, 3vw, 1.4rem);
        line-height: 1.8;
        color: #ffe6ed;
        font-weight: 300;
        letter-spacing: 0.5px;
    }}

    /* Closing poetic quote */
    .poetic-quote {{
        font-family: 'Great Vibes', cursive;
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        color: #ffb3c6;
        margin-top: 2rem;
        text-shadow: 0 0 10px rgba(255, 179, 198, 0.5);
    }}

    /* Custom Streamlit Button Styling */
    div.stButton > button {{
        background: linear-gradient(135deg, #ff0055 0%, #ff4d6d 100%);
        color: #ffffff !important;
        font-family: 'Cinzel', serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        letter-spacing: 2px !important;
        padding: 0.8rem 2.5rem !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.5) !important;
        transition: all 0.4s ease-in-out !important;
        display: block !important;
        margin: 1.5rem auto !important;
        cursor: pointer !important;
    }}

    div.stButton > button:hover {{
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 0 35px rgba(255, 0, 85, 0.85) !important;
        background: linear-gradient(135deg, #ff1744 0%, #ff6685 100%) !important;
    }}

    /* Keyframe Animations */
    @keyframes heartbeat {{
        0% {{ transform: scale(1); }}
        14% {{ transform: scale(1.15); }}
        28% {{ transform: scale(1); }}
        42% {{ transform: scale(1.15); }}
        70% {{ transform: scale(1); }}
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    @keyframes fadeInDown {{
        from {{ opacity: 0; transform: translateY(-30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>

    <div class="bg-sparkles"></div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# JAVASCRIPT FLOATING HEARTS COMPONENT
# Creates dynamic particle animations on click
# ==============================================================================
floating_hearts_js = """
<script>
function createFloatingHeart() {
    const heart = document.createElement('div');
    heart.innerHTML = ['💖', '💗', '💕', '✨', '❤️', '🌹'][Math.floor(Math.random() * 6)];
    heart.style.position = 'fixed';
    heart.style.bottom = '-50px';
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.fontSize = (Math.random() * 20 + 20) + 'px';
    heart.style.opacity = Math.random() * 0.7 + 0.3;
    heart.style.pointerEvents = 'none';
    heart.style.zIndex = '9999';
    heart.style.transition = 'transform ' + (Math.random() * 3 + 4) + 's linear, opacity ' + (Math.random() * 3 + 4) + 's ease-out';
    
    document.body.appendChild(heart);
    
    setTimeout(() => {
        heart.style.transform = 'translateY(-105vh) rotate(' + (Math.random() * 360) + 'deg)';
        heart.style.opacity = '0';
    }, 100);
    
    setTimeout(() => {
        heart.remove();
    }, 7000);
}

// Continuously spawn hearts
setInterval(createFloatingHeart, 600);
</script>
"""
components.html(floating_hearts_js, height=0, width=0)

# ==============================================================================
# STATE MANAGEMENT
# Track button clicks to unveil content smoothly
# ==============================================================================
if "opened" not in st.session_state:
    st.session_state.opened = False
if "one_more_thing" not in st.session_state:
    st.session_state.one_more_thing = False

# ==============================================================================
# MAIN PAGE CONTENT
# ==============================================================================

# Header Section
st.markdown(
    f"""
    <div class="main-container">
        <div class="subtitle">A Message Crafted Just For You</div>
        <div class="girl-name">{GIRL_NAME}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Heartbeat Icon Display
st.markdown(
    """
    <div style="text-align: center;">
        <div class="heart-glow-box">
            <span class="glowing-heart">❤️</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Landing / Unveil Action
if not st.session_state.opened:
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Open My Heart ❤️"):
            st.session_state.opened = True
            st.rerun()

# Revealed Heartfelt Message Section
if st.session_state.opened:
    # Optional audio player
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <audio autoplay loop controls style="height: 30px; opacity: 0.6; filter: invert(0.8);">
                <source src="{AUDIO_URL}" type="audio/mpeg">
            </audio>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Message Box
    st.markdown(
        f"""
        <div class="message-card">
            <div class="message-text">"{YOUR_LOVE_MESSAGE}"</div>
            <div class="poetic-quote">"Some feelings are too beautiful to fit into words."</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Secondary Reveal Action
    if not st.session_state.one_more_thing:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("One More Thing... ✨"):
                st.session_state.one_more_thing = True
                st.rerun()

    # Second Message Reveal
    if st.session_state.one_more_thing:
        st.markdown(
            f"""
            <div class="message-card" style="border-color: rgba(255, 0, 85, 0.4); background: rgba(255, 0, 85, 0.05);">
                <div class="message-text" style="font-style: italic;">
                    "{SECOND_MESSAGE}"
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()
