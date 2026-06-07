import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portfolio Drive | Mkp-7",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
[data-testid="stAppViewContainer"] {background: #0a0a0f;}
iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100vh;overflow:hidden;background:#0a0a0f;font-family:'Segoe UI',system-ui,sans-serif}
#intro{position:fixed;inset:0;background:linear-gradient(135deg,#0a0a0f 0%,#0d1a2e 50%,#1a0a1a 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;gap:0}
.title-wrap{text-align:center;margin-bottom:24px}
.game-title{font-size:56px;font-weight:900;letter-spacing:4px;color:#ff6b35;text-transform:uppercase;text-shadow:0 0 40px rgba(255,107,53,.6),0 0 80px rgba(255,107,53,.3);font-style:italic;line-height:1}
.game-sub{font-size:13px;color:#ff6b35;letter-spacing:8px;text-transform:uppercase;margin-top:4px;opacity:.7}
.vc-stripe{width:300px;height:3px;background:linear-gradient(90deg,transparent,#ff6b35,#ff1493,transparent);margin:16px auto}
.name-badge{font-size:18px;font-weight:600;color:#fff;letter-spacing:2px;margin-bottom:4px;text-transform:uppercase}
.role-badge{font-size:11px;color:#ff6b35;letter-spacing:3px;text-transform:uppercase;margin-bottom:32px}
.legend-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:520px;margin-bottom:28px}
.leg{display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.05);border:1px solid rgba(255,107,53,.2);border-radius:6px;padding:5px 11px;font-size:11px;letter-spacing:1px;text-transform:uppercase}
.leg-dot{width:8px;height:8px;border-radius:50%}
.controls-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;max-width:400px;width:90%;margin-bottom:28px}
.ctrl{background:rgba(255,255,255,.04);border:1px solid rgba(255,107,53,.15);border-radius:10px;padding:12px;text-align:center}
.ctrl-icon{font-size:22px;margin-bottom:5px}
.ctrl-txt{font-size:10px;color:#888;letter-spacing:1px;text-transform:uppercase;line-height:1.4}
.start-btn{background:linear-gradient(135deg,#ff6b35,#ff1493);border:none;border-radius:10px;color:#fff;font-size:16px;font-weight:800;padding:14px 52px;cursor:pointer;letter-spacing:3px;text-transform:uppercase;box-shadow:0 4px 30px rgba(255,107,53,.4);transition:transform .15s,box-shadow .15s}
.start-btn:hover{transform:translateY(-3px);box-shadow:0 8px 40px rgba(255,107,53,.6)}
#c{display:block;width:100%;height:100vh}
#hud{position:fixed;top:16px;left:16px;display:none;z-index:50}
.hud-box{background:rgba(0,0,0,.75);border:1px solid rgba(255,107,53,.3);border-radius:10px;padding:12px 16px;backdrop-filter:blur(10px);margin-bottom:8px}
.hud-name{font-size:13px;font-weight:700;color:#ff6b35;letter-spacing:2px;text-transform:uppercase}
.hud-role{font-size:10px;color:#888;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.hud-spd-lbl{font-size:9px;color:#555;letter-spacing:1px;margin-bottom:3px;text-transform:uppercase}
.hud-spd-bar{height:3px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden;margin-bottom:10px}
.hud-spd-fill{height:100%;background:linear-gradient(90deg,#ff6b35,#ff1493);border-radius:2px;transition:width .1s;width:0%}
.hud-near{font-size:10px;color:#888;letter-spacing:.5px}
.hud-near span{color:#ff6b35;font-weight:600}
#minimap-wrap{position:fixed;bottom:16px;right:16px;display:none;z-index:50}
.mm-label{font-size:9px;color:#555;letter-spacing:1px;text-transform:uppercase;text-align:center;margin-bottom:5px}
#minimap{border:1px solid rgba(255,107,53,.3);border-radius:10px}
#hint{position:fixed;bottom:16px;left:16px;display:none;background:rgba(0,0,0,.7);border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:7px 13px;font-size:10px;color:#555;letter-spacing:.5px;z-index:50}
#ov{position:fixed;inset:0;background:rgba(0,0,0,.8);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(10px)}
#mo{background:#0d0d14;border:1px solid rgba(255,107,53,.3);border-radius:18px;padding:28px;max-width:460px;width:92%;position:relative;max-height:88vh;overflow-y:auto;animation:moin .22s ease}
@keyframes moin{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}
.mo-header{display:flex;align-items:flex-start;gap:14px;margin-bottom:14px}
.mo-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;border:1px solid rgba(255,107,53,.2)}
.mo-title{font-size:17px;font-weight:700;color:#fff;margin-bottom:5px;letter-spacing:.5px}
.mo-lang{font-size:10px;padding:3px 10px;border-radius:20px;display:inline-block;letter-spacing:.5px;text-transform:uppercase;margin-bottom:3px}
.mo-cat{font-size:10px;color:#555;letter-spacing:1px;text-transform:uppercase}
.mo-desc{font-size:12px;color:#888;line-height:1.7;margin-bottom:14px}
.mo-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.mo-tag{font-size:10px;color:#888;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);border-radius:5px;padding:2px 9px;letter-spacing:.3px}
.mo-btns{display:flex;gap:8px;flex-wrap:wrap}
.mo-btn-gh{flex:1;min-width:100px;padding:10px;border-radius:9px;font-size:12px;font-weight:600;text-align:center;text-decoration:none;background:rgba(255,255,255,.06);color:#ccc;border:1px solid rgba(255,255,255,.1);cursor:pointer;display:block;transition:background .15s;letter-spacing:.5px}
.mo-btn-gh:hover{background:rgba(255,255,255,.1);color:#fff}
.mo-btn-live{flex:1;min-width:100px;padding:10px;border-radius:9px;font-size:12px;font-weight:700;text-align:center;text-decoration:none;background:linear-gradient(135deg,#ff6b35,#ff1493);color:#fff;border:none;cursor:pointer;display:block;letter-spacing:.5px}
.mo-close{position:absolute;top:14px;right:14px;width:30px;height:30px;border-radius:8px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);color:#666;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.mo-close:hover{color:#fff;background:rgba(255,107,53,.3)}
#dp{position:fixed;right:16px;bottom:140px;z-index:50;display:none;grid-template-areas:'. u .' 'l . r' '. d .';grid-template-columns:repeat(3,44px);grid-template-rows:repeat(3,44px);gap:4px}
.db{background:rgba(0,0,0,.8);border:1px solid rgba(255,107,53,.25);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:18px;color:#888;cursor:pointer;user-select:none;touch-action:none;transition:all .1s}
.db.on,.db:active{background:rgba(255,107,53,.3);border-color:#ff6b35;color:#fff}
#dpu{grid-area:u}#dpd{grid-area:d}#dpl{grid-area:l}#dpr{grid-area:r}
.toast{position:fixed;top:16px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#ff6b35,#ff1493);color:#fff;border-radius:20px;padding:7px 20px;font-size:11px;font-weight:700;z-index:200;animation:tf 2.8s ease forwards;white-space:nowrap;letter-spacing:1px;text-transform:uppercase}
@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-10px)}12%,78%{opacity:1;transform:translateX(-50%) translateY(0)}100%{opacity:0}}
</style>
</head>
<body>

<div id="intro">
  <div class="title-wrap">
    <div class="game-title">Portfolio<br>Drive</div>
    <div class="game-sub">Vice City Edition</div>
  </div>
  <div class="vc-stripe"></div>
  <div class="name-badge">Mkp-7</div>
  <div class="role-badge">Data Scientist &amp; AI Engineer</div>
  <div class="legend-grid">
    <div class="leg"><div class="leg-dot" style="background:#4fc3f7"></div><span style="color:#aaa">Streamlit</span></div>
    <div class="leg"><div class="leg-dot" style="background:#ffb74d"></div><span style="color:#aaa">Tableau</span></div>
    <div class="leg"><div class="leg-dot" style="background:#ef5350"></div><span style="color:#aaa">Power BI</span></div>
    <div class="leg"><div class="leg-dot" style="background:#ab47bc"></div><span style="color:#aaa">ML / Python</span></div>
    <div class="leg"><div class="leg-dot" style="background:#66bb6a"></div><span style="color:#aaa">Looker / dbt</span></div>
  </div>
  <div class="controls-row">
    <div class="ctrl"><div class="ctrl-icon">🎮</div><div class="ctrl-txt">WASD / Arrow keys</div></div>
    <div class="ctrl"><div class="ctrl-icon">🏢</div><div class="ctrl-txt">Drive near buildings</div></div>
    <div class="ctrl"><div class="ctrl-icon">⏎</div><div class="ctrl-txt">Enter / Space to open</div></div>
  </div>
  <button class="start-btn" onclick="startGame()">Start Engine</button>
</div>

<canvas id="c"></canvas>

<div id="hud">
  <div class="hud-box">
    <div class="hud-name">Mkp-7</div>
    <div class="hud-role">Data Scientist &amp; AI Engineer</div>
    <div class="hud-spd-lbl">Speed</div>
    <div class="hud-spd-bar"><div class="hud-spd-fill" id="spd-fill"></div></div>
    <div class="hud-near" id="hud-near">Drive to a building</div>
  </div>
</div>

<div id="minimap-wrap">
  <div class="mm-label">Map</div>
  <canvas id="minimap" width="120" height="120"></canvas>
</div>

<div id="hint">WASD / Arrow Keys &nbsp;·&nbsp; Enter = open project &nbsp;·&nbsp; Esc = close</div>

<div id="ov">
  <div id="mo">
    <button class="mo-close" onclick="closeModal()">×</button>
    <div class="mo-header">
      <div class="mo-icon" id="mo-icon"></div>
      <div>
        <div class="mo-title" id="mo-title"></div>
        <div class="mo-lang" id="mo-lang"></div>
        <div class="mo-cat" id="mo-cat"></div>
      </div>
    </div>
    <div class="mo-desc" id="mo-desc"></div>
    <div class="mo-tags" id="mo-tags"></div>
    <div class="mo-btns" id="mo-btns"></div>
  </div>
</div>

<div id="dp">
  <div class="db" id="dpu">↑</div>
  <div class="db" id="dpl">←</div>
  <div class="db" id="dpr">→</div>
  <div class="db" id="dpd">↓</div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const PROJECTS = [
  {name:"Revenue Intelligence Agent",icon:"🚗",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · Groq LLM",desc:"Autonomous multi-agent AI pipeline monitoring competitor car rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals. Reduces manual analysis from 3 hours to 15 minutes. Features 5-tab Streamlit dashboard with anomaly flagging (≥20%) and urgency-ranked pricing recommendations.",tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","Revenue Ops","SQLite"],gh:"https://github.com/Mkp-7/Revenue-Management-Agent",live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"AI Pricing Intelligence Agent",icon:"🤖",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · Claude API",desc:"AI-powered competitive pricing agent using Claude API automating real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Identified 12–15% margin improvement opportunities.",tags:["Claude API","Price Monitoring","SQLite","Streamlit","Competitive Intel","ML"],gh:"https://github.com/Mkp-7/AI-Pricing-Agent",live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"EcoRoute Optimizer",icon:"🌿",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · Gemini AI · OR-Tools",desc:"Logistics optimization platform generating carbon-optimized shipping routes across 60+ US cities. Analyzes diesel truck, EV, and rail freight using EPA SmartWay carbon methodology. Integrates OpenRouteService + OpenWeatherMap APIs, SQLite route caching, and NLP conversational interface.",tags:["Gemini AI","OR-Tools","Carbon Optimization","REST APIs","NLP","Streamlit","Logistics"],gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Banking Risk Intelligence",icon:"🏦",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · FDIC API · FRED",desc:"Queried FDIC data for 4,500+ banks, calculated 5 operational risk KRIs against Basel III/CCAR thresholds. Applied Logistic Regression, Random Forest (AUC=0.84), and Gradient Boosting for bank failure risk prediction. Integrated Fed Funds Rate and yield curve from FRED.",tags:["Basel III","FDIC API","FRED","Random Forest","AUC=0.84","CCAR","Risk Modeling"],gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Retail Intelligence Platform",icon:"🛒",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · Groq · Yelp Data",desc:"AI-native customer intelligence platform turning public review data into actionable insights. Modules: Voice of Customer AI, Store Pulse Map, Test & Learn Autopilot (A/B statistical significance), and Analyst Copilot (plain-English Q&A chatbot).",tags:["Groq LLM","Yelp Dataset","NLP","Streamlit","Plotly","A/B Testing","Customer Analytics"],gh:"https://github.com/Mkp-7/retail-intelligence-platform",live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Medmedia Analytics Hub",icon:"🏥",hex:"#4fc3f7",category:"Streamlit App",lang:"Python · LLMs · REST APIs",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables pharma advertiser identification and HCP audience segmentation across 10 clinical specialties.",tags:["Healthcare","NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation","Streamlit"],gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Sales & Demand Forecasting",icon:"📊",hex:"#ffb74d",category:"Tableau Dashboard",lang:"Python · ARIMA · SARIMA",desc:"Fine-tuned ARIMA and SARIMA models to forecast 6-month revenue for 25,432 products across 12 regions at 94% accuracy. Identified top 20% customers driving 62% of total revenue. Built interactive Tableau and Power BI dashboards visualizing revenue trends, seasonal patterns, and KPIs.",tags:["ARIMA","SARIMA","Forecasting","Tableau","Power BI","94% Accuracy","25K+ Products"],gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  {name:"MSU Collaboratory Dashboard",icon:"🎓",hex:"#ffb74d",category:"Tableau Dashboard",lang:"Tableau · 3D Network Graph",desc:"3D visualization of activities at Montclair State University with community partner organizations. Tableau dashboard surfacing Collaboratory data insights. Network graph hosted on GitHub Pages showing cross-organization collaboration patterns.",tags:["Tableau","3D Network Graph","MSU","Community Partners","Data Viz","GitHub Pages"],gh:"https://mkp-7.github.io/Network-Graph/",live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"MSU Student Happiness Study",icon:"😊",hex:"#ffb74d",category:"Tableau Dashboard",lang:"Python · Statistics · Tableau",desc:"Tracked 70 MSU students for 21 days collecting daily activities, social context, location, and self-reported happiness (0–10) at 30-minute intervals. Cleaned 210 Excel sheets, performed hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard analyzing happiness patterns.",tags:["Survey Analysis","Hypothesis Testing","ANOVA","Regression","Tableau","Python","Behavioral Analytics"],gh:"",live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"},
  {name:"Banking Metrics Client Analysis",icon:"💳",hex:"#ef5350",category:"Power BI Dashboard",lang:"Power BI · SQL · Python",desc:"Structured dataset of 3,000 banking clients. Power BI dashboard identifying high-fee accounts (~51% of deposits), Private Bank loans (~$0.9B), and variations across client segments for risk assessment and regulatory reporting.",tags:["Power BI","Banking","Portfolio Analytics","Client Segmentation","Risk Assessment","Regulatory"],gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",live:""},
  {name:"Supply Chain Analytics BI",icon:"📦",hex:"#ef5350",category:"Power BI Dashboard",lang:"Power BI · Power Query · DAX",desc:"Integrated 10 raw Excel supply chain datasets using Power Query (ETL), built a star schema data model. Created 12+ DAX measures for KPIs: closing stock, inventory turnover, stock aging, on-time delivery %, and reorder alerts. Includes logistics maps and drill-through.",tags:["Power BI","DAX","Power Query","Star Schema","ETL","Supply Chain","Inventory"],gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",live:""},
  {name:"Insurance Claims Analysis",icon:"🛡️",hex:"#ef5350",category:"Power BI + ML",lang:"R · SQL Server · Power BI",desc:"Processed 58,000+ insurance policy records in SQL Server, developed Random Forest and Logistic Regression models in R achieving 94% accuracy for 6-month claim likelihood prediction. Power BI dashboards tracking predicted claim probability by car segment, fuel type, and policyholder age.",tags:["Random Forest","Logistic Regression","94% Accuracy","SQL Server","R","Power BI","Insurance"],gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",live:""},
  {name:"Workforce Utilization Analytics",icon:"👥",hex:"#ef5350",category:"Power BI Dashboard",lang:"Power BI · DAX · HR Data",desc:"Power BI dashboard analyzing workforce attendance for 80 employees over 3 months. Computed KPIs: attendance rate, WFH utilization, sick leave. Identified mid-month attendance dips and peak day shifts from Fridays to Mondays for data-driven workforce planning.",tags:["Power BI","HR Analytics","Workforce Planning","DAX","Attendance","WFH","Talent Insights"],gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",live:""},
  {name:"Retail Customer Analytics",icon:"🛍️",hex:"#ab47bc",category:"ML / Python Project",lang:"Python · Scikit-learn · Excel",desc:"Analyzed 25,000+ product records and 10,000+ customer transactions using K-Means clustering (5 segments). Identified top 20% customers driving 60% of revenue. Built automated Excel reporting dashboard tracking 10+ KPIs, reducing manual analysis time by 40%.",tags:["K-Means","Scikit-learn","Pandas","NumPy","Customer Segmentation","Excel Automation","RFM"],gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",live:""},
  {name:"COVID-19 Global Impact Analysis",icon:"🦠",hex:"#ab47bc",category:"ML / Python Project",lang:"Python · EDA · WHO Data",desc:"Analyzed COVID-19 global impact using WHO data (~450,000 records). EDA and Python visualization uncovering pandemic spread patterns. Covered mortality comparisons across WHO regions, global daily cases/deaths over time, and regional disparities in case fatality rates.",tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology","Data Storytelling","Python"],gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",live:""},
  {name:"Diabetes Prediction Model",icon:"🩺",hex:"#ab47bc",category:"ML / Python Project",lang:"Python · Scikit-learn · SVM",desc:"Diabetes prediction system using data from 769 patients. Evaluated Logistic Regression, Random Forest, and Decision Tree. Achieved peak 80% accuracy with SVM. Used Pandas, NumPy, Matplotlib, and Seaborn throughout.",tags:["SVM","Random Forest","Logistic Regression","Feature Selection","Scikit-learn","Healthcare ML"],gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",live:""},
  {name:"Smart Reads: Book Recommender",icon:"📚",hex:"#ab47bc",category:"ML / Python Project",lang:"Python · TF-IDF · SVD",desc:"Analyzed 10,000 books and 1M+ ratings using TF-IDF with Cosine Similarity and SVD for personalized recommendations. Mitigated cold start, scalability, and relevance challenges for accurate recommendations across diverse user preferences.",tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering","Recommendation Engine","1M+ Ratings"],gh:"https://github.com/Mkp-7/Book_Recommendation",live:""},
  {name:"E-Commerce GA4 Analytics Pipeline",icon:"📈",hex:"#66bb6a",category:"Looker / dbt / BigQuery",lang:"dbt · BigQuery · GA4 · Looker",desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling, behavioral segmentation across 269K users, and cross-source identity resolution. Identified 9,630 cart abandonment targets. Projected 23% recovery vs 8% baseline and $25K incremental revenue.",tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","Cart Abandonment","CDP","$25K Revenue"],gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"}
];

// ── THREE.JS 3D SCENE ──
let scene, camera, renderer, carGroup, carBody;
let buildings3d = [], nearBuilding = null, modalOpen = false;
let keys = {}, dpad = {up:0,down:0,left:0,right:0};
let carPos = {x:0, z:0}, carAngle = 0, carSpeed = 0;
let frame = 0, miniCanvas, miniCtx;

const WORLD = 120; // half-size of city
const BLOCK = 22;  // building spacing
const ROAD_W = 8;
const CAR_COLOR = 0xff4500; // GTA Vice City coral-red
const BUILDING_COLS = 5;

function startGame() {
  document.getElementById('intro').style.display = 'none';
  document.getElementById('hud').style.display = 'block';
  document.getElementById('minimap-wrap').style.display = 'block';
  document.getElementById('hint').style.display = 'block';
  document.getElementById('dp').style.display = 'grid';
  miniCanvas = document.getElementById('minimap');
  miniCtx = miniCanvas.getContext('2d');
  initThree();
  buildCity();
  buildCar();
  bindInput();
  animate();
  toast('Drive to a glowing building · Press Enter to explore!');
}

function initThree() {
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0a0f);
  scene.fog = new THREE.Fog(0x0a0a0f, 80, 200);

  // Isometric-ish camera (GTA Vice City feel)
  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 500);
  camera.position.set(0, 35, 50);
  camera.lookAt(0, 0, 0);

  renderer = new THREE.WebGLRenderer({canvas: document.getElementById('c'), antialias: true});
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // Ambient + directional light (Vice City neon night feel)
  scene.add(new THREE.AmbientLight(0x1a0a2a, 0.8));
  const sun = new THREE.DirectionalLight(0xff8855, 1.2);
  sun.position.set(30, 60, 30);
  sun.castShadow = true;
  sun.shadow.mapSize.width = 2048;
  sun.shadow.mapSize.height = 2048;
  sun.shadow.camera.near = 0.5;
  sun.shadow.camera.far = 300;
  sun.shadow.camera.left = -150;
  sun.shadow.camera.right = 150;
  sun.shadow.camera.top = 150;
  sun.shadow.camera.bottom = -150;
  scene.add(sun);

  // Vice City magenta fill light
  const fill = new THREE.DirectionalLight(0xff1493, 0.4);
  fill.position.set(-30, 20, -30);
  scene.add(fill);

  // Cyan rim light
  const rim = new THREE.PointLight(0x00ffff, 0.6, 200);
  rim.position.set(-50, 30, -50);
  scene.add(rim);
}

function buildCity() {
  // Ground plane
  const groundGeo = new THREE.PlaneGeometry(WORLD*2, WORLD*2);
  const groundMat = new THREE.MeshLambertMaterial({color: 0x0d0d14});
  const ground = new THREE.Mesh(groundGeo, groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);

  // Road grid
  buildRoads();

  // Grid lines on ground
  const gridHelper = new THREE.GridHelper(WORLD*2, 40, 0x1a1a2e, 0x1a1a2e);
  gridHelper.position.y = 0.01;
  scene.add(gridHelper);

  // Place buildings
  const cols = BUILDING_COLS;
  const rows = Math.ceil(PROJECTS.length / cols);
  const startX = -(cols - 1) * BLOCK / 2;
  const startZ = -(rows - 1) * BLOCK / 2;

  PROJECTS.forEach((p, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const x = startX + col * BLOCK;
    const z = startZ + row * BLOCK;
    const b = makeBuilding(p, x, z);
    buildings3d.push(b);
  });

  // Streetlamps
  for (let x = -WORLD + 20; x < WORLD; x += 30) {
    for (let z = -WORLD + 20; z < WORLD; z += 30) {
      addStreetlamp(x, z);
    }
  }
}

function buildRoads() {
  const roadMat = new THREE.MeshLambertMaterial({color: 0x111118});
  const lineMat = new THREE.MeshLambertMaterial({color: 0xff6b35, emissive: 0xff6b35, emissiveIntensity: 0.3});

  const cols = BUILDING_COLS;
  const rows = Math.ceil(PROJECTS.length / cols);

  // Horizontal roads
  for (let r = -1; r <= rows; r++) {
    const z = -(rows-1)*BLOCK/2 + r*BLOCK - BLOCK/2 + 5;
    const road = new THREE.Mesh(new THREE.PlaneGeometry(WORLD*2, ROAD_W), roadMat);
    road.rotation.x = -Math.PI/2;
    road.position.set(0, 0.02, z);
    scene.add(road);
    // dashes
    for (let dx = -WORLD + 5; dx < WORLD; dx += 6) {
      const dash = new THREE.Mesh(new THREE.PlaneGeometry(3, 0.3), lineMat);
      dash.rotation.x = -Math.PI/2;
      dash.position.set(dx, 0.03, z);
      scene.add(dash);
    }
  }

  // Vertical roads
  for (let c = -1; c <= cols; c++) {
    const x = -(cols-1)*BLOCK/2 + c*BLOCK - BLOCK/2 + 5;
    const road = new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W, WORLD*2), roadMat);
    road.rotation.x = -Math.PI/2;
    road.position.set(x, 0.02, 0);
    scene.add(road);
    // dashes
    for (let dz = -WORLD + 5; dz < WORLD; dz += 6) {
      const dash = new THREE.Mesh(new THREE.PlaneGeometry(0.3, 3), lineMat);
      dash.rotation.x = -Math.PI/2;
      dash.position.set(x, 0.03, dz);
      scene.add(dash);
    }
  }
}

function makeBuilding(project, x, z) {
  const color = parseInt(project.hex.replace('#',''), 16);
  const h = 8 + Math.random() * 14;
  const w = 6 + Math.random() * 3;
  const group = new THREE.Group();
  group.position.set(x, 0, z);
  group.userData = {project, baseH: h};

  // Sidewalk
  const sidewalk = new THREE.Mesh(
    new THREE.BoxGeometry(w + 2.5, 0.15, w + 2.5),
    new THREE.MeshLambertMaterial({color: 0x1a1a28})
  );
  sidewalk.position.y = 0.075;
  sidewalk.receiveShadow = true;
  group.add(sidewalk);

  // Main building body
  const body = new THREE.Mesh(
    new THREE.BoxGeometry(w, h, w),
    new THREE.MeshLambertMaterial({color: 0x0d1020})
  );
  body.position.y = h/2;
  body.castShadow = true;
  body.receiveShadow = true;
  group.add(body);
  group.userData.body = body;

  // Rooftop accent (colored)
  const roof = new THREE.Mesh(
    new THREE.BoxGeometry(w, 0.8, w),
    new THREE.MeshLambertMaterial({color, emissive: color, emissiveIntensity: 0.4})
  );
  roof.position.y = h + 0.4;
  group.add(roof);
  group.userData.roof = roof;

  // Windows — rows of glowing panes
  const winMat = new THREE.MeshLambertMaterial({color: 0xffd700, emissive: 0xffd700, emissiveIntensity: 0.6});
  const darkWinMat = new THREE.MeshLambertMaterial({color: 0x1a2035, emissive: 0x1a2035, emissiveIntensity: 0});
  const wRows = Math.floor(h / 2.2);
  const wCols = 2;
  const winW = 0.8, winH = 0.6, winD = 0.05;
  for (let r = 0; r < wRows; r++) {
    for (let c = 0; c < wCols; c++) {
      const lit = Math.random() > 0.35;
      const win = new THREE.Mesh(
        new THREE.BoxGeometry(winW, winH, winD),
        lit ? winMat : darkWinMat
      );
      const wx = (c - (wCols-1)/2) * 1.6;
      const wy = 1.5 + r * 2.0;
      win.position.set(wx, wy, w/2 + 0.01);
      group.add(win);
      // back face
      const win2 = win.clone();
      win2.position.z = -w/2 - 0.01;
      win2.rotation.y = Math.PI;
      group.add(win2);
      // sides
      const winS = win.clone();
      winS.position.set(w/2 + 0.01, wy, wx);
      winS.rotation.y = Math.PI/2;
      group.add(winS);
    }
  }

  // Neon sign on building face
  const neonMat = new THREE.MeshLambertMaterial({color, emissive: color, emissiveIntensity: 1.2});
  const neon = new THREE.Mesh(new THREE.BoxGeometry(w * 0.8, 0.3, 0.1), neonMat);
  neon.position.set(0, h * 0.65, w/2 + 0.1);
  group.add(neon);
  group.userData.neon = neon;

  // Point light for glow
  const light = new THREE.PointLight(color, 0, 15);
  light.position.set(0, h/2, 0);
  group.add(light);
  group.userData.light = light;

  scene.add(group);
  return group;
}

function addStreetlamp(x, z) {
  const mat = new THREE.MeshLambertMaterial({color: 0x333340});
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 4, 6), mat);
  pole.position.set(x, 2, z);
  scene.add(pole);
  const lampLight = new THREE.PointLight(0xff8844, 0.4, 20);
  lampLight.position.set(x, 4.2, z);
  scene.add(lampLight);
  const bulb = new THREE.Mesh(
    new THREE.SphereGeometry(0.2, 8, 8),
    new THREE.MeshLambertMaterial({color: 0xffaa55, emissive: 0xffaa55, emissiveIntensity: 1})
  );
  bulb.position.set(x, 4.2, z);
  scene.add(bulb);
}

function buildCar() {
  carGroup = new THREE.Group();

  // ── GTA Vice City-style car ──
  const bodyMat = new THREE.MeshLambertMaterial({color: CAR_COLOR});
  const darkMat = new THREE.MeshLambertMaterial({color: 0x111111});
  const glassMat = new THREE.MeshLambertMaterial({color: 0x4488bb, transparent: true, opacity: 0.7});
  const chromeMat = new THREE.MeshLambertMaterial({color: 0xcccccc, emissive: 0x888888, emissiveIntensity: 0.3});
  const headlightMat = new THREE.MeshLambertMaterial({color: 0xffffcc, emissive: 0xffffcc, emissiveIntensity: 1.5});
  const taillightMat = new THREE.MeshLambertMaterial({color: 0xff2200, emissive: 0xff2200, emissiveIntensity: 1.2});

  // Main body — lower
  const bodyLow = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.6, 4.4), bodyMat);
  bodyLow.position.y = 0.6;
  bodyLow.castShadow = true;
  carGroup.add(bodyLow);

  // Cabin — upper (narrower, shorter)
  const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.65, 2.4), bodyMat);
  cabin.position.set(0, 1.22, -0.1);
  cabin.castShadow = true;
  carGroup.add(cabin);

  // Windshield front
  const windF = new THREE.Mesh(new THREE.BoxGeometry(1.7, 0.55, 0.08), glassMat);
  windF.position.set(0, 1.22, 1.12);
  windF.rotation.x = -0.25;
  carGroup.add(windF);

  // Windshield rear
  const windR = new THREE.Mesh(new THREE.BoxGeometry(1.7, 0.5, 0.08), glassMat);
  windR.position.set(0, 1.18, -1.32);
  windR.rotation.x = 0.25;
  carGroup.add(windR);

  // Side windows
  for (const sx of [-0.91, 0.91]) {
    const winSide = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.45, 1.6), glassMat);
    winSide.position.set(sx, 1.25, -0.1);
    carGroup.add(winSide);
  }

  // Hood
  const hood = new THREE.Mesh(new THREE.BoxGeometry(2.1, 0.12, 1.2), bodyMat);
  hood.position.set(0, 0.96, 1.7);
  hood.rotation.x = 0.08;
  carGroup.add(hood);

  // Trunk
  const trunk = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.12, 0.8), bodyMat);
  trunk.position.set(0, 0.96, -1.95);
  trunk.rotation.x = -0.06;
  carGroup.add(trunk);

  // Bumpers
  const bumperF = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.25, 0.18), chromeMat);
  bumperF.position.set(0, 0.52, 2.22);
  carGroup.add(bumperF);
  const bumperR = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.25, 0.18), chromeMat);
  bumperR.position.set(0, 0.52, -2.22);
  carGroup.add(bumperR);

  // Headlights (2 per side)
  for (const hx of [-0.65, 0.65]) {
    const hl = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.2, 0.1), headlightMat);
    hl.position.set(hx, 0.72, 2.22);
    carGroup.add(hl);
  }

  // Taillights
  for (const tx of [-0.65, 0.65]) {
    const tl = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.2, 0.1), taillightMat);
    tl.position.set(tx, 0.72, -2.22);
    carGroup.add(tl);
  }

  // Wheels (4)
  const wheelGeo = new THREE.CylinderGeometry(0.42, 0.42, 0.28, 16);
  const wheelMat = new THREE.MeshLambertMaterial({color: 0x111111});
  const rimMat = new THREE.MeshLambertMaterial({color: 0xaaaaaa, emissive: 0x888888, emissiveIntensity: 0.3});
  const rimGeo = new THREE.CylinderGeometry(0.26, 0.26, 0.3, 8);
  const wheelPositions = [[-1.05, 0.42, 1.35], [1.05, 0.42, 1.35], [-1.05, 0.42, -1.35], [1.05, 0.42, -1.35]];
  wheelPositions.forEach(([wx, wy, wz]) => {
    const wg = new THREE.Group();
    const w = new THREE.Mesh(wheelGeo, wheelMat);
    w.rotation.z = Math.PI / 2;
    w.castShadow = true;
    wg.add(w);
    const rim = new THREE.Mesh(rimGeo, rimMat);
    rim.rotation.z = Math.PI / 2;
    wg.add(rim);
    wg.position.set(wx, wy, wz);
    carGroup.add(wg);
    wg.userData.isWheel = true;
  });

  // Headlight beams
  const beamL = new THREE.SpotLight(0xffffcc, 1.5, 40, Math.PI * 0.12, 0.3);
  beamL.position.set(-0.5, 0.72, 2.3);
  beamL.target.position.set(-0.5, -1, 15);
  carGroup.add(beamL);
  carGroup.add(beamL.target);

  const beamR = new THREE.SpotLight(0xffffcc, 1.5, 40, Math.PI * 0.12, 0.3);
  beamR.position.set(0.5, 0.72, 2.3);
  beamR.target.position.set(0.5, -1, 15);
  carGroup.add(beamR);
  carGroup.add(beamR.target);

  carGroup.position.set(0, 0, 0);
  scene.add(carGroup);
  carBody = carGroup;
}

// ── PHYSICS ──
const ACCEL = 0.08, FRIC = 0.88, MSPD = 0.7, TURN = 0.045;

function updateCar() {
  if (modalOpen) return;
  frame++;
  const U = keys['ArrowUp']   || keys['w'] || keys['W'] || dpad.up;
  const D = keys['ArrowDown']  || keys['s'] || keys['S'] || dpad.down;
  const L = keys['ArrowLeft']  || keys['a'] || keys['A'] || dpad.left;
  const R = keys['ArrowRight'] || keys['d'] || keys['D'] || dpad.right;

  if (U) carSpeed = Math.min(carSpeed + ACCEL, MSPD);
  else if (D) carSpeed = Math.max(carSpeed - ACCEL, -MSPD * 0.5);
  else carSpeed *= FRIC;

  if (Math.abs(carSpeed) > 0.01) {
    const dir = carSpeed > 0 ? 1 : -1;
    if (L) carAngle += TURN * dir;
    if (R) carAngle -= TURN * dir;
  }

  carPos.x += Math.sin(carAngle) * carSpeed;
  carPos.z += Math.cos(carAngle) * carSpeed;
  carPos.x = Math.max(-WORLD + 3, Math.min(WORLD - 3, carPos.x));
  carPos.z = Math.max(-WORLD + 3, Math.min(WORLD - 3, carPos.z));

  carGroup.position.x = carPos.x;
  carGroup.position.z = carPos.z;
  carGroup.rotation.y = carAngle;

  // Spin wheels
  carGroup.children.forEach(c => {
    if (c.userData.isWheel) c.children[0].rotation.x += carSpeed * 1.5;
  });

  // Camera follows — GTA overhead angle
  const camDist = 35, camH = 28;
  const targetCamX = carPos.x - Math.sin(carAngle) * camDist * 0.3;
  const targetCamZ = carPos.z - Math.cos(carAngle) * camDist * 0.3;
  camera.position.x += (targetCamX - camera.position.x) * 0.08;
  camera.position.z += (targetCamZ + camDist * 0.8 - camera.position.z) * 0.08;
  camera.position.y += (camH - camera.position.y) * 0.08;
  camera.lookAt(carPos.x, 0, carPos.z);

  // Find nearest building
  nearBuilding = null;
  let bestD = 9999;
  buildings3d.forEach(bg => {
    const dx = carPos.x - bg.position.x;
    const dz = carPos.z - bg.position.z;
    const d = Math.sqrt(dx*dx + dz*dz);
    if (d < 12 && d < bestD) {
      nearBuilding = bg;
      bestD = d;
    }
    // Animate glow
    const isNear = nearBuilding === bg;
    const pulse = isNear ? (Math.sin(frame * 0.08) * 0.5 + 0.7) : 0;
    bg.userData.light.intensity = pulse * 2;
    if (bg.userData.neon) bg.userData.neon.material.emissiveIntensity = isNear ? 1.5 + Math.sin(frame*0.1)*0.5 : 0.5;
  });

  // HUD
  document.getElementById('spd-fill').style.width = (Math.abs(carSpeed) / MSPD * 100).toFixed(0) + '%';
  document.getElementById('hud-near').innerHTML = nearBuilding
    ? 'Near: <span>' + nearBuilding.userData.project.name + '</span>'
    : 'Drive to a glowing building';
}

function drawMinimap() {
  const mw = 120, mh = 120;
  mctx = miniCanvas.getContext('2d');
  mctx.fillStyle = '#0a0a0f';
  mctx.fillRect(0, 0, mw, mh);
  const scale = mw / (WORLD * 2);
  const cx = mw / 2, cy = mh / 2;

  // Buildings as dots
  buildings3d.forEach(bg => {
    const px = cx + bg.position.x * scale;
    const py = cy + bg.position.z * scale;
    const isN = bg === nearBuilding;
    mctx.fillStyle = isN ? '#ffffff' : bg.userData.project.hex;
    mctx.beginPath();
    mctx.arc(px, py, isN ? 4 : 2.5, 0, Math.PI*2);
    mctx.fill();
  });

  // Car
  const cpx = cx + carPos.x * scale;
  const cpz = cy + carPos.z * scale;
  mctx.save();
  mctx.translate(cpx, cpz);
  mctx.rotate(-carAngle);
  mctx.fillStyle = '#ff4500';
  mctx.fillRect(-3, -5, 6, 10);
  mctx.fillStyle = '#ffcc00';
  mctx.fillRect(-2.5, -5, 5, 3);
  mctx.restore();

  // Border
  mctx.strokeStyle = 'rgba(255,107,53,.4)';
  mctx.lineWidth = 1;
  mctx.strokeRect(0, 0, mw, mh);
}

function animate() {
  requestAnimationFrame(animate);
  updateCar();
  drawMinimap();
  renderer.render(scene, camera);
}

// ── MODAL ──
function openModal(bg) {
  modalOpen = true;
  const p = bg.userData.project;
  document.getElementById('mo-icon').textContent = p.icon;
  document.getElementById('mo-icon').style.background = p.hex + '22';
  document.getElementById('mo-icon').style.borderColor = p.hex + '44';
  document.getElementById('mo-title').textContent = p.name;
  const ll = document.getElementById('mo-lang');
  ll.textContent = p.lang;
  ll.style.cssText = `background:${p.hex}22;color:${p.hex};border:1px solid ${p.hex}44`;
  document.getElementById('mo-cat').textContent = p.category;
  document.getElementById('mo-desc').textContent = p.desc;
  document.getElementById('mo-tags').innerHTML = p.tags.map(t => '<span class="mo-tag">' + t + '</span>').join('');
  let btns = '';
  if (p.gh)   btns += '<a class="mo-btn-gh" href="' + p.gh + '" target="_blank">⑂ GitHub</a>';
  if (p.live) btns += '<a class="mo-btn-live" href="' + p.live + '" target="_blank">🚀 Live Demo</a>';
  if (!p.gh && !p.live) btns = '<span style="font-size:12px;color:#444">No live link available</span>';
  document.getElementById('mo-btns').innerHTML = btns;
  document.getElementById('ov').style.display = 'flex';
}
function closeModal() {
  document.getElementById('ov').style.display = 'none';
  modalOpen = false;
}
document.getElementById('ov').addEventListener('click', e => {
  if (e.target === document.getElementById('ov')) closeModal();
});

// ── INPUT ──
function bindInput() {
  document.addEventListener('keydown', e => {
    keys[e.key] = true;
    if ((e.key === 'Enter' || e.key === ' ') && nearBuilding && !modalOpen) {
      e.preventDefault();
      openModal(nearBuilding);
    }
    if (e.key === 'Escape' && modalOpen) closeModal();
  });
  document.addEventListener('keyup', e => { keys[e.key] = false; });
  [['dpu','up'],['dpd','down'],['dpl','left'],['dpr','right']].forEach(([id,dir]) => {
    const el = document.getElementById(id);
    const on  = () => { dpad[dir] = 1; el.classList.add('on'); };
    const off = () => { dpad[dir] = 0; el.classList.remove('on'); };
    el.addEventListener('pointerdown', e => { e.preventDefault(); on(); });
    el.addEventListener('pointerup', off);
    el.addEventListener('pointerleave', off);
  });
}

function toast(msg) {
  const t = document.createElement('div');
  t.className = 'toast'; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 2900);
}
</script>
</body>
</html>"""

components.html(HTML, height=760, scrolling=False)
