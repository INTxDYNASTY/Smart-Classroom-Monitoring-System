import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="AI Smart Classroom Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb !important;
    color: #111827 !important;
}

/* Hide Streamlit black header */
header[data-testid="stHeader"] {
    background-color: #f4f7fb !important;
}

/* Sidebar white theme */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb;
}

section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* Sidebar navigation buttons */
div[role="radiogroup"] label {
    background-color: #f8fafc !important;
    padding: 14px 16px !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
    border: 1px solid #e5e7eb !important;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.04);
}

div[role="radiogroup"] label:hover {
    background-color: #eef2ff !important;
    border: 1px solid #6366f1 !important;
}

div[role="radiogroup"] label[data-baseweb="radio"] {
    color: #111827 !important;
}

/* Sidebar status cards */
.status-card-green {
    background-color: #ecfdf5;
    color: #047857 !important;
    padding: 14px;
    border-radius: 14px;
    font-weight: 700;
    margin-bottom: 12px;
    border: 1px solid #bbf7d0;
}

.status-card-blue {
    background-color: #eff6ff;
    color: #1d4ed8 !important;
    padding: 14px;
    border-radius: 14px;
    font-weight: 700;
    margin-bottom: 12px;
    border: 1px solid #bfdbfe;
}

.status-card-yellow {
    background-color: #fffbeb;
    color: #b45309 !important;
    padding: 14px;
    border-radius: 14px;
    font-weight: 700;
    margin-bottom: 12px;
    border: 1px solid #fde68a;
}

/* Headings */
.main-title {
    font-size: 34px;
    font-weight: 850;
    color: #111827;
    margin-bottom: 8px;
}

.main-subtitle {
    color: #6b7280;
    font-size: 16px;
    margin-bottom: 28px;
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    color: #111827;
    margin-top: 18px;
    margin-bottom: 14px;
}

/* Cards */
.card {
    background-color: #ffffff;
    color: #1f2937;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(15,23,42,0.07);
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.metric-card {
    background-color: #ffffff;
    color: #111827;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 5px 16px rgba(15,23,42,0.07);
    border-left: 5px solid #4f46e5;
    min-height: 110px;
}

.metric-label {
    font-size: 14px;
    color: #6b7280;
    font-weight: 700;
}

.metric-value {
    font-size: 28px;
    color: #111827;
    font-weight: 850;
}

/* Pills */
.info-pill {
    display: inline-block;
    background-color: #eef2ff;
    color: #4338ca;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-right: 8px;
    margin-bottom: 8px;
}

/* Force dataframe/table white */
[data-testid="stDataFrame"] {
    background-color: #ffffff !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    border: 1px solid #e5e7eb !important;
}

[data-testid="stTable"] {
    background-color: white !important;
}

/* Metric default cards */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.04);
}

/* Code block light */
[data-testid="stCodeBlock"] {
    background-color: #ffffff !important;
    color: #111827 !important;
    border-radius: 14px !important;
}

/* Matplotlib chart containers */
.element-container:has(.stPlotlyChart),
.element-container:has(img) {
    background-color: #ffffff;
}

/* Remove black chart background inherited from browser/theme */
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 📊 SmartClass AI")
st.sidebar.caption("AI-Enabled Classroom Monitoring")

menu = st.sidebar.radio(
    "Choose Module",
    [
        "🏠 Project Overview",
        "🔍 Live Analysis",
        "⚙️ How It Works",
        "🧠 Model Information"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### System Status")
st.sidebar.markdown('<div class="status-card-green">✅ Main monitoring enabled</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="status-card-blue">📊 Dashboard analytics active</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="status-card-yellow">🎭 Emotion module runs separately</div>', unsafe_allow_html=True)

# ---------------- DATA LOADING ----------------
def load_main_data():
    if os.path.exists("data.csv"):
        try:
            return pd.read_csv("data.csv")
        except:
            return pd.DataFrame()
    return pd.DataFrame()

def load_emotion_data():
    path = "emotion_AI/emotion_data.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return pd.DataFrame()
    return pd.DataFrame()

df = load_main_data()
emotion_df = load_emotion_data()

# ---------------- PROJECT OVERVIEW ----------------
if menu == "🏠 Project Overview":
    st.markdown('<div class="main-title">AI-Enabled Smart Classroom Monitoring System</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Real-time student attention, behavior, emotion, and classroom engagement analytics dashboard.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Project Overview</h2>
        <p>
        The <b>AI-Enabled Smart Classroom Monitoring System</b> is designed to improve the teaching-learning process
        by using Artificial Intelligence, Computer Vision, and real-time analytics. Traditional classrooms depend heavily
        on manual teacher observation, which becomes difficult in large classrooms. This project solves that problem by
        automatically monitoring student behavior and generating useful classroom insights.
        </p>
        <p>
        The system captures live video input from a classroom camera and analyzes student attentiveness, eye movement,
        head direction, drowsiness, mobile phone usage, and facial emotions. These observations are stored in structured
        CSV files and displayed through a professional analytics dashboard.
        </p>
        <p>
        The goal of the system is not to replace teachers, but to support them with real-time feedback such as low attention
        warning, phone usage alert, drowsiness alert, and classroom engagement score.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h3>🎯 Main Objective</h3>
            <p>To monitor student engagement in real time and provide actionable feedback to teachers.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h3>🧠 AI Capabilities</h3>
            <p>Attention detection, drowsiness detection, phone detection, emotion recognition, and multi-student analytics.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h3>📈 Final Output</h3>
            <p>Live classroom dashboard with charts, trends, alerts, and real-time teacher feedback.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)
    st.markdown("""
    <span class="info-pill">Multi-Student Detection</span>
    <span class="info-pill">Attention Score</span>
    <span class="info-pill">Eye Tracking</span>
    <span class="info-pill">Drowsiness Alert</span>
    <span class="info-pill">Phone Detection</span>
    <span class="info-pill">Emotion Analytics</span>
    <span class="info-pill">Real-Time Feedback</span>
    <span class="info-pill">Lecture Trend Graphs</span>
    """, unsafe_allow_html=True)

# ---------------- LIVE ANALYSIS ----------------
elif menu == "🔍 Live Analysis":
    st.markdown('<div class="main-title">Real-Time Classroom Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Live monitoring statistics generated from AI modules.</div>', unsafe_allow_html=True)

    if df.empty:
        st.warning("No monitoring data found. Run main.py first.")
    else:
        latest = df.iloc[-1]

        attention_rate = df["attention"].mean() * 100
        sleep_count = df["sleep"].sum()
        phone_count = df["phone"].sum()

        latest_total = int(latest.get("total_students", 0))
        latest_attentive = int(latest.get("attentive_students", 0))
        latest_not_attentive = int(latest.get("not_attentive_students", 0))

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Attention Rate</div>
                <div class="metric-value">{attention_rate:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Sleep Alerts</div>
                <div class="metric-value">{int(sleep_count)}</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Phone Detections</div>
                <div class="metric-value">{int(phone_count)}</div>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Students Detected</div>
                <div class="metric-value">{latest_total}</div>
            </div>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Attentive Students", latest_attentive)

        with c2:
            st.metric("Not Attentive Students", latest_not_attentive)

        with c3:
            if "feedback" in df.columns:
                st.metric("System Feedback", latest["feedback"])
            else:
                st.metric("System Feedback", "No feedback data")

        st.markdown('<div class="section-title">Compact Analytics Charts</div>', unsafe_allow_html=True)

        g1, g2 = st.columns(2)

        with g1:
            st.markdown("#### Attention Trend")
            fig, ax = plt.subplots(figsize=(4.5, 2.5), facecolor="white")
            ax.set_facecolor("white")
            ax.plot(df["attention"])
            ax.set_xlabel("Frames")
            ax.set_ylabel("Attention")
            ax.grid(True, alpha=0.25)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=False)

        with g2:
            st.markdown("#### Multi-Student Analytics")
            fig2, ax2 = plt.subplots(figsize=(4.5, 2.5), facecolor="white")
            ax2.set_facecolor("white")
            if all(col in df.columns for col in ["total_students", "attentive_students", "not_attentive_students"]):
                ax2.plot(df["total_students"], label="Total")
                ax2.plot(df["attentive_students"], label="Attentive")
                ax2.plot(df["not_attentive_students"], label="Not Attentive")
                ax2.legend(fontsize=8)
            ax2.set_xlabel("Frames")
            ax2.set_ylabel("Count")
            ax2.grid(True, alpha=0.25)
            fig2.tight_layout()
            st.pyplot(fig2, use_container_width=False)

        g3, g4 = st.columns(2)

        with g3:
            st.markdown("#### Sleep Detection")
            fig3, ax3 = plt.subplots(figsize=(4.5, 2.5), facecolor="white")
            ax3.set_facecolor("white")
            ax3.plot(df["sleep"])
            ax3.set_xlabel("Frames")
            ax3.set_ylabel("Sleep")
            ax3.grid(True, alpha=0.25)
            fig3.tight_layout()
            st.pyplot(fig3, use_container_width=False)

        with g4:
            st.markdown("#### Phone Usage")
            fig4, ax4 = plt.subplots(figsize=(4.5, 2.5), facecolor="white")
            ax4.set_facecolor("white")
            ax4.plot(df["phone"])
            ax4.set_xlabel("Frames")
            ax4.set_ylabel("Phone")
            ax4.grid(True, alpha=0.25)
            fig4.tight_layout()
            st.pyplot(fig4, use_container_width=False)

        st.markdown('<div class="section-title">Emotion Analytics</div>', unsafe_allow_html=True)

        if not emotion_df.empty and "emotion" in emotion_df.columns:
            e1, e2 = st.columns([1, 2])
            with e1:
                st.metric("Latest Emotion", emotion_df["emotion"].iloc[-1])
            with e2:
                emotion_counts = emotion_df["emotion"].value_counts()
                fig5, ax5 = plt.subplots(figsize=(5, 2.6), facecolor="white")
                ax5.set_facecolor("white")
                ax5.bar(emotion_counts.index, emotion_counts.values)
                ax5.set_xlabel("Emotion")
                ax5.set_ylabel("Count")
                ax5.grid(True, axis="y", alpha=0.25)
                plt.xticks(rotation=25)
                fig5.tight_layout()
                st.pyplot(fig5, use_container_width=False)
        else:
            st.info("Emotion data not found. Run emotion_detection.py separately.")

        st.markdown('<div class="section-title">Detailed View</div>', unsafe_allow_html=True)
        st.dataframe(df.tail(20), use_container_width=True)

# ---------------- HOW IT WORKS ----------------
elif menu == "⚙️ How It Works":
    st.markdown('<div class="main-title">Methodology & Working Pipeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Step-by-step flow of the AI classroom monitoring system.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>System Methodology</h2>
        <p><b>1. Data Collection:</b> The system captures real-time classroom video using a webcam or classroom camera.</p>
        <p><b>2. Data Preprocessing:</b> Frames are converted into RGB format and prepared for AI model processing.</p>
        <p><b>3. Feature Extraction:</b> Facial landmarks, nose position, iris position, eye region, and object features are extracted.</p>
        <p><b>4. Behavioral Analysis:</b> The system analyzes attentiveness, drowsiness, phone usage, and emotional state.</p>
        <p><b>5. Data Logging:</b> Results are stored in CSV files with timestamps for lecture-wise analytics.</p>
        <p><b>6. Output Generation:</b> Dashboard displays metrics, charts, emotion distribution, and real-time teacher feedback.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Pipeline Flow</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <pre style="background:#ffffff;color:#111827;font-size:15px;border-radius:12px;">
Camera Feed
   ↓
Frame Extraction
   ↓
Face Detection + Landmark Detection
   ↓
Head Pose + Eye Gaze Analysis
   ↓
Attention / Sleep / Phone / Emotion Detection
   ↓
CSV Data Logging
   ↓
Dashboard Visualization
   ↓
Real-Time Feedback to Teacher
    </pre>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MODEL INFO ----------------
elif menu == "🧠 Model Information":
    st.markdown('<div class="main-title">Model Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">AI models, libraries, and techniques used in the system.</div>', unsafe_allow_html=True)

    model_data = pd.DataFrame({
        "Module": [
            "Face Detection",
            "Attention Detection",
            "Eye Visibility Detection",
            "Sleep Detection",
            "Phone Detection",
            "Emotion Detection",
            "Dashboard Analytics"
        ],
        "Technology / Model": [
            "MediaPipe Face Mesh",
            "Head Pose + Eye Gaze Estimation",
            "Eye Region Intensity Analysis",
            "Eye Aspect Ratio (EAR)",
            "YOLOv8",
            "DeepFace + TensorFlow",
            "Streamlit + Pandas + Matplotlib"
        ],
        "Purpose": [
            "Detect face landmarks for multiple students",
            "Classify attentive or not attentive behavior",
            "Detect hidden eyes or sunglasses-like obstruction",
            "Detect prolonged eye closure and drowsiness",
            "Detect mobile phone usage in classroom",
            "Recognize facial emotion from webcam frames",
            "Generate graphs, metrics, and classroom reports"
        ]
    })

    st.dataframe(model_data, use_container_width=True)

    st.markdown("""
    <div class="card">
        <h2>Real-Time Feedback Rules</h2>
        <p>📱 <b>Phone detected:</b> System warns teacher about phone usage.</p>
        <p>😴 <b>Drowsiness detected:</b> System suggests taking a short interactive break.</p>
        <p>📉 <b>Low attention:</b> System suggests asking questions or changing teaching method.</p>
        <p>⚠️ <b>Moderate attention:</b> System suggests increasing classroom interaction.</p>
        <p>✅ <b>Good engagement:</b> System suggests continuing the lecture.</p>
    </div>
    """, unsafe_allow_html=True)