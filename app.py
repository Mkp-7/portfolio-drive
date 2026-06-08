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

/* ════════════════════════════════════
   INTRO / LANDING PAGE
════════════════════════════════════ */
#intro{
  position:fixed;inset:0;z-index:999;
  background:#04080f;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  overflow:hidden;
}

/* Animated particle canvas behind intro */
#particle-canvas{position:absolute;inset:0;z-index:0}

/* Glowing grid lines */
#intro::before{
  content:'';position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(74,144,217,.06) 1px,transparent 1px),
    linear-gradient(90deg,rgba(74,144,217,.06) 1px,transparent 1px);
  background-size:60px 60px;
  animation:gridScroll 20s linear infinite;
  z-index:1;
}
@keyframes gridScroll{from{background-position:0 0}to{background-position:60px 60px}}

/* Radial spotlight */
#intro::after{
  content:'';position:absolute;inset:0;z-index:2;
  background:radial-gradient(ellipse 70% 60% at 50% 45%,rgba(74,144,217,.08) 0%,transparent 70%);
  pointer-events:none;
}

.intro-content{
  position:relative;z-index:10;
  display:flex;flex-direction:column;align-items:center;
  max-width:780px;width:90%;text-align:center;
}

/* Availability pill */
.avail-pill{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(62,207,142,.08);border:1px solid rgba(62,207,142,.25);
  border-radius:20px;padding:5px 14px;
  font-size:11px;letter-spacing:1.5px;color:#3ecf8e;text-transform:uppercase;
  margin-bottom:28px;
  animation:fadeDown .8s ease both;
}
.avail-dot{width:7px;height:7px;border-radius:50%;background:#3ecf8e;animation:dotPulse 2s ease infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.85)}}

/* Name */
.intro-name{
  font-size:clamp(44px,7vw,72px);font-weight:700;
  color:#eef2ff;letter-spacing:-2px;line-height:1;
  margin-bottom:12px;
  animation:fadeUp .9s .1s ease both;
}
.intro-name .accent{
  background:linear-gradient(135deg,#4a90d9,#7eb8f7);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}

/* Role */
.intro-role{
  font-size:clamp(14px,2vw,18px);color:#5a7096;
  letter-spacing:1px;margin-bottom:32px;
  animation:fadeUp .9s .2s ease both;
}
.intro-role strong{color:#8aaccc;font-weight:500}

/* Domain tags */
.domain-row{
  display:flex;flex-wrap:wrap;justify-content:center;gap:8px;
  margin-bottom:36px;
  animation:fadeUp .9s .3s ease both;
}
.domain-tag{
  font-size:11px;letter-spacing:.8px;text-transform:uppercase;
  padding:5px 13px;border-radius:6px;
  border:1px solid rgba(255,255,255,.1);
  color:#8aaccc;background:rgba(255,255,255,.04);
  transition:all .2s;
}
.domain-tag:hover{border-color:rgba(74,144,217,.4);color:#c8d8f0;background:rgba(74,144,217,.08)}

/* Stats row */
.stats-row{
  display:flex;gap:0;margin-bottom:40px;
  border:1px solid rgba(255,255,255,.08);border-radius:12px;overflow:hidden;
  animation:fadeUp .9s .4s ease both;
}
.stat-item{
  flex:1;padding:16px 20px;text-align:center;
  border-right:1px solid rgba(255,255,255,.08);
  background:rgba(255,255,255,.02);
}
.stat-item:last-child{border-right:none}
.stat-num{font-size:22px;font-weight:700;color:#eef2ff;margin-bottom:2px}
.stat-lbl{font-size:10px;letter-spacing:1px;color:#3a4d68;text-transform:uppercase}

/* CTA row */
.cta-row{
  display:flex;gap:12px;margin-bottom:28px;
  animation:fadeUp .9s .5s ease both;
}
.btn-primary{
  display:inline-flex;align-items:center;gap:8px;
  background:#4a90d9;border:none;border-radius:8px;
  color:#fff;font-size:13px;font-weight:600;
  padding:13px 28px;cursor:pointer;letter-spacing:.5px;
  transition:all .2s;text-decoration:none;
}
.btn-primary:hover{background:#5aa0e9;transform:translateY(-1px)}
.btn-outline{
  display:inline-flex;align-items:center;gap:8px;
  background:transparent;border:1px solid rgba(255,255,255,.15);border-radius:8px;
  color:#8aaccc;font-size:13px;font-weight:500;
  padding:13px 22px;cursor:pointer;letter-spacing:.5px;
  transition:all .2s;text-decoration:none;
}
.btn-outline:hover{border-color:rgba(255,255,255,.35);color:#c8d8f0;transform:translateY(-1px)}
.btn-enter{
  display:inline-flex;align-items:center;gap:8px;
  background:linear-gradient(135deg,rgba(74,144,217,.15),rgba(74,144,217,.05));
  border:1px solid rgba(74,144,217,.35);border-radius:8px;
  color:#7eb8f7;font-size:13px;font-weight:600;
  padding:13px 24px;cursor:pointer;letter-spacing:.5px;
  transition:all .2s;
}
.btn-enter:hover{background:rgba(74,144,217,.2);border-color:rgba(74,144,217,.6);transform:translateY(-1px)}

/* District preview */
.dist-row{
  display:flex;flex-wrap:wrap;justify-content:center;gap:6px;
  animation:fadeUp .9s .6s ease both;
}
.dist-chip{
  display:inline-flex;align-items:center;gap:6px;
  font-size:10px;letter-spacing:.5px;color:#3a4d68;
  padding:4px 10px;border-radius:4px;
  border:1px solid rgba(255,255,255,.05);
}
.dist-pip{width:6px;height:6px;border-radius:50%;flex-shrink:0}

/* Scroll hint */
.scroll-hint{
  margin-top:24px;font-size:10px;letter-spacing:2px;color:#2a3a52;text-transform:uppercase;
  animation:fadeUp .9s .7s ease both;
}

@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeDown{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}

/* ════════════════════════════════════
   GAME
════════════════════════════════════ */
#c{display:block;width:100%;height:100vh}

/* HUD */
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

/* MINIMAP */
#mm-wrap{position:fixed;bottom:16px;right:16px;display:none;z-index:50}
.mm-lbl{font-size:9px;letter-spacing:2px;color:#253545;text-transform:uppercase;text-align:center;margin-bottom:4px}
#mm{border-radius:10px;border:1px solid rgba(74,144,217,.14)}

/* HINT */
#hint-box{position:fixed;bottom:16px;left:16px;display:none;background:rgba(4,8,15,.88);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:7px 13px;font-size:10px;color:#2e4058;z-index:50;line-height:2}

/* DPAD */
#dpad{
  position:fixed;right:16px;bottom:136px;z-index:50;display:none;
  grid-template-areas:'. u .' 'l . r' '. d .';
  grid-template-columns:repeat(3,42px);grid-template-rows:repeat(3,42px);gap:3px;
}
.dp-btn{
  background:rgba(4,8,15,.88);border:1px solid rgba(74,144,217,.2);
  border-radius:8px;display:flex;align-items:center;justify-content:center;
  font-size:16px;color:#4a6a8a;cursor:pointer;
  user-select:none;-webkit-user-select:none;touch-action:none;transition:all .1s;
}
.dp-btn:active,.dp-btn.on{background:rgba(74,144,217,.25);border-color:#4a90d9;color:#7eb8f7}
#dp-u{grid-area:u}#dp-d{grid-area:d}#dp-l{grid-area:l}#dp-r{grid-area:r}

/* MODAL */
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

<!-- ════════════ INTRO ════════════ -->
<div id="intro">
  <canvas id="particle-canvas"></canvas>

  <div class="intro-content">
    <div class="avail-pill">
      <span class="avail-dot"></span>
      Open to opportunities
    </div>

    <div class="intro-name">
      Mukund <span class="accent">Patel</span>
    </div>

    <div class="intro-role">
      <strong>Data Scientist</strong> &nbsp;·&nbsp; <strong>AI Engineer</strong> &nbsp;·&nbsp; <strong>Analytics Professional</strong>
    </div>

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
      <div class="stat-item">
        <div class="stat-num">18</div>
        <div class="stat-lbl">Projects</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">5</div>
        <div class="stat-lbl">Domains</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">6</div>
        <div class="stat-lbl">Live Apps</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">Python · SQL · R</div>
        <div class="stat-lbl">Core Stack</div>
      </div>
    </div>

    <div class="cta-row">
      <a class="btn-outline" href="https://www.linkedin.com/in/mukund-patel7" target="_blank">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a class="btn-outline" href="https://github.com/Mkp-7" target="_blank">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
        GitHub
      </a>
      <button class="btn-primary" onclick="startGame()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Explore Portfolio
      </button>
    </div>

    <div class="dist-row">
      <div class="dist-chip"><div class="dist-pip" style="background:#4a90d9"></div>Retail &amp; Commerce</div>
      <div class="dist-chip"><div class="dist-pip" style="background:#e85555"></div>Finance &amp; Banking</div>
      <div class="dist-chip"><div class="dist-pip" style="background:#f5a623"></div>Operations &amp; Logistics</div>
      <div class="dist-chip"><div class="dist-pip" style="background:#3ecf8e"></div>Healthcare &amp; Life Sci.</div>
      <div class="dist-chip"><div class="dist-pip" style="background:#9b6dff"></div>Research &amp; Education</div>
    </div>

    <div class="scroll-hint">18 projects across 5 districts · Drive to explore</div>
  </div>
</div>

<!-- ════════════ GAME ════════════ -->
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
  <span style="color:#8aaccc">W A S D</span> / Arrows — Drive &nbsp;·&nbsp; <span style="color:#8aaccc">Enter</span> — Open project
</div>

<!-- D-PAD for mobile -->
<div id="dpad">
  <div class="dp-btn" id="dp-u">↑</div>
  <div class="dp-btn" id="dp-l">←</div>
  <div class="dp-btn" id="dp-r">→</div>
  <div class="dp-btn" id="dp-d">↓</div>
</div>

<!-- MODAL -->
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
// ════════════════════════════════════
//  INTRO PARTICLE CANVAS
// ════════════════════════════════════
(function(){
  const canvas=document.getElementById('particle-canvas');
  const ctx=canvas.getContext('2d');
  let W,H,pts=[];
  function resize(){
    W=canvas.width=canvas.offsetWidth||window.innerWidth;
    H=canvas.height=canvas.offsetHeight||window.innerHeight;
  }
  resize();window.addEventListener('resize',resize);
  for(let i=0;i<90;i++) pts.push({
    x:Math.random()*1600-800,y:Math.random()*900-450,
    vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,
    r:Math.random()*1.8+.4,a:Math.random()
  });
  function drawPts(){
    ctx.clearRect(0,0,W,H);
    const cx=W/2,cy=H/2;
    pts.forEach(p=>{
      p.x+=p.vx;p.y+=p.vy;
      if(p.x<-800)p.x=800;if(p.x>800)p.x=-800;
      if(p.y<-450)p.y=450;if(p.y>450)p.y=-450;
      ctx.beginPath();
      ctx.arc(cx+p.x,cy+p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=`rgba(74,144,217,${p.a*.35})`;
      ctx.fill();
    });
    // Draw faint connecting lines between close particles
    for(let i=0;i<pts.length;i++){
      for(let j=i+1;j<pts.length;j++){
        const dx=(pts[i].x-pts[j].x),dy=(pts[i].y-pts[j].y);
        const d=Math.sqrt(dx*dx+dy*dy);
        if(d<120){
          ctx.beginPath();
          ctx.moveTo(cx+pts[i].x,cy+pts[i].y);
          ctx.lineTo(cx+pts[j].x,cy+pts[j].y);
          ctx.strokeStyle=`rgba(74,144,217,${(1-d/120)*.08})`;
          ctx.lineWidth=.5;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(drawPts);
  }
  drawPts();
})();

// ════════════════════════════════════
//  DISTRICTS & PROJECTS
// ════════════════════════════════════
const DISTRICTS={
  retail:   {name:"Retail & Commerce",      color:0x4a90d9,hex:"#4a90d9",particles:"box"},
  finance:  {name:"Finance & Banking",      color:0xe85555,hex:"#e85555",particles:"cone"},
  ops:      {name:"Operations & Logistics", color:0xf5a623,hex:"#f5a623",particles:"cylinder"},
  health:   {name:"Healthcare & Life Sci.", color:0x3ecf8e,hex:"#3ecf8e",particles:"sphere"},
  research: {name:"Research & Education",   color:0x9b6dff,hex:"#9b6dff",particles:"tetra"},
};

const PROJECTS=[
  {name:"AI Pricing Intelligence",      icon:"🤖",district:"retail",  stat:"20+ SKUs · 95% accuracy",    cat:"Streamlit Application",   stack:"Python · Claude API",               desc:"Competitive pricing agent using the Claude API to automate real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Surfaced 12–15% margin improvement opportunities.",                                                                                            tags:["Claude API","Price Monitoring","Competitive Intel","ML"],                       gh:"https://github.com/Mkp-7/AI-Pricing-Agent",                                       live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"Retail Intelligence Platform", icon:"🛒",district:"retail",  stat:"4 AI modules · Live app",    cat:"Streamlit Application",   stack:"Python · Groq LLM · Yelp Dataset",  desc:"AI-native customer intelligence platform converting public review data into operational insights. Four modules: Voice of Customer AI, Store Pulse Map (regional benchmarking), Test & Learn Autopilot (A/B statistical significance), and Analyst Copilot (plain-English Q&A chatbot).",                                                                               tags:["Groq LLM","NLP","Plotly","A/B Testing","Customer Analytics"],                  gh:"https://github.com/Mkp-7/retail-intelligence-platform",                           live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Retail Customer Analytics",    icon:"🛍️",district:"retail",  stat:"25K products · -40% time",   cat:"ML & Python",             stack:"Python · Scikit-learn · K-Means",   desc:"Analyzed 25,000+ product records and 10,000+ customer transactions. K-Means clustering (5 segments) identified top 20% of customers contributing 60% of revenue. Automated Excel reporting dashboard tracking 10+ KPIs, reducing manual analysis time by 40%.",                                                                                                         tags:["K-Means","Customer Segmentation","RFM","Pandas","Excel Automation"],            gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",              live:""},
  {name:"E-Commerce Funnel Analytics",  icon:"📈",district:"retail",  stat:"269K users · $25K revenue",  cat:"Looker · dbt · BigQuery", stack:"dbt · BigQuery · GA4 · Looker",    desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling and behavioral segmentation across 269K users. Identified 9,630 cart abandonment targets. Simulated email recovery campaign projecting 23% recovery vs 8% baseline and $25K incremental revenue.",                                                                                              tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","$25K Revenue"],            gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",                                live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"},
  {name:"Sales & Demand Forecasting",   icon:"📊",district:"retail",  stat:"94% accuracy · 25K SKUs",    cat:"Tableau Dashboard",       stack:"Python · ARIMA · SARIMA · Tableau", desc:"Fine-tuned ARIMA and SARIMA models forecasting 6-month revenue for 25,432 products across 12 regions at 94% accuracy. Identified top 20% of customers contributing 62% of revenue. Interactive Tableau and Power BI dashboards for pricing and promotion strategy.",                                                                                                  tags:["ARIMA","SARIMA","94% Accuracy","Tableau","Power BI"],                          gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",                             live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  {name:"Banking Risk Intelligence",    icon:"🏦",district:"finance", stat:"4500+ banks · AUC 0.84",     cat:"Streamlit Application",   stack:"Python · FDIC API · FRED",          desc:"Operational risk monitoring platform querying FDIC data for 4,500+ banks. Calculates 5 risk KRIs against Basel III and CCAR thresholds. Applies Random Forest (AUC=0.84) and Gradient Boosting for bank failure prediction. Integrates Fed Funds Rate and yield-curve from FRED.",                                                                                    tags:["Basel III","FDIC API","FRED","Random Forest AUC=0.84","CCAR"],                 gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",                                 live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Banking Client Analysis",      icon:"💳",district:"finance", stat:"3000 clients · $0.9B loans", cat:"Power BI Dashboard",      stack:"Power BI · SQL · Python",           desc:"Structured 3,000 banking client records integrating portfolio, relationship, and product-level dimensions. Dashboard identifies high-fee accounts (~51% of deposits), Private Bank loan exposure (~$0.9B), and cross-segment variation for risk assessment and regulatory reporting.",                                                                                    tags:["Power BI","Client Segmentation","Portfolio Analytics","Risk Assessment"],       gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",     live:""},
  {name:"Insurance Claims Prediction",  icon:"🛡️",district:"finance", stat:"58K records · 94% accuracy", cat:"Power BI + ML",           stack:"R · SQL Server · Power BI",         desc:"Processed 58,000+ insurance policy records in SQL Server. Random Forest and Logistic Regression in R achieving 94% accuracy for 6-month claim likelihood prediction. Power BI dashboard tracks predicted claim probability by vehicle segment, fuel type, and policyholder demographics.",                                                                          tags:["Random Forest","94% Accuracy","SQL Server","R","Power BI"],                    gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",                              live:""},
  {name:"Revenue Intelligence Agent",   icon:"🚗",district:"ops",    stat:"10 airports · 3hrs→15min",   cat:"Streamlit Application",   stack:"Python · Groq LLM · GitHub Actions",desc:"Autonomous multi-agent pipeline monitoring competitor car-rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals. Reduces analyst workflow from 3 hours to 15 minutes. 5-tab Streamlit dashboard with anomaly flagging.",                                                                               tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","SQLite"],                  gh:"https://github.com/Mkp-7/Revenue-Management-Agent",                               live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"EcoRoute Optimizer",           icon:"🌿",district:"ops",    stat:"60+ US cities · EPA method", cat:"Streamlit Application",   stack:"Python · Gemini AI · OR-Tools",     desc:"Logistics optimization platform generating carbon-minimized shipping routes across 60+ US cities. Evaluates diesel, EV, and rail freight via EPA SmartWay carbon methodology. Integrates OpenRouteService and OpenWeatherMap APIs with SQLite route caching and a natural-language query interface.",                                                                  tags:["Gemini AI","OR-Tools","Carbon Optimization","NLP","REST APIs"],                gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",                                     live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Supply Chain Analytics",       icon:"📦",district:"ops",    stat:"10 datasets · 12+ KPIs",     cat:"Power BI Dashboard",      stack:"Power BI · Power Query · DAX",      desc:"Integrated 10 raw Excel supply chain datasets via Power Query ETL and built a star schema data model. Created 12+ DAX measures for KPIs including inventory turnover, stock aging, on-time delivery %, and reorder alerts. Includes logistics maps and drill-through analysis.",                                                                                    tags:["Power BI","DAX","Power Query","Star Schema","ETL","Inventory"],                gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",                              live:""},
  {name:"Workforce Utilization",        icon:"👥",district:"ops",    stat:"80 employees · 3 months",    cat:"Power BI Dashboard",      stack:"Power BI · DAX · HR Analytics",     desc:"Dashboard analyzing attendance for 80 employees over 3 months, tracking presence, WFH utilization, and leave patterns. Computed KPIs including attendance rate, WFH utilization, and sick leave frequency. Identified mid-month attendance dips and peak day shifts from Fridays to Mondays.",                                                                       tags:["Power BI","HR Analytics","DAX","WFH Utilization","Workforce Planning"],        gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",                        live:""},
  {name:"Medmedia Analytics Hub",       icon:"🏥",district:"health", stat:"470K trials · 35M papers",   cat:"Streamlit Application",   stack:"Python · LLMs · ClinicalTrials.gov",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables HCP audience segmentation across 10 clinical specialties and AI-generated content strategy.",                                                                               tags:["Healthcare NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation"],      gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",                                 live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Diabetes Risk Prediction",     icon:"🩺",district:"health", stat:"769 patients · 80% accuracy",cat:"ML & Python",             stack:"Python · SVM · Scikit-learn",       desc:"Multi-model diabetes prediction system trained on clinical data from 769 patients. Evaluated Logistic Regression, Decision Tree, Random Forest, and SVM. Achieved peak predictive accuracy of 80% with SVM. Applied feature selection and exploratory analysis throughout.",                                                                                          tags:["SVM","Random Forest","Logistic Regression","Healthcare ML","Feature Selection"],gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",                              live:""},
  {name:"COVID-19 Global Impact",       icon:"🦠",district:"research",stat:"450K records · WHO data",   cat:"Exploratory Data Analysis",stack:"Python · EDA · WHO Data",           desc:"Global COVID-19 analysis using WHO data (~450,000 records). Covers mortality comparisons across WHO regions, global daily case and death trajectories, country-level outbreaks on peak days, and regional disparities in case fatality rates.",                                                                                                                      tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology","Data Storytelling"],    gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",                        live:""},
  {name:"MSU Collaboratory",            icon:"🎓",district:"research",stat:"3D network · MSU partners", cat:"Tableau Dashboard",       stack:"Tableau · 3D Network Graph",        desc:"3D network visualization of interdisciplinary activities and partnerships at Montclair State University. Tableau dashboard surfacing Collaboratory data insights across community partner organizations. Companion network graph on GitHub Pages showing cross-organizational topology.",                                                                               tags:["Tableau","3D Network Graph","MSU","Community Partners","GitHub Pages"],         gh:"https://mkp-7.github.io/Network-Graph/",                                          live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"Student Wellbeing Study",      icon:"📋",district:"research",stat:"70 students · 21 days",     cat:"Tableau Dashboard",       stack:"Python · Statistics · Tableau",     desc:"Longitudinal study tracking 70 MSU students over 21 days. Collected daily activities, social context, location, and self-reported happiness (0–10) at 30-minute intervals. Conducted hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard identifies happiness patterns by activity category.",                                                          tags:["Hypothesis Testing","ANOVA","Regression","Tableau","Behavioral Analytics"],    gh:"",                                                                                live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"},
  {name:"Book Recommendation Engine",   icon:"📚",district:"research",stat:"10K books · 1M+ ratings",   cat:"ML & Python",             stack:"Python · TF-IDF · SVD",             desc:"Recommendation engine trained on 10,000 books and 1M+ ratings. Employs TF-IDF with Cosine Similarity and SVD for personalized recommendations. Addresses cold start, scalability, and relevance challenges for accurate suggestions across diverse reader profiles.",                                                                                                  tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering","1M+ Ratings"],    gh:"https://github.com/Mkp-7/Book_Recommendation",                                    live:""},
];

const DIST_ORDER=['retail','finance','ops','health','research'];
const ROW_COLS={retail:5,finance:3,ops:4,health:2,research:4};

// ════════════════════════════════════
//  SCENE STATE
// ════════════════════════════════════
let scene,camera,renderer,clock;
let carGroup,carWheels=[];
let buildings=[];
let nearEntry=null,modalOpen=false;
let keys={},dpadState={up:0,down:0,left:0,right:0};
let carPos=new THREE.Vector3(0,0,110);
let carAngle=Math.PI,carSpeed=0;
let frame=0;
let mmCanvas,mmCtx;
let visitedSet=new Set();
let allParticleGroups=[];
let audioCtx=null,engineOsc=null,engineGain=null;
let lastNearEntry=null;

const CAM_BACK=11,CAM_UP=5.5,CAM_LAG=0.09;
let camPos=new THREE.Vector3(0,8,122);
const BLK_X=24,BLK_Z=30,ROAD_W=10,CITY_H=155;

// ════════════════════════════════════
//  START GAME
// ════════════════════════════════════
function startGame(){
  document.getElementById('intro').style.display='none';
  document.getElementById('c').style.display='block';
  ['hud','mm-wrap','hint-box'].forEach(id=>document.getElementById(id).style.display='block');
  document.getElementById('dpad').style.display='grid';
  mmCanvas=document.getElementById('mm');mmCtx=mmCanvas.getContext('2d');
  init3D();buildCity();buildCar();bindInput();initAudio();
  clock=new THREE.Clock();loop();
  showToast('Drive into a glowing zone · Press Enter to open a project');
}

// ════════════════════════════════════
//  THREE.JS
// ════════════════════════════════════
function init3D(){
  scene=new THREE.Scene();
  scene.background=new THREE.Color(0x04080f);
  scene.fog=new THREE.FogExp2(0x04080f,0.007);
  camera=new THREE.PerspectiveCamera(55,innerWidth/innerHeight,0.1,400);
  camera.position.copy(camPos);
  renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true,powerPreference:'high-performance'});
  renderer.setSize(innerWidth,innerHeight);
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.shadowMap.enabled=true;
  renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure=1.1;
  window.addEventListener('resize',()=>{
    camera.aspect=innerWidth/innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth,innerHeight);
  });
  scene.add(new THREE.AmbientLight(0x8899bb,0.5));
  const sun=new THREE.DirectionalLight(0xeef2ff,1.8);
  sun.position.set(60,100,40);sun.castShadow=true;
  sun.shadow.mapSize.set(4096,4096);
  sun.shadow.camera.near=1;sun.shadow.camera.far=400;
  sun.shadow.camera.left=sun.shadow.camera.bottom=-200;
  sun.shadow.camera.right=sun.shadow.camera.top=200;
  sun.shadow.bias=-0.0004;scene.add(sun);
  scene.add(new THREE.DirectionalLight(0x2233aa,0.3));
}

function projPos(p){
  const row=DIST_ORDER.indexOf(p.district);
  const distProjs=PROJECTS.filter(x=>x.district===p.district);
  const col=distProjs.indexOf(p);
  const cols=ROW_COLS[p.district];
  const startX=-((cols-1)*BLK_X)/2;
  const startZ=-((DIST_ORDER.length-1)*BLK_Z)/2;
  return{x:startX+col*BLK_X,z:startZ+row*BLK_Z};
}

function buildCity(){
  // Ground
  const ground=new THREE.Mesh(new THREE.PlaneGeometry(CITY_H*2.5,CITY_H*2.5),
    new THREE.MeshLambertMaterial({color:0x060a10}));
  ground.rotation.x=-Math.PI/2;ground.receiveShadow=true;scene.add(ground);
  scene.add(new THREE.GridHelper(CITY_H*2.4,110,0x0d1420,0x090f18));
  makeRoads();makeDistrictZones();placeBuildings();makeDistrictSigns();placeLamps();
}

function makeRoads(){
  const rM=new THREE.MeshLambertMaterial({color:0x0a0e18});
  const lM=new THREE.MeshLambertMaterial({color:0x1e2e48,emissive:0x102030,emissiveIntensity:0.45});
  const sM=new THREE.MeshLambertMaterial({color:0x111c2c});
  const ROWS=DIST_ORDER.length;
  const startZ=-((ROWS-1)*BLK_Z)/2;
  for(let r=-1;r<=ROWS;r++) makeHR(startZ+r*BLK_Z-BLK_Z/2+BLK_Z/2,rM,lM,sM);
  const startX=-((5-1)*BLK_X)/2;
  for(let c=-1;c<=5;c++) makeVR(startX+c*BLK_X-BLK_X/2+BLK_X/2,rM,lM,sM);
}

function makeHR(rz,rM,lM,sM){
  const len=CITY_H*2.2;
  const r=new THREE.Mesh(new THREE.PlaneGeometry(len,ROAD_W),rM);
  r.rotation.x=-Math.PI/2;r.position.set(0,0.05,rz);r.receiveShadow=true;scene.add(r);
  for(const oz of[-ROAD_W/2+0.3,ROAD_W/2-0.3]){
    const k=new THREE.Mesh(new THREE.BoxGeometry(len,0.16,0.3),sM);
    k.position.set(0,0.08,rz+oz);scene.add(k);
  }
  for(let x=-len/2+3;x<len/2;x+=7){
    const d=new THREE.Mesh(new THREE.PlaneGeometry(3.2,0.2),lM);
    d.rotation.x=-Math.PI/2;d.position.set(x,0.07,rz);scene.add(d);
  }
}

function makeVR(rx,rM,lM,sM){
  const len=CITY_H*2.2;
  const r=new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W,len),rM);
  r.rotation.x=-Math.PI/2;r.position.set(rx,0.05,0);r.receiveShadow=true;scene.add(r);
  for(const ox of[-ROAD_W/2+0.3,ROAD_W/2-0.3]){
    const k=new THREE.Mesh(new THREE.BoxGeometry(0.3,0.16,len),sM);
    k.position.set(rx+ox,0.08,0);scene.add(k);
  }
  for(let z=-len/2+3;z<len/2;z+=7){
    const d=new THREE.Mesh(new THREE.PlaneGeometry(0.2,3.2),lM);
    d.rotation.x=-Math.PI/2;d.position.set(rx,0.07,z);scene.add(d);
  }
}

function makeDistrictZones(){
  const startZ=-((DIST_ORDER.length-1)*BLK_Z)/2;
  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[dk];
    const startX=-((cols-1)*BLK_X)/2;
    const zone=new THREE.Mesh(
      new THREE.PlaneGeometry(cols*BLK_X+3,BLK_Z-ROAD_W-1),
      new THREE.MeshLambertMaterial({color:dist.color,transparent:true,opacity:0.038})
    );
    zone.rotation.x=-Math.PI/2;
    zone.position.set(startX+(cols-1)*BLK_X/2,0.055,startZ+row*BLK_Z);
    scene.add(zone);
  });
}

function makeDistrictSigns(){
  const startZ=-((DIST_ORDER.length-1)*BLK_Z)/2;
  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[dk];
    const startX=-((cols-1)*BLK_X)/2;
    const cx=startX+(cols-1)*BLK_X/2;
    const rz=startZ+row*BLK_Z-BLK_Z/2+1.5;
    makeSign(cx,rz,dist.name,dist.color);
  });
}

function makeSign(x,z,label,color){
  const g=new THREE.Group();g.position.set(x,0,z);
  const pM=new THREE.MeshLambertMaterial({color:0x3a4558});
  for(const ox of[-3.2,3.2]){
    const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.09,0.11,4.2,8),pM);
    pole.position.set(ox,2.1,0);g.add(pole);
  }
  const board=new THREE.Mesh(new THREE.BoxGeometry(7.5,1.1,0.18),
    new THREE.MeshLambertMaterial({color:0x08101e}));
  board.position.set(0,4.2,0);g.add(board);
  const strip=new THREE.Mesh(new THREE.BoxGeometry(7.5,0.18,0.22),
    new THREE.MeshLambertMaterial({color,emissive:color,emissiveIntensity:0.6}));
  strip.position.set(0,4.79,0);g.add(strip);
  const can=document.createElement('canvas');can.width=512;can.height=80;
  const ctx=can.getContext('2d');ctx.clearRect(0,0,512,80);
  ctx.font='bold 28px Segoe UI,Arial';ctx.fillStyle='#c8d8f0';
  ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(label.toUpperCase(),256,40);
  const tex=new THREE.CanvasTexture(can);
  const sign=new THREE.Mesh(new THREE.PlaneGeometry(7,0.9),
    new THREE.MeshBasicMaterial({map:tex,transparent:true}));
  sign.position.set(0,4.2,0.1);g.add(sign);
  const pl=new THREE.PointLight(color,0.45,14);pl.position.set(0,4.5,1.2);g.add(pl);
  scene.add(g);
}

function placeBuildings(){
  PROJECTS.forEach((p,i)=>{
    const{x,z}=projPos(p);
    buildings.push(makeBuilding(p,x,z,i));
  });
}

function makeBuilding(p,bx,bz,idx){
  const dist=DISTRICTS[p.district];
  const hc=dist.color;
  const style=idx%4,bH=9+(idx%7)*3.2,bW=7.5,bD=6.5;
  const g=new THREE.Group();g.position.set(bx,0,bz);

  const pave=new THREE.Mesh(new THREE.BoxGeometry(bW+3,0.2,bD+3),
    new THREE.MeshLambertMaterial({color:0x0e1826}));
  pave.position.y=0.1;pave.receiveShadow=true;g.add(pave);

  const body=new THREE.Mesh(new THREE.BoxGeometry(bW,bH,bD),
    new THREE.MeshLambertMaterial({color:0x0c1422}));
  body.position.y=bH/2+0.2;body.castShadow=true;body.receiveShadow=true;g.add(body);

  if(style===0){
    const gM=new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.06,transparent:true,opacity:0.78});
    const s=new THREE.Mesh(new THREE.BoxGeometry(bW-1,bH,0.09),gM);
    s.position.set(0,bH/2+0.2,bD/2+0.05);g.add(s);
    const s2=s.clone();s2.position.z=-bD/2-0.05;g.add(s2);
  }else if(style===1){
    for(let b=1;b<Math.floor(bH/2.8);b++){
      const band=new THREE.Mesh(new THREE.BoxGeometry(bW+0.1,0.16,bD+0.1),
        new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.14}));
      band.position.y=0.2+b*2.8;g.add(band);
    }
  }else if(style===2){
    const cM=new THREE.MeshLambertMaterial({color:0x182236});
    for(const[cx,cz]of[[-bW/2+0.4,-bD/2+0.4],[bW/2-0.4,-bD/2+0.4],[-bW/2+0.4,bD/2-0.4],[bW/2-0.4,bD/2-0.4]]){
      const col=new THREE.Mesh(new THREE.BoxGeometry(0.65,bH,0.65),cM);
      col.position.set(cx,bH/2+0.2,cz);g.add(col);
    }
  }else{
    const top=new THREE.Mesh(new THREE.BoxGeometry(bW*0.62,bH*0.38,bD*0.62),
      new THREE.MeshLambertMaterial({color:0x0c1422}));
    top.position.y=bH+bH*0.38/2-0.4;top.castShadow=true;g.add(top);
    const ledge=new THREE.Mesh(new THREE.BoxGeometry(bW+0.3,0.28,bD+0.3),
      new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.22}));
    ledge.position.y=bH+0.2;g.add(ledge);
  }

  addWins(g,bW,bH,bD);
  makePoster(g,p,dist,bW,bH,bD);

  const roofBar=new THREE.Mesh(new THREE.BoxGeometry(bW,0.3,bD),
    new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.55}));
  roofBar.position.y=bH+0.38;g.add(roofBar);
  const rL=new THREE.PointLight(hc,0.65,22);rL.position.set(0,bH+2,0);g.add(rL);

  // Particles
  const pg=makeParticles(p.district,hc,bW,bH);
  g.add(pg);allParticleGroups.push({group:pg,building:null});

  // Entrance
  const eZ=bD/2+3.6;
  const lTex=makeRoadTex(p.name,dist.hex);
  const lMesh=new THREE.Mesh(new THREE.PlaneGeometry(9.5,2),
    new THREE.MeshBasicMaterial({map:lTex,transparent:true,depthWrite:false}));
  lMesh.rotation.x=-Math.PI/2;lMesh.position.set(0,0.11,eZ+3.8);g.add(lMesh);

  const eMat=new THREE.MeshBasicMaterial({color:hc,transparent:true,opacity:0.12,depthWrite:false});
  const ePlane=new THREE.Mesh(new THREE.PlaneGeometry(5.5,3.2),eMat);
  ePlane.rotation.x=-Math.PI/2;ePlane.position.set(0,0.12,eZ);g.add(ePlane);

  const fM=new THREE.MeshBasicMaterial({color:hc,transparent:true,opacity:0.45});
  [[5.5,0.1,0,eZ-1.6],[5.5,0.1,0,eZ+1.6],[0.1,3.2,-2.75,eZ],[0.1,3.2,2.75,eZ]].forEach(([fw,fh,fx,fz_])=>{
    const l=new THREE.Mesh(new THREE.PlaneGeometry(fw,fh),fM.clone());
    l.rotation.x=-Math.PI/2;l.position.set(fx,0.13,fz_);g.add(l);
  });
  const pstM=new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.65});
  for(const[px,pz_]of[[-2.5,eZ-1.4],[2.5,eZ-1.4],[-2.5,eZ+1.4],[2.5,eZ+1.4]]){
    const post=new THREE.Mesh(new THREE.CylinderGeometry(0.07,0.07,1.0,8),pstM.clone());
    post.position.set(px,0.5,pz_);g.add(post);
    const ball=new THREE.Mesh(new THREE.SphereGeometry(0.11,8,8),pstM.clone());
    ball.position.set(px,1.1,pz_);g.add(ball);
  }
  const eL=new THREE.PointLight(hc,0,12);eL.position.set(0,0.4,eZ);g.add(eL);

  const entranceWorld=new THREE.Vector3(bx,0,bz+eZ);
  const bbox=new THREE.Box2(
    new THREE.Vector2(bx-bW/2-0.5,bz-bD/2-0.5),
    new THREE.Vector2(bx+bW/2+0.5,bz+bD/2+0.5)
  );
  scene.add(g);
  return{group:g,bbox,entranceWorld,project:p,eMat,eLight:eL,visited:false,distHex:dist.hex,particleGroup:pg};
}

function makePoster(g,p,dist,bW,bH,bD){
  const can=document.createElement('canvas');can.width=512;can.height=320;
  const ctx=can.getContext('2d');
  ctx.fillStyle='#0b1525';ctx.fillRect(0,0,512,320);
  ctx.fillStyle=dist.hex;ctx.fillRect(0,0,512,10);
  ctx.font='52px serif';ctx.textAlign='center';ctx.fillText(p.icon,256,82);
  ctx.font='bold 30px Segoe UI,Arial';ctx.fillStyle='#eef2ff';ctx.textBaseline='top';
  let nm=p.name;
  if(ctx.measureText(nm).width>480)nm=nm.slice(0,22)+'…';
  ctx.fillText(nm,256,105);
  ctx.font='20px Segoe UI,Arial';ctx.fillStyle=dist.hex;ctx.fillText(p.stat,256,156);
  ctx.font='14px Segoe UI,Arial';ctx.fillStyle='rgba(180,200,225,0.45)';ctx.fillText(dist.name.toUpperCase(),256,196);
  ctx.fillStyle=dist.hex;ctx.globalAlpha=0.22;ctx.fillRect(0,307,512,13);ctx.globalAlpha=1;
  const tex=new THREE.CanvasTexture(can);
  const poster=new THREE.Mesh(new THREE.PlaneGeometry(bW*0.82,bH*0.48),
    new THREE.MeshBasicMaterial({map:tex,transparent:true}));
  poster.position.set(0,bH*0.52,bD/2+0.07);g.add(poster);
  const p2=poster.clone();p2.position.z=-bD/2-0.07;p2.rotation.y=Math.PI;g.add(p2);
}

function makeParticles(dk,color,bW,bH){
  const group=new THREE.Group();
  for(let i=0;i<18;i++){
    let geo;
    if(dk==='retail')      geo=new THREE.BoxGeometry(0.18,0.18,0.18);
    else if(dk==='finance')geo=new THREE.ConeGeometry(0.12,0.28,4);
    else if(dk==='ops')    geo=new THREE.CylinderGeometry(0.06,0.06,0.3,6);
    else if(dk==='health') geo=new THREE.SphereGeometry(0.12,8,8);
    else                   geo=new THREE.TetrahedronGeometry(0.13);
    const m=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color,transparent:true,opacity:0}));
    const angle=Math.random()*Math.PI*2,radius=2.2+Math.random()*3.5;
    m.position.set(Math.cos(angle)*radius,1.5+Math.random()*bH*.85,Math.sin(angle)*radius);
    m.userData={baseAngle:angle,radius,speed:.003+Math.random()*.005,ySpeed:.007+Math.random()*.008,yBase:m.position.y,yAmp:.7+Math.random()*1.2,phase:Math.random()*Math.PI*2,color};
    group.add(m);
  }
  group.userData.isParticleGroup=true;
  return group;
}

function makeRoadTex(text,hex){
  const can=document.createElement('canvas');can.width=512;can.height=112;
  const ctx=can.getContext('2d');ctx.clearRect(0,0,512,112);
  ctx.font='bold 32px Segoe UI,Arial';ctx.fillStyle=hex;
  ctx.textAlign='center';ctx.textBaseline='middle';
  let label=text;while(ctx.measureText(label).width>490&&label.length>4)label=label.slice(0,-1);
  if(label!==text)label=label.trim()+'…';
  ctx.fillText(label,256,56);
  return new THREE.CanvasTexture(can);
}

function addWins(g,bW,bH,bD){
  const litM=new THREE.MeshLambertMaterial({color:0xfff0b0,emissive:0xfff0b0,emissiveIntensity:0.65});
  const dkM=new THREE.MeshLambertMaterial({color:0x0a1020});
  const cols=3,rows=Math.max(2,Math.floor((bH-1.5)/2.2));
  const gapX=(bW-1.8)/(cols-1),gapY=(bH-1.5)/(rows+1);
  for(let r=0;r<rows;r++) for(let c=0;c<cols;c++){
    const wx=-bW/2+0.9+c*gapX,wy=0.2+gapY+r*gapY,lit=Math.random()>.32;
    const wf=new THREE.Mesh(new THREE.BoxGeometry(0.62,0.82,0.07),lit?litM:dkM);
    wf.position.set(wx,wy,bD/2+0.04);g.add(wf);
    const wb=wf.clone();wb.position.z=-bD/2-0.04;g.add(wb);
  }
}

function placeLamps(){
  const pM=new THREE.MeshLambertMaterial({color:0x606878});
  const bM=new THREE.MeshLambertMaterial({color:0xffeedd,emissive:0xffeedd,emissiveIntensity:1});
  const startZ=-((DIST_ORDER.length-1)*BLK_Z)/2;
  for(let c=-1;c<=5;c++) for(let r=-1;r<=DIST_ORDER.length;r++){
    const lx=-((5-1)*BLK_X)/2+c*BLK_X-BLK_X/2;
    const lz=startZ+r*BLK_Z-BLK_Z/2;
    const lg=new THREE.Group();lg.position.set(lx,0,lz);
    const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.07,0.09,5,8),pM);
    pole.position.y=2.5;lg.add(pole);
    const arm=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.07,1.1),pM);
    arm.position.set(0,5.1,0.55);lg.add(arm);
    const head=new THREE.Mesh(new THREE.BoxGeometry(0.34,0.15,0.55),bM);
    head.position.set(0,4.98,1.0);lg.add(head);
    const pl=new THREE.PointLight(0xfff0e0,0.28,16);pl.position.set(0,4.9,1.0);lg.add(pl);
    scene.add(lg);
  }
}

// ════════════════════════════════════
//  CAR
// ════════════════════════════════════
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
  const grille=new THREE.Mesh(new THREE.BoxGeometry(1.5,0.2,0.08),dM);grille.position.set(0,0.52,2.44);carGroup.add(grille);
  for(const hx of[-0.74,0.74]){
    const hl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),hM);hl.position.set(hx,0.74,2.45);carGroup.add(hl);
    const beam=new THREE.SpotLight(0xffffff,0.9,28,Math.PI*0.1,0.5);
    beam.position.set(hx,0.74,2.5);beam.target.position.set(hx*1.1,-2,15);
    carGroup.add(beam);carGroup.add(beam.target);
  }
  for(const tx of[-0.74,0.74]){const tl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),tM);tl.position.set(tx,0.74,-2.45);carGroup.add(tl);}
  for(const sx of[-1.23,1.23]){const mir=new THREE.Mesh(new THREE.BoxGeometry(0.08,0.13,0.32),cM);mir.position.set(sx,1.1,0.65);carGroup.add(mir);}

  [[-1.14,0.42,1.52],[1.14,0.42,1.52],[-1.14,0.42,-1.52],[1.14,0.42,-1.52]].forEach(([wx,wy,wz])=>{
    const wg=new THREE.Group();
    const tyre=new THREE.Mesh(new THREE.CylinderGeometry(0.42,0.42,0.26,20),yM);tyre.rotation.z=Math.PI/2;tyre.castShadow=true;wg.add(tyre);
    const rim=new THREE.Mesh(new THREE.CylinderGeometry(0.27,0.27,0.27,10),rM);rim.rotation.z=Math.PI/2;wg.add(rim);
    for(let s=0;s<5;s++){
      const spk=new THREE.Mesh(new THREE.BoxGeometry(0.05,0.52,0.05),rM);
      spk.rotation.z=Math.PI/2;spk.rotation.x=(s/5)*Math.PI*2;
      spk.position.y=Math.sin((s/5)*Math.PI*2)*0.14;spk.position.z=Math.cos((s/5)*Math.PI*2)*0.14;wg.add(spk);
    }
    wg.position.set(wx,wy,wz);wg.userData.isWheel=true;carGroup.add(wg);carWheels.push(wg);
  });
  carGroup.position.copy(carPos);scene.add(carGroup);
}

// ════════════════════════════════════
//  AUDIO
// ════════════════════════════════════
function initAudio(){
  try{
    audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    engineGain=audioCtx.createGain();engineGain.gain.value=0;engineGain.connect(audioCtx.destination);
    engineOsc=audioCtx.createOscillator();engineOsc.type='sawtooth';engineOsc.frequency.value=55;
    const f=audioCtx.createBiquadFilter();f.type='lowpass';f.frequency.value=200;
    engineOsc.connect(f);f.connect(engineGain);engineOsc.start();
  }catch(e){}
}
function playChime(){
  if(!audioCtx)return;
  try{
    [880,1100].forEach((freq,i)=>setTimeout(()=>{
      const o=audioCtx.createOscillator(),g=audioCtx.createGain();
      o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';
      g.gain.setValueAtTime(0.15,audioCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.5);
      o.start();o.stop(audioCtx.currentTime+0.5);
    },i*110));
  }catch(e){}
}
function playOpen(){
  if(!audioCtx)return;
  try{
    [440,554,660].forEach((freq,i)=>setTimeout(()=>{
      const o=audioCtx.createOscillator(),g=audioCtx.createGain();
      o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';
      g.gain.setValueAtTime(0.09,audioCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.28);
      o.start();o.stop(audioCtx.currentTime+0.28);
    },i*75));
  }catch(e){}
}

// ════════════════════════════════════
//  MAIN LOOP  (car speed reduced)
// ════════════════════════════════════
const ACCEL=0.038,FRIC=0.88,MAX_SPD=0.36,TURN=0.034;

function loop(){
  requestAnimationFrame(loop);frame++;clock.getDelta();

  if(!modalOpen){
    const U=keys['ArrowUp']  ||keys['w']||keys['W']||dpadState.up;
    const D=keys['ArrowDown'] ||keys['s']||keys['S']||dpadState.down;
    const L=keys['ArrowLeft'] ||keys['a']||keys['A']||dpadState.left;
    const R=keys['ArrowRight']||keys['d']||keys['D']||dpadState.right;

    if(U)carSpeed=Math.min(carSpeed+ACCEL,MAX_SPD);
    else if(D)carSpeed=Math.max(carSpeed-ACCEL,-MAX_SPD*.5);
    else carSpeed*=FRIC;

    if(Math.abs(carSpeed)>.004){
      const dir=carSpeed>0?1:-1;
      if(L)carAngle+=TURN*dir;if(R)carAngle-=TURN*dir;
    }

    const nx=carPos.x+Math.sin(carAngle)*carSpeed;
    const nz=carPos.z+Math.cos(carAngle)*carSpeed;
    let blocked=false;
    const pt=new THREE.Vector2(nx,nz);
    for(const b of buildings){if(b.bbox.containsPoint(pt)){blocked=true;break;}}
    if(Math.abs(nx)>CITY_H-2||Math.abs(nz)>CITY_H-2)blocked=true;
    if(!blocked){carPos.x=nx;carPos.z=nz;}else{carSpeed*=-.25;}

    carGroup.position.x=carPos.x;carGroup.position.z=carPos.z;carGroup.rotation.y=carAngle;
    carWheels.forEach(wg=>{wg.children[0].rotation.x+=carSpeed*2.2;});

    if(engineOsc&&audioCtx){
      engineOsc.frequency.value=55+Math.abs(carSpeed)/MAX_SPD*80;
      engineGain.gain.value=Math.abs(carSpeed)>.01?.04:0;
    }
  }

  // Third-person follow camera
  const behind=new THREE.Vector3(
    carPos.x-Math.sin(carAngle)*CAM_BACK,CAM_UP,
    carPos.z-Math.cos(carAngle)*CAM_BACK
  );
  camPos.lerp(behind,CAM_LAG);
  camera.position.copy(camPos);
  camera.lookAt(carPos.x+Math.sin(carAngle)*4,1.2,carPos.z+Math.cos(carAngle)*4);

  // Entrance detection + glow
  nearEntry=null;let bestD=9999;
  buildings.forEach(b=>{
    const dx=carPos.x-b.entranceWorld.x,dz=carPos.z-b.entranceWorld.z;
    const d=Math.sqrt(dx*dx+dz*dz);
    const pulse=Math.abs(Math.sin(frame*.07));
    if(d<3.5){
      b.eMat.opacity=.48+pulse*.32;b.eLight.intensity=2.0+pulse*1.2;
      if(d<bestD){nearEntry=b;bestD=d;}
    }else if(d<9){
      const t=1-(d-3.5)/5.5;b.eMat.opacity=.12+t*.12;b.eLight.intensity=t*.4;
    }else{b.eMat.opacity=.08;b.eLight.intensity=0;}
  });

  if(nearEntry&&nearEntry!==lastNearEntry)playChime();
  lastNearEntry=nearEntry;

  // Particles
  buildings.forEach(b=>{
    const isN=nearEntry===b;
    if(!b.particleGroup)return;
    b.particleGroup.children.forEach(mesh=>{
      const ud=mesh.userData;if(!ud.speed)return;
      ud.baseAngle+=ud.speed;
      mesh.position.x=Math.cos(ud.baseAngle)*ud.radius;
      mesh.position.z=Math.sin(ud.baseAngle)*ud.radius;
      mesh.position.y=ud.yBase+Math.sin(frame*ud.ySpeed+ud.phase)*ud.yAmp;
      mesh.rotation.x+=0.02;mesh.rotation.y+=0.015;
      const tgt=isN?.75:.15;
      mesh.material.opacity+=(tgt-mesh.material.opacity)*.05;
    });
  });

  // HUD
  document.getElementById('spd-fill').style.width=(Math.abs(carSpeed)/MAX_SPD*100).toFixed(0)+'%';
  const pEl=document.getElementById('hud-proj'),eEl=document.getElementById('hud-enter');
  if(nearEntry){
    pEl.innerHTML='<span style="color:'+nearEntry.distHex+'">'+nearEntry.project.name+'</span>';
    eEl.style.display='block';
  }else{pEl.textContent='Navigate to a project entrance';eEl.style.display='none';}
  document.getElementById('hud-visited').textContent=visitedSet.size+' / 18 explored';

  drawMinimap();renderer.render(scene,camera);
}

// ════════════════════════════════════
//  MINIMAP
// ════════════════════════════════════
function drawMinimap(){
  const mw=140,mh=140;mmCtx.fillStyle='#04080f';mmCtx.fillRect(0,0,mw,mh);
  const scale=mw/(CITY_H*2),ox=mw/2,oz=mh/2;
  buildings.forEach(b=>{
    const px=ox+b.entranceWorld.x*scale,pz=oz+b.entranceWorld.z*scale;
    const isN=b===nearEntry,isV=b.visited;
    mmCtx.globalAlpha=isN?1:isV?.55:.38;
    mmCtx.fillStyle=isV?'#3ecf8e':b.distHex;
    mmCtx.beginPath();mmCtx.arc(px,pz,isN?5:2.8,0,Math.PI*2);mmCtx.fill();
    if(isV){mmCtx.strokeStyle='#3ecf8e';mmCtx.lineWidth=1;mmCtx.beginPath();mmCtx.arc(px,pz,4.5,0,Math.PI*2);mmCtx.stroke();}
    mmCtx.globalAlpha=1;
  });
  const cpx=ox+carPos.x*scale,cpz=oz+carPos.z*scale;
  mmCtx.save();mmCtx.translate(cpx,cpz);mmCtx.rotate(-carAngle);
  mmCtx.fillStyle='#ffffff';mmCtx.beginPath();
  mmCtx.moveTo(0,-5.5);mmCtx.lineTo(3.2,4);mmCtx.lineTo(0,2);mmCtx.lineTo(-3.2,4);
  mmCtx.closePath();mmCtx.fill();mmCtx.restore();
  mmCtx.strokeStyle='rgba(74,144,217,.14)';mmCtx.lineWidth=1;mmCtx.strokeRect(0,0,mw,mh);
}

// ════════════════════════════════════
//  MODAL
// ════════════════════════════════════
function openModal(b){
  modalOpen=true;
  if(!b.visited){b.visited=true;visitedSet.add(b.project.name);}
  const p=b.project,dist=DISTRICTS[p.district];
  document.getElementById('mo-ico').textContent=p.icon;
  document.getElementById('mo-ico').style.cssText='background:'+dist.hex+'18;border:1px solid '+dist.hex+'30;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0';
  const ce=document.getElementById('mo-cat');ce.textContent=p.cat;ce.style.color=dist.hex;
  document.getElementById('mo-name').textContent=p.name;
  document.getElementById('mo-stack').textContent=p.stack;
  const de=document.getElementById('mo-dist');
  de.textContent=dist.name;de.style.cssText='background:'+dist.hex+'18;color:'+dist.hex+';border:1px solid '+dist.hex+'30;display:inline-block;font-size:9px;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px';
  document.getElementById('mo-desc').textContent=p.desc;
  document.getElementById('mo-tags').innerHTML=p.tags.map(t=>'<span class="mo-tag">'+t+'</span>').join('');
  let btns='';
  if(p.gh)   btns+='<a class="mo-gh"   href="'+p.gh+'"   target="_blank">View on GitHub</a>';
  if(p.live) btns+='<a class="mo-live" href="'+p.live+'" target="_blank">Live Demo →</a>';
  if(!p.gh&&!p.live)btns='<span style="font-size:11px;color:#2e4058">No live link available</span>';
  document.getElementById('mo-btns').innerHTML=btns;
  document.getElementById('ov').style.display='flex';
  playOpen();
}
function closeModal(){document.getElementById('ov').style.display='none';modalOpen=false;}
document.getElementById('ov').addEventListener('click',e=>{if(e.target===document.getElementById('ov'))closeModal();});

// ════════════════════════════════════
//  INPUT + DPAD
// ════════════════════════════════════
function bindInput(){
  document.addEventListener('keydown',e=>{
    keys[e.key]=true;
    if((e.key==='Enter'||e.key===' ')&&nearEntry&&!modalOpen){e.preventDefault();openModal(nearEntry);}
    if(e.key==='Escape'&&modalOpen)closeModal();
    if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();
  });
  document.addEventListener('keyup',e=>{keys[e.key]=false;});

  [['dp-u','up'],['dp-d','down'],['dp-l','left'],['dp-r','right']].forEach(([id,dir])=>{
    const el=document.getElementById(id);
    const on=()=>{dpadState[dir]=1;el.classList.add('on');if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();};
    const off=()=>{dpadState[dir]=0;el.classList.remove('on');};
    el.addEventListener('pointerdown',e=>{e.preventDefault();on();});
    el.addEventListener('pointerup',off);el.addEventListener('pointerleave',off);
  });
}

// ════════════════════════════════════
//  TOAST
// ════════════════════════════════════
function showToast(msg){
  const s=document.createElement('style');
  s.textContent='@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}10%,75%{opacity:1;transform:translateX(-50%)}100%{opacity:0}}';
  document.head.appendChild(s);
  const t=document.createElement('div');
  t.style.cssText='position:fixed;top:18px;left:50%;transform:translateX(-50%);background:#4a90d9;color:#fff;border-radius:8px;padding:8px 20px;font-size:11px;font-weight:600;z-index:300;animation:tf 3.2s ease forwards;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap';
  t.textContent=msg;document.body.appendChild(t);setTimeout(()=>t.remove(),3300);
}
</script>
</body>
</html>"""

components.html(HTML, height=760, scrolling=False)
