import sys
import os
import sqlite3
import random
import pandas as pd
import streamlit as st
from src.chains.rag_chain import SupportPearlzRAG

# Fix module import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------
# DATABASE SETUP (SQLite for Live Orders & Tickets)
# --------------------------------------------------
def init_db():
    conn = sqlite3.connect("store_data.db")
    cursor = conn.cursor()
    # Orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT,
            item TEXT,
            status TEXT,
            address TEXT
        )
    """)
    # Tickets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            customer_name TEXT,
            issue TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --------------------------------------------------
# PAGE CONFIGURATION & CSS
# --------------------------------------------------
st.set_page_config(
    page_title="SupportPearlz AI | Action Engine",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main { padding-top: 1rem; }
    .hero-container {
        display: flex;
        align-items: center;
        gap: 20px;
        background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 100%);
        padding: 20px 24px;
        border-radius: 16px;
        color: white;
        margin-bottom: 20px;
    }
    .hero-image { width: 75px; height: 75px; border-radius: 12px; }
    .hero-text h1 { margin: 0; font-size: 1.8rem; color: #ffffff !important; }
    .hero-text p { margin-top: 4px; margin-bottom: 0; opacity: 0.9; font-size: 0.9rem; }
    .lock-notice {
        padding: 16px;
        border-radius: 12px;
        background-color: #fffbe0;
        border: 1px solid #fef08a;
        color: #713f12;
        text-align: center;
        margin-top: 20px;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "rag" not in st.session_state:
    st.session_state.rag = None

# --------------------------------------------------
# SIDEBAR CONTROLS & ACTION FORMS
# --------------------------------------------------
with st.sidebar:
    st.title("💎 SupportPearlz")
    st.caption("⚡ E-Commerce Action & Support Hub")

    st.divider()

    st.subheader("🔑 Access Key")
    user_api_key = st.text_input(
        "Enter API Key to unlock:",
        type="password",
        value=st.session_state.api_key,
        help="Enter key to unlock all features."
    )

    if user_api_key != st.session_state.api_key:
        st.session_state.api_key = user_api_key
        if user_api_key:
            try:
                st.session_state.rag = SupportPearlzRAG(api_key=user_api_key)
                st.success("✅ System Unlocked!")
            except Exception:
                st.error("❌ Key Validation Failed.")
                st.session_state.rag = None
        else:
            st.session_state.rag = None

    is_unlocked = st.session_state.rag is not None

    st.divider()

    # ACTION 1: LIVE ORDER PLACEMENT
    st.subheader("🛍️ Place New Order")
    with st.form("order_form", clear_on_submit=True):
        cust_name = st.text_input("Customer Name")
        item_name = st.selectbox("Select Product", ["Pearlz Wireless Earbuds", "Smart Watch v2", "RGB Mechanical Keyboard"])
        delivery_addr = st.text_area("Delivery Address")
        submit_order = st.form_submit_button("🛒 Submit Order", use_container_width=True)

        if submit_order:
            if cust_name and delivery_addr:
                generated_id = f"ORD-{random.randint(1000, 9999)}"
                conn = sqlite3.connect("store_data.db")
                c = conn.cursor()
                c.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", (generated_id, cust_name, item_name, "Processing 📦", delivery_addr))
                conn.commit()
                conn.close()
                st.success(f"Order Placed! Your Order ID: **{generated_id}**")
            else:
                st.warning("Please fill all details.")

    st.divider()

    # ACTION 2: TICKET CREATION
    st.subheader("🎫 Raise Support Ticket")
    with st.form("ticket_form", clear_on_submit=True):
        t_name = st.text_input("Your Name")
        t_issue = st.text_area("Describe Your Problem")
        submit_ticket = st.form_submit_button("📩 Create Ticket", use_container_width=True)

        if submit_ticket:
            if t_name and t_issue:
                t_id = f"TCK-{random.randint(100, 999)}"
                conn = sqlite3.connect("store_data.db")
                c = conn.cursor()
                c.execute("INSERT INTO tickets VALUES (?, ?, ?, ?)", (t_id, t_name, t_issue, "Open 🟡"))
                conn.commit()
                conn.close()
                st.info(f"Ticket Created! ID: **{t_id}**")
            else:
                st.warning("Please describe your issue.")

    st.divider()

    # SIMPLE OWNER DASHBOARD TOGGLE
    show_admin = st.checkbox("👑 Show Admin Panel")

    st.divider()

    if st.button("🔄 Reset Chat Session", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# ADMIN DASHBOARD VIEW (SHOWS WHEN CHECKBOX IS TICKED)
# --------------------------------------------------
if show_admin:
    st.markdown("## 👑 Store Owner Dashboard")
    st.info("Live customer orders aur support tickets ka data niche tables mein display ho raha hai.")

    col1, col2 = st.columns(2)

    conn = sqlite3.connect("store_data.db")

    with col1:
        st.subheader("📦 Live Customer Orders")
        orders_df = pd.read_sql_query("SELECT * FROM orders", conn)
        if not orders_df.empty:
            st.dataframe(orders_df, use_container_width=True)
        else:
            st.write("No orders placed yet.")

    with col2:
        st.subheader("🎫 Raised Support Tickets")
        tickets_df = pd.read_sql_query("SELECT * FROM tickets", conn)
        if not tickets_df.empty:
            st.dataframe(tickets_df, use_container_width=True)
        else:
            st.write("No active support tickets.")

    conn.close()
    st.markdown("---")

# --------------------------------------------------
# HERO HEADER
# --------------------------------------------------
st.markdown(
    """
    <div class="hero-container">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" class="hero-image" alt="AI Support Bot">
        <div class="hero-text">
            <h1>🛍️ SupportPearlz AI Engine 🤖</h1>
            <p>Live Order Placement • Real-time DB Tracking • Automated RAG Support</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if not is_unlocked:
    st.markdown(
        """
        <div class="lock-notice">
            🔒 <b>System Locked</b><br>
            Please enter your API key in the left sidebar to activate Chat Assistant & Database Actions.
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# CHAT LOGIC WITH DATABASE LOOKUP & RAG
# --------------------------------------------------
if is_unlocked:
    user_question = st.chat_input("Ask a question OR enter Order ID (e.g. ORD-1234)...")

    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            # CHECK IF USER PROVIDED AN ORDER ID
            if "ORD-" in user_question.upper():
                order_id_search = user_question.upper().strip()
                conn = sqlite3.connect("store_data.db")
                c = conn.cursor()
                c.execute("SELECT * FROM orders WHERE order_id=?", (order_id_search,))
                row = c.fetchone()
                conn.close()

                if row:
                    response_text = f"📦 **Live Order Details Found:**\n\n- **Order ID:** `{row[0]}`\n- **Customer:** {row[1]}\n- **Item:** {row[2]}\n- **Status:** `{row[3]}`\n- **Delivery Address:** {row[4]}"
                else:
                    response_text = f"❌ No order found matching ID `{order_id_search}` in our database. Please check your Order ID or place a new order using the sidebar."

                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

            else:
                # ROUTE TO RAG KNOWLEDGE BASE
                with st.spinner("Searching Knowledge Base..."):
                    try:
                        history = [(m["role"], m["content"]) for m in st.session_state.messages[:-1]]
                        response = st.session_state.rag.ask(question=user_question, history=history)
                        
                        st.markdown(response.answer)
                        st.caption(f"🎯 **Confidence:** `{response.confidence}`")
                        
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response.answer
                        })
                    except Exception as e:
                        err_msg = f"Sorry, could not process request: {str(e)}"
                        st.error(err_msg)
                        st.session_state.messages.append({"role": "assistant", "content": err_msg})