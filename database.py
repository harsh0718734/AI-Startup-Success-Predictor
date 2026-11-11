"""
database.py - Data Persistence Layer
Manages startup records (CRUD) using CSV as a lightweight store.
"""

import os
import pandas as pd
import json
from datetime import datetime

STARTUPS_FILE = "data/startups_db.csv"
MASTER_DATASET = "data/india_startup.csv"

STARTUP_COLUMNS = [
    "id", "name", "industry", "funding_usd_m", "revenue_usd_k",
    "employees", "market_size_score", "growth_rate_pct", "expenses_usd_k",
    "location", "logo_path", "added_by", "added_at",
]


# ─────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────

def _ensure_db():
    if not os.path.exists(STARTUPS_FILE):
        pd.DataFrame(columns=STARTUP_COLUMNS).to_csv(STARTUPS_FILE, index=False)


import streamlit as st

@st.cache_data
def load_master() -> pd.DataFrame:
    """Load the main India startup dataset."""
    if not os.path.exists(MASTER_DATASET):
         return pd.DataFrame()
    return pd.read_csv(MASTER_DATASET)


def load_startups() -> pd.DataFrame:
    """Load user-added startups (with cache invalidation on file change)."""
    mtime = os.path.getmtime(STARTUPS_FILE) if os.path.exists(STARTUPS_FILE) else 0
    return _load_startups_internal(mtime)


@st.cache_data
def _load_startups_internal(mtime) -> pd.DataFrame:
    _ensure_db()
    df = pd.read_csv(STARTUPS_FILE)
    if df.empty:
        return pd.DataFrame(columns=STARTUP_COLUMNS)
    return df


def save_startup(record: dict) -> bool:
    """Append a new startup record."""
    _ensure_db()
    df = load_startups()
    record["id"] = f"USR-{len(df)+1:04d}"
    record["added_at"] = str(datetime.now())
    new_row = pd.DataFrame([record])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(STARTUPS_FILE, index=False)
    return True


def delete_startup(startup_id: str) -> bool:
    _ensure_db()
    df = load_startups()
    df = df[df["id"] != startup_id]
    df.to_csv(STARTUPS_FILE, index=False)
    return True


def get_startup_by_name(name: str) -> pd.Series | None:
    """Search across master + user DB."""
    master = load_master()
    match = master[master["Startup_Name"].str.lower() == name.lower()]
    if not match.empty:
        return match.iloc[0]
    user_db = load_startups()
    match2 = user_db[user_db["name"].str.lower() == name.lower()]
    if not match2.empty:
        return match2.iloc[0]
    return None
