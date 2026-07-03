import streamlit as st
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Guess the Number", page_icon="🎯", layout="centered")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & base ── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #0b0f1a !important;
}
[data-testid="stAppViewContainer"] > .main {
    background: #0b0f1a;
}
[data-testid="stSidebar"] { display: none; }
* { box-sizing: border-box; }

/* ── Typography ── */
body, p, div, span, label {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #c8d6f0;
}

/* ── Hero title ── */
.hero-title {
    font-family: 'Space Mono', monospace !important;
    font-size: clamp(2rem, 6vw, 3.8rem);
    font-weight: 700;
    color: #00e5ff;
    letter-spacing: -1px;
    line-height: 1.1;
    margin: 0 0 6px 0;
}
.hero-sub {
    font-size: 1rem;
    color: #5a7a9a;
    margin-bottom: 2.5rem;
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Card ── */
.game-card {
    background: #111827;
    border: 1px solid #1e2d42;
    border-radius: 16px;
    padding: 2.2rem 2.4rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.game-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00e5ff, #7b61ff);
    border-radius: 16px 16px 0 0;
}

/* ── Stats row ── */
.stats-row {
    display: flex;
    gap: 1.2rem;
    margin-bottom: 1.8rem;
}
.stat-pill {
    flex: 1;
    background: #0d1520;
    border: 1px solid #1e2d42;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    text-align: center;
}
.stat-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #3a5a7a;
    margin-bottom: 2px;
    font-family: 'Space Mono', monospace !important;
}
.stat-value {
    font-family: 'Space Mono', monospace !important;
    font-size: 1.4rem;
    font-weight: 700;
    color: #00e5ff;
}

/* ── Hint badge ── */
.hint-badge {
    display: inline-block;
    padding: 0.5rem 1.1rem;
    border-radius: 8px;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 1.5rem;
}
.hint-higher { background: #0a2a1a; color: #00e676; border: 1px solid #00e676; }
.hint-lower  { background: #2a0a0a; color: #ff5252; border: 1px solid #ff5252; }
.hint-start  { background: #0d1520; color: #5a7a9a; border: 1px solid #1e2d42; }

/* ── Input ── */
.stNumberInput > div > div > input {
    background: #0d1520 !important;
    border: 1px solid #1e2d42 !important;
    border-radius: 10px !important;
    color: #00e5ff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    padding: 0.8rem !important;
    transition: border-color 0.2s;
}
.stNumberInput > div > div > input:focus {
    border-color: #00e5ff !important;
    box-shadow: 0 0 0 3px rgba(0,229,255,0.12) !important;
}
.stNumberInput > div > div > button {
    background: #1e2d42 !important;
    border: none !important;
    color: #00e5ff !important;
}
.stNumberInput label {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.8rem !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #3a5a7a !important;
}

/* ── Buttons ── */
.stButton > button {
    width: 100%;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.3px;
    padding: 0.65rem 0 !important;
    transition: all 0.18s ease;
    border: none !important;
}
.stButton:first-of-type > button {
    background: linear-gradient(135deg, #00e5ff, #00b8d4) !important;
    color: #0b0f1a !important;
}
.stButton:first-of-type > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 24px rgba(0,229,255,0.25) !important;
}
.stButton:last-of-type > button {
    background: #0d1520 !important;
    color: #5a7a9a !important;
    border: 1px solid #1e2d42 !important;
}
.stButton:last-of-type > button:hover {
    color: #00e5ff !important;
    border-color: #00e5ff !important;
}

/* ── Win / Loss banner ── */
.result-banner {
    border-radius: 12px;
    padding: 1.6rem 2rem;
    text-align: center;
    margin-bottom: 1.2rem;
}
.result-banner.win {
    background: linear-gradient(135deg, #002a1a, #001f30);
    border: 1px solid #00e676;
}
.result-banner.lose {
    background: linear-gradient(135deg, #1a0010, #120010);
    border: 1px solid #7b61ff;
}
.result-emoji { font-size: 2.8rem; margin-bottom: 0.4rem; }
.result-title {
    font-family: 'Space Mono', monospace !important;
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}
.result-title.win { color: #00e676; }
.result-title.lose { color: #7b61ff; }
.result-msg { color: #5a7a9a; font-size: 0.9rem; }

/* ── History ── */
.history-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0;
    border-bottom: 1px solid #1e2d42;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.82rem;
}
.history-item:last-child { border-bottom: none; }
.hist-num { color: #c8d6f0; }
.hist-hint-h { color: #00e676; }
.hist-hint-l { color: #ff5252; }
.hist-hint-w { color: #00e5ff; }
.history-title {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #3a5a7a;
    margin-bottom: 0.6rem;
    font-family: 'Space Mono', monospace !important;
}

/* ── Range bar ── */
.range-wrap {
    margin-bottom: 1.4rem;
}
.range-label {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.72rem;
    color: #3a5a7a;
    margin-bottom: 4px;
}
.range-track {
    height: 6px;
    background: #1e2d42;
    border-radius: 99px;
    overflow: hidden;
    position: relative;
}
.range-fill {
    height: 100%;
    background: linear-gradient(90deg, #00e5ff, #7b61ff);
    border-radius: 99px;
    transition: width 0.4s ease;
}

/* ── Max attempts warning ── */
.max-att-warn {
    background: #1a0d00;
    border: 1px solid #ff9100;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-size: 0.82rem;
    color: #ff9100;
    font-family: 'Space Mono', monospace !important;
    margin-bottom: 1.2rem;
    text-align: center;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
MAX_TRIES = 7

def new_game():
    st.session_state.number   = random.randint(1, 10)
    st.session_state.tries    = 0
    st.session_state.status   = "playing"   # playing | won | lost
    st.session_state.hint     = "start"     # start | higher | lower
    st.session_state.history  = []
    st.session_state.low      = 1
    st.session_state.high     = 10
    st.session_state.guess    = 5

if "number" not in st.session_state:
    new_game()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown('<h1 class="hero-title">GUESS_<br>THE NUMBER</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">1 → 10 &nbsp;·&nbsp; Up to 7 attempts</p>', unsafe_allow_html=True)

# ── Win / Loss result ─────────────────────────────────────────────────────────
if st.session_state.status == "won":
    st.balloons()
    st.markdown(f"""
    <div class="result-banner win">
        <div class="result-emoji">🎯</div>
        <div class="result-title win">CRACKED IT</div>
        <div class="result-msg">You nailed <strong style="color:#00e5ff">{st.session_state.number}</strong> in <strong style="color:#00e676">{st.session_state.tries}</strong> {"try" if st.session_state.tries == 1 else "tries"}.</div>
    </div>""", unsafe_allow_html=True)

elif st.session_state.status == "lost":
    st.balloons()
    st.markdown(f"""
    <div class="result-banner lose">
        <div class="result-emoji">💀</div>
        <div class="result-title lose">OUT OF TRIES</div>
        <div class="result-msg">The number was <strong style="color:#7b61ff">{st.session_state.number}</strong>. Better luck next time.</div>
    </div>""", unsafe_allow_html=True)

# ── Game card ─────────────────────────────────────────────────────────────────
st.markdown('<div class="game-card">', unsafe_allow_html=True)

# Stats row
remaining = MAX_TRIES - st.session_state.tries
st.markdown(f"""
<div class="stats-row">
    <div class="stat-pill">
        <div class="stat-label">Attempt</div>
        <div class="stat-value">{st.session_state.tries}<span style="font-size:0.9rem;color:#3a5a7a">/{MAX_TRIES}</span></div>
    </div>
    <div class="stat-pill">
        <div class="stat-label">Remaining</div>
        <div class="stat-value" style="color:{'#ff5252' if remaining <= 2 else '#00e5ff'}">{remaining}</div>
    </div>
    <div class="stat-pill">
        <div class="stat-label">Range</div>
        <div class="stat-value" style="font-size:1rem;padding-top:4px">{st.session_state.low}–{st.session_state.high}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Range bar — narrows as user eliminates numbers
span     = st.session_state.high - st.session_state.low + 1
pct      = round((1 - (span - 1) / 9) * 100)
st.markdown(f"""
<div class="range-wrap">
    <div class="range-label"><span>Narrowed in</span><span>{pct}%</span></div>
    <div class="range-track"><div class="range-fill" style="width:{pct}%"></div></div>
</div>
""", unsafe_allow_html=True)

# Hint badge
hint_map = {
    "start":  ('hint-start',  '🎮  Enter your first guess'),
    "higher": ('hint-higher', '▲  Go higher'),
    "lower":  ('hint-lower',  '▼  Go lower'),
}
cls, txt = hint_map[st.session_state.hint]
st.markdown(f'<span class="hint-badge {cls}">{txt}</span>', unsafe_allow_html=True)

# Low-tries warning
if remaining <= 2 and st.session_state.status == "playing":
    st.markdown(f'<div class="max-att-warn">⚠ Only {remaining} {"try" if remaining == 1 else "tries"} left — choose wisely.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close card

# ── Input + action (only while playing) ──────────────────────────────────────
if st.session_state.status == "playing":
    guess_val = st.number_input(
        "YOUR GUESS",
        min_value=1, max_value=10,
        value=st.session_state.guess,
        step=1,
        key="guess_input",
    )

    col_guess, col_new = st.columns([3, 1])
    with col_guess:
        if st.button("Submit guess", use_container_width=True):
            st.session_state.tries += 1
            st.session_state.guess  = guess_val

            if guess_val == st.session_state.number:
                st.session_state.status = "won"
                st.session_state.history.append((guess_val, "win"))
            elif st.session_state.tries >= MAX_TRIES:
                st.session_state.status = "lost"
                st.session_state.history.append((guess_val, "higher" if guess_val < st.session_state.number else "lower"))
            elif guess_val < st.session_state.number:
                st.session_state.hint = "higher"
                st.session_state.low  = max(st.session_state.low, guess_val + 1)
                st.session_state.history.append((guess_val, "higher"))
            else:
                st.session_state.hint = "lower"
                st.session_state.high = min(st.session_state.high, guess_val - 1)
                st.session_state.history.append((guess_val, "lower"))
            st.rerun()

    with col_new:
        if st.button("New game", use_container_width=True):
            new_game()
            st.rerun()

else:
    if st.button("Play again", use_container_width=True):
        new_game()
        st.rerun()

# ── Guess history ─────────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.markdown('<div class="history-title">Guess history</div>', unsafe_allow_html=True)

    hint_label = {"higher": ("hist-hint-h", "▲ too low"), "lower": ("hist-hint-l", "▼ too high"), "win": ("hist-hint-w", "✓ correct")}

    for i, (g, h) in enumerate(st.session_state.history, 1):
        cls, lbl = hint_label[h]
        st.markdown(f"""
        <div class="history-item">
            <span style="color:#3a5a7a">#{i:02d}</span>
            <span class="hist-num">{g}</span>
            <span class="{cls}">{lbl}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)