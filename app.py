import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MKP | Portfolio Drive",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; }
    [data-testid="stAppViewContainer"] { background: #0d1117; }
</style>
""", unsafe_allow_html=True)

GAME_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 100%; height: 100%; overflow: hidden; background: #0d1117; font-family: 'Segoe UI', system-ui, sans-serif; }

#intro {
  position: fixed; inset: 0; background: #0d1117;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  z-index: 200; gap: 0;
}
.intro-title {
  font-size: 52px; font-weight: 700; letter-spacing: -1px;
  background: linear-gradient(135deg, #378add, #7f77dd, #1d9e75);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
}
.intro-sub {
  font-size: 16px; color: #7a8899; margin-bottom: 6px;
}
.intro-role {
  font-size: 13px; color: #378add; background: rgba(55,138,221,0.1);
  border: 1px solid rgba(55,138,221,0.2); border-radius: 20px;
  padding: 4px 14px; margin-bottom: 40px;
}
.intro-car { font-size: 64px; margin-bottom: 20px; animation: bounce 1s ease-in-out infinite; }
@keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
.intro-instructions {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;
  max-width: 520px; width: 90%; margin-bottom: 36px;
}
.intro-card {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px; padding: 14px; text-align: center;
}
.intro-card .icon { font-size: 22px; margin-bottom: 6px; }
.intro-card .label { font-size: 11px; color: #8b949e; line-height: 1.4; }
.start-btn {
  background: linear-gradient(135deg, #378add, #7f77dd);
  border: none; border-radius: 12px; color: #fff;
  font-size: 16px; font-weight: 600; padding: 14px 48px;
  cursor: pointer; letter-spacing: 0.5px;
  transition: transform 0.15s, box-shadow 0.15s;
  box-shadow: 0 4px 24px rgba(55,138,221,0.35);
}
.start-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(55,138,221,0.5); }

canvas { display: block; }

#hud {
  position: fixed; top: 16px; left: 16px;
  background: rgba(13,17,23,0.92); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 12px 16px; z-index: 50; min-width: 180px;
  backdrop-filter: blur(12px);
}
.hud-name { font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 2px; }
.hud-role { font-size: 11px; color: #378add; margin-bottom: 10px; }
.hud-sep { height: 1px; background: rgba(255,255,255,0.06); margin-bottom: 10px; }
.hud-speed-label { font-size: 10px; color: #5a6370; margin-bottom: 4px; }
.hud-speed-bar { height: 4px; background: rgba(255,255,255,0.08); border-radius: 2px; overflow: hidden; }
.hud-speed-fill { height: 100%; background: linear-gradient(90deg, #1d9e75, #378add); border-radius: 2px; transition: width 0.1s; }
.hud-nearby { margin-top: 10px; font-size: 11px; color: #8b949e; }
.hud-nearby span { color: #ffe066; }

#minimap-wrap {
  position: fixed; bottom: 16px; right: 16px;
  background: rgba(13,17,23,0.92); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 10px; z-index: 50;
  backdrop-filter: blur(12px);
}
.minimap-label { font-size: 9px; color: #5a6370; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; text-align:center; }

#controls-hint {
  position: fixed; bottom: 16px; left: 16px;
  background: rgba(13,17,23,0.85); border: 1px solid rgba(255,255,255,0.06);
  border-radius: 10px; padding: 8px 14px; z-index: 50;
  font-size: 11px; color: #5a6370;
}

#modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.7);
  display: none; align-items: center; justify-content: center; z-index: 100;
  backdrop-filter: blur(6px);
}
#modal {
  background: #161b22; border: 1px solid rgba(255,255,255,0.1);
  border-radius: 20px; padding: 28px; max-width: 420px; width: 90%;
  animation: slideUp 0.25s ease;
}
@keyframes slideUp { from{transform:translateY(20px);opacity:0} to{transform:translateY(0);opacity:1} }
.modal-header { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 16px; }
.modal-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
.modal-title { font-size: 18px; font-weight: 600; color: #fff; margin-bottom: 4px; }
.modal-lang { font-size: 11px; padding: 2px 10px; border-radius: 20px; display: inline-block; }
.modal-desc { font-size: 13px; color: #8b949e; line-height: 1.65; margin-bottom: 18px; }
.modal-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 18px; }
.modal-tag { font-size: 11px; color: #7a8899; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 3px 10px; }
.modal-stats { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-bottom: 20px; }
.modal-stat { background: rgba(255,255,255,0.04); border-radius: 10px; padding: 10px; text-align: center; }
.modal-stat .sv { font-size: 18px; font-weight: 600; color: #fff; }
.modal-stat .sl { font-size: 10px; color: #5a6370; margin-top: 2px; }
.modal-btns { display: flex; gap: 10px; }
.btn-gh { flex: 1; padding: 10px; border-radius: 10px; font-size: 13px; font-weight: 500; text-align: center; text-decoration: none; background: rgba(255,255,255,0.06); color: #e6f1fb; border: 1px solid rgba(255,255,255,0.1); cursor: pointer; transition: background 0.15s; display: block; }
.btn-gh:hover { background: rgba(255,255,255,0.1); }
.btn-live { flex: 1; padding: 10px; border-radius: 10px; font-size: 13px; font-weight: 600; text-align: center; text-decoration: none; background: linear-gradient(135deg, #378add, #7f77dd); color: #fff; border: none; cursor: pointer; display: block; transition: opacity 0.15s; }
.btn-live:hover { opacity: 0.88; }
.btn-close { width: 36px; height: 36px; border-radius: 8px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.08); color: #8b949e; font-size: 18px; cursor: pointer; display: flex; align-items: center; justify-content: center; position: absolute; top: 16px; right: 16px; }
.btn-close:hover { background: rgba(255,255,255,0.1); color: #fff; }

#dpad {
  position: fixed; right: 16px; bottom: 140px; z-index: 50;
  display: grid; grid-template-areas: ". u ." "l . r" ". d .";
  grid-template-columns: repeat(3, 44px); grid-template-rows: repeat(3, 44px); gap: 4px;
}
.dp { background: rgba(20,26,36,0.92); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; color: #e6f1fb; cursor: pointer; user-select: none; -webkit-user-select: none; touch-action: none; transition: background 0.1s; }
.dp:active, .dp.pressed { background: rgba(55,138,221,0.4); border-color: #378add; }
#dp-u { grid-area: u; } #dp-l { grid-area: l; } #dp-r { grid-area: r; } #dp-d { grid-area: d; }

.toast {
  position: fixed; top: 16px; left: 50%; transform: translateX(-50%);
  background: rgba(29,158,117,0.9); color: #fff; border-radius: 20px;
  padding: 8px 20px; font-size: 13px; font-weight: 500; z-index: 150;
  animation: fadeInOut 2.5s ease forwards;
}
@keyframes fadeInOut { 0%{opacity:0;transform:translateX(-50%) translateY(-10px)} 15%,75%{opacity:1;transform:translateX(-50%) translateY(0)} 100%{opacity:0} }
</style>
</head>
<body>

<div id="intro">
  <div class="intro-car">🚗</div>
  <div class="intro-title">Portfolio Drive</div>
  <div class="intro-sub">Mustafa Kazi Pasha · Data Scientist & AI Engineer</div>
  <div class="intro-role">🤖 ML · AI Agents · Analytics · Streamlit</div>
  <div class="intro-instructions">
    <div class="intro-card"><div class="icon">🎮</div><div class="label">WASD or Arrow keys to drive</div></div>
    <div class="intro-card"><div class="icon">🏢</div><div class="label">Pull up to a glowing building</div></div>
    <div class="intro-card"><div class="icon">⏎</div><div class="label">Press Enter or Space to open</div></div>
  </div>
  <button class="start-btn" onclick="startGame()">Start Driving →</button>
</div>

<canvas id="c"></canvas>

<div id="hud" style="display:none">
  <div class="hud-name">Mustafa Kazi Pasha</div>
  <div class="hud-role">Data Scientist & AI Engineer</div>
  <div class="hud-sep"></div>
  <div class="hud-speed-label">SPEED</div>
  <div class="hud-speed-bar"><div class="hud-speed-fill" id="speed-fill" style="width:0%"></div></div>
  <div class="hud-nearby" id="hud-nearby">Drive to a glowing building</div>
</div>

<div id="minimap-wrap" style="display:none">
  <div class="minimap-label">City Map</div>
  <canvas id="mini" width="110" height="110"></canvas>
</div>

<div id="controls-hint" style="display:none">WASD / ↑↓←→ · Mobile: D-pad</div>

<div id="modal-overlay">
  <div id="modal" style="position:relative">
    <button class="btn-close" onclick="closeModal()">×</button>
    <div class="modal-header">
      <div class="modal-icon" id="m-icon"></div>
      <div>
        <div class="modal-title" id="m-title"></div>
        <div class="modal-lang" id="m-lang"></div>
      </div>
    </div>
    <div class="modal-desc" id="m-desc"></div>
    <div class="modal-tags" id="m-tags"></div>
    <div class="modal-stats">
      <div class="modal-stat"><div class="sv" id="m-stars">–</div><div class="sl">⭐ Stars</div></div>
      <div class="modal-stat"><div class="sv" id="m-lang2">–</div><div class="sl">Language</div></div>
      <div class="modal-stat"><div class="sv" id="m-status">Live</div><div class="sl">Status</div></div>
    </div>
    <div class="modal-btns">
      <a class="btn-gh" id="m-gh" href="#" target="_blank">⑂ GitHub Repo</a>
      <a class="btn-live" id="m-live" href="#" target="_blank">🚀 Live Demo</a>
    </div>
  </div>
</div>

<div id="dpad" style="display:none">
  <div class="dp" id="dp-u">↑</div>
  <div class="dp" id="dp-l">←</div>
  <div class="dp" id="dp-r">→</div>
  <div class="dp" id="dp-d">↓</div>
</div>

<script>
const PROJECTS = [
  {
    name: "Retail Intelligence Platform",
    icon: "🛒", color: "#1d9e75", langColor: "rgba(29,158,117,0.15)", textColor: "#1d9e75",
    lang: "Python", stars: 12,
    desc: "End-to-end retail analytics platform with AI-powered demand forecasting, customer segmentation, inventory optimization, and real-time sales dashboards. Built with multi-page Streamlit architecture.",
    tags: ["Streamlit", "Machine Learning", "Forecasting", "Retail Analytics", "AI"],
    github: "https://github.com/Mkp-7/Retail-Intelligence-Platform",
    live: "https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"
  },
  {
    name: "Revenue Management Agent",
    icon: "💰", color: "#378add", langColor: "rgba(55,138,221,0.15)", textColor: "#378add",
    lang: "Python", stars: 9,
    desc: "AI-powered revenue management system using autonomous agents for dynamic pricing, yield optimization, and revenue forecasting. Integrates LLM-based decision making for hospitality and travel industries.",
    tags: ["AI Agents", "LLM", "Dynamic Pricing", "Revenue Ops", "Streamlit"],
    github: "https://github.com/Mkp-7/Revenue-Management-Agent",
    live: "https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"
  },
  {
    name: "EcoRoute Optimizer",
    icon: "🌿", color: "#639922", langColor: "rgba(99,153,34,0.15)", textColor: "#639922",
    lang: "Python", stars: 7,
    desc: "Sustainable logistics platform that optimizes delivery routes to minimize carbon emissions. Uses OR-Tools and genetic algorithms with real-time traffic integration and environmental impact scoring.",
    tags: ["OR-Tools", "Optimization", "Sustainability", "Logistics", "Routing"],
    github: "https://github.com/Mkp-7/EcoRoute-Optimizer",
    live: "https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"
  },
  {
    name: "AI Pricing Agent",
    icon: "🤖", color: "#7f77dd", langColor: "rgba(127,119,221,0.15)", textColor: "#7f77dd",
    lang: "Python", stars: 15,
    desc: "Autonomous AI agent for competitive price intelligence. Monitors competitor pricing in real-time, runs ML models to recommend optimal prices, and automates repricing decisions with explainable AI.",
    tags: ["AI Agent", "Pricing Strategy", "NLP", "Explainable AI", "Automation"],
    github: "https://github.com/Mkp-7/AI-Pricing-Agent",
    live: "https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"
  },
  {
    name: "Banking Risk Analytics",
    icon: "🏦", color: "#d85a30", langColor: "rgba(216,90,48,0.15)", textColor: "#d85a30",
    lang: "Python", stars: 11,
    desc: "Comprehensive banking risk intelligence platform covering credit risk, market risk, and operational risk. Features stress testing, PD/LGD/EAD modeling, and regulatory capital calculations (Basel III).",
    tags: ["Risk Modeling", "Basel III", "Credit Risk", "Finance", "ML"],
    github: "https://github.com/Mkp-7/Banking-Risk-Analytics",
    live: "https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"
  },
  {
    name: "MedMedia Analytics",
    icon: "🏥", color: "#d4537e", langColor: "rgba(212,83,126,0.15)", textColor: "#d4537e",
    lang: "Python", stars: 8,
    desc: "Healthcare media analytics platform analyzing pharmaceutical marketing effectiveness, patient engagement, and HCP outreach. Combines NLP sentiment analysis with multi-channel attribution modeling.",
    tags: ["Healthcare", "NLP", "Sentiment Analysis", "Marketing Analytics", "Pharma"],
    github: "https://github.com/Mkp-7/MedMedia-Analytics",
    live: "https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"
  }
];

const W = 1400, H = 1400;
const ROAD_COLOR = '#161d2a';
const ROAD_LINE = '#1e2a3d';
const GROUND = '#0f1520';
const SIDEWALK = '#131924';

const ROAD_LAYOUT = [
  {x:0, y:430, w:W, h:90},
  {x:0, y:880, w:W, h:90},
  {x:430, y:0, w:90, h:H},
  {x:880, y:0, w:90, h:H},
];

const BUILDING_SLOTS = [
  {x:215, y:215}, {x:655, y:215}, {x:1185, y:215},
  {x:215, y:655}, {x:1185, y:655},
  {x:215, y:1185}, {x:655, y:1185}, {x:1185, y:1185},
  // center district
  {x:655, y:655},
];

let buildings = [];
let car = {x:700, y:700, angle:0, speed:0};
let cam = {x:700, y:700};
let keys = {};
let dpad = {up:false,down:false,left:false,right:false};
let near = null, modal = false, animId = null;
let canvas, ctx, mini, mctx;
let particles = [], stars = [];
let frame = 0;

function initStars() {
  for (let i = 0; i < 120; i++) {
    stars.push({x: Math.random()*W, y: Math.random()*H, r: Math.random()*1.5+0.5, a: Math.random()});
  }
}

function placeBuildings() {
  buildings = PROJECTS.map((p, i) => {
    const slot = BUILDING_SLOTS[i];
    return { ...p, x: slot.x, y: slot.y, w: 110, h: 110, lit: Array.from({length:15}, ()=>Math.random()>0.35) };
  });
}

function startGame() {
  document.getElementById('intro').style.display = 'none';
  document.getElementById('hud').style.display = 'block';
  document.getElementById('minimap-wrap').style.display = 'block';
  document.getElementById('controls-hint').style.display = 'block';
  document.getElementById('dpad').style.display = 'grid';
  canvas = document.getElementById('c');
  ctx = canvas.getContext('2d');
  mini = document.getElementById('mini');
  mctx = mini.getContext('2d');
  resize();
  window.addEventListener('resize', resize);
  placeBuildings();
  initStars();
  bindInput();
  loop();
  showToast("Welcome! Drive to a glowing building 🏢");
}

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

function drawGround() {
  ctx.fillStyle = GROUND;
  ctx.fillRect(0, 0, W, H);

  // decorative grid
  ctx.strokeStyle = 'rgba(30,42,61,0.4)';
  ctx.lineWidth = 0.5;
  for (let x = 0; x < W; x += 80) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
  }
  for (let y = 0; y < H; y += 80) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
  }

  // ambient stars (decorative ground marks)
  stars.forEach(s => {
    ctx.globalAlpha = s.a * 0.3;
    ctx.fillStyle = '#378add';
    ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill();
  });
  ctx.globalAlpha = 1;
}

function drawRoads() {
  ROAD_LAYOUT.forEach(r => {
    ctx.fillStyle = ROAD_COLOR;
    ctx.fillRect(r.x, r.y, r.w, r.h);
  });

  // dashes
  ctx.setLineDash([28, 18]);
  ctx.strokeStyle = ROAD_LINE;
  ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(0, 475); ctx.lineTo(W, 475); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0, 925); ctx.lineTo(W, 925); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(475, 0); ctx.lineTo(475, H); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(925, 0); ctx.lineTo(925, H); ctx.stroke();
  ctx.setLineDash([]);

  // intersection fills
  [[430,430,90,90],[430,880,90,90],[880,430,90,90],[880,880,90,90]].forEach(([x,y,w,h]) => {
    ctx.fillStyle = '#1a2133';
    ctx.fillRect(x, y, w, h);
  });
}

function drawBuilding(b) {
  const bx = b.x - b.w/2, by = b.y - b.h/2;
  const isNear = near === b;
  const pulse = isNear ? Math.sin(frame * 0.07) * 0.4 + 0.6 : 1;

  // sidewalk pad
  ctx.fillStyle = SIDEWALK;
  ctx.beginPath(); ctx.roundRect(bx - 12, by - 12, b.w + 24, b.h + 24, 8); ctx.fill();

  // glow
  if (isNear) {
    ctx.shadowColor = b.color;
    ctx.shadowBlur = 28 * pulse;
  }

  // main body
  ctx.fillStyle = isNear ? b.color : adjustColor(b.color, -60);
  ctx.beginPath(); ctx.roundRect(bx, by, b.w, b.h, 10); ctx.fill();
  ctx.shadowBlur = 0;

  // top accent bar
  ctx.fillStyle = b.color;
  ctx.globalAlpha = 0.6;
  ctx.beginPath(); ctx.roundRect(bx, by, b.w, 14, [10,10,0,0]); ctx.fill();
  ctx.globalAlpha = 1;

  // windows
  const cols = 4, rows = 4;
  const ww = 12, wh = 9, px = 12, py = 20;
  const sx = (b.w - px*2 - ww*(cols)) / (cols-1);
  const sy = (b.h - py - 12 - wh*(rows)) / (rows-1);
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const wx = bx + px + c*(ww+sx);
      const wy = by + py + r*(wh+sy);
      const lit = b.lit[r*cols+c];
      ctx.fillStyle = lit ? '#ffe877' : 'rgba(130,190,255,0.15)';
      ctx.globalAlpha = lit ? (isNear ? 1 : 0.8) : 0.4;
      ctx.fillRect(wx, wy, ww, wh);
      ctx.globalAlpha = 1;
    }
  }

  // icon
  ctx.font = '20px serif';
  ctx.textAlign = 'center';
  ctx.fillText(b.icon, b.x, by - 16);

  // label
  ctx.font = `${isNear ? '600' : '500'} 11px system-ui`;
  ctx.fillStyle = isNear ? '#fff' : 'rgba(200,210,225,0.75)';
  ctx.fillText(b.name.length > 18 ? b.name.slice(0,18)+'…' : b.name, b.x, by + b.h + 20);

  // enter prompt
  if (isNear) {
    ctx.font = '700 10px system-ui';
    ctx.fillStyle = '#ffe066';
    ctx.globalAlpha = pulse;
    ctx.fillText('▶ PRESS ENTER', b.x, by - 30);
    ctx.globalAlpha = 1;
  }
}

function adjustColor(hex, amt) {
  const n = parseInt(hex.slice(1), 16);
  const r = Math.max(0, Math.min(255, (n>>16) + amt));
  const g = Math.max(0, Math.min(255, ((n>>8)&0xff) + amt));
  const b2 = Math.max(0, Math.min(255, (n&0xff) + amt));
  return `rgb(${r},${g},${b2})`;
}

function drawCar() {
  const cw = 24, ch = 38;
  ctx.save();
  ctx.translate(car.x, car.y);
  ctx.rotate(car.angle);

  // shadow
  ctx.fillStyle = 'rgba(0,0,0,0.3)';
  ctx.beginPath(); ctx.ellipse(2, 4, cw/2+4, ch/4+2, 0, 0, Math.PI*2); ctx.fill();

  // body
  ctx.fillStyle = '#f1c40f';
  ctx.beginPath(); ctx.roundRect(-cw/2, -ch/2, cw, ch, 6); ctx.fill();

  // roof/windshield
  ctx.fillStyle = '#e67e22';
  ctx.fillRect(-cw/2, -ch/2, cw, 10);
  ctx.fillStyle = 'rgba(160,230,255,0.7)';
  ctx.fillRect(-cw/2+3, -ch/2+2, cw-6, 7);

  // headlights
  ctx.fillStyle = 'rgba(255,245,180,0.95)';
  ctx.fillRect(-cw/2+2, -ch/2+1, 5, 4);
  ctx.fillRect(cw/2-7, -ch/2+1, 5, 4);

  // taillights
  ctx.fillStyle = '#e74c3c';
  ctx.fillRect(-cw/2+2, ch/2-6, 5, 4);
  ctx.fillRect(cw/2-7, ch/2-6, 5, 4);

  // speed lines when fast
  if (Math.abs(car.speed) > 3) {
    ctx.strokeStyle = 'rgba(255,255,255,0.15)';
    ctx.lineWidth = 1;
    for (let i = 0; i < 4; i++) {
      const lx = (-cw/2 + 4) + i * 6;
      ctx.beginPath(); ctx.moveTo(lx, ch/2); ctx.lineTo(lx - 2, ch/2 + 12); ctx.stroke();
    }
  }
  ctx.restore();

  // exhaust particles
  if (Math.abs(car.speed) > 1 && frame % 3 === 0) {
    const px = car.x - Math.sin(car.angle) * 20 + (Math.random()-0.5)*6;
    const py = car.y + Math.cos(car.angle) * 20 + (Math.random()-0.5)*6;
    particles.push({x:px, y:py, vx:(Math.random()-0.5)*0.4, vy:(Math.random()-0.5)*0.4, life:1, r:3});
  }
}

function drawParticles() {
  particles = particles.filter(p => p.life > 0);
  particles.forEach(p => {
    ctx.globalAlpha = p.life * 0.4;
    ctx.fillStyle = '#aaa';
    ctx.beginPath(); ctx.arc(p.x, p.y, p.r * p.life, 0, Math.PI*2); ctx.fill();
    p.x += p.vx; p.y += p.vy; p.life -= 0.06;
  });
  ctx.globalAlpha = 1;
}

function drawMini() {
  const s = 110 / W;
  mctx.fillStyle = '#0a0f18';
  mctx.fillRect(0, 0, 110, 110);
  mctx.fillStyle = '#1a2235';
  ROAD_LAYOUT.forEach(r => mctx.fillRect(r.x*s, r.y*s, r.w*s, r.h*s));
  buildings.forEach(b => {
    mctx.fillStyle = b.color;
    mctx.beginPath(); mctx.arc(b.x*s, b.y*s, 4, 0, Math.PI*2); mctx.fill();
  });
  mctx.fillStyle = '#f1c40f';
  mctx.beginPath(); mctx.arc(car.x*s, car.y*s, 4, 0, Math.PI*2); mctx.fill();

  // viewport rect
  const vw = (canvas.width / W) * 110;
  const vh = (canvas.height / H) * 110;
  const vx = ((cam.x - canvas.width/2) / W) * 110;
  const vy = ((cam.y - canvas.height/2) / H) * 110;
  mctx.strokeStyle = 'rgba(255,255,255,0.2)';
  mctx.lineWidth = 1;
  mctx.strokeRect(Math.max(0,vx), Math.max(0,vy), Math.min(110,vw), Math.min(110,vh));
}

const ACCEL = 0.25, FRICTION = 0.87, MAX_SPD = 6.5, TURN = 0.055;

function update() {
  if (modal) return;
  frame++;
  const up = keys['ArrowUp']||keys['w']||keys['W']||dpad.up;
  const dn = keys['ArrowDown']||keys['s']||keys['S']||dpad.down;
  const lt = keys['ArrowLeft']||keys['a']||keys['A']||dpad.left;
  const rt = keys['ArrowRight']||keys['d']||keys['D']||dpad.right;

  if (up) car.speed = Math.min(car.speed + ACCEL, MAX_SPD);
  else if (dn) car.speed = Math.max(car.speed - ACCEL, -MAX_SPD * 0.5);
  else car.speed *= FRICTION;

  if (Math.abs(car.speed) > 0.15) {
    const dir = car.speed > 0 ? 1 : -1;
    if (lt) car.angle -= TURN * dir;
    if (rt) car.angle += TURN * dir;
  }

  car.x += Math.sin(car.angle) * car.speed;
  car.y -= Math.cos(car.angle) * car.speed;
  car.x = Math.max(24, Math.min(W-24, car.x));
  car.y = Math.max(24, Math.min(H-24, car.y));

  cam.x += (car.x - cam.x) * 0.1;
  cam.y += (car.y - cam.y) * 0.1;

  near = null;
  for (const b of buildings) {
    const dx = car.x - b.x, dy = car.y - b.y;
    if (Math.sqrt(dx*dx+dy*dy) < 85) { near = b; break; }
  }

  const fill = (Math.abs(car.speed)/MAX_SPD*100).toFixed(0);
  document.getElementById('speed-fill').style.width = fill + '%';
  document.getElementById('hud-nearby').innerHTML = near
    ? `Near: <span>${near.name}</span>`
    : 'Drive to a glowing building';
}

function render() {
  const cw = canvas.width, ch = canvas.height;
  ctx.clearRect(0, 0, cw, ch);
  ctx.save();
  ctx.translate(-cam.x + cw/2, -cam.y + ch/2);
  drawGround();
  drawRoads();
  drawParticles();
  buildings.forEach(drawBuilding);
  drawCar();
  ctx.restore();
  drawMini();
}

function loop() {
  update();
  render();
  animId = requestAnimationFrame(loop);
}

function openModal(b) {
  modal = true;
  document.getElementById('m-icon').textContent = b.icon;
  document.getElementById('m-icon').style.background = b.langColor;
  document.getElementById('m-title').textContent = b.name;
  document.getElementById('m-lang').textContent = b.lang;
  document.getElementById('m-lang').style.background = b.langColor;
  document.getElementById('m-lang').style.color = b.textColor;
  document.getElementById('m-lang').style.border = `1px solid ${b.color}44`;
  document.getElementById('m-desc').textContent = b.desc;
  document.getElementById('m-tags').innerHTML = b.tags.map(t => `<span class="modal-tag">${t}</span>`).join('');
  document.getElementById('m-stars').textContent = b.stars;
  document.getElementById('m-lang2').textContent = b.lang;
  document.getElementById('m-gh').href = b.github;
  document.getElementById('m-live').href = b.live;
  document.getElementById('modal-overlay').style.display = 'flex';
}

function closeModal() {
  document.getElementById('modal-overlay').style.display = 'none';
  modal = false;
}

function showToast(msg) {
  const t = document.createElement('div');
  t.className = 'toast'; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 2600);
}

document.addEventListener('keydown', e => {
  keys[e.key] = true;
  if ((e.key === 'Enter' || e.key === ' ') && near && !modal) openModal(near);
  if (e.key === 'Escape' && modal) closeModal();
});
document.addEventListener('keyup', e => { keys[e.key] = false; });

document.getElementById('modal-overlay').addEventListener('click', e => {
  if (e.target === document.getElementById('modal-overlay')) closeModal();
});

function bindDpad(id, dir) {
  const el = document.getElementById(id);
  const on = () => dpad[dir] = true;
  const off = () => dpad[dir] = false;
  el.addEventListener('pointerdown', e => { e.preventDefault(); on(); el.classList.add('pressed'); });
  el.addEventListener('pointerup', () => { off(); el.classList.remove('pressed'); });
  el.addEventListener('pointerleave', () => { off(); el.classList.remove('pressed'); });
}
bindDpad('dp-u','up'); bindDpad('dp-d','down');
bindDpad('dp-l','left'); bindDpad('dp-r','right');
</script>
</body>
</html>
"""

components.html(GAME_HTML, height=700, scrolling=False)

st.markdown("""
<div style="text-align:center; color: #30363d; font-size:12px; margin-top:4px;">
  Built with Streamlit · <a href="https://github.com/Mkp-7" style="color:#378add; text-decoration:none;">github.com/Mkp-7</a>
</div>
""", unsafe_allow_html=True)
