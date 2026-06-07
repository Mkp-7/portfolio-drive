import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portfolio | Mkp-7",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
[data-testid="stAppViewContainer"] {background: #080c14;}
iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100vh;overflow:hidden;background:#080c14;font-family:'Segoe UI',system-ui,sans-serif}

#intro{position:fixed;inset:0;background:#080c14;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;padding:20px}
.intro-eyebrow{font-size:11px;letter-spacing:4px;color:#4a90d9;text-transform:uppercase;margin-bottom:10px}
.intro-name{font-size:46px;font-weight:700;color:#f0f4ff;letter-spacing:-1px;line-height:1;margin-bottom:6px}
.intro-title{font-size:13px;color:#6b7fa8;letter-spacing:2px;text-transform:uppercase;margin-bottom:32px}
.intro-divider{width:40px;height:2px;background:#4a90d9;margin:0 auto 28px}
.intro-legend{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;max-width:480px;margin-bottom:24px}
.leg{display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:6px;padding:5px 11px;font-size:11px;color:#6b7fa8}
.leg-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.intro-hint{font-size:11px;color:#3d4f6b;text-align:center;margin-bottom:26px;line-height:2;max-width:400px}
.intro-btn{background:#4a90d9;border:none;border-radius:8px;color:#fff;font-size:13px;font-weight:600;padding:12px 38px;cursor:pointer;letter-spacing:1px;text-transform:uppercase;transition:all .2s}
.intro-btn:hover{background:#5aa0e9;transform:translateY(-1px)}

#c{display:block;width:100%;height:100vh}

#hud{position:fixed;top:18px;left:18px;display:none;z-index:50}
.hud-card{background:rgba(8,12,20,.88);border:1px solid rgba(74,144,217,.15);border-radius:12px;padding:13px 17px;backdrop-filter:blur(16px)}
.hud-label{font-size:9px;letter-spacing:2px;color:#3d4f6b;text-transform:uppercase;margin-bottom:1px}
.hud-value{font-size:12px;font-weight:600;color:#c8d8f0}
.hud-accent{color:#4a90d9}
.hud-sep{height:1px;background:rgba(255,255,255,.05);margin:8px 0}
.hud-bar{height:2px;background:rgba(255,255,255,.06);border-radius:1px;overflow:hidden;margin-top:5px}
.hud-bar-fill{height:100%;background:#4a90d9;border-radius:1px;transition:width .08s;width:0%}
.hud-project{font-size:10px;color:#3d4f6b;margin-top:8px;min-height:14px}
.hud-project span{color:#4a90d9;font-weight:600}
.hud-enter{font-size:11px;font-weight:700;color:#f5c842;margin-top:5px;display:none;animation:pulse 1s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}

#mm-wrap{position:fixed;bottom:18px;right:18px;display:none;z-index:50}
.mm-label{font-size:9px;letter-spacing:2px;color:#3d4f6b;text-transform:uppercase;text-align:center;margin-bottom:4px}
#mm{border-radius:10px;border:1px solid rgba(74,144,217,.15)}

#hint{position:fixed;bottom:18px;left:18px;display:none;background:rgba(8,12,20,.82);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:8px 14px;font-size:10px;color:#3d4f6b;z-index:50;line-height:2}

#ov{position:fixed;inset:0;background:rgba(0,0,0,.8);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(14px)}
#mo{background:#0c1220;border:1px solid rgba(74,144,217,.18);border-radius:16px;padding:28px;max-width:480px;width:92%;position:relative;max-height:88vh;overflow-y:auto;animation:moin .2s ease}
@keyframes moin{from{transform:translateY(14px);opacity:0}to{transform:translateY(0);opacity:1}}
.mo-close{position:absolute;top:14px;right:14px;width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);color:#6b7fa8;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}
.mo-close:hover{background:rgba(255,255,255,.1);color:#f0f4ff}
.mo-header{display:flex;align-items:flex-start;gap:13px;margin-bottom:16px}
.mo-ico{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0}
.mo-eyebrow{font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}
.mo-name{font-size:16px;font-weight:700;color:#f0f4ff;line-height:1.3;margin-bottom:4px}
.mo-stack{font-size:10px;color:#6b7fa8}
.mo-desc{font-size:12.5px;color:#8a9bb8;line-height:1.78;margin-bottom:14px}
.mo-tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:16px}
.mo-tag{font-size:10px;color:#6b7fa8;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:3px 9px}
.mo-btns{display:flex;gap:8px;flex-wrap:wrap}
.mo-gh{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:600;text-align:center;text-decoration:none;background:rgba(255,255,255,.05);color:#c8d8f0;border:1px solid rgba(255,255,255,.1);display:block;transition:background .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-gh:hover{background:rgba(255,255,255,.1)}
.mo-live{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:700;text-align:center;text-decoration:none;background:#4a90d9;color:#fff;border:none;display:block;transition:opacity .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-live:hover{opacity:.88}
</style>
</head>
<body>

<div id="intro">
  <div class="intro-eyebrow">Interactive Portfolio</div>
  <div class="intro-name">Mkp-7</div>
  <div class="intro-title">Data Scientist &amp; AI Engineer</div>
  <div class="intro-divider"></div>
  <div class="intro-legend">
    <div class="leg"><div class="leg-dot" style="background:#4a90d9"></div>Streamlit Apps</div>
    <div class="leg"><div class="leg-dot" style="background:#f5a623"></div>Tableau</div>
    <div class="leg"><div class="leg-dot" style="background:#e85555"></div>Power BI</div>
    <div class="leg"><div class="leg-dot" style="background:#9b6dff"></div>ML &amp; Python</div>
    <div class="leg"><div class="leg-dot" style="background:#3ecf8e"></div>Looker &amp; dbt</div>
  </div>
  <div class="intro-hint">
    <strong style="color:#c8d8f0">W A S D</strong> or <strong style="color:#c8d8f0">Arrow Keys</strong> to drive<br>
    Project names are written on the road in front of each building<br>
    Drive into the <strong style="color:#c8d8f0">glowing zone</strong> — it lights up as you enter<br>
    Press <strong style="color:#c8d8f0">Enter</strong> to open the project card
  </div>
  <button class="intro-btn" onclick="startGame()">Enter Portfolio</button>
</div>

<canvas id="c"></canvas>

<div id="hud">
  <div class="hud-card">
    <div class="hud-label">Portfolio</div>
    <div class="hud-value hud-accent">Mkp-7</div>
    <div class="hud-sep"></div>
    <div class="hud-label">Speed</div>
    <div class="hud-bar"><div class="hud-bar-fill" id="spd-fill"></div></div>
    <div class="hud-project" id="hud-proj">Navigate to a project</div>
    <div class="hud-enter" id="hud-enter">⏎ Press Enter</div>
  </div>
</div>

<div id="mm-wrap">
  <div class="mm-label">Overview</div>
  <canvas id="mm" width="130" height="130"></canvas>
</div>

<div id="hint">
  <span style="color:#c8d8f0">W A S D</span> / Arrows — Drive &nbsp;·&nbsp; <span style="color:#c8d8f0">Enter</span> — Open project
</div>

<div id="ov">
  <div id="mo">
    <button class="mo-close" onclick="closeModal()">✕</button>
    <div class="mo-header">
      <div class="mo-ico" id="mo-ico"></div>
      <div>
        <div class="mo-eyebrow" id="mo-cat"></div>
        <div class="mo-name" id="mo-name"></div>
        <div class="mo-stack" id="mo-stack"></div>
      </div>
    </div>
    <div class="mo-desc" id="mo-desc"></div>
    <div class="mo-tags" id="mo-tags"></div>
    <div class="mo-btns" id="mo-btns"></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const PROJECTS = [
  {name:"Revenue Intelligence Agent",icon:"🚗",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Groq LLM · GitHub Actions",desc:"Autonomous multi-agent pipeline monitoring competitor car-rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals. Reduces analyst workflow from 3 hours to 15 minutes. 5-tab Streamlit dashboard with anomaly flagging (≥20%) and urgency-ranked pricing recommendations.",tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","SQLite","REST APIs"],gh:"https://github.com/Mkp-7/Revenue-Management-Agent",live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"AI Pricing Intelligence",icon:"🤖",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Claude API · Streamlit",desc:"Competitive pricing agent using the Claude API to automate real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Surfaced 12–15% margin improvement opportunities on systematically underpriced items.",tags:["Claude API","Price Monitoring","Competitive Intel","ML","Streamlit"],gh:"https://github.com/Mkp-7/AI-Pricing-Agent",live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"EcoRoute Optimizer",icon:"🌿",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Gemini AI · OR-Tools",desc:"Logistics optimization platform generating carbon-minimized shipping routes across 60+ US cities. Evaluates diesel, EV, and rail freight via EPA SmartWay carbon methodology. Integrates OpenRouteService and OpenWeatherMap APIs, SQLite route caching, and a natural-language query interface.",tags:["Gemini AI","OR-Tools","Carbon Optimization","NLP","REST APIs"],gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Banking Risk Intelligence",icon:"🏦",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · FDIC API · FRED · Scikit-learn",desc:"Operational risk monitoring platform querying FDIC data for 4,500+ banks. Calculates 5 risk KRIs against Basel III and CCAR thresholds. Applies Logistic Regression, Random Forest (AUC = 0.84), and Gradient Boosting for bank failure prediction. Integrates Fed Funds Rate and yield-curve signals from FRED.",tags:["Basel III","FDIC API","FRED","Random Forest AUC=0.84","CCAR"],gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Retail Intelligence Platform",icon:"🛒",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Groq LLM · Yelp Dataset",desc:"AI-native customer intelligence platform converting public review data into operational insights. Four modules: Voice of Customer AI, Store Pulse Map (regional benchmarking), Test & Learn Autopilot (statistical significance), and Analyst Copilot (plain-English Q&A chatbot).",tags:["Groq LLM","Yelp Dataset","NLP","Plotly","A/B Testing"],gh:"https://github.com/Mkp-7/retail-intelligence-platform",live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Medmedia Analytics Hub",icon:"🏥",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · LLMs · ClinicalTrials.gov",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables HCP audience segmentation across 10 clinical specialties and AI-generated content strategy.",tags:["Healthcare NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation"],gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Sales & Demand Forecasting",icon:"📊",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Python · ARIMA · SARIMA · Tableau",desc:"Fine-tuned ARIMA and SARIMA models forecasting 6-month revenue for 25,432 products across 12 regions at 94% accuracy. Identified top 20% of customers contributing 62% of total revenue. Interactive Tableau and Power BI dashboards for pricing and promotion strategy.",tags:["ARIMA","SARIMA","94% Accuracy","Tableau","Power BI"],gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  {name:"MSU Collaboratory",icon:"🎓",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Tableau · 3D Network Graph",desc:"3D network visualization of interdisciplinary activities and partnerships at Montclair State University across community partner organizations. Companion network graph on GitHub Pages illustrating cross-organizational collaboration topology.",tags:["Tableau","3D Network Graph","MSU","Community Partners"],gh:"https://mkp-7.github.io/Network-Graph/",live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"Student Wellbeing Study",icon:"📋",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Python · Statistics · Tableau",desc:"Longitudinal study tracking 70 MSU students over 21 days. Collected daily activities, social context, location, and self-reported happiness (0–10) at 30-minute intervals. Conducted hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard identifies happiness patterns by activity category.",tags:["Hypothesis Testing","ANOVA","Regression","Tableau","Behavioral Analytics"],gh:"",live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"},
  {name:"Banking Client Analysis",icon:"💳",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · SQL · Python",desc:"Structured 3,000 banking client records integrating portfolio, relationship, and product-level dimensions. Dashboard identifies high-fee accounts (~51% of deposits), Private Bank loan exposure (~$0.9B), and cross-segment variation for risk assessment and regulatory reporting.",tags:["Power BI","Client Segmentation","Portfolio Analytics","Risk Assessment"],gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",live:""},
  {name:"Supply Chain Analytics",icon:"📦",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · Power Query · DAX",desc:"Integrated 10 raw Excel supply chain datasets via Power Query ETL and built a star schema data model. 12+ DAX measures for KPIs including inventory turnover, stock aging, on-time delivery %, and reorder alerts. Includes logistics maps and drill-through.",tags:["Power BI","DAX","Power Query","Star Schema","ETL"],gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",live:""},
  {name:"Insurance Claims Prediction",icon:"🛡️",hex:"#e85555",cat:"Power BI + Machine Learning",stack:"R · SQL Server · Power BI",desc:"Processed 58,000+ insurance policy records in SQL Server. Random Forest and Logistic Regression in R achieving 94% accuracy for 6-month claim likelihood. Power BI dashboard tracks predicted claim probability by vehicle segment, fuel type, and policyholder demographics.",tags:["Random Forest","94% Accuracy","SQL Server","R","Power BI"],gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",live:""},
  {name:"Workforce Utilization",icon:"👥",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · DAX · HR Analytics",desc:"Dashboard analyzing attendance for 80 employees over 3 months, tracking presence, WFH utilization, and leave. KPIs: attendance rate, WFH utilization, sick leave frequency. Identified mid-month attendance dips and a shift in peak days from Fridays to Mondays.",tags:["Power BI","HR Analytics","DAX","WFH Utilization"],gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",live:""},
  {name:"Retail Customer Analytics",icon:"🛍️",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · Scikit-learn · K-Means",desc:"Analyzed 25,000+ product records and 10,000+ customer transactions. K-Means clustering (5 segments) identified the top 20% of customers contributing 60% of revenue. Automated Excel reporting dashboard tracking 10+ KPIs, reducing manual analysis time by 40%.",tags:["K-Means","Scikit-learn","Customer Segmentation","RFM","Pandas"],gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",live:""},
  {name:"COVID-19 Global Impact",icon:"🦠",hex:"#9b6dff",cat:"Exploratory Data Analysis",stack:"Python · EDA · WHO Data",desc:"Global COVID-19 analysis using WHO data (~450,000 records). Covers mortality comparisons across WHO regions, daily case and death trajectories, country-level outbreaks on peak days, and regional disparities in case fatality rates.",tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology"],gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",live:""},
  {name:"Diabetes Risk Prediction",icon:"🩺",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · SVM · Scikit-learn",desc:"Multi-model diabetes prediction system on 769 patients. Evaluated Logistic Regression, Decision Tree, Random Forest, and SVM. Achieved peak accuracy of 80% with SVM. Applied feature selection and exploratory analysis throughout.",tags:["SVM","Random Forest","Logistic Regression","Healthcare ML"],gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",live:""},
  {name:"Book Recommendation Engine",icon:"📚",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · TF-IDF · SVD",desc:"Recommendation engine on 10,000 books and 1M+ ratings. Employs TF-IDF with Cosine Similarity and SVD. Addresses cold start, scalability, and relevance challenges for accurate suggestions across diverse reader profiles.",tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering"],gh:"https://github.com/Mkp-7/Book_Recommendation",live:""},
  {name:"E-Commerce Funnel Analytics",icon:"📈",hex:"#3ecf8e",cat:"Looker · dbt · BigQuery",stack:"dbt · BigQuery · GA4 · Looker Studio",desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling and behavioral segmentation across 269K users. Identified 9,630 cart abandonment targets. Simulated email recovery campaign projecting 23% recovery rate vs 8% baseline and $25K incremental revenue.",tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","$25K Revenue"],gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"}
];

// ── SCENE STATE ──
let scene, camera, renderer, clock;
let carGroup, carWheels = [];
let buildings = [];
let nearEntry = null, modalOpen = false;
let keys = {};
let carPos = new THREE.Vector3(4, 0, 80);
let carAngle = Math.PI, carSpeed = 0;
let frame = 0;
let mmCanvas, mmCtx;

// Third-person camera
const CAM_OFFSET_BACK = 10;
const CAM_OFFSET_UP   = 5;
const CAM_LAG = 0.10;
let camPos = new THREE.Vector3(0, 8, 90);

const CITY_HALF = 110;
const COLS = 5;
const ROWS = Math.ceil(PROJECTS.length / COLS);
const BLK_X = 26, BLK_Z = 30;
const ROAD_W = 10;

// ── START ──
function startGame() {
  document.getElementById('intro').style.display = 'none';
  ['hud','mm-wrap','hint'].forEach(id => document.getElementById(id).style.display = 'block');
  mmCanvas = document.getElementById('mm');
  mmCtx = mmCanvas.getContext('2d');
  init3D();
  buildCity();
  buildCar();
  bindInput();
  clock = new THREE.Clock();
  loop();
}

// ── THREE INIT ──
function init3D() {
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x080c14);
  scene.fog = new THREE.FogExp2(0x080c14, 0.008);

  camera = new THREE.PerspectiveCamera(55, innerWidth / innerHeight, 0.1, 400);
  camera.position.copy(camPos);
  camera.lookAt(carPos);

  renderer = new THREE.WebGLRenderer({canvas: document.getElementById('c'), antialias: true, powerPreference: 'high-performance'});
  renderer.setSize(innerWidth, innerHeight);
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;

  window.addEventListener('resize', () => {
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
  });

  // Lights
  scene.add(new THREE.AmbientLight(0x8899bb, 0.55));

  const sun = new THREE.DirectionalLight(0xeef2ff, 1.9);
  sun.position.set(60, 100, 40);
  sun.castShadow = true;
  sun.shadow.mapSize.set(4096, 4096);
  sun.shadow.camera.near = 1;
  sun.shadow.camera.far = 400;
  sun.shadow.camera.left = sun.shadow.camera.bottom = -180;
  sun.shadow.camera.right = sun.shadow.camera.top  = 180;
  sun.shadow.bias = -0.0004;
  scene.add(sun);

  const fill = new THREE.DirectionalLight(0x2233aa, 0.35);
  fill.position.set(-60, 30, -60);
  scene.add(fill);
}

// ── CITY ──
function buildCity() {
  // Ground
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(CITY_HALF * 2.5, CITY_HALF * 2.5),
    new THREE.MeshLambertMaterial({color: 0x090d18})
  );
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);

  // Subtle grid
  const grid = new THREE.GridHelper(CITY_HALF * 2.4, 100, 0x111930, 0x0d1428);
  grid.position.y = 0.06;
  scene.add(grid);

  makeRoads();
  placeBuildings();
  placeLamps();
}

function makeRoads() {
  const roadMat = new THREE.MeshLambertMaterial({color: 0x0c1018});
  const lineMat = new THREE.MeshLambertMaterial({color: 0x253550, emissive: 0x152840, emissiveIntensity: 0.5});
  const sideMat = new THREE.MeshLambertMaterial({color: 0x151e2e});

  const startX = -((COLS - 1) * BLK_X) / 2;
  const startZ = -((ROWS - 1) * BLK_Z) / 2;

  // Horizontal roads (between row blocks + one before and after)
  for (let r = -1; r <= ROWS; r++) {
    const rz = startZ + r * BLK_Z - BLK_Z / 2 + BLK_Z / 2;
    addHRoad(rz, roadMat, lineMat, sideMat);
  }
  // Vertical roads
  for (let c = -1; c <= COLS; c++) {
    const rx = startX + c * BLK_X - BLK_X / 2 + BLK_X / 2;
    addVRoad(rx, roadMat, lineMat, sideMat);
  }
}

function addHRoad(rz, roadMat, lineMat, sideMat) {
  const len = CITY_HALF * 2.4;
  const road = new THREE.Mesh(new THREE.PlaneGeometry(len, ROAD_W), roadMat);
  road.rotation.x = -Math.PI / 2;
  road.position.set(0, 0.05, rz);
  road.receiveShadow = true;
  scene.add(road);
  // Kerbs
  for (const oz of [-ROAD_W / 2 + 0.3, ROAD_W / 2 - 0.3]) {
    const kerb = new THREE.Mesh(new THREE.BoxGeometry(len, 0.18, 0.35), sideMat);
    kerb.position.set(0, 0.09, rz + oz);
    scene.add(kerb);
  }
  // Centre dashes
  for (let x = -len / 2 + 3; x < len / 2; x += 7) {
    const d = new THREE.Mesh(new THREE.PlaneGeometry(3.5, 0.22), lineMat);
    d.rotation.x = -Math.PI / 2;
    d.position.set(x, 0.07, rz);
    scene.add(d);
  }
}

function addVRoad(rx, roadMat, lineMat, sideMat) {
  const len = CITY_HALF * 2.4;
  const road = new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W, len), roadMat);
  road.rotation.x = -Math.PI / 2;
  road.position.set(rx, 0.05, 0);
  road.receiveShadow = true;
  scene.add(road);
  for (const ox of [-ROAD_W / 2 + 0.3, ROAD_W / 2 - 0.3]) {
    const kerb = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.18, len), sideMat);
    kerb.position.set(rx + ox, 0.09, 0);
    scene.add(kerb);
  }
  for (let z = -len / 2 + 3; z < len / 2; z += 7) {
    const d = new THREE.Mesh(new THREE.PlaneGeometry(0.22, 3.5), lineMat);
    d.rotation.x = -Math.PI / 2;
    d.position.set(rx, 0.07, z);
    scene.add(d);
  }
}

// ── PROJECT NAME ON ROAD (canvas texture) ──
function makeRoadLabel(text, color) {
  const canvas = document.createElement('canvas');
  canvas.width = 512; canvas.height = 128;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, 512, 128);
  ctx.font = 'bold 38px Segoe UI, Arial';
  ctx.fillStyle = color || '#4a90d9';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  // truncate if long
  let label = text;
  while (ctx.measureText(label).width > 480 && label.length > 4) label = label.slice(0, -1);
  if (label !== text) label = label.trim() + '…';
  ctx.fillText(label, 256, 64);
  const tex = new THREE.CanvasTexture(canvas);
  return tex;
}

// ── BUILDINGS ──
function placeBuildings() {
  const startX = -((COLS - 1) * BLK_X) / 2;
  const startZ = -((ROWS - 1) * BLK_Z) / 2;

  PROJECTS.forEach((p, i) => {
    const col = i % COLS;
    const row = Math.floor(i / COLS);
    const bx = startX + col * BLK_X;
    const bz = startZ + row * BLK_Z;
    const bld = makeBuilding(p, bx, bz, i);
    buildings.push(bld);
  });
}

function makeBuilding(p, bx, bz, idx) {
  const hexColor = parseInt(p.hex.replace('#', ''), 16);
  const style = idx % 4;
  const bH = 10 + (idx % 6) * 3;
  const bW = 8, bD = 7;

  const g = new THREE.Group();
  g.position.set(bx, 0, bz);

  // Pavement
  const pave = new THREE.Mesh(
    new THREE.BoxGeometry(bW + 3, 0.22, bD + 3),
    new THREE.MeshLambertMaterial({color: 0x111828})
  );
  pave.position.y = 0.11;
  pave.receiveShadow = true;
  g.add(pave);

  // Body
  const body = new THREE.Mesh(
    new THREE.BoxGeometry(bW, bH, bD),
    new THREE.MeshLambertMaterial({color: 0x0f1826})
  );
  body.position.y = bH / 2 + 0.22;
  body.castShadow = true;
  body.receiveShadow = true;
  g.add(body);

  // Style variations
  if (style === 0) {
    // Glass curtain strips
    const gMat = new THREE.MeshLambertMaterial({color: hexColor, emissive: hexColor, emissiveIntensity: 0.05, transparent: true, opacity: 0.8});
    const strip = new THREE.Mesh(new THREE.BoxGeometry(bW - 0.8, bH, 0.1), gMat);
    strip.position.set(0, bH / 2 + 0.22, bD / 2 + 0.06);
    g.add(strip);
    const s2 = strip.clone(); s2.position.z = -bD / 2 - 0.06;
    g.add(s2);
  } else if (style === 1) {
    // Horizontal banding
    for (let b = 1; b < Math.floor(bH / 2.8); b++) {
      const band = new THREE.Mesh(
        new THREE.BoxGeometry(bW + 0.1, 0.18, bD + 0.1),
        new THREE.MeshLambertMaterial({color: hexColor, emissive: hexColor, emissiveIntensity: 0.12})
      );
      band.position.y = 0.22 + b * 2.8;
      g.add(band);
    }
  } else if (style === 2) {
    // Corner columns
    const colMat = new THREE.MeshLambertMaterial({color: 0x1c2840});
    for (const [cx, cz] of [[-bW/2+0.4,-bD/2+0.4],[bW/2-0.4,-bD/2+0.4],[-bW/2+0.4,bD/2-0.4],[bW/2-0.4,bD/2-0.4]]) {
      const col = new THREE.Mesh(new THREE.BoxGeometry(0.7, bH, 0.7), colMat);
      col.position.set(cx, bH / 2 + 0.22, cz);
      g.add(col);
    }
  } else {
    // Stepped tower
    const top = new THREE.Mesh(
      new THREE.BoxGeometry(bW * 0.65, bH * 0.4, bD * 0.65),
      new THREE.MeshLambertMaterial({color: 0x0f1826})
    );
    top.position.y = bH + (bH * 0.4) / 2 - 0.3;
    top.castShadow = true;
    g.add(top);
    const ledge = new THREE.Mesh(
      new THREE.BoxGeometry(bW + 0.4, 0.3, bD + 0.4),
      new THREE.MeshLambertMaterial({color: hexColor, emissive: hexColor, emissiveIntensity: 0.25})
    );
    ledge.position.y = bH + 0.22;
    g.add(ledge);
  }

  // Windows
  addWins(g, bW, bH, bD);

  // Rooftop
  const roofBar = new THREE.Mesh(
    new THREE.BoxGeometry(bW, 0.35, bD),
    new THREE.MeshLambertMaterial({color: hexColor, emissive: hexColor, emissiveIntensity: 0.55})
  );
  roofBar.position.y = bH + 0.4;
  g.add(roofBar);

  const roofLight = new THREE.PointLight(hexColor, 0.7, 22);
  roofLight.position.set(0, bH + 2, 0);
  g.add(roofLight);
  g.userData.roofLight = roofLight;

  // ── ENTRANCE ZONE ──
  // Sits in the road in front of the building (positive Z side)
  const eZ = bD / 2 + 3.8;

  // Road label — project name printed on the pavement before entrance
  const labelTex = makeRoadLabel(p.name, p.hex);
  const labelMesh = new THREE.Mesh(
    new THREE.PlaneGeometry(10, 2.2),
    new THREE.MeshBasicMaterial({map: labelTex, transparent: true, depthWrite: false})
  );
  labelMesh.rotation.x = -Math.PI / 2;
  labelMesh.position.set(0, 0.12, eZ + 3.5); // placed further out on the road
  g.add(labelMesh);
  g.userData.labelMesh = labelMesh;

  // Entrance zone floor — glowing rectangle on the road
  const eGeo = new THREE.PlaneGeometry(5.5, 3.2);
  const eMat = new THREE.MeshBasicMaterial({
    color: hexColor,
    transparent: true,
    opacity: 0.18,
    depthWrite: false
  });
  const ePlane = new THREE.Mesh(eGeo, eMat);
  ePlane.rotation.x = -Math.PI / 2;
  ePlane.position.set(0, 0.13, eZ);
  g.add(ePlane);
  g.userData.ePlane = ePlane;
  g.userData.eMat = eMat;
  g.userData.eBaseOpacity = 0.18;
  g.userData.eHex = hexColor;

  // Entrance border frame (4 thin lines)
  const frameMat = new THREE.MeshBasicMaterial({color: hexColor, transparent: true, opacity: 0.55});
  for (const [fw, fh, fx, fz_] of [
    [5.5, 0.12, 0, eZ - 1.6],
    [5.5, 0.12, 0, eZ + 1.6],
    [0.12, 3.2, -2.75, eZ],
    [0.12, 3.2,  2.75, eZ]
  ]) {
    const line = new THREE.Mesh(new THREE.PlaneGeometry(fw, fh), frameMat.clone());
    line.rotation.x = -Math.PI / 2;
    line.position.set(fx, 0.14, fz_);
    g.add(line);
  }

  // Corner posts
  const postMat = new THREE.MeshLambertMaterial({color: hexColor, emissive: hexColor, emissiveIntensity: 0.6});
  for (const [px, pz_] of [[-2.5, eZ - 1.4], [2.5, eZ - 1.4], [-2.5, eZ + 1.4], [2.5, eZ + 1.4]]) {
    const post = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 1.1, 8), postMat.clone());
    post.position.set(px, 0.55, pz_);
    g.add(post);
    const ball = new THREE.Mesh(new THREE.SphereGeometry(0.11, 8, 8), postMat.clone());
    ball.position.set(px, 1.15, pz_);
    g.add(ball);
  }

  // Entrance point light (dim by default, brightens on approach)
  const eLight = new THREE.PointLight(hexColor, 0, 12);
  eLight.position.set(0, 0.5, eZ);
  g.add(eLight);
  g.userData.eLight = eLight;

  // World-space entrance centre
  const entranceWorld = new THREE.Vector3(bx, 0, bz + eZ);

  // Bounding box for collision
  const bbox = new THREE.Box2(
    new THREE.Vector2(bx - bW / 2 - 0.4, bz - bD / 2 - 0.4),
    new THREE.Vector2(bx + bW / 2 + 0.4, bz + bD / 2 + 0.4)
  );

  scene.add(g);
  return {group: g, bbox, entranceWorld, project: p};
}

function addWins(g, bW, bH, bD) {
  const litMat  = new THREE.MeshLambertMaterial({color: 0xfff0b0, emissive: 0xfff0b0, emissiveIntensity: 0.65});
  const darkMat = new THREE.MeshLambertMaterial({color: 0x0a1020});
  const cols = 3, rows = Math.max(2, Math.floor((bH - 1.5) / 2.2));
  const gapX = (bW - 1.8) / (cols - 1);
  const gapY = (bH - 1.5) / (rows + 1);
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const wx = -bW / 2 + 0.9 + c * gapX;
      const wy = 0.22 + gapY + r * gapY;
      const lit = Math.random() > 0.3;
      const m = lit ? litMat : darkMat;
      const wf = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.85, 0.07), m);
      wf.position.set(wx, wy, bD / 2 + 0.04);
      g.add(wf);
      const wb = wf.clone();
      wb.position.z = -bD / 2 - 0.04;
      g.add(wb);
    }
  }
}

function placeLamps() {
  const pMat = new THREE.MeshLambertMaterial({color: 0x707888});
  const bMat = new THREE.MeshLambertMaterial({color: 0xffeedd, emissive: 0xffeedd, emissiveIntensity: 1});
  const startX = -((COLS - 1) * BLK_X) / 2;
  const startZ = -((ROWS - 1) * BLK_Z) / 2;
  for (let c = 0; c <= COLS; c++) {
    for (let r = 0; r <= ROWS; r++) {
      const lx = startX + c * BLK_X - BLK_X / 2;
      const lz = startZ + r * BLK_Z - BLK_Z / 2;
      addLamp(lx, lz, pMat, bMat);
    }
  }
}

function addLamp(lx, lz, pMat, bMat) {
  const lg = new THREE.Group();
  lg.position.set(lx, 0, lz);
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.09, 5, 8), pMat);
  pole.position.y = 2.5;
  lg.add(pole);
  const arm = new THREE.Mesh(new THREE.BoxGeometry(0.07, 0.07, 1.1), pMat);
  arm.position.set(0, 5.1, 0.55);
  lg.add(arm);
  const head = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.16, 0.55), bMat);
  head.position.set(0, 4.98, 1.0);
  lg.add(head);
  const pl = new THREE.PointLight(0xfff0e0, 0.3, 16);
  pl.position.set(0, 4.9, 1.0);
  lg.add(pl);
  scene.add(lg);
}

// ── CAR ──
function buildCar() {
  carGroup = new THREE.Group();
  const bodyMat  = new THREE.MeshLambertMaterial({color: 0x1a3060});
  const darkMat  = new THREE.MeshLambertMaterial({color: 0x080c14});
  const chrMat   = new THREE.MeshLambertMaterial({color: 0xaab4c0, emissive: 0x606870, emissiveIntensity: 0.2});
  const glassMat = new THREE.MeshLambertMaterial({color: 0x4477aa, transparent: true, opacity: 0.55, emissive: 0x223366, emissiveIntensity: 0.05});
  const hlMat    = new THREE.MeshLambertMaterial({color: 0xfffff0, emissive: 0xfffff0, emissiveIntensity: 2.2});
  const tlMat    = new THREE.MeshLambertMaterial({color: 0xff2000, emissive: 0xff2000, emissiveIntensity: 1.8});
  const rimMat   = new THREE.MeshLambertMaterial({color: 0xc0c8d4, emissive: 0x808898, emissiveIntensity: 0.2});
  const tyreMat  = new THREE.MeshLambertMaterial({color: 0x111111});

  // Lower body
  const lo = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.52, 4.8), bodyMat);
  lo.position.y = 0.56; lo.castShadow = true;
  carGroup.add(lo);

  // Side skirts
  for (const sx of [-1.21, 1.21]) {
    const sk = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.26, 4.5), darkMat);
    sk.position.set(sx, 0.43, 0);
    carGroup.add(sk);
  }

  // Cabin
  const cab = new THREE.Mesh(new THREE.BoxGeometry(2.05, 0.68, 2.6), bodyMat);
  cab.position.set(0, 1.28, -0.15); cab.castShadow = true;
  carGroup.add(cab);

  // Roof
  const roof = new THREE.Mesh(new THREE.BoxGeometry(1.95, 0.1, 2.4), darkMat);
  roof.position.set(0, 1.68, -0.15);
  carGroup.add(roof);

  // Windshields
  const wf = new THREE.Mesh(new THREE.BoxGeometry(1.95, 0.6, 0.09), glassMat);
  wf.position.set(0, 1.3, 1.12); wf.rotation.x = -0.28;
  carGroup.add(wf);
  const wr = new THREE.Mesh(new THREE.BoxGeometry(1.95, 0.55, 0.09), glassMat);
  wr.position.set(0, 1.27, -1.48); wr.rotation.x = 0.26;
  carGroup.add(wr);

  // Side windows
  for (const sx of [-1.04, 1.04]) {
    const ws = new THREE.Mesh(new THREE.BoxGeometry(0.07, 0.48, 1.85), glassMat);
    ws.position.set(sx, 1.32, -0.15);
    carGroup.add(ws);
  }

  // Hood & trunk
  const hood = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.09, 1.55), bodyMat);
  hood.position.set(0, 0.9, 1.88); hood.rotation.x = 0.05;
  carGroup.add(hood);
  const trunk = new THREE.Mesh(new THREE.BoxGeometry(2.1, 0.09, 0.9), bodyMat);
  trunk.position.set(0, 0.9, -2.1); trunk.rotation.x = -0.04;
  carGroup.add(trunk);

  // Bumpers
  const bfm = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.28, 0.18), chrMat);
  bfm.position.set(0, 0.46, 2.43);
  carGroup.add(bfm);
  const brm = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.28, 0.18), chrMat);
  brm.position.set(0, 0.46, -2.43);
  carGroup.add(brm);

  // Grille
  const grille = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.2, 0.08), darkMat);
  grille.position.set(0, 0.52, 2.44);
  carGroup.add(grille);

  // Headlights
  for (const hx of [-0.74, 0.74]) {
    const hl = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.17, 0.08), hlMat);
    hl.position.set(hx, 0.74, 2.45);
    carGroup.add(hl);
    const beam = new THREE.SpotLight(0xffffff, 1.0, 30, Math.PI * 0.1, 0.5);
    beam.position.set(hx, 0.74, 2.5);
    beam.target.position.set(hx * 1.1, -2, 16);
    carGroup.add(beam); carGroup.add(beam.target);
  }

  // Taillights
  for (const tx of [-0.74, 0.74]) {
    const tl = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.17, 0.08), tlMat);
    tl.position.set(tx, 0.74, -2.45);
    carGroup.add(tl);
  }

  // Mirrors
  for (const sx of [-1.23, 1.23]) {
    const mir = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.13, 0.32), chrMat);
    mir.position.set(sx, 1.1, 0.65);
    carGroup.add(mir);
  }

  // Wheels
  const wps = [[-1.14, 0.42, 1.52], [1.14, 0.42, 1.52], [-1.14, 0.42, -1.52], [1.14, 0.42, -1.52]];
  wps.forEach(([wx, wy, wz]) => {
    const wg = new THREE.Group();
    const tyre = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.26, 20), tyreMat);
    tyre.rotation.z = Math.PI / 2; tyre.castShadow = true;
    wg.add(tyre);
    const rim = new THREE.Mesh(new THREE.CylinderGeometry(0.27, 0.27, 0.27, 10), rimMat);
    rim.rotation.z = Math.PI / 2;
    wg.add(rim);
    for (let s = 0; s < 5; s++) {
      const spoke = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.52, 0.05), rimMat);
      spoke.rotation.z = Math.PI / 2;
      spoke.rotation.x = (s / 5) * Math.PI * 2;
      spoke.position.y = Math.sin((s / 5) * Math.PI * 2) * 0.14;
      spoke.position.z = Math.cos((s / 5) * Math.PI * 2) * 0.14;
      wg.add(spoke);
    }
    wg.position.set(wx, wy, wz);
    wg.userData.isWheel = true;
    carGroup.add(wg);
    carWheels.push(wg);
  });

  carGroup.position.copy(carPos);
  scene.add(carGroup);
}

// ── MAIN LOOP ──
const ACCEL = 0.05, FRIC = 0.88, MAX_SPD = 0.5, TURN = 0.036;

function loop() {
  requestAnimationFrame(loop);
  frame++;
  clock.getDelta();

  if (!modalOpen) {
    const U = keys['ArrowUp']    || keys['w'] || keys['W'];
    const D = keys['ArrowDown']  || keys['s'] || keys['S'];
    const L = keys['ArrowLeft']  || keys['a'] || keys['A'];
    const R = keys['ArrowRight'] || keys['d'] || keys['D'];

    if (U) carSpeed = Math.min(carSpeed + ACCEL, MAX_SPD);
    else if (D) carSpeed = Math.max(carSpeed - ACCEL, -MAX_SPD * 0.5);
    else carSpeed *= FRIC;

    if (Math.abs(carSpeed) > 0.004) {
      const dir = carSpeed > 0 ? 1 : -1;
      if (L) carAngle += TURN * dir;
      if (R) carAngle -= TURN * dir;
    }

    const nx = carPos.x + Math.sin(carAngle) * carSpeed;
    const nz = carPos.z + Math.cos(carAngle) * carSpeed;
    const testPt = new THREE.Vector2(nx, nz);
    let blocked = false;
    for (const b of buildings) {
      if (b.bbox.containsPoint(testPt)) { blocked = true; break; }
    }
    if (Math.abs(nx) > CITY_HALF - 2 || Math.abs(nz) > CITY_HALF - 2) blocked = true;

    if (!blocked) { carPos.x = nx; carPos.z = nz; }
    else { carSpeed *= -0.25; }

    carGroup.position.x = carPos.x;
    carGroup.position.z = carPos.z;
    carGroup.rotation.y = carAngle;

    // Spin wheels
    carWheels.forEach(wg => { wg.children[0].rotation.x += carSpeed * 2.2; });
  }

  // ── THIRD-PERSON CAMERA ──
  // Target position: behind and above the car
  const behind = new THREE.Vector3(
    carPos.x - Math.sin(carAngle) * CAM_OFFSET_BACK,
    CAM_OFFSET_UP,
    carPos.z - Math.cos(carAngle) * CAM_OFFSET_BACK
  );
  // Smooth follow
  camPos.lerp(behind, CAM_LAG);
  camera.position.copy(camPos);
  // Always look slightly ahead of the car
  const lookTarget = new THREE.Vector3(
    carPos.x + Math.sin(carAngle) * 4,
    1.2,
    carPos.z + Math.cos(carAngle) * 4
  );
  camera.lookAt(lookTarget);

  // ── ENTRANCE DETECTION & GLOW ──
  nearEntry = null;
  let bestD = 9999;
  buildings.forEach(b => {
    const dx = carPos.x - b.entranceWorld.x;
    const dz = carPos.z - b.entranceWorld.z;
    const d = Math.sqrt(dx * dx + dz * dz);
    const inZone = d < 3.5;

    // Smooth glow: base opacity + active pulse
    const pulse = Math.abs(Math.sin(frame * 0.07));
    if (inZone) {
      b.group.userData.eMat.opacity = 0.45 + pulse * 0.35;
      b.group.userData.eLight.intensity = 1.8 + pulse * 1.2;
      if (d < bestD) { nearEntry = b; bestD = d; }
    } else if (d < 9) {
      // Dim approach glow
      const t = 1 - (d - 3.5) / 5.5;
      b.group.userData.eMat.opacity = 0.18 + t * 0.15;
      b.group.userData.eLight.intensity = t * 0.5;
    } else {
      b.group.userData.eMat.opacity = 0.12;
      b.group.userData.eLight.intensity = 0;
    }
  });

  // HUD update
  document.getElementById('spd-fill').style.width = (Math.abs(carSpeed) / MAX_SPD * 100).toFixed(0) + '%';
  const projEl  = document.getElementById('hud-proj');
  const enterEl = document.getElementById('hud-enter');
  if (nearEntry) {
    projEl.innerHTML = '<span>' + nearEntry.project.name + '</span>';
    enterEl.style.display = 'block';
  } else {
    projEl.textContent = 'Navigate to a project entrance';
    enterEl.style.display = 'none';
  }

  drawMinimap();
  renderer.render(scene, camera);
}

// ── MINIMAP ──
function drawMinimap() {
  const mw = 130, mh = 130;
  mmCtx.fillStyle = '#080c14';
  mmCtx.fillRect(0, 0, mw, mh);
  const scale = mw / (CITY_HALF * 2);
  const ox = mw / 2, oz = mh / 2;

  buildings.forEach(b => {
    const px = ox + b.entranceWorld.x * scale;
    const pz = oz + b.entranceWorld.z * scale;
    const isN = b === nearEntry;
    mmCtx.globalAlpha = isN ? 1 : 0.6;
    mmCtx.fillStyle = b.project.hex;
    mmCtx.beginPath();
    mmCtx.arc(px, pz, isN ? 4.5 : 2.8, 0, Math.PI * 2);
    mmCtx.fill();
    mmCtx.globalAlpha = 1;
  });

  // Car arrow
  const cpx = ox + carPos.x * scale;
  const cpz = oz + carPos.z * scale;
  mmCtx.save();
  mmCtx.translate(cpx, cpz);
  mmCtx.rotate(-carAngle);
  mmCtx.fillStyle = '#ffffff';
  mmCtx.beginPath();
  mmCtx.moveTo(0, -5);
  mmCtx.lineTo(3, 4);
  mmCtx.lineTo(0, 2);
  mmCtx.lineTo(-3, 4);
  mmCtx.closePath();
  mmCtx.fill();
  mmCtx.restore();

  mmCtx.strokeStyle = 'rgba(74,144,217,.18)';
  mmCtx.lineWidth = 1;
  mmCtx.strokeRect(0, 0, mw, mh);
}

// ── MODAL ──
function openModal(b) {
  modalOpen = true;
  const p = b.project;
  document.getElementById('mo-ico').textContent = p.icon;
  document.getElementById('mo-ico').style.cssText = 'background:' + p.hex + '18;border:1px solid ' + p.hex + '30;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0';
  const catEl = document.getElementById('mo-cat');
  catEl.textContent = p.cat; catEl.style.color = p.hex;
  document.getElementById('mo-name').textContent = p.name;
  document.getElementById('mo-stack').textContent = p.stack;
  document.getElementById('mo-desc').textContent = p.desc;
  document.getElementById('mo-tags').innerHTML = p.tags.map(t => '<span class="mo-tag">' + t + '</span>').join('');
  let btns = '';
  if (p.gh)   btns += '<a class="mo-gh" href="' + p.gh + '" target="_blank">View on GitHub</a>';
  if (p.live) btns += '<a class="mo-live" href="' + p.live + '" target="_blank">Live Demo →</a>';
  if (!p.gh && !p.live) btns = '<span style="font-size:11px;color:#3d4f6b">No live link available</span>';
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
    if ((e.key === 'Enter' || e.key === ' ') && nearEntry && !modalOpen) {
      e.preventDefault(); openModal(nearEntry);
    }
    if (e.key === 'Escape' && modalOpen) closeModal();
  });
  document.addEventListener('keyup', e => { keys[e.key] = false; });
}

// Toast
function showToast(msg) {
  const style = document.createElement('style');
  style.textContent = '@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}10%,75%{opacity:1;transform:translateX(-50%)}100%{opacity:0}}';
  document.head.appendChild(style);
  const t = document.createElement('div');
  t.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:#4a90d9;color:#fff;border-radius:8px;padding:8px 20px;font-size:11px;font-weight:600;z-index:300;animation:tf 3.2s ease forwards;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3300);
}
</script>
</body>
</html>"""

components.html(HTML, height=760, scrolling=False)
