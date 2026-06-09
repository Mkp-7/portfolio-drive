import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mukund Patel | Portfolio", page_icon="🚗", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"]{background:#04080f}
iframe{border:none!important}
</style>""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100vh;overflow:hidden;background:#04080f;font-family:'Segoe UI',system-ui,sans-serif}
#intro{position:fixed;inset:0;z-index:999;background:#04080f;display:flex;flex-direction:column;overflow:hidden}
#particle-canvas{position:absolute;inset:0;z-index:0;pointer-events:none}
#intro::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(74,144,217,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(74,144,217,.06) 1px,transparent 1px);background-size:60px 60px;animation:gridScroll 20s linear infinite;z-index:1;pointer-events:none}
@keyframes gridScroll{from{background-position:0 0}to{background-position:60px 60px}}
#intro::after{content:'';position:absolute;inset:0;z-index:2;background:radial-gradient(ellipse 70% 60% at 50% 45%,rgba(74,144,217,.08) 0%,transparent 70%);pointer-events:none}
#lnav{position:absolute;top:0;left:0;right:0;z-index:20;height:52px;display:flex;align-items:center;justify-content:space-between;padding:0 28px;background:rgba(4,8,15,.88);border-bottom:1px solid rgba(74,144,217,.1);backdrop-filter:blur(16px)}
.lnav-logo{font-size:14px;font-weight:700;color:#eef2ff;letter-spacing:.5px}
.lnav-logo span{color:#4a90d9}
.lnav-links{display:flex;gap:2px}
.lnav-link{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#3a4d68;padding:6px 11px;border-radius:6px;cursor:pointer;transition:all .2s;border:none;background:none;font-family:inherit}
.lnav-link:hover,.lnav-link.active{color:#c8d8f0;background:rgba(74,144,217,.1)}
.lnav-cta{font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;background:#4a90d9;color:#fff;border:none;border-radius:6px;padding:7px 15px;cursor:pointer;transition:all .2s;font-family:inherit}
.lnav-cta:hover{background:#5aa0e9}
#lscroll{position:absolute;inset:0;top:52px;overflow-y:auto;overflow-x:hidden;z-index:10}
.lsec{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px 24px 40px;position:relative}
.lsec-inner{width:100%;max-width:820px;margin:0 auto}
.lsec-eye{font-size:10px;letter-spacing:3px;color:#4a90d9;text-transform:uppercase;margin-bottom:8px}
.lsec-title{font-size:clamp(24px,4vw,36px);font-weight:700;color:#eef2ff;letter-spacing:-1px;margin-bottom:8px}
.lsec-div{width:32px;height:2px;background:#4a90d9;margin:0 0 26px;transform:scaleX(0);transform-origin:left;transition:transform .6s .2s ease}
.reveal{opacity:0;transform:translateY(32px);transition:opacity .65s ease,transform .65s ease}
.reveal.in{opacity:1;transform:translateY(0)}
.stagger>*{opacity:0;transform:translateY(20px);transition:opacity .5s ease,transform .5s ease}
.stagger.in>*{opacity:1;transform:translateY(0)}
.stagger.in>*:nth-child(1){transition-delay:.05s}.stagger.in>*:nth-child(2){transition-delay:.15s}.stagger.in>*:nth-child(3){transition-delay:.25s}.stagger.in>*:nth-child(4){transition-delay:.35s}.stagger.in>*:nth-child(5){transition-delay:.45s}
.lsec-inner.in .lsec-div{transform:scaleX(1)}
.lsummary{font-size:13.5px;color:#4a6080;line-height:1.82;max-width:640px;margin:0 auto 24px;animation:fadeUp .9s .25s ease both}
.lsummary strong{color:#7a9ab8;font-weight:500}
.l2col{display:grid;grid-template-columns:1fr 1fr;gap:14px;width:100%}
@media(max-width:580px){.l2col{grid-template-columns:1fr}}
.lcard{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:20px}
.lcard-head{font-size:10px;letter-spacing:2px;color:#4a90d9;text-transform:uppercase;margin-bottom:14px}
.lfield{margin-bottom:12px}.lfield:last-child{margin-bottom:0}
.lfield-lbl{font-size:9px;letter-spacing:1px;color:#2e4058;text-transform:uppercase;margin-bottom:3px}
.lfield-val{font-size:12.5px;color:#7a9ab8;line-height:1.6}
.lfield-val strong{color:#c8d8f0;font-weight:500}
.lchips{display:flex;flex-wrap:wrap;gap:5px;margin-top:5px}
.lchip{font-size:10px;color:#4a7096;background:rgba(74,144,217,.07);border:1px solid rgba(74,144,217,.14);border-radius:4px;padding:3px 8px}
.lexp{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:18px 20px;margin-bottom:12px;border-left:3px solid #4a90d9}
.lexp-hd{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;gap:12px}
.lexp-role{font-size:14px;font-weight:600;color:#eef2ff;margin-bottom:3px}
.lexp-org{font-size:11px;margin-bottom:7px}
.lexp-date{font-size:9px;letter-spacing:1px;color:#2e4058;text-transform:uppercase;white-space:nowrap;padding-top:3px}
.lexp-tags{margin-bottom:4px}
.letag{display:inline-block;font-size:9px;letter-spacing:.5px;border-radius:3px;padding:2px 7px;margin-right:4px;margin-bottom:3px;text-transform:uppercase;border:1px solid}
.lexp-ul{list-style:none;padding:0}
.lexp-ul li{font-size:12px;color:#4a6080;line-height:1.72;padding-left:14px;position:relative;margin-bottom:4px}
.lexp-ul li::before{content:'→';position:absolute;left:0;color:#4a90d9;font-size:9px;top:4px}
.lcont-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;width:100%}
.lcont-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:18px;text-align:center;transition:all .2s;text-decoration:none;display:block;color:inherit}
.lcont-card:hover{background:rgba(74,144,217,.06);border-color:rgba(74,144,217,.22);transform:translateY(-2px)}
.lcont-icon{font-size:24px;margin-bottom:9px}
.lcont-lbl{font-size:9px;letter-spacing:2px;color:#2e4058;text-transform:uppercase;margin-bottom:4px}
.lcont-val{font-size:12px;color:#7a9ab8;font-weight:500}
.lexplore-banner{background:rgba(74,144,217,.07);border:1px solid rgba(74,144,217,.18);border-radius:12px;padding:24px;text-align:center;margin-top:18px;width:100%}
#back-btn{position:fixed;top:14px;right:14px;z-index:300;display:none;background:rgba(4,8,15,.9);border:1px solid rgba(74,144,217,.2);border-radius:8px;color:#4a90d9;font-size:10px;font-weight:600;padding:8px 14px;cursor:pointer;letter-spacing:.5px;text-transform:uppercase;font-family:inherit;transition:all .2s}
#back-btn:hover{background:rgba(74,144,217,.1)}
.intro-content{position:relative;z-index:10;display:flex;flex-direction:column;align-items:center;max-width:780px;width:90%;text-align:center;padding:30px 0 20px}
.avail-pill{display:inline-flex;align-items:center;gap:8px;background:rgba(62,207,142,.08);border:1px solid rgba(62,207,142,.25);border-radius:20px;padding:5px 14px;font-size:11px;letter-spacing:1.5px;color:#3ecf8e;text-transform:uppercase;margin-bottom:28px;animation:fadeDown .8s ease both}
.avail-dot{width:7px;height:7px;border-radius:50%;background:#3ecf8e;animation:dotPulse 2s ease infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.85)}}
.intro-name{font-size:clamp(44px,7vw,72px);font-weight:700;color:#eef2ff;letter-spacing:-2px;line-height:1;margin-bottom:12px;animation:fadeUp .9s .1s ease both}
.intro-name .accent{background:linear-gradient(135deg,#4a90d9,#7eb8f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.intro-role{font-size:clamp(14px,2vw,18px);color:#5a7096;letter-spacing:1px;margin-bottom:32px;animation:fadeUp .9s .2s ease both}
.intro-role strong{color:#8aaccc;font-weight:500}
.domain-row{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-bottom:36px;animation:fadeUp .9s .3s ease both}
.domain-tag{font-size:11px;letter-spacing:.8px;text-transform:uppercase;padding:5px 13px;border-radius:6px;border:1px solid rgba(255,255,255,.1);color:#8aaccc;background:rgba(255,255,255,.04);transition:all .2s}
.domain-tag:hover{border-color:rgba(74,144,217,.4);color:#c8d8f0;background:rgba(74,144,217,.08)}
.stats-row{display:flex;gap:0;margin-bottom:40px;border:1px solid rgba(255,255,255,.08);border-radius:12px;overflow:hidden;animation:fadeUp .9s .4s ease both}
.stat-item{flex:1;padding:16px 20px;text-align:center;border-right:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.02)}
.stat-item:last-child{border-right:none}
.stat-num{font-size:22px;font-weight:700;color:#eef2ff;margin-bottom:2px}
.stat-lbl{font-size:10px;letter-spacing:1px;color:#3a4d68;text-transform:uppercase}
.cta-row{display:flex;gap:12px;margin-bottom:28px;animation:fadeUp .9s .5s ease both}
.btn-primary{display:inline-flex;align-items:center;gap:8px;background:#4a90d9;border:none;border-radius:8px;color:#fff;font-size:13px;font-weight:600;padding:13px 28px;cursor:pointer;letter-spacing:.5px;transition:all .2s;text-decoration:none}
.btn-primary:hover{background:#5aa0e9;transform:translateY(-1px)}
.btn-outline{display:inline-flex;align-items:center;gap:8px;background:transparent;border:1px solid rgba(255,255,255,.15);border-radius:8px;color:#8aaccc;font-size:13px;font-weight:500;padding:13px 22px;cursor:pointer;letter-spacing:.5px;transition:all .2s;text-decoration:none}
.btn-outline:hover{border-color:rgba(255,255,255,.35);color:#c8d8f0;transform:translateY(-1px)}
.dist-row{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;animation:fadeUp .9s .6s ease both}
.dist-chip{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;padding:8px 16px;border-radius:8px;border:1px solid;transition:all .22s;cursor:default}
.dist-chip:hover{transform:translateY(-2px);filter:brightness(1.18)}
.dist-pip{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.scroll-hint{margin-top:24px;font-size:10px;letter-spacing:2px;color:#2a3a52;text-transform:uppercase;animation:fadeUp .9s .7s ease both}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeDown{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}
#c{display:block;width:100%;height:100vh}
#hud{position:fixed;top:16px;left:16px;display:none;z-index:50;min-width:192px}
.hud-box{background:rgba(4,8,15,.9);border:1px solid rgba(74,144,217,.14);border-radius:12px;padding:12px 15px;backdrop-filter:blur(16px);margin-bottom:6px}
.hud-lbl{font-size:9px;letter-spacing:2px;color:#253545;text-transform:uppercase;margin-bottom:1px}
.hud-val{font-size:12px;font-weight:600;color:#c8d8f0}.hud-acc{color:#4a90d9}
.hud-sep{height:1px;background:rgba(255,255,255,.05);margin:8px 0}
.hud-bar{height:2px;background:rgba(255,255,255,.06);border-radius:1px;overflow:hidden;margin:4px 0 8px}
.hud-bfill{height:100%;background:#4a90d9;border-radius:1px;transition:width .08s;width:0%}
.hud-proj{font-size:10px;color:#2e4058;min-height:13px}
.hud-proj span{font-weight:600}
.hud-enter{font-size:11px;font-weight:700;color:#f5c842;margin-top:4px;display:none;animation:blink .85s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
.hud-visited{font-size:10px;color:#3ecf8e;margin-top:5px}
#mm-wrap{position:fixed;bottom:16px;right:16px;display:none;z-index:50}
.mm-lbl{font-size:9px;letter-spacing:2px;color:#253545;text-transform:uppercase;text-align:center;margin-bottom:4px}
#mm{border-radius:10px;border:1px solid rgba(74,144,217,.14)}
#hint-box{position:fixed;bottom:16px;left:16px;display:none;background:rgba(4,8,15,.88);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:7px 13px;font-size:10px;color:#2e4058;z-index:50;line-height:2}
#dpad{position:fixed;right:16px;bottom:136px;z-index:50;display:none;grid-template-areas:'. u .' 'l . r' '. d .';grid-template-columns:repeat(3,42px);grid-template-rows:repeat(3,42px);gap:3px}
.dp-btn{background:rgba(4,8,15,.88);border:1px solid rgba(74,144,217,.2);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;color:#4a6a8a;cursor:pointer;user-select:none;-webkit-user-select:none;touch-action:none;transition:all .1s}
.dp-btn:active,.dp-btn.on{background:rgba(74,144,217,.25);border-color:#4a90d9;color:#7eb8f7}
#dp-u{grid-area:u}#dp-d{grid-area:d}#dp-l{grid-area:l}#dp-r{grid-area:r}
#ov{position:fixed;inset:0;background:rgba(0,0,0,.82);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(14px)}
#mo{background:#090f1c;border:1px solid rgba(74,144,217,.18);border-radius:16px;padding:26px;max-width:480px;width:92%;position:relative;max-height:88vh;overflow-y:auto;animation:moin .2s ease}
@keyframes moin{from{transform:translateY(14px);opacity:0}to{transform:translateY(0);opacity:1}}
.mo-close{position:absolute;top:14px;right:14px;width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);color:#5a7096;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}
.mo-close:hover{background:rgba(255,255,255,.1);color:#eef2ff}
.mo-head{display:flex;align-items:flex-start;gap:13px;margin-bottom:14px}
.mo-ico{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0}
.mo-eye{font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}
.mo-name{font-size:16px;font-weight:700;color:#eef2ff;line-height:1.3;margin-bottom:4px}
.mo-stack{font-size:10px;color:#5a7096}
.mo-dist{display:inline-block;font-size:9px;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px}
.mo-desc{font-size:12.5px;color:#7a8faa;line-height:1.78;margin-bottom:14px}
.mo-tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:16px}
.mo-tag{font-size:10px;color:#5a7096;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:3px 9px}
.mo-btns{display:flex;gap:8px;flex-wrap:wrap}
.mo-gh{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:600;text-align:center;text-decoration:none;background:rgba(255,255,255,.05);color:#c8d8f0;border:1px solid rgba(255,255,255,.1);display:block;transition:background .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-gh:hover{background:rgba(255,255,255,.1)}
.mo-live{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:700;text-align:center;text-decoration:none;background:#4a90d9;color:#fff;border:none;display:block;letter-spacing:.5px;text-transform:uppercase;transition:opacity .15s}
.mo-live:hover{opacity:.88}
</style>
</head>
<body>

<div id="intro">
<canvas id="particle-canvas"></canvas>
<nav id="lnav">
  <div class="lnav-logo">Mukund <span>Patel</span></div>
  <div class="lnav-links">
    <button class="lnav-link active" onclick="navTo('s-hero')">Home</button>
    <button class="lnav-link" onclick="navTo('s-about')">About</button>
    <button class="lnav-link" onclick="navTo('s-exp')">Experience</button>
    <button class="lnav-link" onclick="navTo('s-contact')">Contact</button>
  </div>
  <button class="lnav-cta" onclick="startGame()">&#9654; Explore Projects</button>
</nav>

<div id="lscroll">
<section class="lsec" id="s-hero">
  <div class="intro-content">
    <div class="avail-pill"><span class="avail-dot"></span>Open to full-time opportunities</div>
    <div class="intro-name">Mukund <span class="accent">Patel</span></div>
    <div class="intro-role"><strong>Data Scientist</strong> &nbsp;·&nbsp; <strong>AI Engineer</strong> &nbsp;·&nbsp; <strong>Analytics Professional</strong></div>
    <div class="lsummary">MS Data Science graduate from <strong>Montclair State University</strong> (GPA 4.0) with hands-on experience at the <strong>MTA New York</strong> building data pipelines and BI dashboards. I build end-to-end analytics solutions across transportation, finance, healthcare, retail, and logistics.</div>
    <div class="domain-row">
      <span class="domain-tag">AI Agents &amp; LLMs</span>
      <span class="domain-tag">Revenue Management</span>
      <span class="domain-tag">Pricing Analytics</span>
      <span class="domain-tag">Transportation &amp; Logistics</span>
      <span class="domain-tag">Financial Risk</span>
      <span class="domain-tag">Healthcare Analytics</span>
      <span class="domain-tag">BI &amp; Dashboards</span>
      <span class="domain-tag">ML &amp; Forecasting</span>
    </div>
    <div class="stats-row">
      <div class="stat-item"><div class="stat-num">18</div><div class="stat-lbl">Projects</div></div>
      <div class="stat-item"><div class="stat-num">4.0</div><div class="stat-lbl">GPA</div></div>
      <div class="stat-item"><div class="stat-num">6</div><div class="stat-lbl">Live Apps</div></div>
      <div class="stat-item"><div class="stat-num">MTA NY</div><div class="stat-lbl">Experience</div></div>
    </div>
    <div class="cta-row">
      <a class="btn-outline" href="https://www.linkedin.com/in/mukund-patel7" target="_blank">LinkedIn</a>
      <a class="btn-outline" href="https://github.com/Mkp-7" target="_blank">GitHub</a>
      <button class="btn-primary" onclick="startGame()">&#9654; Explore Portfolio</button>
    </div>
    <div class="dist-row">
      <div class="dist-chip" style="color:#7eb8f7;background:rgba(74,144,217,.12);border-color:rgba(74,144,217,.4)"><div class="dist-pip" style="background:#4a90d9"></div>Retail &amp; Commerce</div>
      <div class="dist-chip" style="color:#f08080;background:rgba(232,85,85,.12);border-color:rgba(232,85,85,.4)"><div class="dist-pip" style="background:#e85555"></div>Finance &amp; Banking</div>
      <div class="dist-chip" style="color:#f5c878;background:rgba(245,166,35,.12);border-color:rgba(245,166,35,.4)"><div class="dist-pip" style="background:#f5a623"></div>Operations &amp; Logistics</div>
      <div class="dist-chip" style="color:#6ee8b4;background:rgba(62,207,142,.12);border-color:rgba(62,207,142,.4)"><div class="dist-pip" style="background:#3ecf8e"></div>Healthcare &amp; Life Sci.</div>
      <div class="dist-chip" style="color:#c4a8ff;background:rgba(155,109,255,.12);border-color:rgba(155,109,255,.4)"><div class="dist-pip" style="background:#9b6dff"></div>Research &amp; Education</div>
    </div>
    <div class="scroll-hint">&#8595; &nbsp; scroll to explore &nbsp; &#8595;</div>
  </div>
</section>

<section class="lsec" id="s-about">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">About</div>
    <div class="lsec-title reveal">Who Am I</div>
    <div class="lsec-div"></div>
    <div class="l2col stagger">
      <div class="lcard">
        <div class="lcard-head">Education</div>
        <div class="lfield"><div class="lfield-lbl">Master of Science · Data Science</div><div class="lfield-val"><strong>Montclair State University</strong></div><div class="lfield-val">New Jersey, USA · GPA 4.0 / 4.0</div><div class="lfield-val">Sep 2024 – May 2026</div></div>
        <div class="lfield"><div class="lfield-lbl">Bachelor of Engineering · Information Technology</div><div class="lfield-val"><strong>CVM University, India</strong></div><div class="lfield-val">GPA 3.58 / 4.0 · Jun 2020 – Mar 2024</div></div>
      </div>
      <div class="lcard">
        <div class="lcard-head">Technical Skills</div>
        <div class="lfield"><div class="lfield-lbl">Languages</div><div class="lchips"><span class="lchip">Python</span><span class="lchip">SQL</span><span class="lchip">R</span><span class="lchip">DAX</span></div></div>
        <div class="lfield"><div class="lfield-lbl">BI & Visualization</div><div class="lchips"><span class="lchip">Tableau</span><span class="lchip">Power BI</span><span class="lchip">Looker Studio</span><span class="lchip">ArcGIS</span></div></div>
        <div class="lfield"><div class="lfield-lbl">AI & ML</div><div class="lchips"><span class="lchip">Scikit-learn</span><span class="lchip">TensorFlow</span><span class="lchip">Claude API</span><span class="lchip">Groq</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="lsec" id="s-exp">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">Career</div>
    <div class="lsec-title reveal">Professional Experience</div>
    <div class="lsec-div"></div>
    <div class="stagger">
    <div class="lexp" style="border-left-color:#4a90d9">
      <div class="lexp-hd"><div><div class="lexp-role">Data Analyst Intern</div><div class="lexp-org" style="color:#4a90d9">MTA - Metropolitan Transportation Authority · New York, NY</div></div><div class="lexp-date">Oct 2025 – May 2026</div></div>
      <ul class="lexp-ul"><li>Automated data processing for 8,500+ events using Python and Office Scripts.</li><li>Built computer vision pipeline detecting bus lane violations at 92% accuracy.</li><li>Developed ETL workflow processing driver trip logs at 30-minute intervals.</li></ul>
    </div>
    <div class="lexp" style="border-left-color:#9b6dff">
      <div class="lexp-hd"><div><div class="lexp-role">Graduate Research Assistant</div><div class="lexp-org" style="color:#9b6dff">Montclair State University · New Jersey</div></div><div class="lexp-date">Aug 2025 – May 2026</div></div>
      <ul class="lexp-ul"><li>Standardized 8,000+ student records using SQL for federal compliance reporting.</li><li>Created Tableau dashboards analyzing 5+ years of enrollment and academic outcome data.</li></ul>
    </div>
    </div>
  </div>
</section>

<section class="lsec" id="s-contact">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">Get In Touch</div>
    <div class="lsec-title reveal">Contact</div>
    <div class="lsec-div"></div>
    <div class="lcont-grid stagger">
      <a class="lcont-card" href="mailto:mkpatel4102@gmail.com"><div class="lcont-icon">✉️</div><div class="lcont-lbl">Email</div><div class="lcont-val">mkpatel4102@gmail.com</div></a>
      <a class="lcont-card" href="https://www.linkedin.com/in/mukund-patel7" target="_blank"><div class="lcont-icon">💼</div><div class="lcont-lbl">LinkedIn</div><div class="lcont-val">linkedin.com/in/mukund-patel7</div></a>
      <a class="lcont-card" href="https://github.com/Mkp-7" target="_blank"><div class="lcont-icon">💻</div><div class="lcont-lbl">GitHub</div><div class="lcont-val">github.com/Mkp-7</div></a>
    </div>
    <div class="lexplore-banner reveal">
      <div style="font-size:17px;font-weight:600;color:#eef2ff;margin-bottom:8px">Explore Projects Interactively</div>
      <div style="font-size:13px;color:#4a6080;margin-bottom:16px;line-height:1.7">Drive through a 3D city where each building is a project.</div>
      <button class="btn-primary" onclick="startGame()">&#9654; Enter Portfolio City</button>
    </div>
  </div>
</section>
</div>
</div>

<button id="back-btn" onclick="backToPortfolio()">&#8592; Portfolio</button>
<canvas id="c" style="display:none"></canvas>

<div id="hud">
  <div class="hud-box">
    <div class="hud-lbl">Portfolio</div>
    <div class="hud-val hud-acc">Mukund Patel</div>
    <div class="hud-sep"></div>
    <div class="hud-lbl">Speed</div>
    <div class="hud-bar"><div class="hud-bfill" id="spd-fill"></div></div>
    <div class="hud-proj" id="hud-proj">Navigate to a project entrance</div>
    <div class="hud-enter" id="hud-enter">⏎ Press Enter to open</div>
    <div class="hud-visited" id="hud-visited">0 / 18 explored</div>
  </div>
</div>

<div id="mm-wrap">
  <div class="mm-lbl">City Map</div>
  <canvas id="mm" width="140" height="140"></canvas>
</div>

<div id="hint-box">
  <span style="color:#8aaccc">W A S D</span> / Arrows - Drive &nbsp;·&nbsp; <span style="color:#8aaccc">Enter</span> - Open project
</div>

<div id="dpad">
  <div class="dp-btn" id="dp-u">↑</div>
  <div class="dp-btn" id="dp-l">←</div>
  <div class="dp-btn" id="dp-r">→</div>
  <div class="dp-btn" id="dp-d">↓</div>
</div>

<div id="ov">
  <div id="mo">
    <button class="mo-close" onclick="closeModal()">✕</button>
    <div class="mo-head">
      <div class="mo-ico" id="mo-ico"></div>
      <div>
        <div class="mo-eye" id="mo-cat"></div>
        <div class="mo-name" id="mo-name"></div>
        <div class="mo-stack" id="mo-stack"></div>
        <div class="mo-dist" id="mo-dist"></div>
      </div>
    </div>
    <div class="mo-desc" id="mo-desc"></div>
    <div class="mo-tags" id="mo-tags"></div>
    <div class="mo-btns" id="mo-btns"></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
// ── Particle canvas ──────────────────────────────────────────
(function(){
  const canvas=document.getElementById('particle-canvas');
  const ctx=canvas.getContext('2d');
  let W,H,pts=[];
  function resize(){W=canvas.width=canvas.offsetWidth||innerWidth;H=canvas.height=canvas.offsetHeight||innerHeight;}
  resize();window.addEventListener('resize',resize);
  for(let i=0;i<90;i++)pts.push({x:Math.random()*1600-800,y:Math.random()*900-450,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,r:Math.random()*1.8+.4,a:Math.random()});
  function drawPts(){
    ctx.clearRect(0,0,W,H);const cx=W/2,cy=H/2;
    pts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<-800)p.x=800;if(p.x>800)p.x=-800;if(p.y<-450)p.y=450;if(p.y>450)p.y=-450;ctx.beginPath();ctx.arc(cx+p.x,cy+p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(74,144,217,${p.a*.35})`;ctx.fill();});
    for(let i=0;i<pts.length;i++)for(let j=i+1;j<pts.length;j++){const dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y,d=Math.sqrt(dx*dx+dy*dy);if(d<120){ctx.beginPath();ctx.moveTo(cx+pts[i].x,cy+pts[i].y);ctx.lineTo(cx+pts[j].x,cy+pts[j].y);ctx.strokeStyle=`rgba(74,144,217,${(1-d/120)*.08})`;ctx.lineWidth=.5;ctx.stroke();}}
    requestAnimationFrame(drawPts);
  }
  drawPts();
})();

// ── Districts & Projects ─────────────────────────────────────
const DISTRICTS={
  retail:  {name:"Retail & Commerce",      color:0x4a90d9,hex:"#4a90d9"},
  finance: {name:"Finance & Banking",      color:0xe85555,hex:"#e85555"},
  ops:     {name:"Operations & Logistics", color:0xf5a623,hex:"#f5a623"},
  health:  {name:"Healthcare & Life Sci.", color:0x3ecf8e,hex:"#3ecf8e"},
  research:{name:"Research & Education",   color:0x9b6dff,hex:"#9b6dff"},
};

const PROJECTS=[
  {name:"AI Pricing Intelligence",      icon:"🤖",district:"retail",  cat:"Streamlit Application",   stack:"Python · Claude API",              desc:"Competitive pricing agent using the Claude API to automate real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy.",tags:["Claude API","Price Monitoring","ML"],gh:"https://github.com/Mkp-7/AI-Pricing-Agent",live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"Retail Intelligence Platform", icon:"🛒",district:"retail",  cat:"Streamlit Application",   stack:"Python · Groq LLM · Yelp Dataset", desc:"AI-native customer intelligence platform converting public review data into operational insights. Four modules: Voice of Customer AI, Store Pulse Map, Test & Learn Autopilot, and Analyst Copilot.",tags:["Groq LLM","NLP","A/B Testing"],gh:"https://github.com/Mkp-7/retail-intelligence-platform",live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Retail Customer Analytics",    icon:"🛍️",district:"retail",  cat:"ML & Python",             stack:"Python · Scikit-learn · K-Means",  desc:"Analyzed 25,000+ product records and 10,000+ customer transactions. K-Means clustering identified top 20% of customers contributing 60% of revenue.",tags:["K-Means","Customer Segmentation","RFM"],gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",live:""},
  {name:"E-Commerce Funnel Analytics",  icon:"📈",district:"retail",  cat:"Looker · dbt · BigQuery", stack:"dbt · BigQuery · GA4 · Looker",   desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling and behavioral segmentation across 269K users. Identified 9,630 cart abandonment targets projecting $25K incremental revenue.",tags:["dbt","BigQuery","GA4","Looker Studio"],gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",live:"https://datastudio.google.com/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989"},
  {name:"Sales & Demand Forecasting",   icon:"📊",district:"retail",  cat:"Tableau Dashboard",       stack:"Python · ARIMA · SARIMA · Tableau",desc:"Fine-tuned ARIMA and SARIMA models forecasting 6-month revenue for 25,432 products across 12 regions at 94% accuracy.",tags:["ARIMA","SARIMA","94% Accuracy","Tableau"],gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  {name:"Banking Risk Intelligence",    icon:"🏦",district:"finance", cat:"Streamlit Application",   stack:"Python · FDIC API · FRED",         desc:"Operational risk monitoring platform querying FDIC data for 4,500+ banks. Applies Random Forest (AUC=0.84) and Gradient Boosting for bank failure prediction.",tags:["Basel III","FDIC API","Random Forest AUC=0.84"],gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Banking Client Analysis",      icon:"💳",district:"finance", cat:"Power BI Dashboard",      stack:"Power BI · SQL · Python",           desc:"Structured 3,000 banking client records integrating portfolio, relationship, and product-level dimensions for risk assessment.",tags:["Power BI","Client Segmentation","Portfolio Analytics"],gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",live:""},
  {name:"Insurance Claims Prediction",  icon:"🛡️",district:"finance", cat:"Power BI + ML",           stack:"R · SQL Server · Power BI",        desc:"Processed 58,000+ insurance policy records. Random Forest and Logistic Regression achieving 94% accuracy for 6-month claim likelihood prediction.",tags:["Random Forest","94% Accuracy","SQL Server","R"],gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",live:""},
  {name:"Revenue Intelligence Agent",   icon:"🚗",district:"ops",    cat:"Streamlit Application",   stack:"Python · Groq LLM · GitHub Actions",desc:"Autonomous multi-agent pipeline monitoring competitor car-rental pricing across 8 competitors and 10 US airports. Reduces analyst workflow from 3 hours to 15 minutes.",tags:["AI Agents","Groq LLM","Streamlit","SQLite"],gh:"https://github.com/Mkp-7/Revenue-Management-Agent",live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"EcoRoute Optimizer",           icon:"🌿",district:"ops",    cat:"Streamlit Application",   stack:"Python · Gemini AI · OR-Tools",    desc:"Logistics optimization platform generating carbon-minimized shipping routes across 60+ US cities. Evaluates diesel, EV, and rail freight via EPA SmartWay carbon methodology.",tags:["Gemini AI","OR-Tools","Carbon Optimization"],gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Supply Chain Analytics",       icon:"📦",district:"ops",    cat:"Power BI Dashboard",      stack:"Power BI · Power Query · DAX",     desc:"Integrated 10 raw Excel supply chain datasets via Power Query ETL and built a star schema data model with 12+ DAX KPI measures.",tags:["Power BI","DAX","Star Schema","ETL"],gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",live:""},
  {name:"Workforce Utilization",        icon:"👥",district:"ops",    cat:"Power BI Dashboard",      stack:"Power BI · DAX · HR Analytics",   desc:"Dashboard analyzing attendance for 80 employees over 3 months, tracking presence, WFH utilization, and leave patterns.",tags:["Power BI","HR Analytics","WFH Utilization"],gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",live:""},
  {name:"Medmedia Analytics Hub",       icon:"🏥",district:"health", cat:"Streamlit Application",   stack:"Python · LLMs · ClinicalTrials.gov",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases analyzing 470,000+ active clinical trials.",tags:["Healthcare NLP","ClinicalTrials.gov","PubMed"],gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Diabetes Risk Prediction",     icon:"🩺",district:"health", cat:"ML & Python",             stack:"Python · SVM · Scikit-learn",      desc:"Multi-model diabetes prediction system trained on 769 patients. Achieved 80% accuracy with SVM across Logistic Regression, Decision Tree, Random Forest, and SVM.",tags:["SVM","Random Forest","Healthcare ML"],gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",live:""},
  {name:"COVID-19 Global Impact",       icon:"🦠",district:"research",cat:"Exploratory Data Analysis",stack:"Python · EDA · WHO Data",         desc:"Global COVID-19 analysis using WHO data (~450,000 records) covering mortality comparisons, global daily trajectories, and regional disparities.",tags:["EDA","WHO Data","Epidemiology"],gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",live:""},
  {name:"MSU Collaboratory",            icon:"🎓",district:"research",cat:"Tableau Dashboard",       stack:"Tableau · 3D Network Graph",       desc:"3D network visualization of interdisciplinary activities and partnerships at Montclair State University across community partner organizations.",tags:["Tableau","3D Network Graph","MSU"],gh:"https://mkp-7.github.io/Network-Graph/",live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"Student Wellbeing Study",      icon:"📋",district:"research",cat:"Tableau Dashboard",       stack:"Python · Statistics · Tableau",   desc:"Longitudinal study tracking 70 MSU students over 21 days. Conducted hypothesis testing (t-tests, ANOVA, regression) identifying happiness patterns.",tags:["Hypothesis Testing","ANOVA","Tableau"],gh:"",live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1"},
  {name:"Book Recommendation Engine",   icon:"📚",district:"research",cat:"ML & Python",             stack:"Python · TF-IDF · SVD",           desc:"Recommendation engine trained on 10,000 books and 1M+ ratings. Employs TF-IDF with Cosine Similarity and SVD for personalized recommendations.",tags:["TF-IDF","SVD","Collaborative Filtering"],gh:"https://github.com/Mkp-7/Book_Recommendation",live:""},
];

const DIST_ORDER=['research','health','ops','finance','retail'];
const ROW_COLS={retail:5,finance:3,ops:4,health:2,research:4};

// ── Layout constants ─────────────────────────────────────────
// BW = building slot width, RW = road width (wider now), STEP = BW+RW
const BW=16, RW=22, STEP=BW+RW; // road is 22 units wide (was 18)
// Building heights vary per index
const BHEIGHTS=[9,14,10,16,8,12,11,15,9,13,10,14,8,11,13,9,16,10];
// Building widths vary per index (within slot, max ~BW*0.78)
const BWIDTHS=[12,10,13,11,12,9,11,13,10,12,11,10,13,11,9,12,10,13];

function bColX(c){ return -72+c*STEP; }
function bRowZ(r){ return -72+r*STEP; }

// ── Scene state ───────────────────────────────────────────────
let scene,camera,renderer,clock;
let carGroup,carWheels=[];
let buildings=[];
let nearEntry=null,modalOpen=false;
let keys={},dpadState={up:0,down:0,left:0,right:0};
let carPos=new THREE.Vector3(0,0,100);
let carAngle=Math.PI,carSpeed=0;
let frame=0;
let mmCanvas,mmCtx;
let visitedSet=new Set();
let audioCtx=null,engineOsc=null,engineGain=null;
let lastNearEntry=null;
let camPos=new THREE.Vector3(0,8,112);
let isDrag=false,lastMX=0,lastMY=0,camTheta=0,camPhi=0.38,camOrbit=false;
const CAM_BACK=11,CAM_UP=5.5,CAM_LAG=0.09,CAM_R=13;

function projPos(p){
  const row=DIST_ORDER.indexOf(p.district);
  const distProjs=PROJECTS.filter(x=>x.district===p.district);
  const col=distProjs.indexOf(p);
  const cols=ROW_COLS[p.district];
  const startCol=Math.floor((5-cols)/2);
  return{x:bColX(startCol+col),z:bRowZ(row)};
}

// ── Nav scroll ────────────────────────────────────────────────
function navTo(id){const el=document.getElementById(id),sc=document.getElementById('lscroll');if(!el||!sc)return;sc.scrollTo({top:el.offsetTop,behavior:'smooth'});}
document.addEventListener('DOMContentLoaded',()=>{
  const sc=document.getElementById('lscroll');if(!sc)return;
  const secs=['s-hero','s-about','s-exp','s-contact'];
  const links=document.querySelectorAll('.lnav-link');
  sc.addEventListener('scroll',()=>{
    const st=sc.scrollTop+80;
    secs.forEach((id,i)=>{const el=document.getElementById(id);if(!el)return;if(el.offsetTop<=st&&el.offsetTop+el.offsetHeight>st){links.forEach(l=>l.classList.remove('active'));if(links[i])links[i].classList.add('active');}});
  });
  const obs=new IntersectionObserver((entries)=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');const inner=e.target.closest('.lsec-inner');if(inner)inner.classList.add('in');}});},{root:sc,threshold:0.15});
  sc.querySelectorAll('.reveal,.stagger').forEach(el=>obs.observe(el));
});

// ── Start / back ──────────────────────────────────────────────
function startGame(){
  document.getElementById('intro').style.display='none';
  document.getElementById('c').style.display='block';
  document.getElementById('back-btn').style.display='block';
  ['hud','mm-wrap','hint-box'].forEach(id=>document.getElementById(id).style.display='block');
  document.getElementById('dpad').style.display='grid';
  mmCanvas=document.getElementById('mm');mmCanvas.width=140;mmCanvas.height=140;mmCtx=mmCanvas.getContext('2d');
  init3D();buildCity();buildCar();bindInput();initAudio();clock=new THREE.Clock();loop();
  showToast('Drive into a glowing zone · Press Enter to open a project');
}
function backToPortfolio(){
  document.getElementById('intro').style.display='flex';
  document.getElementById('c').style.display='none';
  document.getElementById('back-btn').style.display='none';
  ['hud','mm-wrap','hint-box'].forEach(id=>document.getElementById(id).style.display='none');
  document.getElementById('dpad').style.display='none';
}

// ── Three.js init ─────────────────────────────────────────────
function init3D(){
  scene=new THREE.Scene();scene.background=new THREE.Color(0x04080f);scene.fog=new THREE.FogExp2(0x04080f,0.007);
  camera=new THREE.PerspectiveCamera(55,innerWidth/innerHeight,0.1,400);camera.position.copy(camPos);
  renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true,powerPreference:'high-performance'});
  renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.1;
  window.addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);});
  scene.add(new THREE.AmbientLight(0x8899bb,0.5));
  const sun=new THREE.DirectionalLight(0xeef2ff,1.8);sun.position.set(60,100,40);sun.castShadow=true;sun.shadow.mapSize.set(4096,4096);sun.shadow.camera.near=1;sun.shadow.camera.far=400;sun.shadow.camera.left=sun.shadow.camera.bottom=-220;sun.shadow.camera.right=sun.shadow.camera.top=220;sun.shadow.bias=-0.0004;scene.add(sun);
  scene.add(new THREE.DirectionalLight(0x2233aa,0.3));
}

// ── City ──────────────────────────────────────────────────────
function buildCity(){
  const ground=new THREE.Mesh(new THREE.PlaneGeometry(500,500),new THREE.MeshLambertMaterial({color:0x060a10}));
  ground.rotation.x=-Math.PI/2;ground.receiveShadow=true;scene.add(ground);
  scene.add(new THREE.GridHelper(480,130,0x0d1420,0x090f18));
  makeRoads();makeDistrictZones();placeBuildings();makeDistrictSigns();
}

function makeRoads(){
  const rM=new THREE.MeshLambertMaterial({color:0x0a0e18});
  const lM=new THREE.MeshLambertMaterial({color:0x1e2e48,emissive:0x102030,emissiveIntensity:0.4});
  const sM=new THREE.MeshLambertMaterial({color:0x111c2c});
  const len=220;
  // 6 horizontal road strips at rRowZ positions (between building rows)
  // Road centres: halfway between building row Z values
  // Building rows at bRowZ(0..4): -72,-34,4,42,80 (approx with STEP=38)
  // Road strips between them: -72-STEP/2, -72+STEP/2... etc
  // Actually roads run between building cols/rows - let's define road centres
  // Horizontal roads (parallel to X axis): 6 rows
  const hRoadZ=[-90,-52,-14,24,62,100]; // between & outside building rows
  hRoadZ.forEach(rz=>{
    const road=new THREE.Mesh(new THREE.PlaneGeometry(len,RW),rM);
    road.rotation.x=-Math.PI/2;road.position.set(0,0.05,rz);road.receiveShadow=true;scene.add(road);
    [-RW/2+0.4,RW/2-0.4].forEach(oz=>{const k=new THREE.Mesh(new THREE.BoxGeometry(len,0.16,0.35),sM);k.position.set(0,0.08,rz+oz);scene.add(k);});
    for(let x=-len/2+4;x<len/2;x+=9){const d=new THREE.Mesh(new THREE.PlaneGeometry(4.5,0.24),lM);d.rotation.x=-Math.PI/2;d.position.set(x,0.07,rz);scene.add(d);}
  });
  // Vertical roads (parallel to Z axis): 6 columns
  const vRoadX=[-101,-63,-25,13,51,89];
  vRoadX.forEach(rx=>{
    const road=new THREE.Mesh(new THREE.PlaneGeometry(RW,len),rM);
    road.rotation.x=-Math.PI/2;road.position.set(rx,0.05,0);road.receiveShadow=true;scene.add(road);
    [-RW/2+0.4,RW/2-0.4].forEach(ox=>{const k=new THREE.Mesh(new THREE.BoxGeometry(0.35,0.16,len),sM);k.position.set(rx+ox,0.08,0);scene.add(k);});
    for(let z=-len/2+4;z<len/2;z+=9){const d=new THREE.Mesh(new THREE.PlaneGeometry(0.24,4.5),lM);d.rotation.x=-Math.PI/2;d.position.set(rx,0.07,z);scene.add(d);}
  });
}

function makeDistrictZones(){
  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];const cols=ROW_COLS[dk];const startCol=Math.floor((5-cols)/2);
    const leftX=bColX(startCol)-BW/2,rightX=bColX(startCol+cols-1)+BW/2;
    const cx=(leftX+rightX)/2,w=rightX-leftX;
    const zone=new THREE.Mesh(new THREE.PlaneGeometry(w,BW*0.9),new THREE.MeshLambertMaterial({color:dist.color,transparent:true,opacity:0.04}));
    zone.rotation.x=-Math.PI/2;zone.position.set(cx,0.055,bRowZ(row));scene.add(zone);
  });
}

// ── District signs - NO POLES - bar connects directly between outermost buildings ──
function makeDistrictSigns(){
  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[dk];
    const startCol=Math.floor((5-cols)/2);
    const rowZ=bRowZ(row);

    // Find max height of buildings in this district
    const distIdxs=PROJECTS.map((p,i)=>p.district===dk?i:-1).filter(i=>i>=0);
    const maxH=Math.max(...distIdxs.map(i=>BHEIGHTS[i%18]));
    const barY=maxH+1.8; // float just above tallest building

    // Bar spans from left building face to right building face
    const leftBW=BWIDTHS[distIdxs[0]%18];
    const rightBW=BWIDTHS[distIdxs[distIdxs.length-1]%18];
    const leftBX=bColX(startCol);
    const rightBX=bColX(startCol+cols-1);
    // Bar endpoints: inner face of outermost buildings (Z faces toward viewer)
    // Bar runs along X between building centres; length covers from left-building-left-edge to right-building-right-edge
    const barW=(rightBX+rightBW/2)-(leftBX-leftBW/2);
    const cx=(leftBX+rightBX)/2;

    // Main glowing beam - thin horizontal bar
    const beam=new THREE.Mesh(
      new THREE.BoxGeometry(barW,0.22,0.22),
      new THREE.MeshLambertMaterial({color:dist.color,emissive:dist.color,emissiveIntensity:0.7})
    );
    beam.position.set(cx,barY,rowZ);scene.add(beam);

    // Small bracket caps at ends where bar meets building wall
    [leftBX-leftBW/2-0.05, rightBX+rightBW/2+0.05].forEach((ex,ei)=>{
      // Vertical bracket tab pressed against building side
      const tab=new THREE.Mesh(
        new THREE.BoxGeometry(0.18,1.2,0.22),
        new THREE.MeshLambertMaterial({color:dist.color,emissive:dist.color,emissiveIntensity:0.65})
      );
      tab.position.set(ex+(ei===0?0.09:-0.09),barY,rowZ);scene.add(tab);
      // Horizontal stub connecting tab to bar
      const stub=new THREE.Mesh(
        new THREE.BoxGeometry(0.28,0.22,0.22),
        new THREE.MeshLambertMaterial({color:dist.color,emissive:dist.color,emissiveIntensity:0.65})
      );
      stub.position.set(ei===0?leftBX-leftBW/2+0.14:rightBX+rightBW/2-0.14,barY,rowZ);scene.add(stub);
    });

    // Label panels on front (+Z) and back (-Z) of bar - centered on bar
    function makeLabelTex(){
      const cw=1024,ch=80;
      const can=document.createElement('canvas');can.width=cw;can.height=ch;
      const ctx=can.getContext('2d');
      ctx.fillStyle='rgba(4,10,22,0.92)';ctx.fillRect(0,0,cw,ch);
      ctx.fillStyle=dist.hex;ctx.fillRect(0,0,cw,6);ctx.fillRect(0,ch-6,cw,6);
      ctx.font='bold 40px Segoe UI,Arial';ctx.fillStyle=dist.hex;
      ctx.textAlign='center';ctx.textBaseline='middle';
      ctx.fillText(dist.name.toUpperCase(),cw/2,ch/2);
      const tex=new THREE.CanvasTexture(can);
      tex.anisotropy=renderer.capabilities.getMaxAnisotropy();
      return tex;
    }
    const labelW=Math.min(barW,cols*BW*0.9);
    const labelH=0.85;
    const matF=new THREE.MeshBasicMaterial({map:makeLabelTex(),transparent:true,depthWrite:false});
    const matB=new THREE.MeshBasicMaterial({map:makeLabelTex(),transparent:true,depthWrite:false});
    const front=new THREE.Mesh(new THREE.PlaneGeometry(labelW,labelH),matF);
    front.position.set(cx,barY,rowZ-0.12);scene.add(front);
    const back=new THREE.Mesh(new THREE.PlaneGeometry(labelW,labelH),matB);
    back.position.set(cx,barY,rowZ+0.12);back.rotation.y=Math.PI;scene.add(back);

    // Subtle glow light
    const pl=new THREE.PointLight(dist.color,0.5,barW+10);
    pl.position.set(cx,barY+1,rowZ);scene.add(pl);
  });
}

function placeBuildings(){
  PROJECTS.forEach((p,i)=>{const{x,z}=projPos(p);buildings.push(makeBuilding(p,x,z,i));});
}

// ── Building - variable width & height ────────────────────────
function makeBuilding(p,bx,bz,idx){
  const dist=DISTRICTS[p.district];
  const hc=dist.color;
  const bH=BHEIGHTS[idx%18];
  const bW=BWIDTHS[idx%18];      // variable width
  const bD=BWIDTHS[(idx+3)%18];  // variable depth (offset for variety)

  const g=new THREE.Group();g.position.set(bx,0,bz);

  const pave=new THREE.Mesh(new THREE.BoxGeometry(bW+2.4,0.18,bD+2.4),new THREE.MeshLambertMaterial({color:0x0e1826}));
  pave.position.y=0.09;pave.receiveShadow=true;g.add(pave);

  const body=new THREE.Mesh(new THREE.BoxGeometry(bW,bH,bD),new THREE.MeshLambertMaterial({color:0x111824}));
  body.position.y=bH/2+0.18;body.castShadow=true;body.receiveShadow=true;g.add(body);

  const cap=new THREE.Mesh(new THREE.BoxGeometry(bW+0.2,0.6,bD+0.2),new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.45}));
  cap.position.y=bH+0.48;g.add(cap);

  const base=new THREE.Mesh(new THREE.BoxGeometry(bW+0.25,0.24,bD+0.25),new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.18}));
  base.position.y=0.30;g.add(base);

  const rL=new THREE.PointLight(hc,0.7,30);rL.position.set(0,bH+2.5,0);g.add(rL);

  makePoster(g,p,dist,bW,bH,bD);

  const eHalfW=bW/2+3.2,eHalfD=bD/2+3.2;
  const eMat=new THREE.MeshBasicMaterial({color:hc,transparent:true,opacity:0.10,depthWrite:false});
  const ePlane=new THREE.Mesh(new THREE.PlaneGeometry(eHalfW*2,eHalfD*2),eMat);
  ePlane.rotation.x=-Math.PI/2;ePlane.position.y=0.13;g.add(ePlane);

  const dotM=new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.65});
  [[eHalfW,eHalfD],[-eHalfW,eHalfD],[eHalfW,-eHalfD],[-eHalfW,-eHalfD]].forEach(([dx,dz])=>{
    const dot=new THREE.Mesh(new THREE.CylinderGeometry(0.18,0.18,0.5,8),dotM.clone());dot.position.set(dx,0.25,dz);g.add(dot);
  });

  const eLight=new THREE.PointLight(hc,0,14);eLight.position.set(0,0.5,0);g.add(eLight);

  const bbox=new THREE.Box2(new THREE.Vector2(bx-bW/2-0.1,bz-bD/2-0.1),new THREE.Vector2(bx+bW/2+0.1,bz+bD/2+0.1));
  const entranceWorld=new THREE.Vector3(bx,0,bz);

  const pg=makeParticles(p.district,hc,bH);g.add(pg);
  scene.add(g);
  return{group:g,bbox,entranceWorld,project:p,eMat,eLight,visited:false,distHex:dist.hex,particleGroup:pg,bW,bH};
}

function makePoster(g,p,dist,bW,bH,bD){
  const PX=96;const cw=Math.round(bW*PX),ch=Math.round(bH*PX);
  function buildCanvas(){
    const can=document.createElement('canvas');can.width=cw;can.height=ch;const ctx=can.getContext('2d');
    ctx.fillStyle='#111824';ctx.fillRect(0,0,cw,ch);
    ctx.fillStyle=dist.hex;ctx.fillRect(0,0,cw,ch*0.04);
    ctx.textAlign='center';ctx.textBaseline='top';
    const pad=cw*0.08,maxW=cw-pad*2;
    function wrap(text,font,mW){ctx.font=font;const words=text.split(' ');const lines=[];let line='';words.forEach(w=>{const t=line?line+' '+w:w;if(ctx.measureText(t).width>mW&&line){lines.push(line);line=w;}else line=t;});if(line)lines.push(line);return lines;}
    let y=ch*0.14;const nameSz=cw*0.085;const nameFont=`900 ${nameSz}px Segoe UI,Arial`;
    const nameLines=wrap(p.name,nameFont,maxW);ctx.font=nameFont;ctx.fillStyle='#f0f4ff';
    const nameLineH=nameSz*1.28;nameLines.forEach((line,i)=>{ctx.fillText(line,cw/2,y+i*nameLineH);});y+=nameLines.length*nameLineH+nameSz*0.45;
    ctx.fillStyle=dist.hex;ctx.globalAlpha=0.4;ctx.fillRect(pad,y,maxW,2);ctx.globalAlpha=1;y+=nameSz*0.55;
    const catSz=nameSz*0.62;const catLines=wrap(p.cat,`700 ${catSz}px Segoe UI,Arial`,maxW);ctx.font=`700 ${catSz}px Segoe UI,Arial`;ctx.fillStyle=dist.hex;const catLineH=catSz*1.3;catLines.forEach((line,i)=>{ctx.fillText(line,cw/2,y+i*catLineH);});
    const tex=new THREE.CanvasTexture(can);tex.anisotropy=renderer.capabilities.getMaxAnisotropy();return tex;
  }
  const eps=0.05;
  const front=new THREE.Mesh(new THREE.PlaneGeometry(bW,bH),new THREE.MeshBasicMaterial({map:buildCanvas(),transparent:true,depthWrite:false}));
  front.position.set(0,bH/2+0.18,bD/2+eps);g.add(front);
  const back=new THREE.Mesh(new THREE.PlaneGeometry(bW,bH),new THREE.MeshBasicMaterial({map:buildCanvas(),transparent:true,depthWrite:false}));
  back.position.set(0,bH/2+0.18,-bD/2-eps);back.rotation.y=Math.PI;g.add(back);
}

function makeParticles(dk,color,bH){
  const gr=new THREE.Group();
  for(let i=0;i<14;i++){
    let geo;
    if(dk==='retail')geo=new THREE.BoxGeometry(0.16,0.16,0.16);
    else if(dk==='finance')geo=new THREE.ConeGeometry(0.11,0.24,4);
    else if(dk==='ops')geo=new THREE.CylinderGeometry(0.055,0.055,0.26,6);
    else if(dk==='health')geo=new THREE.SphereGeometry(0.11,8,8);
    else geo=new THREE.TetrahedronGeometry(0.12);
    const m=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color,transparent:true,opacity:0}));
    const angle=Math.random()*Math.PI*2,radius=2+Math.random()*3;
    m.position.set(Math.cos(angle)*radius,1.2+Math.random()*bH*.8,Math.sin(angle)*radius);
    m.userData={ba:angle,r:radius,sp:.003+Math.random()*.004,ys:.006+Math.random()*.007,yb:m.position.y,ya:.6+Math.random()*1.1,ph:Math.random()*Math.PI*2};
    gr.add(m);
  }
  return gr;
}

// ── Car ───────────────────────────────────────────────────────
function buildCar(){
  carGroup=new THREE.Group();
  const bM=new THREE.MeshLambertMaterial({color:0x1a3060});
  const dM=new THREE.MeshLambertMaterial({color:0x080c14});
  const cM=new THREE.MeshLambertMaterial({color:0xaab4c0,emissive:0x606870,emissiveIntensity:0.2});
  const gM=new THREE.MeshLambertMaterial({color:0x4477aa,transparent:true,opacity:0.55,emissive:0x223366,emissiveIntensity:0.05});
  const hM=new THREE.MeshLambertMaterial({color:0xfffff0,emissive:0xfffff0,emissiveIntensity:2.2});
  const tM=new THREE.MeshLambertMaterial({color:0xff2000,emissive:0xff2000,emissiveIntensity:1.8});
  const rM=new THREE.MeshLambertMaterial({color:0xc0c8d4,emissive:0x808898,emissiveIntensity:0.2});
  const yM=new THREE.MeshLambertMaterial({color:0x111111});
  const lo=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.52,4.8),bM);lo.position.y=0.56;lo.castShadow=true;carGroup.add(lo);
  for(const sx of[-1.21,1.21]){const sk=new THREE.Mesh(new THREE.BoxGeometry(0.09,0.26,4.5),dM);sk.position.set(sx,0.43,0);carGroup.add(sk);}
  const cab=new THREE.Mesh(new THREE.BoxGeometry(2.05,0.68,2.6),bM);cab.position.set(0,1.28,-0.15);cab.castShadow=true;carGroup.add(cab);
  const roof=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.1,2.4),dM);roof.position.set(0,1.68,-0.15);carGroup.add(roof);
  const wf=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.6,0.09),gM);wf.position.set(0,1.3,1.12);wf.rotation.x=-0.28;carGroup.add(wf);
  const wr=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.55,0.09),gM);wr.position.set(0,1.27,-1.48);wr.rotation.x=0.26;carGroup.add(wr);
  for(const sx of[-1.04,1.04]){const ws=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.48,1.85),gM);ws.position.set(sx,1.32,-0.15);carGroup.add(ws);}
  const hood=new THREE.Mesh(new THREE.BoxGeometry(2.3,0.09,1.55),bM);hood.position.set(0,0.9,1.88);hood.rotation.x=0.05;carGroup.add(hood);
  const trunk=new THREE.Mesh(new THREE.BoxGeometry(2.1,0.09,0.9),bM);trunk.position.set(0,0.9,-2.1);trunk.rotation.x=-0.04;carGroup.add(trunk);
  const bf=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.28,0.18),cM);bf.position.set(0,0.46,2.43);carGroup.add(bf);
  const br=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.28,0.18),cM);br.position.set(0,0.46,-2.43);carGroup.add(br);
  for(const hx of[-0.74,0.74]){
    const hl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),hM);hl.position.set(hx,0.74,2.45);carGroup.add(hl);
    const beam=new THREE.SpotLight(0xffffff,0.9,28,Math.PI*0.1,0.5);beam.position.set(hx,0.74,2.5);beam.target.position.set(hx*1.1,-2,15);carGroup.add(beam);carGroup.add(beam.target);
  }
  for(const tx of[-0.74,0.74]){const tl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),tM);tl.position.set(tx,0.74,-2.45);carGroup.add(tl);}
  for(const sx of[-1.23,1.23]){const mir=new THREE.Mesh(new THREE.BoxGeometry(0.08,0.13,0.32),cM);mir.position.set(sx,1.1,0.65);carGroup.add(mir);}
  [[-1.14,0.42,1.52],[1.14,0.42,1.52],[-1.14,0.42,-1.52],[1.14,0.42,-1.52]].forEach(([wx,wy,wz])=>{
    const wg=new THREE.Group();wg.position.set(wx,wy,wz);wg.userData.isWheel=true;
    const spin=new THREE.Group();wg.add(spin);wg.userData.spin=spin;
    const tyre=new THREE.Mesh(new THREE.CylinderGeometry(0.42,0.42,0.26,20),yM);tyre.rotation.z=Math.PI/2;tyre.castShadow=true;spin.add(tyre);
    const rim=new THREE.Mesh(new THREE.CylinderGeometry(0.27,0.27,0.27,10),rM);rim.rotation.z=Math.PI/2;spin.add(rim);
    for(let s=0;s<5;s++){const spk=new THREE.Mesh(new THREE.BoxGeometry(0.05,0.52,0.05),rM);spk.rotation.z=Math.PI/2;spk.rotation.x=(s/5)*Math.PI*2;spk.position.y=Math.sin((s/5)*Math.PI*2)*0.14;spk.position.z=Math.cos((s/5)*Math.PI*2)*0.14;spin.add(spk);}
    carGroup.add(wg);carWheels.push(wg);
  });
  carGroup.position.copy(carPos);scene.add(carGroup);
}

// ── Audio ─────────────────────────────────────────────────────
function initAudio(){
  try{audioCtx=new(window.AudioContext||window.webkitAudioContext)();engineGain=audioCtx.createGain();engineGain.gain.value=0;engineGain.connect(audioCtx.destination);engineOsc=audioCtx.createOscillator();engineOsc.type='sawtooth';engineOsc.frequency.value=55;const f=audioCtx.createBiquadFilter();f.type='lowpass';f.frequency.value=200;engineOsc.connect(f);f.connect(engineGain);engineOsc.start();}catch(e){}
}
function playChime(){if(!audioCtx)return;try{[880,1100].forEach((freq,i)=>setTimeout(()=>{const o=audioCtx.createOscillator(),g=audioCtx.createGain();o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';g.gain.setValueAtTime(0.15,audioCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.5);o.start();o.stop(audioCtx.currentTime+0.5);},i*110));}catch(e){}}
function playOpen(){if(!audioCtx)return;try{[440,554,660].forEach((freq,i)=>setTimeout(()=>{const o=audioCtx.createOscillator(),g=audioCtx.createGain();o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';g.gain.setValueAtTime(0.09,audioCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.28);o.start();o.stop(audioCtx.currentTime+0.28);},i*75));}catch(e){}}

// ── Main loop ─────────────────────────────────────────────────
const ACCEL=0.038,FRIC=0.88,MAX_SPD=0.36,BOOST_SPD=1.1,BOOST_ACCEL=0.12;

function loop(){
  requestAnimationFrame(loop);frame++;clock.getDelta();
  if(!modalOpen){
    const U=keys['ArrowUp']  ||keys['w']||keys['W']||dpadState.up;
    const D=keys['ArrowDown'] ||keys['s']||keys['S']||dpadState.down;
    const L=keys['ArrowLeft'] ||keys['a']||keys['A']||dpadState.left;
    const R=keys['ArrowRight']||keys['d']||keys['D']||dpadState.right;
    const boost=keys['Shift']||keys['Control'];
    const mspd=boost?BOOST_SPD:MAX_SPD,macc=boost?BOOST_ACCEL:ACCEL;
    if(U)carSpeed=Math.min(carSpeed+macc,mspd);else if(D)carSpeed=Math.max(carSpeed-macc,-mspd*.5);else carSpeed*=FRIC;
    if(Math.abs(carSpeed)>.004){const dir=carSpeed>0?1:-1;if(L)carAngle+=0.034*dir;if(R)carAngle-=0.034*dir;}
    const nx=carPos.x+Math.sin(carAngle)*carSpeed,nz=carPos.z+Math.cos(carAngle)*carSpeed;
    let blocked=false;const pt=new THREE.Vector2(nx,nz);
    for(const b of buildings){if(b.bbox.containsPoint(pt)){blocked=true;break;}}
    if(Math.abs(nx)>115||Math.abs(nz)>115)blocked=true;
    if(!blocked){carPos.x=nx;carPos.z=nz;}else{carSpeed*=-.25;}
    carGroup.position.x=carPos.x;carGroup.position.z=carPos.z;carGroup.rotation.y=carAngle;
    carWheels.forEach(wg=>{if(wg.userData.spin)wg.userData.spin.rotation.x+=carSpeed*2.5;});
    if(engineOsc&&audioCtx){engineOsc.frequency.value=55+Math.abs(carSpeed)/mspd*80;engineGain.gain.value=Math.abs(carSpeed)>.01?.04:0;}
  }
  if(camOrbit){
    const r=CAM_R+8;
    camera.position.set(carPos.x+r*Math.sin(camPhi)*Math.sin(camTheta+carAngle),carPos.y+r*Math.cos(camPhi),carPos.z+r*Math.sin(camPhi)*Math.cos(camTheta+carAngle));
    camera.lookAt(carPos.x,1.5,carPos.z);
  }else{
    const behind=new THREE.Vector3(carPos.x-Math.sin(carAngle)*CAM_BACK,CAM_UP,carPos.z-Math.cos(carAngle)*CAM_BACK);
    camPos.lerp(behind,CAM_LAG);camera.position.copy(camPos);
    camera.lookAt(carPos.x+Math.sin(carAngle)*4,1.2,carPos.z+Math.cos(carAngle)*4);
  }
  nearEntry=null;let bestD=9999;
  buildings.forEach(b=>{
    const dx=carPos.x-b.entranceWorld.x,dz=carPos.z-b.entranceWorld.z,d=Math.sqrt(dx*dx+dz*dz);
    const inZone=d<7.5;const pulse=Math.abs(Math.sin(frame*.07));
    if(inZone){b.eMat.opacity=.48+pulse*.32;b.eLight.intensity=2.0+pulse*1.2;if(d<bestD){nearEntry=b;bestD=d;}}
    else if(d<13){const t=1-(d-7.5)/5.5;b.eMat.opacity=.10+t*.12;b.eLight.intensity=t*.4;}
    else{b.eMat.opacity=.06;b.eLight.intensity=0;}
  });
  if(nearEntry&&nearEntry!==lastNearEntry)playChime();
  lastNearEntry=nearEntry;
  buildings.forEach(b=>{
    const isN=nearEntry===b;if(!b.particleGroup)return;
    b.particleGroup.children.forEach(mesh=>{
      const ud=mesh.userData;if(!ud.sp)return;
      ud.ba+=ud.sp;mesh.position.x=Math.cos(ud.ba)*ud.r;mesh.position.z=Math.sin(ud.ba)*ud.r;
      mesh.position.y=ud.yb+Math.sin(frame*ud.ys+ud.ph)*ud.ya;mesh.rotation.x+=0.02;mesh.rotation.y+=0.015;
      const tgt=isN?.75:.12;mesh.material.opacity+=(tgt-mesh.material.opacity)*.05;
    });
  });
  document.getElementById('spd-fill').style.width=(Math.abs(carSpeed)/MAX_SPD*100).toFixed(0)+'%';
  const pEl=document.getElementById('hud-proj'),eEl=document.getElementById('hud-enter');
  if(nearEntry){pEl.innerHTML='<span style="color:'+nearEntry.distHex+'">'+nearEntry.project.name+'</span>';eEl.style.display='block';}
  else{pEl.textContent='Navigate to a project entrance';eEl.style.display='none';}
  document.getElementById('hud-visited').textContent=visitedSet.size+' / 18 explored';
  drawMinimap();renderer.render(scene,camera);
}

// ── Minimap ───────────────────────────────────────────────────
function drawMinimap(){
  const mw=140,mh=140;mmCtx.fillStyle='#04080f';mmCtx.fillRect(0,0,mw,mh);
  const scale=mw/260,ox=mw/2,oz=mh/2;
  buildings.forEach(b=>{
    const px=ox+b.entranceWorld.x*scale,pz=oz+b.entranceWorld.z*scale;
    const isN=b===nearEntry,isV=b.visited;
    mmCtx.globalAlpha=isN?1:isV?.55:.38;mmCtx.fillStyle=isV?'#3ecf8e':b.distHex;
    mmCtx.beginPath();mmCtx.arc(px,pz,isN?5:2.8,0,Math.PI*2);mmCtx.fill();
    if(isV){mmCtx.strokeStyle='#3ecf8e';mmCtx.lineWidth=1;mmCtx.beginPath();mmCtx.arc(px,pz,4.5,0,Math.PI*2);mmCtx.stroke();}
    mmCtx.globalAlpha=1;
  });
  const cpx=ox+carPos.x*scale,cpz=oz+carPos.z*scale;
  mmCtx.save();mmCtx.translate(cpx,cpz);mmCtx.rotate(-carAngle+Math.PI);
  mmCtx.fillStyle='#f5c842';mmCtx.beginPath();mmCtx.moveTo(0,-6.5);mmCtx.lineTo(4,5);mmCtx.lineTo(0,2.5);mmCtx.lineTo(-4,5);mmCtx.closePath();mmCtx.fill();
  mmCtx.fillStyle='#fff';mmCtx.beginPath();mmCtx.arc(0,0,1.8,0,Math.PI*2);mmCtx.fill();mmCtx.restore();
  mmCtx.strokeStyle='rgba(74,144,217,.14)';mmCtx.lineWidth=1;mmCtx.strokeRect(0,0,mw,mh);
}

// ── Modal ─────────────────────────────────────────────────────
function openModal(b){
  modalOpen=true;if(!b.visited){b.visited=true;visitedSet.add(b.project.name);}
  const p=b.project,dist=DISTRICTS[p.district];
  document.getElementById('mo-ico').textContent=p.icon;
  document.getElementById('mo-ico').style.cssText='background:'+dist.hex+'18;border:1px solid '+dist.hex+'30;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0';
  const ce=document.getElementById('mo-cat');ce.textContent=p.cat;ce.style.color=dist.hex;
  document.getElementById('mo-name').textContent=p.name;
  document.getElementById('mo-stack').textContent=p.stack;
  const de=document.getElementById('mo-dist');de.textContent=dist.name;de.style.cssText='background:'+dist.hex+'18;color:'+dist.hex+';border:1px solid '+dist.hex+'30;display:inline-block;font-size:9px;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px';
  document.getElementById('mo-desc').textContent=p.desc;
  document.getElementById('mo-tags').innerHTML=p.tags.map(t=>'<span class="mo-tag">'+t+'</span>').join('');
  let btns='';
  if(p.gh)btns+='<a class="mo-gh" href="'+p.gh+'" target="_blank">View on GitHub</a>';
  if(p.live)btns+='<a class="mo-live" href="'+p.live+'" target="_blank">Live Demo →</a>';
  if(!p.gh&&!p.live)btns='<span style="font-size:11px;color:#2e4058">No live link available</span>';
  document.getElementById('mo-btns').innerHTML=btns;
  document.getElementById('ov').style.display='flex';playOpen();
}
function closeModal(){document.getElementById('ov').style.display='none';modalOpen=false;}
document.getElementById('ov').addEventListener('click',e=>{if(e.target===document.getElementById('ov'))closeModal();});

// ── Input + D-pad ─────────────────────────────────────────────
function bindInput(){
  document.addEventListener('keydown',e=>{
    keys[e.key]=true;
    if((e.key==='Enter'||e.key===' ')&&nearEntry&&!modalOpen){e.preventDefault();openModal(nearEntry);}
    if(e.key==='Escape'&&modalOpen)closeModal();
    if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();
  });
  document.addEventListener('keyup',e=>{keys[e.key]=false;});
  const cv=document.getElementById('c');
  cv.addEventListener('mousedown',e=>{isDrag=true;lastMX=e.clientX;lastMY=e.clientY;camOrbit=true;});
  window.addEventListener('mouseup',()=>{isDrag=false;});
  window.addEventListener('mousemove',e=>{if(!isDrag)return;const dx=e.clientX-lastMX,dy=e.clientY-lastMY;camTheta-=dx*0.008;camPhi=Math.max(0.1,Math.min(1.4,camPhi+dy*0.006));lastMX=e.clientX;lastMY=e.clientY;});
  cv.addEventListener('dblclick',()=>{camOrbit=false;camTheta=0;camPhi=0.38;});
  cv.addEventListener('touchstart',e=>{if(e.touches.length===1){lastMX=e.touches[0].clientX;lastMY=e.touches[0].clientY;camOrbit=true;}},{passive:true});
  cv.addEventListener('touchmove',e=>{if(e.touches.length!==1)return;const dx=e.touches[0].clientX-lastMX,dy=e.touches[0].clientY-lastMY;camTheta-=dx*0.008;camPhi=Math.max(0.1,Math.min(1.4,camPhi+dy*0.006));lastMX=e.touches[0].clientX;lastMY=e.touches[0].clientY;},{passive:true});
  [['dp-u','up'],['dp-d','down'],['dp-l','left'],['dp-r','right']].forEach(([id,dir])=>{
    const el=document.getElementById(id);
    const on=()=>{dpadState[dir]=1;el.classList.add('on');if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();};
    const off=()=>{dpadState[dir]=0;el.classList.remove('on');};
    el.addEventListener('pointerdown',e=>{e.preventDefault();on();});el.addEventListener('pointerup',off);el.addEventListener('pointerleave',off);
  });
}

// ── Toast ─────────────────────────────────────────────────────
function showToast(msg){
  const s=document.createElement('style');s.textContent='@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}10%,75%{opacity:1;transform:translateX(-50%)}100%{opacity:0}}';document.head.appendChild(s);
  const t=document.createElement('div');t.style.cssText='position:fixed;top:18px;left:50%;transform:translateX(-50%);background:#4a90d9;color:#fff;border-radius:8px;padding:8px 20px;font-size:11px;font-weight:600;z-index:300;animation:tf 3.2s ease forwards;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap';
  t.textContent=msg;document.body.appendChild(t);setTimeout(()=>t.remove(),3300);
}
</script>
</body>
</html>
"""

components.html(HTML, height=760, scrolling=False)
