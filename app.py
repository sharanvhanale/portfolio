import streamlit as st

st.set_page_config(
    page_title="Sharan K. Vhanale — PhD Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Hero gradient banner */
.hero-banner {
    background: linear-gradient(135deg, #f0ebff 0%, #e8f8f0 100%);
    border-radius: 20px;
    padding: 2.5rem 3rem;
    border: 1px solid #d6c8f5;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(124,45,237,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #6d28d9, #059669);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0; line-height: 1.1;
}
.hero-title {
    color: #374151;
    font-size: 1.05rem;
    margin-top: 0.5rem;
    font-weight: 500;
}
.phd-badge {
    display: inline-block;
    background: linear-gradient(90deg, #ede9fe, #d1fae5);
    border: 1px solid #a78bfa;
    border-radius: 50px;
    padding: 0.4rem 1.1rem;
    font-size: 0.82rem;
    font-weight: 600;
    color: #5b21b6;
    margin-top: 0.8rem;
}
.stat-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.2rem 1rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(109,40,217,0.06);
}
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(90deg, #6d28d9, #059669);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label { color: #6b7280; font-size: 0.82rem; margin-top: 2px; }

.section-eyebrow {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7c2ded;
    margin-bottom: 0.25rem;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #12203f;
    margin-bottom: 0.4rem;
}
.section-sub { color: #6b7280; font-size: 0.95rem; margin-bottom: 1.5rem; }

.timeline-card {
    background: white;
    border-left: 4px solid #7c2ded;
    border-radius: 0 14px 14px 0;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.timeline-role { font-weight: 700; font-size: 1.05rem; color: #12203f; }
.timeline-company { color: #7c2ded; font-weight: 600; font-size: 0.92rem; }
.timeline-date {
    display: inline-block;
    background: #ede9fe;
    color: #5b21b6;
    border-radius: 20px;
    padding: 0.15rem 0.7rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.timeline-desc { color: #374151; font-size: 0.9rem; line-height: 1.6; }

.skill-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.1rem;
    text-align: center;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
    transition: all 0.2s;
    height: 100%;
}
.skill-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
.skill-name { font-weight: 700; color: #12203f; font-size: 0.9rem; }
.skill-desc { color: #6b7280; font-size: 0.78rem; margin-top: 0.2rem; }

.proj-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.3rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    height: 100%;
}
.proj-title { font-weight: 700; font-size: 1rem; color: #12203f; margin-bottom: 0.4rem; }
.proj-desc { color: #374151; font-size: 0.88rem; line-height: 1.55; }

.pub-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.3rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.pub-title { font-weight: 700; color: #12203f; font-size: 0.95rem; line-height: 1.4; }
.pub-conf {
    display: inline-block;
    background: #f3f4f6;
    color: #374151;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.78rem;
    font-weight: 600;
}
.scopus-badge {
    display: inline-block;
    background: #fff7ed;
    color: #c2410c;
    border: 1px solid #fed7aa;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.78rem;
    font-weight: 600;
    margin-left: 0.3rem;
}
.best-paper {
    display: inline-block;
    background: #fefce8;
    color: #a16207;
    border: 1px solid #fde68a;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.78rem;
    font-weight: 600;
    margin-left: 0.3rem;
}
.cite-chip {
    float: right;
    background: #f3f4f6;
    color: #374151;
    border-radius: 8px;
    padding: 0.1rem 0.55rem;
    font-size: 0.8rem;
    font-weight: 600;
}

.edu-card {
    background: linear-gradient(135deg, #faf5ff, #f0fdf4);
    border: 1px solid #d8b4fe;
    border-radius: 14px;
    padding: 1.5rem;
}
.edu-degree { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: #12203f; }
.edu-uni { color: #6b7280; font-size: 0.88rem; margin-top: 0.2rem; }
.grade-row { display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0; border-bottom: 1px solid #e5e7eb; }
.grade-label { color: #6b7280; font-size: 0.85rem; }
.grade-value { font-weight: 700; color: #12203f; }
.bavarian-value { font-weight: 700; color: #059669; }

.metric-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.4rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.metric-value { font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 700; color: #6d28d9; }
.metric-label { color: #6b7280; font-size: 0.82rem; margin-top: 0.2rem; }
.metric-platform { font-weight: 700; color: #12203f; font-size: 0.92rem; margin-bottom: 0.5rem; }

.cert-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.9rem;
    margin-bottom: 0.7rem;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
}
.cert-icon { font-size: 1.4rem; }
.cert-title { font-weight: 600; color: #12203f; font-size: 0.9rem; }
.cert-org { color: #6b7280; font-size: 0.8rem; }
.cert-year {
    margin-left: auto;
    background: #f3f4f6;
    color: #374151;
    border-radius: 8px;
    padding: 0.15rem 0.55rem;
    font-size: 0.78rem;
    font-weight: 600;
    white-space: nowrap;
}

.impact-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.3rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    height: 100%;
}

.research-panel {
    background: linear-gradient(135deg, #f5f3ff 0%, #ecfdf5 100%);
    border: 1px solid #c4b5fd;
    border-radius: 20px;
    padding: 2rem;
}
.research-thread {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

.social-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 50px;
    padding: 0.35rem 0.9rem;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none;
    color: #374151;
    margin: 0.2rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}

.iis-step {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
}
.step-num {
    background: linear-gradient(135deg, #7c2ded, #059669);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
    line-height: 32px;
    text-align: center;
}

.footer-band {
    background: #12203f;
    border-radius: 20px;
    padding: 2.5rem 3rem;
    color: white;
    margin-top: 2rem;
    text-align: center;
}
.footer-name { font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 700; }
.footer-tagline { color: #9ca3af; font-size: 0.92rem; margin-top: 0.5rem; }

div[data-testid="stHorizontalBlock"] > div { padding: 0 0.4rem; }
section[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-banner">
    <p style="color:#7c2ded;font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.4rem;">
        🎓 PhD Application Portfolio
    </p>
    <p class="hero-name">Sharan Kashinath Vhanale</p>
    <p class="hero-title">
        Assistant Professor &nbsp;|&nbsp; AI &amp; Deep Learning Engineer &nbsp;|&nbsp;
        Robotics &amp; ML &nbsp;|&nbsp; Full Stack .NET Developer
    </p>
    <div>
        <span style="color:#374151;font-size:0.9rem;">📍 Pune, Maharashtra, India</span>
    </div>
    <div class="phd-badge">
        🎯 Actively targeting PhD positions — TUM • Max Planck • RWTH Aachen • TU Berlin • Heidelberg • KIT • ETH Zurich • Stuttgart
    </div>
</div>
""", unsafe_allow_html=True)

# Stats
c1, c2, c3, c4 = st.columns(4)
for col, num, label in [
    (c1, "7+", "Years Experience"),
    (c2, "6+", "Publications"),
    (c3, "56", "Total Citations"),
    (c4, "7+", "Institutions Mentored"),
]:
    col.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{num}</div>
        <div class="stat-label">{label}</div>
    </div>""", unsafe_allow_html=True)

# Social links
st.markdown("""
<div style="margin:1.2rem 0 0.5rem;text-align:center;">
    <a class="social-pill" href="https://www.linkedin.com/in/sharan-vhanale/" target="_blank">🔗 LinkedIn</a>
    <a class="social-pill" href="https://github.com/sharanvhanale" target="_blank">🐙 GitHub</a>
    <a class="social-pill" href="https://scholar.google.com/citations?user=QYnqe70AAAAJ" target="_blank">📚 Google Scholar</a>
    <a class="social-pill" href="https://www.researchgate.net/profile/Sharan-Vhanale" target="_blank">🔬 ResearchGate</a>
    <a class="social-pill" href="https://www.scopus.com/authid/detail.uri?authorId=57194378808" target="_blank">📖 Scopus</a>
    <a class="social-pill" href="https://orcid.org/0000-0003-4557-7324" target="_blank">🆔 ORCID</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# NAVIGATION TABS
# ══════════════════════════════════════════════════════════════════════════════
tabs = st.tabs([
    "💼 Experience",
    "🛠️ Tech Stack",
    "🚀 Projects",
    "🧠 EEG Research",
    "📊 Metrics",
    "📄 Publications",
    "🎓 Education",
    "🏆 Certifications",
    "🤝 Collaboration",
    "🖥️ IIS Deploy",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown('<p class="section-eyebrow">Career Journey</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Professional Experience</p>', unsafe_allow_html=True)

    for role, company, location, date, desc in [
        (
            "Assistant Professor",
            "Tolani Maritime Institute",
            "Pune, India",
            "Jan 2022 – Present",
            "Department of Computer Engineering. Courses: AIML, NLP, Robotics, ML, Python, Data Science. "
            "Research: EEG-BCI, GNN, XAI, LLMs. Mentored 15+ final year projects, drafted 2 patent applications "
            "with student teams. Serving as IEEE Student Branch Faculty Coordinator.",
        ),
        (
            "Senior Software Engineer",
            "Flo2Cash",
            "Auckland, NZ (Remote)",
            "Jun 2021 – Dec 2021",
            ".NET Core microservices for payment gateway integrations. Angular frontend development. "
            "Achieved 40% performance improvement in high-volume transaction processing pipelines.",
        ),
        (
            ".NET Developer",
            "Saviant Consulting",
            "Pune, India",
            "Mar 2017 – Mar 2020",
            "Full stack C#/.NET development. Built SignalR real-time dashboards for industrial IoT data monitoring. "
            "Optimized SQL Server queries and managed CI/CD pipelines in Azure DevOps. Delivered solutions for 3 enterprise clients.",
        ),
    ]:
        st.markdown(f"""
        <div class="timeline-card">
            <span class="timeline-date">{date}</span>
            <div class="timeline-role">{role}</div>
            <div class="timeline-company">{company} &nbsp;·&nbsp; {location}</div>
            <div class="timeline-desc" style="margin-top:0.5rem;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — TECH STACK
# ══════════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown('<p class="section-eyebrow">Toolkit</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Technical Expertise</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Comprehensive stack across AI research and enterprise full-stack development.</p>', unsafe_allow_html=True)

    skills = [
        ("🧠", "Deep Learning", "PyTorch, TensorFlow"),
        ("🔥", "PyTorch & Python", "Primary ML Stack"),
        ("🕸️", "Graph Neural Networks", "GNN, PyG"),
        ("🔍", "Explainable AI", "XAI, SHAP, LIME"),
        ("💬", "Large Language Models", "BART, GPT Fine-tuning"),
        ("👁️", "Computer Vision", "CNN, ViT, OpenCV"),
        ("💻", "C# / .NET", "Core, MVC, Web API"),
        ("🗄️", "SQL Server & Azure", "DB, DevOps, Cloud"),
        ("⚡", "Angular & SignalR", "Real-time Web"),
        ("🤖", "Robotics & IIoT", "ROS, Digital Twin"),
    ]

    rows = [skills[i:i+4] for i in range(0, len(skills), 4)]
    for row in rows:
        cols = st.columns(len(row))
        for col, (icon, name, desc) in zip(cols, row):
            col.markdown(f"""
            <div class="skill-card">
                <div class="skill-icon">{icon}</div>
                <div class="skill-name">{name}</div>
                <div class="skill-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown('<p class="section-eyebrow">Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Featured Projects</p>', unsafe_allow_html=True)

    st.markdown("#### 🔬 Research Projects")
    r1, r2, r3 = st.columns(3)
    for col, title, desc, tags in [
        (r1, "EEG-to-Text Decoding",
         "Translating raw EEG signals to natural language using VQ-VAE + BART + GNN pipeline.",
         ["EEG", "VQ-VAE", "BART", "GNN", "BCI"]),
        (r2, "Emotion AI Multimodal",
         "Sensor fusion of EEG, facial expressions, and voice for robust emotion recognition.",
         ["Multimodal", "Emotion AI", "Fusion"]),
        (r3, "GNN Power Grid Stability",
         "Graph neural network architecture for intelligent power grid fault detection.",
         ["GNN", "Power Systems", "Fault Detection"]),
    ]:
        col.markdown(f"""
        <div class="proj-card">
            <div class="proj-title">{title}</div>
            <div class="proj-desc">{desc}</div>
            <div style="margin-top:0.8rem">{" ".join(f'<span style="background:#ede9fe;color:#5b21b6;border-radius:6px;padding:0.15rem 0.55rem;font-size:0.75rem;font-weight:600;margin-right:0.3rem">{t}</span>' for t in tags)}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("#### 🏭 Industry Projects")
    i1, i2, i3 = st.columns(3)
    for col, title, desc, tags in [
        (i1, "P-H Dashboard",
         "Real-time .NET + SignalR dashboard for large-scale industrial process monitoring.",
         [".NET", "SignalR", "Real-time"]),
        (i2, "RL Industrial Optimization",
         "Reinforcement learning agents for process control and production optimization.",
         ["RL", "IIoT", "Optimization"]),
        (i3, "Digital Twin IIoT",
         "Digital twin framework connecting physical robotic systems to virtual counterparts.",
         ["Digital Twin", "IIoT", "Robotics"]),
    ]:
        col.markdown(f"""
        <div class="proj-card">
            <div class="proj-title">{title}</div>
            <div class="proj-desc">{desc}</div>
            <div style="margin-top:0.8rem">{" ".join(f'<span style="background:#d1fae5;color:#065f46;border-radius:6px;padding:0.15rem 0.55rem;font-size:0.75rem;font-weight:600;margin-right:0.3rem">{t}</span>' for t in tags)}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — EEG/BCI RESEARCH
# ══════════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="research-panel">
        <span style="display:inline-block;background:#7c2ded;color:white;border-radius:20px;padding:0.25rem 0.9rem;font-size:0.8rem;font-weight:700;margin-bottom:1rem;">
            Primary Research Focus
        </span>
        <p style="font-family:'Playfair Display',serif;font-size:1.8rem;font-weight:700;color:#12203f;margin-bottom:0.4rem;">
            EEG-to-Language Research
        </p>
        <p style="color:#7c2ded;font-weight:600;margin-bottom:0.8rem;">
            Decoding neural signals into natural language using deep learning
        </p>
        <p style="color:#374151;line-height:1.7;max-width:700px;">
            My core research focuses on translating raw EEG brain signals into coherent text using a novel 
            multi-stage pipeline: <strong>VQ-VAE</strong> for neural tokenization → <strong>GNN</strong> for 
            spatial electrode-relationship modeling → <strong>BART</strong> for sequence-to-sequence language 
            generation → <strong>XAI</strong> for interpretability and clinical validation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("#### Research Threads")

    t1, t2 = st.columns(2)
    threads = [
        ("⚡", "Neural Tokenization (VQ-VAE)",
         "Discrete latent code learning from raw, continuous EEG signals via Vector Quantization.",
         ["VQ-VAE", "Quantization", "Latent Space"]),
        ("🕸️", "Spatial Modeling (GNN)",
         "Graph-based EEG electrode topology modeling to capture dynamic brain-region interactions.",
         ["GNN", "Graph Learning", "Topology"]),
        ("💬", "Language Decoding (BART)",
         "Transformer seq2seq architecture to translate neural tokens into coherent natural language.",
         ["BART", "Transformer", "NLP"]),
        ("🔍", "Interpretability (XAI)",
         "SHAP/LIME visual feature-importance maps to validate deep neural decisions for clinical use.",
         ["XAI", "SHAP", "Interpretability"]),
    ]
    for i, (icon, title, desc, tags) in enumerate(threads):
        col = t1 if i % 2 == 0 else t2
        col.markdown(f"""
        <div class="research-thread">
            <div style="font-size:1.3rem;margin-bottom:0.3rem;">{icon}</div>
            <div style="font-weight:700;color:#12203f;margin-bottom:0.3rem;">{title}</div>
            <div style="color:#374151;font-size:0.88rem;line-height:1.5;margin-bottom:0.6rem;">{desc}</div>
            <div>{" ".join(f'<span style="background:#f3f4f6;color:#374151;border-radius:6px;padding:0.12rem 0.5rem;font-size:0.75rem;font-weight:600;margin-right:0.25rem">{t}</span>' for t in tags)}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — RESEARCH METRICS
# ══════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown('<p class="section-eyebrow">Academic Impact</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Research Metrics</p>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    for col, icon, platform, value, sub, url in [
        (m1, "📚", "Google Scholar", "56", "Citations · h-index: 2",
         "https://scholar.google.com/citations?user=QYnqe70AAAAJ"),
        (m2, "📖", "Scopus", "40", "Citations · ID: 57194378808",
         "https://www.scopus.com/authid/detail.uri?authorId=57194378808"),
        (m3, "🔬", "ResearchGate", "2,138", "Total Profile Reads",
         "https://www.researchgate.net/profile/Sharan-Vhanale"),
        (m4, "🆔", "ORCID", "Verified", "0000-0003-4557-7324",
         "https://orcid.org/0000-0003-4557-7324"),
    ]:
        col.markdown(f"""
        <div class="metric-card">
            <div style="font-size:1.8rem;margin-bottom:0.3rem;">{icon}</div>
            <div class="metric-platform">{platform}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{sub}</div>
            <div style="margin-top:0.8rem;">
                <a href="{url}" target="_blank" style="color:#7c2ded;font-size:0.82rem;font-weight:600;text-decoration:none;">
                    View Profile ↗
                </a>
            </div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 6 — PUBLICATIONS
# ══════════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.markdown('<p class="section-eyebrow">Academic Output</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Selected Publications</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Peer-reviewed research across IEEE, Springer, and international journals.</p>', unsafe_allow_html=True)

    publications = [
        ("EEG-Based Emotion Recognition Using Deep Learning: A Comparative Study",
         "IEEE INDICON 2023", 12, True, False, ["EEG", "Emotion Recognition", "Deep Learning"]),
        ("Multi-Modal Emotion Recognition: EEG, Facial, and Voice Fusion",
         "IEEE INDICON 2022", 6, True, True, ["Multimodal", "Emotion AI"]),
        ("Graph Neural Networks for Power Grid Stability Analysis",
         "IEEE Access 2023", 8, True, False, ["GNN", "Power Grid", "Stability"]),
        ("Explainable AI for Brain-Computer Interfaces: A Survey",
         "Springer Neural Computing 2022", 15, True, False, ["XAI", "BCI", "Survey"]),
        ("VQ-VAE Based EEG Signal Tokenization for Language Decoding",
         "IEEE EMBC 2023", 6, True, False, ["VQ-VAE", "EEG", "Language Decoding"]),
        ("Real-Time Industrial Process Monitoring Using Digital Twin",
         "IJECES 2021", 9, False, False, ["Digital Twin", "IIoT"]),
    ]

    col_a, col_b = st.columns(2)
    for i, (title, conf, cites, scopus, best, tags) in enumerate(publications):
        col = col_a if i % 2 == 0 else col_b
        badges = f'<span class="pub-conf">{conf}</span>'
        if scopus:
            badges += '<span class="scopus-badge">Scopus Indexed</span>'
        if best:
            badges += '<span class="best-paper">🏆 Best Paper Award</span>'
        tag_html = " ".join(f'<span style="background:#f3f4f6;color:#374151;border-radius:5px;padding:0.1rem 0.45rem;font-size:0.75rem;font-weight:500;margin-right:0.25rem">{t}</span>' for t in tags)
        col.markdown(f"""
        <div class="pub-card">
            <div style="margin-bottom:0.6rem;">
                {badges}
                <span class="cite-chip">💬 {cites}</span>
            </div>
            <div class="pub-title">{title}</div>
            <div style="margin-top:0.7rem;">{tag_html}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 — EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.markdown('<p class="section-eyebrow">Background</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Education & Qualifications</p>', unsafe_allow_html=True)

    e1, e2 = st.columns(2)
    for col, degree, year, cgpa, bavarian in [
        (e1, "MTech — Mechatronics & Robotics", "2021", "8.5 / 10", "1.5"),
        (e2, "BE — Computer Engineering", "2017", "8.45 / 10", "1.6"),
    ]:
        col.markdown(f"""
        <div class="edu-card">
            <div style="font-size:1.6rem;margin-bottom:0.5rem;">🎓</div>
            <div class="edu-degree">{degree}</div>
            <div class="edu-uni">Savitribai Phule Pune University (SPPU) &nbsp;·&nbsp; {year}</div>
            <div style="margin-top:1rem;">
                <div class="grade-row">
                    <span class="grade-label">Indian CGPA (Scale 10)</span>
                    <span class="grade-value">{cgpa}</span>
                </div>
                <div class="grade-row" style="border-bottom:none;">
                    <span class="grade-label">German Bavarian Grade</span>
                    <span class="bavarian-value">{bavarian} — Sehr Gut</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
    with st.expander("📐 View German Bavarian Grade Conversion Formula"):
        st.markdown("""
**Formula:**  `German Grade = 1 + 3 × ((N_max − N_d) / (N_max − N_min))`

| Variable | Value | Description |
|----------|-------|-------------|
| N_max | 10.0 | Maximum possible score |
| N_min | 6.5 | Minimum passing score |
| N_d (MTech) | 8.5 | Achieved CGPA |
| N_d (BE) | 8.45 | Achieved CGPA |

**MTech Calculation:**  
`1 + 3 × ((10 − 8.5) / (10 − 6.5))` = `1 + 3 × 0.429` = **1.5** *(Sehr Gut / Very Good)*

**BE Calculation:**  
`1 + 3 × ((10 − 8.45) / (10 − 6.5))` = `1 + 3 × 0.443` = **1.6** *(Sehr Gut / Very Good)*
""")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 8 — CERTIFICATIONS & AWARDS
# ══════════════════════════════════════════════════════════════════════════════
with tabs[7]:
    st.markdown('<p class="section-eyebrow">Recognition</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Certifications & Awards</p>', unsafe_allow_html=True)

    certs = [
        ("🏆", "IEEE INDICON Best Paper Award", "IEEE", "2022"),
        ("🎖️", "IBM Data Science Professional Certificate", "IBM / Coursera", "2022"),
        ("🥇", "NPTEL Deep Learning — Elite + Gold", "IIT (NPTEL)", "2023"),
        ("🥈", "NPTEL Machine Learning — Elite", "IIT (NPTEL)", "2022"),
        ("🌟", "AICTE Margdarshan Mentor Recognition", "AICTE", "2023"),
        ("📘", "AI/ML Faculty Development Program", "ICT Academy", "2022"),
    ]
    for icon, title, org, year in certs:
        st.markdown(f"""
        <div class="cert-card">
            <span class="cert-icon">{icon}</span>
            <div>
                <div class="cert-title">{title}</div>
                <div class="cert-org">{org}</div>
            </div>
            <span class="cert-year">{year}</span>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 9 — COLLABORATION & SOCIAL IMPACT
# ══════════════════════════════════════════════════════════════════════════════
with tabs[8]:
    st.markdown('<p class="section-eyebrow">Giving Back</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Collaboration & Social Impact</p>', unsafe_allow_html=True)

    ci1, ci2, ci3 = st.columns(3)
    for col, icon, title, stat, desc in [
        (ci1, "👩‍🏫", "Student Mentorship", "15+ Projects",
         "Guided 15+ final year engineering projects at Tolani Maritime Institute. "
         "Drafted 2 patent applications with student teams. Serving as IEEE Student Branch Faculty Coordinator."),
        (ci2, "🌾", "Rural Digital Literacy", "200+ Beneficiaries",
         "Organized digital literacy workshops in rural Maharashtra, helping bridge the digital divide "
         "for underserved communities across multiple villages."),
        (ci3, "⚡", "IEEE Volunteering", "Section Member",
         "Active member of IEEE Pune Section. Organized technical symposiums, "
         "presented at seminars, and served as a paper reviewer for regional IEEE conferences."),
    ]:
        col.markdown(f"""
        <div class="impact-card">
            <div style="font-size:1.8rem;margin-bottom:0.5rem;">{icon}</div>
            <div style="font-weight:700;font-size:1rem;color:#12203f;margin-bottom:0.3rem;">{title}</div>
            <div style="display:inline-block;background:#ede9fe;color:#5b21b6;border-radius:8px;padding:0.15rem 0.6rem;font-size:0.8rem;font-weight:600;margin-bottom:0.7rem;">
                {stat}
            </div>
            <div style="color:#374151;font-size:0.88rem;line-height:1.6;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 10 — IIS DEPLOYMENT
# ══════════════════════════════════════════════════════════════════════════════
with tabs[9]:
    st.markdown('<p class="section-eyebrow">Technical Documentation</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Local IIS Deployment Guide</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Run the React portfolio on Windows Server via IIS Reverse Proxy + NSSM.</p>', unsafe_allow_html=True)

    steps = [
        ("Install Prerequisites",
         "Ensure **Node.js 20 LTS** is installed on the Windows Server machine.",
         None),
        ("Copy Application Files",
         "Clone or copy the repository files into your web root directory.",
         "C:\\inetpub\\portfolio\\"),
        ("Install Dependencies & Build",
         "Open PowerShell or Command Prompt as Administrator in the portfolio folder.",
         "npm install\nnpm run build"),
        ("Configure NSSM Service",
         "Install [NSSM](https://nssm.cc/) (Non-Sucking Service Manager) and register the Node.js app as a Windows Service.",
         'nssm install PortfolioApp "node" "C:\\inetpub\\portfolio\\dist\\index.mjs"'),
        ("Configure IIS Reverse Proxy",
         "Install **IIS Application Request Routing (ARR)** and **URL Rewrite** modules. Add a reverse proxy rule:",
         '<rule name="ReverseProxy" stopProcessing="true">\n  <match url="(.*)" />\n  <action type="Rewrite" url="http://localhost:PORT/{R:1}" />\n</rule>'),
        ("Access via LAN",
         "The portfolio is now accessible over your local network:",
         "http://192.168.x.x/portfolio\nhttp://SERVER-NAME/portfolio"),
    ]

    for i, (title, desc, code) in enumerate(steps):
        with st.expander(f"Step {i+1}: {title}", expanded=(i == 0)):
            st.markdown(desc)
            if code:
                st.code(code, language="bash" if i != 4 else "xml")

    st.info("💡 **Tip:** Since the portfolio is a static React/Vite site, you can also simply point IIS to the `dist/` folder as a static site — no Node.js service or reverse proxy needed!")

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.divider()
st.markdown("""
<div class="footer-band">
    <div class="footer-name">Sharan Kashinath Vhanale</div>
    <div class="footer-tagline">Seeking PhD opportunities in AI, Deep Learning & BCI Research in Germany</div>
    <div style="margin-top:1.2rem;display:flex;justify-content:center;gap:1.5rem;flex-wrap:wrap;">
        <a href="mailto:vhanalesharan05@gmail.com" style="color:#a78bfa;font-size:0.88rem;text-decoration:none;">✉️ vhanalesharan05@gmail.com</a>
        <a href="mailto:sharanvhanale@gmail.com" style="color:#a78bfa;font-size:0.88rem;text-decoration:none;">✉️ sharanvhanale@gmail.com</a>
        <span style="color:#9ca3af;font-size:0.88rem;">📍 Pune, Maharashtra, India</span>
    </div>
    <div style="margin-top:1rem;color:#4b5563;font-size:0.8rem;">© 2025 Sharan Kashinath Vhanale · Designed for PhD Applications</div>
</div>
""", unsafe_allow_html=True)
