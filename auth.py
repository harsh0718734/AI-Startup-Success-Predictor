"""
auth.py - Authentication Module
Handles login, signup, session management, and role-based access
"""

import streamlit as st
import hashlib
import json
import os
from datetime import datetime

USERS_FILE = "data/users.json"

# ─────────────────────────────────────────
# Utility helpers
# ─────────────────────────────────────────

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _load_users() -> dict:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    # Seed with demo accounts
    default = {
        "owner@demo.com": {
            "name": "Demo Owner",
            "password": _hash_password("owner123"),
            "role": "Startup Owner",
            "created": str(datetime.now()),
        },
        "investor@demo.com": {
            "name": "Demo Investor",
            "password": _hash_password("investor123"),
            "role": "Investor",
            "created": str(datetime.now()),
        },
    }
    _save_users(default)
    return default


def _save_users(users: dict):
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


# ─────────────────────────────────────────
# Public API
# ─────────────────────────────────────────

def is_logged_in() -> bool:
    return st.session_state.get("logged_in", False)


def current_user() -> dict:
    return st.session_state.get("user_info", {})


def logout():
    for key in ["logged_in", "user_info"]:
        st.session_state.pop(key, None)
    st.rerun()


def login_page():
    """Render the combined Login / Signup page."""
    st.title("🚀 StartupSense AI")
    st.markdown("**Intelligent Decision-Support for Startup Success**")
    st.divider()

    tab_login, tab_signup = st.tabs(["🔑 Login", "📝 Sign Up"])

    with tab_login:
        _render_login()

    with tab_signup:
        _render_signup()


def _render_login():
    st.subheader("Welcome back!")
    with st.form("login_form"):
        email = st.text_input("📧 Email", placeholder="you@example.com")
        password = st.text_input("🔒 Password", type="password")
        role_hint = st.selectbox("Role hint (optional)", ["—", "Startup Owner", "Investor"])
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        users = _load_users()
        hashed = _hash_password(password)
        if email in users and users[email]["password"] == hashed:
            user = users[email]
            st.session_state["logged_in"] = True
            st.session_state["user_info"] = {
                "email": email,
                "name": user["name"],
                "role": user["role"],
            }
            st.success(f"✅ Welcome, {user['name']}!")
            st.rerun()
        else:
            st.error("❌ Invalid email or password.")

    st.caption("Demo → owner@demo.com / owner123   |   investor@demo.com / investor123")


def _render_signup():
    st.subheader("Create your account")
    with st.form("signup_form"):
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email")
        password = st.text_input("🔒 Password", type="password")
        confirm = st.text_input("🔒 Confirm Password", type="password")
        role = st.selectbox("🎭 Role", ["Startup Owner", "Investor"])
        submitted = st.form_submit_button("Create Account", use_container_width=True)

    if submitted:
        if not all([name, email, password, confirm]):
            st.error("All fields are required.")
        elif password != confirm:
            st.error("Passwords do not match.")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")
        else:
            users = _load_users()
            if email in users:
                st.error("Email already registered.")
            else:
                users[email] = {
                    "name": name,
                    "password": _hash_password(password),
                    "role": role,
                    "created": str(datetime.now()),
                }
                _save_users(users)
                st.success("✅ Account created! Please log in.")


def profile_settings_page():
    """Render the Profile & Settings page."""
    user = current_user()
    st.title("⚙️ Profile & Settings")

    col1, col2 = st.columns([1, 2])
    with col1:
        with st.container(border=True):
            st.write("👤")
            st.subheader(user.get('name','—'))
            st.info(user.get('role','—'))

    with col2:
        st.markdown("### Account Details")
        st.info(f"**Name:** {user.get('name')}")
        st.info(f"**Email:** {user.get('email')}")
        st.info(f"**Role:** {user.get('role')}")

        st.markdown("### Change Password")
        with st.form("change_pw"):
            old_pw = st.text_input("Current Password", type="password")
            new_pw = st.text_input("New Password", type="password")
            confirm_pw = st.text_input("Confirm New Password", type="password")
            if st.form_submit_button("Update Password"):
                users = _load_users()
                email = user.get("email")
                if users.get(email, {}).get("password") == _hash_password(old_pw):
                    if new_pw == confirm_pw and len(new_pw) >= 6:
                        users[email]["password"] = _hash_password(new_pw)
                        _save_users(users)
                        st.success("Password updated!")
                    else:
                        st.error("New passwords don't match or are too short.")
                else:
                    st.error("Current password is incorrect.")

    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True, type="primary"):
        logout()
