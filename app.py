"""
app.py - StartupSense AI  ·  Main Entry Point
=========================================================
Intelligent Decision-Support System for Startup Failure
Prediction and Risk Evaluation (India Startup Dataset)

Run:   streamlit run app.py
"""

import streamlit as st
from streamlit_option_menu import option_menu

# ── local modules ──────────────────────────────────────
import auth
from pages.owner_pages import (
    render_home,
    render_dataset_explorer,
    render_dashboard,
    render_add_startup,
    render_prediction,
    render_growth_prediction,
    render_recommendations,
    render_idea_validator,
    render_competitor_benchmarking,
    render_runway_simulator,
    render_mentor_chatbot,
)
from pages.investor_pages import (
    render_investor_home,
    render_all_startups,
    render_startup_analysis,
    render_founder_pitches,
    render_comparison,
    render_chatbot,
)

# ─────────────────────────────────────────
# Page configuration
# ─────────────────────────────────────────
st.set_page_config(
    page_title="StartupSense AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────
# Global CSS
# ─────────────────────────────────────────
# ─────────────────────────────────────────
# Global CSS (Minimal)
st.markdown(
    """
    <style>
    #MainMenu { visibility: hidden; }
    footer    { visibility: hidden; }
    [data-testid="stSidebarNav"] { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────
# Auth gate
# ─────────────────────────────────────────
if not auth.is_logged_in():
    auth.login_page()
    st.stop()

# ─────────────────────────────────────────
# Sidebar brand + user info
# ─────────────────────────────────────────
user  = auth.current_user()
role  = user.get("role", "")
name  = user.get("name", "User")

with st.sidebar:
    st.title("🚀 StartupSense AI")
    st.info(f"Logged in as: **{name}**\nRole: **{role}**")
    st.divider()

    # ── Navigation menus ──────────────────
    if role == "Startup Owner":
        selected = option_menu(
            menu_title="Navigation",
            options=[
                "Home", "Idea Validator", "Dashboard", 
                "Add Startup", "Prediction", "Growth Prediction", 
                "Competitor Benchmarking", "Runway Simulator", 
                "Recommendations", "Startup Mentor", "Dataset Explorer", 
                "Profile & Settings",
            ],
            icons=[
                "house-fill", "lightbulb", "bar-chart-fill",
                "building", "robot", "graph-up-arrow",
                "trophy", "wallet",
                "stars", "chat-dots", "table",
                "gear-fill",
            ],
            menu_icon="cast",
            default_index=0,
        )
    else:  # Investor
        selected = option_menu(
            menu_title="Navigation",
            options=[
                "Home", "All Startups", "Startup Analysis", "Founder Pitches",
                "Comparison", "AI Chatbot", "Profile & Settings",
            ],
            icons=[
                "house-fill", "grid-fill", "search", "briefcase-fill",
                "bar-chart-line-fill", "robot", "gear-fill",
            ],
            menu_icon="cast",
            default_index=0,
        )


# ─────────────────────────────────────────
# Route to the correct page
# ─────────────────────────────────────────

# ── Startup Owner routes ──────────────────────
if role == "Startup Owner":
    if selected == "Home":
        render_home()
    elif selected == "Idea Validator":
        render_idea_validator()
    elif selected == "Dataset Explorer":
        render_dataset_explorer()
    elif selected == "Dashboard":
        render_dashboard()
    elif selected == "Add Startup":
        render_add_startup(user.get("email", ""))
    elif selected == "Prediction":
        render_prediction()
    elif selected == "Growth Prediction":
        render_growth_prediction()
    elif selected == "Competitor Benchmarking":
        render_competitor_benchmarking()
    elif selected == "Runway Simulator":
        render_runway_simulator()
    elif selected == "Recommendations":
        render_recommendations()
    elif selected == "Startup Mentor":
        render_mentor_chatbot()
    elif selected == "Profile & Settings":
        auth.profile_settings_page()

# EOF

# ── Investor routes ───────────────────────────
else:
    if selected == "Home":
        render_investor_home()
    elif selected == "All Startups":
        render_all_startups()
    elif selected == "Startup Analysis":
        render_startup_analysis()
    elif selected == "Founder Pitches":
        render_founder_pitches()
    elif selected == "Comparison":
        render_comparison()
    elif selected == "AI Chatbot":
        render_chatbot()
    elif selected == "Profile & Settings":
        auth.profile_settings_page()
