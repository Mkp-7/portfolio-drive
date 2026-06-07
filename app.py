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

/* ── INTRO ── */
#intro{position:fixed;inset:0;background:#080c14;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;padding:20px}
.intro-eyebrow{font-size:11px;letter-spacing:4px;color:#4a90d9;text-transform:uppercase;margin-bottom:12px}
.intro-name{font-size:48px;font-weight:700;color:#f0f4ff;letter-spacing:-1px;line-height:1;margin-bottom:6px}
.intro-title{font-size:14px;color:#6b7fa8;letter-spacing:2px;text-transform:uppercase;margin-bottom:40px}
.intro-divider{width:48px;height:2px;background:#4a90d9;margin:0 auto 36px}
.intro-legend{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:500px;margin-bottom:32px}
.leg{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:6px;padding:6px 12px;font-size:11px;color:#6b7fa8;letter-spacing:.5px}
.leg-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.intro-hint{font-size:11px;color:#3d4f6b;text-align:center;margin-bottom:28px;letter-spacing:.5px;line-height:1.8}
.intro-btn{background:#4a90d9;border:none;border-radius:8px;color:#fff;font-size:13px;font-weight:600;padding:13px 40px;cursor:pointer;letter-spacing:1px;text-transform:uppercase;transition:all .2s}
.intro-btn:hover{background:#5aa0e9;transform:translateY(-1px)}

/* ── CANVAS ── */
#c{display:block;width:100%;height:100vh;cursor:grab}
#c:active{cursor:grabbing}

/* ── HUD ── */
#hud{position:fixed;top:20px;left:20px;display:none;z-index:50;min-width:200px}
.hud-card{background:rgba(8,12,20,.85);border:1px solid rgba(74,144,217,.15);border-radius:12px;padding:14px 18px;backdrop-filter:blur(16px);margin-bottom:8px}
.hud-label{font-size:9px;letter-spacing:2px;color:#3d4f6b;text-transform:uppercase;margin-bottom:2px}
.hud-value{font-size:13px;font-weight:600;color:#c8d8f0}
.hud-value.accent{color:#4a90d9}
.hud-bar{height:2px;background:rgba(255,255,255,.06);border-radius:1px;overflow:hidden;margin-top:6px}
.hud-bar-fill{height:100%;background:#4a90d9;border-radius:1px;transition:width .1s;width:0%}
.hud-nearby{font-size:10px;color:#3d4f6b;margin-top:8px;letter-spacing:.3px}
.hud-nearby span{color:#4a90d9;font-weight:600}
.hud-prompt{font-size:10px;color:#e3b341;margin-top:4px;letter-spacing:.3px;display:none}

/* ── MINIMAP ── */
#mm-wrap{position:fixed;bottom:20px;right:20px;display:none;z-index:50}
.mm-label{font-size:9px;letter-spacing:2px;color:#3d4f6b;text-transform:uppercase;text-align:center;margin-bottom:5px}
#mm{border-radius:10px;border:1px solid rgba(74,144,217,.15)}

/* ── HINT ── */
#hint{position:fixed;bottom:20px;left:20px;display:none;background:rgba(8,12,20,.8);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:8px 14px;font-size:10px;color:#3d4f6b;z-index:50;letter-spacing:.3px;line-height:1.9}

/* ── MODAL ── */
#ov{position:fixed;inset:0;background:rgba(0,0,0,.78);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(12px)}
#mo{background:#0c1220;border:1px solid rgba(74,144,217,.2);border-radius:16px;padding:28px;max-width:480px;width:92%;position:relative;max-height:88vh;overflow-y:auto;animation:moin .2s ease}
@keyframes moin{from{transform:translateY(16px);opacity:0}to{transform:translateY(0);opacity:1}}
.mo-close{position:absolute;top:16px;right:16px;width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);color:#6b7fa8;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}
.mo-close:hover{background:rgba(255,255,255,.1);color:#f0f4ff}
.mo-header{display:flex;align-items:flex-start;gap:14px;margin-bottom:18px}
.mo-ico{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0}
.mo-eyebrow{font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:5px}
.mo-name{font-size:17px;font-weight:700;color:#f0f4ff;line-height:1.3;margin-bottom:5px}
.mo-stack{font-size:10px;color:#6b7fa8;letter-spacing:.5px}
.mo-desc{font-size:12.5px;color:#8a9bb8;line-height:1.75;margin-bottom:16px}
.mo-tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:18px}
.mo-tag{font-size:10px;color:#6b7fa8;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:3px 9px;letter-spacing:.3px}
.mo-btns{display:flex;gap:8px;flex-wrap:wrap}
.mo-btn-gh{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:600;text-align:center;text-decoration:none;background:rgba(255,255,255,.05);color:#c8d8f0;border:1px solid rgba(255,255,255,.1);display:block;transition:background .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-btn-gh:hover{background:rgba(255,255,255,.1)}
.mo-btn-live{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:700;text-align:center;text-decoration:none;background:#4a90d9;color:#fff;border:none;display:block;transition:opacity .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-btn-live:hover{opacity:.88}
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
    Navigate with <strong style="color:#c8d8f0">W A S D</strong> or <strong style="color:#c8d8f0">Arrow Keys</strong> &nbsp;·&nbsp; Rotate camera by <strong style="color:#c8d8f0">dragging</strong><br>
    Pull up to a <strong style="color:#c8d8f0">marked entry point</strong> in front of each building &nbsp;·&nbsp; Press <strong style="color:#c8d8f0">Enter</strong> to view project
  </div>
  <button class="intro-btn" onclick="startGame()">Enter Portfolio</button>
</div>

<canvas id="c"></canvas>

<div id="hud">
  <div class="hud-card">
    <div class="hud-label">Portfolio</div>
    <div class="hud-value accent">Mkp-7</div>
    <div class="hud-label" style="margin-top:6px">Role</div>
    <div class="hud-value" style="font-size:11px">Data Scientist &amp; AI Engineer</div>
    <div class="hud-bar"><div class="hud-bar-fill" id="spd-fill"></div></div>
    <div class="hud-nearby" id="hud-nearby">Navigate to a project entrance</div>
    <div class="hud-prompt" id="hud-prompt">⏎ Press Enter to open project</div>
  </div>
</div>

<div id="mm-wrap">
  <div class="mm-label">Overview</div>
  <canvas id="mm" width="130" height="130"></canvas>
</div>

<div id="hint">
  <span style="color:#c8d8f0">W A S D</span> / Arrow keys &nbsp;—&nbsp; Drive<br>
  <span style="color:#c8d8f0">Drag</span> &nbsp;—&nbsp; Rotate camera<br>
  <span style="color:#c8d8f0">Enter</span> &nbsp;—&nbsp; Open project at entrance
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
// ─────────────────────────────────────────
//  PROJECT DATA
// ─────────────────────────────────────────
const PROJECTS = [
  {name:"Revenue Intelligence Agent",icon:"🚗",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Groq LLM · GitHub Actions",desc:"Autonomous multi-agent pipeline monitoring competitor car-rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals via REST APIs. Reduces manual analyst workflow from 3 hours to 15 minutes through GitHub Actions automation. Features a 5-tab Streamlit dashboard with anomaly flagging and urgency-ranked pricing recommendations.",tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","SQLite","REST APIs"],gh:"https://github.com/Mkp-7/Revenue-Management-Agent",live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"AI Pricing Intelligence Agent",icon:"🤖",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Claude API · Streamlit",desc:"Competitive pricing agent using the Claude API to automate real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Surfaced 12–15% margin improvement opportunities on systematically underpriced items.",tags:["Claude API","Price Monitoring","SQLite","Competitive Intel","ML","Streamlit"],gh:"https://github.com/Mkp-7/AI-Pricing-Agent",live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"EcoRoute Optimizer",icon:"🌿",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Gemini AI · OR-Tools",desc:"Logistics optimization platform generating carbon-minimized shipping routes across 60+ US cities. Evaluates diesel, EV, and rail freight via EPA SmartWay carbon methodology and multi-objective optimization. Integrates OpenRouteService and OpenWeatherMap APIs, SQLite route caching, and a natural-language query interface.",tags:["Gemini AI","OR-Tools","Carbon Optimization","NLP","REST APIs","Streamlit"],gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Banking Risk Intelligence Platform",icon:"🏦",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · FDIC API · FRED · Scikit-learn",desc:"Operational risk monitoring platform querying FDIC data for 4,500+ banks. Calculates 5 risk KRIs against Basel III and CCAR thresholds. Applies Logistic Regression, Random Forest (AUC = 0.84), and Gradient Boosting for bank failure prediction. Integrates Fed Funds Rate and yield-curve signals from FRED.",tags:["Basel III","FDIC API","FRED","Random Forest AUC=0.84","CCAR","Risk Modeling"],gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Retail Intelligence Platform",icon:"🛒",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · Groq LLM · Yelp Dataset · Plotly",desc:"AI-native customer intelligence platform converting public review data into operational insights. Four modules: Voice of Customer AI (theme clustering and executive summaries), Store Pulse Map (regional benchmarking), Test & Learn Autopilot (statistical significance testing), and Analyst Copilot (plain-English Q&A chatbot).",tags:["Groq LLM","Yelp Dataset","NLP","Plotly","A/B Testing","Customer Analytics"],gh:"https://github.com/Mkp-7/retail-intelligence-platform",live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Medmedia Analytics Hub",icon:"🏥",hex:"#4a90d9",cat:"Streamlit Application",stack:"Python · LLMs · ClinicalTrials.gov · PubMed",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables pharmaceutical advertiser identification, HCP audience segmentation across 10 clinical specialties, and AI-generated content strategy.",tags:["Healthcare NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation","Streamlit"],gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Sales & Demand Forecasting",icon:"📊",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Python · ARIMA · SARIMA · Tableau · Power BI",desc:"Fine-tuned ARIMA and SARIMA models to forecast 6-month revenue for 25,432 products across 12 regions, achieving 94% accuracy. Identified the top 20% of customers contributing 62% of total revenue. Delivered interactive Tableau and Power BI dashboards visualizing trends, seasonality, and KPIs to drive pricing and promotion strategy.",tags:["ARIMA","SARIMA","94% Accuracy","Tableau","Power BI","25K+ Products"],gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  {name:"MSU Collaboratory Dashboard",icon:"🎓",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Tableau · 3D Network Graph · GitHub Pages",desc:"3D network visualization of interdisciplinary activities and partnerships at Montclair State University. Tableau dashboard surfacing Collaboratory data insights across community partner organizations. Companion graph hosted on GitHub Pages illustrating cross-organizational collaboration topology.",tags:["Tableau","3D Network Graph","MSU","Community Partners","GitHub Pages"],gh:"https://mkp-7.github.io/Network-Graph/",live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"Student Wellbeing Analytics",icon:"📋",hex:"#f5a623",cat:"Tableau Dashboard",stack:"Python · Statistics · Tableau",desc:"Longitudinal study tracking 70 MSU students over 21 days. Collected daily activities, timing, social context, location, and self-reported happiness scores (0–10) at 30-minute intervals. Cleaned 210 Excel sheets in Python and conducted hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard identifies happiness patterns by weekly cycle and activity category.",tags:["Hypothesis Testing","ANOVA","Regression","Tableau","Behavioral Analytics","Python"],gh:"",live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"},
  {name:"Banking Client Portfolio Analysis",icon:"💳",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · SQL · Python",desc:"Structured and transformed a dataset of 3,000 banking clients integrating portfolio, relationship, and product-level dimensions. Dashboard identifies high-fee accounts (~51% of deposits), Private Bank loan exposure (~$0.9B), and cross-segment variation, providing actionable insight for risk assessment, regulatory reporting, and onboarding review.",tags:["Power BI","Client Segmentation","Portfolio Analytics","Risk Assessment","Regulatory"],gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",live:""},
  {name:"Supply Chain Analytics",icon:"📦",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · Power Query · DAX · Excel",desc:"Integrated 10 raw Excel supply chain datasets using Power Query ETL and built a star schema data model. Developed an interactive Power BI dashboard tracking inventory, procurement, sales, production, and shipment. Created 12+ DAX measures for KPIs including closing stock, inventory turnover, stock aging, on-time delivery %, and reorder alerts.",tags:["Power BI","DAX","Power Query","Star Schema","ETL","Inventory"],gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",live:""},
  {name:"Insurance Claims Prediction",icon:"🛡️",hex:"#e85555",cat:"Power BI + Machine Learning",stack:"R · SQL Server · Power BI",desc:"Processed 58,000+ insurance policy records in SQL Server, engineered predictive features, and developed Random Forest and Logistic Regression models in R achieving 94% accuracy for 6-month claim likelihood. Power BI dashboard tracks predicted claim probability by vehicle segment, fuel type, transmission, and policyholder demographics.",tags:["Random Forest","Logistic Regression","94% Accuracy","SQL Server","R","Power BI"],gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",live:""},
  {name:"Workforce Utilization Analytics",icon:"👥",hex:"#e85555",cat:"Power BI Dashboard",stack:"Power BI · DAX · HR Analytics",desc:"Dashboard analyzing workforce attendance data for 80 employees over 3 months, tracking presence, WFH utilization, and leave patterns. Computed KPIs including attendance rate, WFH utilization, and sick leave frequency. Identified mid-month attendance dips and a shift in peak attendance days from Fridays to Mondays.",tags:["Power BI","HR Analytics","DAX","WFH Utilization","Workforce Planning"],gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",live:""},
  {name:"Retail Customer Analytics",icon:"🛍️",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · Scikit-learn · K-Means · Excel",desc:"Analyzed 25,000+ product records and 10,000+ customer transactions. Applied K-Means clustering (5 segments) and repeat-rate modeling to identify the top 20% of customers contributing 60% of revenue. Automated an Excel reporting dashboard tracking 10+ KPIs, reducing manual analysis time by 40%.",tags:["K-Means","Scikit-learn","Customer Segmentation","RFM","Excel Automation","Pandas"],gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",live:""},
  {name:"COVID-19 Global Impact Study",icon:"🦠",hex:"#9b6dff",cat:"Exploratory Data Analysis",stack:"Python · EDA · WHO Data · Matplotlib",desc:"Global COVID-19 impact analysis using WHO data (~450,000 records). EDA and Python visualization uncovering pandemic spread dynamics: mortality comparisons across WHO regions, daily case and death trajectories, country-level outbreaks on peak days, and regional disparities in case fatality rates.",tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology","Data Storytelling"],gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",live:""},
  {name:"Diabetes Risk Prediction",icon:"🩺",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · SVM · Scikit-learn",desc:"Multi-model diabetes prediction system trained on clinical data from 769 patients. Evaluated Logistic Regression, Decision Tree, Random Forest, and SVM. Achieved peak predictive accuracy of 80% with SVM. Applied feature selection, exploratory analysis, and preprocessing throughout.",tags:["SVM","Random Forest","Logistic Regression","Feature Selection","Healthcare ML"],gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",live:""},
  {name:"Book Recommendation Engine",icon:"📚",hex:"#9b6dff",cat:"Machine Learning · Python",stack:"Python · TF-IDF · SVD · Collaborative Filtering",desc:"Recommendation engine trained on 10,000 books and 1M+ ratings. Employs TF-IDF with Cosine Similarity and SVD for personalized recommendations. Addresses cold start, scalability, and relevance challenges to deliver accurate suggestions across diverse reader profiles.",tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering","1M+ Ratings"],gh:"https://github.com/Mkp-7/Book_Recommendation",live:""},
  {name:"E-Commerce Funnel Analytics",icon:"📈",hex:"#3ecf8e",cat:"Looker · dbt · BigQuery",stack:"dbt · BigQuery · GA4 · Looker Studio",desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling, behavioral segmentation across 269K users, and cross-source identity resolution. Identified 9,630 cart abandonment targets via GA4 UNNEST queries. Simulated email recovery campaign projecting 23% recovery rate versus 8% baseline and $25K incremental revenue.",tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","Cart Abandonment","$25K Revenue"],gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"}
];

// ─────────────────────────────────────────
//  SCENE GLOBALS
// ─────────────────────────────────────────
let scene, camera, renderer, clock;
let carGroup;
let buildings = [];   // {group, bbox, entrancePos, project}
let nearEntry = null;
let modalOpen = false;
let keys = {};
let carPos = new THREE.Vector3(0, 0, 60);
let carAngle = 0, carSpeed = 0;
let frame = 0;

// Mouse camera orbit
let isDragging = false, lastMX = 0, lastMY = 0;
let camTheta = 0.4, camPhi = 1.0, camRadius = 40;
const CAM_TARGET = new THREE.Vector3();

// Minimap
let mmCanvas, mmCtx;

// City layout
const CITY_SIZE = 180;
const BLOCK_W = 22, BLOCK_D = 22;
const COLS = 5;
const ROWS = Math.ceil(PROJECTS.length / COLS);
const ROAD_W = 10;

// ─────────────────────────────────────────
//  ENTRY POINT
// ─────────────────────────────────────────
function startGame() {
  document.getElementById('intro').style.display = 'none';
  ['hud','mm-wrap','hint'].forEach(id => document.getElementById(id).style.display = 'block');
  mmCanvas = document.getElementById('mm');
  mmCtx = mmCanvas.getContext('2d');
  initScene();
  buildCity();
  buildCar();
  bindInput();
  clock = new THREE.Clock();
  animate();
  showToast('Navigate to a marked entrance · Press Enter to view project');
}

// ─────────────────────────────────────────
//  THREE.JS INIT
// ─────────────────────────────────────────
function initScene() {
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x080c14);
  scene.fog = new THREE.FogExp2(0x080c14, 0.006);

  camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.1, 600);
  updateCamera();

  renderer = new THREE.WebGLRenderer({canvas: document.getElementById('c'), antialias: true, powerPreference:'high-performance'});
  renderer.setSize(innerWidth, innerHeight);
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;

  window.addEventListener('resize', () => {
    camera.aspect = innerWidth/innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
  });

  // Lighting
  scene.add(new THREE.AmbientLight(0x8899cc, 0.5));

  const sun = new THREE.DirectionalLight(0xeef0ff, 1.8);
  sun.position.set(60, 100, 60);
  sun.castShadow = true;
  sun.shadow.mapSize.set(4096, 4096);
  sun.shadow.camera.near = 1;
  sun.shadow.camera.far = 400;
  sun.shadow.camera.left = sun.shadow.camera.bottom = -200;
  sun.shadow.camera.right = sun.shadow.camera.top = 200;
  sun.shadow.bias = -0.0005;
  scene.add(sun);

  // Subtle blue fill
  const fill = new THREE.DirectionalLight(0x2244aa, 0.4);
  fill.position.set(-60, 40, -60);
  scene.add(fill);
}

function updateCamera() {
  const x = CAM_TARGET.x + camRadius * Math.sin(camPhi) * Math.sin(camTheta);
  const y = CAM_TARGET.y + camRadius * Math.cos(camPhi);
  const z = CAM_TARGET.z + camRadius * Math.sin(camPhi) * Math.cos(camTheta);
  camera.position.set(x, y, z);
  camera.lookAt(CAM_TARGET);
}

// ─────────────────────────────────────────
//  CITY CONSTRUCTION
// ─────────────────────────────────────────
const MAT = {
  ground:    () => new THREE.MeshLambertMaterial({color: 0x0a0e1a}),
  pavement:  () => new THREE.MeshLambertMaterial({color: 0x111722}),
  road:      () => new THREE.MeshLambertMaterial({color: 0x0d1018}),
  roadLine:  () => new THREE.MeshLambertMaterial({color: 0x2a3a5a, emissive: 0x1a2a4a, emissiveIntensity: 0.4}),
  bldgBase:  (c) => new THREE.MeshLambertMaterial({color: c || 0x10182a}),
  bldgFace:  () => new THREE.MeshLambertMaterial({color: 0x141e30}),
  glass:     (c) => new THREE.MeshLambertMaterial({color: c, emissive: c, emissiveIntensity: 0.08, transparent: true, opacity: 0.85}),
  winLit:    () => new THREE.MeshLambertMaterial({color: 0xfff0c0, emissive: 0xfff0c0, emissiveIntensity: 0.7}),
  winDark:   () => new THREE.MeshLambertMaterial({color: 0x0a1020, emissive: 0x050810, emissiveIntensity: 0}),
  accentEmit:(c) => new THREE.MeshLambertMaterial({color: c, emissive: c, emissiveIntensity: 0.6}),
  entrance:  (c) => new THREE.MeshLambertMaterial({color: c, emissive: c, emissiveIntensity: 0.9, transparent: true, opacity: 0.85}),
  lamp:      () => new THREE.MeshLambertMaterial({color: 0x888fa0}),
  lampGlow:  () => new THREE.MeshLambertMaterial({color: 0xffeedd, emissive: 0xffeedd, emissiveIntensity: 1}),
};

function buildCity() {
  // Ground
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(CITY_SIZE*2, CITY_SIZE*2), MAT.ground());
  ground.rotation.x = -Math.PI/2;
  ground.receiveShadow = true;
  scene.add(ground);

  // Subtle grid
  const grid = new THREE.GridHelper(CITY_SIZE*2, 80, 0x151d30, 0x0f1520);
  grid.position.y = 0.05;
  scene.add(grid);

  buildRoadNetwork();

  // Place buildings in a grid
  const startX = -((COLS-1) * BLOCK_W) / 2;
  const startZ = -((ROWS-1) * BLOCK_D) / 2;

  PROJECTS.forEach((p, i) => {
    const col = i % COLS;
    const row = Math.floor(i / COLS);
    const x = startX + col * BLOCK_W;
    const z = startZ + row * BLOCK_D;
    const bld = makeBuilding(p, x, z, i);
    buildings.push(bld);
  });

  // Streetlamps along roads
  placeStreetlamps();
}

function buildRoadNetwork() {
  const startX = -((COLS-1)*BLOCK_W)/2;
  const startZ = -((ROWS-1)*BLOCK_D)/2;

  // Horizontal roads (between block rows)
  for (let r = -1; r <= ROWS; r++) {
    const z = startZ + r * BLOCK_D - BLOCK_D/2 + BLOCK_D/2;
    addRoadH(z, CITY_SIZE * 2);
  }
  // Vertical roads
  for (let c = -1; c <= COLS; c++) {
    const x = startX + c * BLOCK_W - BLOCK_W/2 + BLOCK_W/2;
    addRoadV(x, CITY_SIZE * 2);
  }
}

function addRoadH(z, len) {
  const road = new THREE.Mesh(new THREE.PlaneGeometry(len, ROAD_W), MAT.road());
  road.rotation.x = -Math.PI/2;
  road.position.set(0, 0.08, z);
  scene.add(road);
  // Centre line
  for (let x = -len/2 + 4; x < len/2; x += 7) {
    const dash = new THREE.Mesh(new THREE.PlaneGeometry(3.5, 0.25), MAT.roadLine());
    dash.rotation.x = -Math.PI/2;
    dash.position.set(x, 0.1, z);
    scene.add(dash);
  }
  // Edge lines
  for (const oz of [-ROAD_W/2 + 0.4, ROAD_W/2 - 0.4]) {
    const edge = new THREE.Mesh(new THREE.PlaneGeometry(len, 0.2), MAT.roadLine());
    edge.rotation.x = -Math.PI/2;
    edge.position.set(0, 0.1, z + oz);
    scene.add(edge);
  }
}

function addRoadV(x, len) {
  const road = new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W, len), MAT.road());
  road.rotation.x = -Math.PI/2;
  road.position.set(x, 0.08, 0);
  scene.add(road);
  for (let z = -len/2 + 4; z < len/2; z += 7) {
    const dash = new THREE.Mesh(new THREE.PlaneGeometry(0.25, 3.5), MAT.roadLine());
    dash.rotation.x = -Math.PI/2;
    dash.position.set(x, 0.1, z);
    scene.add(dash);
  }
}

// Varied building styles by index
function makeBuilding(project, x, z, idx) {
  const col = parseInt(project.hex.replace('#',''), 16);
  const style = idx % 4; // 4 architectural styles
  const h = 10 + (idx % 7) * 3.5;
  const w = 7, d = 7;
  const group = new THREE.Group();
  group.position.set(x, 0, z);

  // Pavement block
  const pave = new THREE.Mesh(new THREE.BoxGeometry(w+4, 0.2, d+4), MAT.pavement());
  pave.position.y = 0.1;
  pave.receiveShadow = true;
  group.add(pave);

  // Main body
  const body = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), MAT.bldgFace());
  body.position.y = h/2 + 0.2;
  body.castShadow = true;
  body.receiveShadow = true;
  group.add(body);

  // Style-specific facade details
  if (style === 0) {
    // Glass curtain-wall strips on all 4 faces
    const strip = new THREE.Mesh(new THREE.BoxGeometry(w-0.6, h, 0.12), MAT.glass(col));
    strip.position.set(0, h/2+0.2, d/2+0.06);
    group.add(strip);
    const strip2 = strip.clone();
    strip2.position.z = -d/2-0.06;
    group.add(strip2);
  } else if (style === 1) {
    // Horizontal banding
    const bands = Math.floor(h/3);
    for (let b = 0; b < bands; b++) {
      const band = new THREE.Mesh(new THREE.BoxGeometry(w+0.1, 0.2, d+0.1), MAT.accentEmit(col));
      band.position.y = 1.5 + b * 3 + 0.2;
      band.material.emissiveIntensity = 0.15;
      group.add(band);
    }
  } else if (style === 2) {
    // Corner columns
    for (const [cx, cz] of [[-w/2+0.3,-d/2+0.3],[w/2-0.3,-d/2+0.3],[-w/2+0.3,d/2-0.3],[w/2-0.3,d/2-0.3]]) {
      const col3d = new THREE.Mesh(new THREE.BoxGeometry(0.6, h, 0.6), new THREE.MeshLambertMaterial({color: 0x1e2a40}));
      col3d.position.set(cx, h/2+0.2, cz);
      group.add(col3d);
    }
  } else {
    // Setback upper floor
    const upper = new THREE.Mesh(new THREE.BoxGeometry(w*0.7, h*0.35, d*0.7), MAT.bldgFace());
    upper.position.y = h + h*0.35/2 - 0.5;
    upper.castShadow = true;
    group.add(upper);
    const ledge = new THREE.Mesh(new THREE.BoxGeometry(w+0.3, 0.3, d+0.3), MAT.accentEmit(col));
    ledge.position.y = h + 0.2;
    ledge.material.emissiveIntensity = 0.2;
    group.add(ledge);
  }

  // Windows — front and back faces
  addWindowGrid(group, w, h, d, 0.2);

  // Rooftop accent bar
  const roofBar = new THREE.Mesh(new THREE.BoxGeometry(w, 0.4, d), MAT.accentEmit(col));
  roofBar.position.y = h + 0.4;
  roofBar.material.emissiveIntensity = 0.5;
  group.add(roofBar);

  // Rooftop light
  const roofLight = new THREE.PointLight(col, 0.6, 25);
  roofLight.position.set(0, h + 2, 0);
  group.add(roofLight);

  // ── ENTRANCE ZONE ──
  // Marked spot in front of building (positive Z face)
  const entranceOffset = d/2 + 3.5;
  const entranceLocal = new THREE.Vector3(0, 0, entranceOffset);
  const entranceWorld = entranceLocal.clone().add(new THREE.Vector3(x, 0, z));

  // Entrance pavement
  const epad = new THREE.Mesh(new THREE.BoxGeometry(4, 0.25, 2.5), MAT.pavement());
  epad.position.set(0, 0.12, entranceOffset - 0.5);
  group.add(epad);

  // Glowing entrance marker (flat ring on ground)
  const ering = new THREE.Mesh(new THREE.PlaneGeometry(3.5, 2), MAT.entrance(col));
  ering.rotation.x = -Math.PI/2;
  ering.position.set(0, 0.26, entranceOffset - 0.5);
  group.add(ering);
  group.userData.entranceMarker = ering;

  // Small marker post
  for (const ox of [-1.5, 1.5]) {
    const post = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 1.4, 8), MAT.accentEmit(col));
    post.position.set(ox, 0.9, entranceOffset - 0.5);
    group.add(post);
    const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.12, 8, 8), MAT.accentEmit(col));
    bulb.position.set(ox, 1.6, entranceOffset - 0.5);
    group.add(bulb);
  }

  // "ENTER" sign above doorway
  const door = new THREE.Mesh(new THREE.BoxGeometry(1.8, 2.4, 0.08), new THREE.MeshLambertMaterial({color: 0x0a1020}));
  door.position.set(0, 1.4, d/2 + 0.04);
  group.add(door);
  const doorFrame = new THREE.Mesh(new THREE.BoxGeometry(2.0, 2.6, 0.06), MAT.accentEmit(col));
  doorFrame.position.set(0, 1.4, d/2 + 0.01);
  doorFrame.material.emissiveIntensity = 0.3;
  group.add(doorFrame);

  // Compute bounding box for collision
  const bb = new THREE.Box2(
    new THREE.Vector2(x - w/2 - 0.3, z - d/2 - 0.3),
    new THREE.Vector2(x + w/2 + 0.3, z + d/2 + 0.3)
  );

  scene.add(group);
  return {group, bbox: bb, entranceWorld, project};
}

function addWindowGrid(group, w, h, d, baseY) {
  const wW = 0.7, wH = 0.9;
  const cols = 3, rows = Math.floor((h - 1.5) / 2.0);
  const gapX = (w - 1.5) / (cols - 1);
  const gapY = (h - 1.5) / (rows + 1);

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const wx = -w/2 + 0.75 + c * gapX;
      const wy = baseY + gapY + r * gapY;
      const lit = Math.random() > 0.32;
      const mat = lit ? MAT.winLit() : MAT.winDark();
      // Front face
      const win = new THREE.Mesh(new THREE.BoxGeometry(wW, wH, 0.08), mat);
      win.position.set(wx, wy, d/2 + 0.05);
      group.add(win);
      // Back face
      const winB = win.clone();
      winB.position.z = -d/2 - 0.05;
      group.add(winB);
    }
  }
}

function placeStreetlamps() {
  const lampMat = MAT.lamp();
  const glowMat = MAT.lampGlow();
  const startX = -((COLS-1)*BLOCK_W)/2;
  const startZ = -((ROWS-1)*BLOCK_D)/2;

  for (let c = -1; c <= COLS; c++) {
    for (let r = -1; r <= ROWS; r++) {
      const x = startX + c * BLOCK_W + 4;
      const z = startZ + r * BLOCK_D + 4;
      addLamp(x, z, lampMat, glowMat);
    }
  }
}

function addLamp(x, z, lampMat, glowMat) {
  const g = new THREE.Group();
  g.position.set(x, 0, z);
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.09, 5, 8), lampMat);
  pole.position.y = 2.5;
  g.add(pole);
  const arm = new THREE.Mesh(new THREE.BoxGeometry(0.07, 0.07, 1.2), lampMat);
  arm.position.set(0, 5.1, 0.6);
  g.add(arm);
  const head = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.18, 0.6), glowMat);
  head.position.set(0, 4.98, 1.1);
  g.add(head);
  const pl = new THREE.PointLight(0xfff0e0, 0.35, 18);
  pl.position.set(0, 4.9, 1.1);
  g.add(pl);
  scene.add(g);
}

// ─────────────────────────────────────────
//  CAR
// ─────────────────────────────────────────
function buildCar() {
  carGroup = new THREE.Group();
  const bodyC = 0x1a2a5a;
  const bodyMat = new THREE.MeshLambertMaterial({color: bodyC});
  const darkMat = new THREE.MeshLambertMaterial({color: 0x080c14});
  const chromeMat = new THREE.MeshLambertMaterial({color: 0xb0bcc8, emissive: 0x888fa0, emissiveIntensity: 0.2});
  const glassMat = new THREE.MeshLambertMaterial({color: 0x6699cc, transparent: true, opacity: 0.6, emissive: 0x3355aa, emissiveIntensity: 0.05});
  const hlMat = new THREE.MeshLambertMaterial({color: 0xfffff0, emissive: 0xfffff0, emissiveIntensity: 2});
  const tlMat = new THREE.MeshLambertMaterial({color: 0xff2200, emissive: 0xff2200, emissiveIntensity: 1.5});
  const rimMat = new THREE.MeshLambertMaterial({color: 0xc0c8d4, emissive: 0x808898, emissiveIntensity: 0.2});

  // Lower body
  const lo = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.55, 4.8), bodyMat);
  lo.position.y = 0.58; lo.castShadow = true;
  carGroup.add(lo);

  // Side skirts (slight overhang)
  for (const sx of [-1.22, 1.22]) {
    const skirt = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.28, 4.4), new THREE.MeshLambertMaterial({color: 0x111827}));
    skirt.position.set(sx, 0.44, 0);
    carGroup.add(skirt);
  }

  // Cabin
  const cab = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.7, 2.6), bodyMat);
  cab.position.set(0, 1.28, -0.2); cab.castShadow = true;
  carGroup.add(cab);

  // Roof
  const roof = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.12, 2.4), new THREE.MeshLambertMaterial({color: 0x111827}));
  roof.position.set(0, 1.68, -0.2);
  carGroup.add(roof);

  // Front windshield
  const wf = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.62, 0.1), glassMat);
  wf.position.set(0, 1.3, 1.13); wf.rotation.x = -0.28;
  carGroup.add(wf);
  // Rear windshield
  const wr = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.56, 0.1), glassMat);
  wr.position.set(0, 1.27, -1.5); wr.rotation.x = 0.26;
  carGroup.add(wr);
  // Side windows
  for (const sx of [-1.02, 1.02]) {
    const ws = new THREE.Mesh(new THREE.BoxGeometry(0.07, 0.5, 1.8), glassMat);
    ws.position.set(sx, 1.32, -0.2);
    carGroup.add(ws);
  }

  // Hood
  const hood = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.1, 1.5), bodyMat);
  hood.position.set(0, 0.9, 1.85); hood.rotation.x = 0.06;
  carGroup.add(hood);
  // Trunk lid
  const trunk = new THREE.Mesh(new THREE.BoxGeometry(2.1, 0.1, 0.9), bodyMat);
  trunk.position.set(0, 0.9, -2.1); trunk.rotation.x = -0.04;
  carGroup.add(trunk);

  // Bumpers
  const bf = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.3, 0.2), chromeMat);
  bf.position.set(0, 0.48, 2.42);
  carGroup.add(bf);
  const br = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.3, 0.2), chromeMat);
  br.position.set(0, 0.48, -2.42);
  carGroup.add(br);

  // Grille
  const grille = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.22, 0.1), darkMat);
  grille.position.set(0, 0.55, 2.43);
  carGroup.add(grille);

  // Headlights (2 pairs)
  for (const hx of [-0.72, 0.72]) {
    const hl = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.18, 0.1), hlMat);
    hl.position.set(hx, 0.76, 2.44);
    carGroup.add(hl);
    const beam = new THREE.SpotLight(0xffffff, 1.2, 35, Math.PI*0.1, 0.4);
    beam.position.set(hx, 0.76, 2.5);
    beam.target.position.set(hx*1.1, -2, 18);
    carGroup.add(beam); carGroup.add(beam.target);
  }
  // Taillights
  for (const tx of [-0.72, 0.72]) {
    const tl = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.18, 0.1), tlMat);
    tl.position.set(tx, 0.76, -2.44);
    carGroup.add(tl);
  }

  // Mirror housings
  for (const sx of [-1.21, 1.21]) {
    const mirror = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.15, 0.35), chromeMat);
    mirror.position.set(sx, 1.12, 0.7);
    carGroup.add(mirror);
  }

  // Wheels
  const wPositions = [[-1.12,0.4,1.5],[1.12,0.4,1.5],[-1.12,0.4,-1.5],[1.12,0.4,-1.5]];
  wPositions.forEach(([wx,wy,wz]) => {
    const wg = new THREE.Group();
    // Tyre
    const tyre = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.26, 20), new THREE.MeshLambertMaterial({color: 0x111111}));
    tyre.rotation.z = Math.PI/2;
    tyre.castShadow = true;
    wg.add(tyre);
    // Rim face
    const rim = new THREE.Mesh(new THREE.CylinderGeometry(0.28, 0.28, 0.28, 10), rimMat);
    rim.rotation.z = Math.PI/2;
    wg.add(rim);
    // 5 spokes
    for (let s = 0; s < 5; s++) {
      const spoke = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.5, 0.05), rimMat);
      spoke.rotation.z = Math.PI/2;
      spoke.rotation.x = (s/5)*Math.PI*2;
      spoke.position.y = Math.sin((s/5)*Math.PI*2)*0.14;
      spoke.position.z = Math.cos((s/5)*Math.PI*2)*0.14;
      wg.add(spoke);
    }
    wg.position.set(wx, wy, wz);
    wg.userData.isWheel = true;
    carGroup.add(wg);
  });

  carGroup.position.copy(carPos);
  carGroup.position.y = 0;
  scene.add(carGroup);
}

// ─────────────────────────────────────────
//  GAME LOOP
// ─────────────────────────────────────────
const ACCEL = 0.055, FRIC = 0.88, MAX_SPD = 0.55, TURN = 0.038;

function animate() {
  requestAnimationFrame(animate);
  frame++;
  const dt = clock.getDelta();

  // Drive
  if (!modalOpen) {
    const U = keys['ArrowUp']   || keys['w'] || keys['W'];
    const D = keys['ArrowDown']  || keys['s'] || keys['S'];
    const L = keys['ArrowLeft']  || keys['a'] || keys['A'];
    const R = keys['ArrowRight'] || keys['d'] || keys['D'];

    if (U) carSpeed = Math.min(carSpeed + ACCEL, MAX_SPD);
    else if (D) carSpeed = Math.max(carSpeed - ACCEL, -MAX_SPD*0.5);
    else carSpeed *= FRIC;

    if (Math.abs(carSpeed) > 0.005) {
      const dir = carSpeed > 0 ? 1 : -1;
      if (L) carAngle += TURN * dir;
      if (R) carAngle -= TURN * dir;
    }

    const dx = Math.sin(carAngle) * carSpeed;
    const dz = Math.cos(carAngle) * carSpeed;
    const newX = carPos.x + dx;
    const newZ = carPos.z + dz;

    // Collision vs all buildings
    let blocked = false;
    const testPt = new THREE.Vector2(newX, newZ);
    for (const b of buildings) {
      if (b.bbox.containsPoint(testPt)) { blocked = true; break; }
    }
    // World boundary
    if (Math.abs(newX) > CITY_SIZE/2 - 2 || Math.abs(newZ) > CITY_SIZE/2 - 2) blocked = true;

    if (!blocked) {
      carPos.x = newX; carPos.z = newZ;
    } else {
      carSpeed *= -0.3;
    }

    carGroup.position.x = carPos.x;
    carGroup.position.z = carPos.z;
    carGroup.rotation.y = carAngle;

    // Spin wheels
    carGroup.children.forEach(c => {
      if (c.userData.isWheel) {
        c.children[0].rotation.x += carSpeed * 2.2;
      }
    });
  }

  // Camera follows car (orbit style)
  CAM_TARGET.lerp(new THREE.Vector3(carPos.x, 1.5, carPos.z), 0.1);
  updateCamera();

  // Entrance detection
  nearEntry = null;
  let bestD = 9999;
  buildings.forEach(b => {
    const dx = carPos.x - b.entranceWorld.x;
    const dz = carPos.z - b.entranceWorld.z;
    const d = Math.sqrt(dx*dx + dz*dz);
    if (d < 4.5 && d < bestD) { nearEntry = b; bestD = d; }

    // Entrance marker pulse
    const isN = (nearEntry === b);
    const pulse = 0.3 + (isN ? Math.abs(Math.sin(frame * 0.06)) * 0.7 : 0);
    if (b.group.userData.entranceMarker) {
      b.group.userData.entranceMarker.material.opacity = pulse;
    }
  });

  // HUD
  document.getElementById('spd-fill').style.width = (Math.abs(carSpeed)/MAX_SPD*100).toFixed(0) + '%';
  const nearDiv = document.getElementById('hud-nearby');
  const promptDiv = document.getElementById('hud-prompt');
  if (nearEntry) {
    nearDiv.innerHTML = 'At entrance: <span>' + nearEntry.project.name + '</span>';
    promptDiv.style.display = 'block';
  } else {
    nearDiv.textContent = 'Navigate to a project entrance';
    promptDiv.style.display = 'none';
  }

  drawMinimap();
  renderer.render(scene, camera);
}

// ─────────────────────────────────────────
//  MINIMAP
// ─────────────────────────────────────────
function drawMinimap() {
  const mw = 130, mh = 130;
  mmCtx.fillStyle = '#080c14';
  mmCtx.fillRect(0, 0, mw, mh);
  const scale = mw / CITY_SIZE;
  const ox = mw/2, oz = mh/2;

  buildings.forEach(b => {
    const px = ox + b.entranceWorld.x * scale;
    const pz = oz + b.entranceWorld.z * scale;
    const isN = b === nearEntry;
    mmCtx.fillStyle = b.project.hex;
    mmCtx.globalAlpha = isN ? 1 : 0.65;
    mmCtx.beginPath();
    mmCtx.arc(px, pz, isN ? 4 : 2.8, 0, Math.PI*2);
    mmCtx.fill();
    mmCtx.globalAlpha = 1;
  });

  // Car
  const cpx = ox + carPos.x * scale;
  const cpz = oz + carPos.z * scale;
  mmCtx.save();
  mmCtx.translate(cpx, cpz);
  mmCtx.rotate(-carAngle);
  mmCtx.fillStyle = '#ffffff';
  mmCtx.fillRect(-2.5, -4, 5, 8);
  mmCtx.fillStyle = '#aaddff';
  mmCtx.fillRect(-2, -4, 4, 3);
  mmCtx.restore();

  // Border
  mmCtx.strokeStyle = 'rgba(74,144,217,.2)';
  mmCtx.lineWidth = 1;
  mmCtx.strokeRect(0, 0, mw, mh);
}

// ─────────────────────────────────────────
//  MODAL
// ─────────────────────────────────────────
function openModal(b) {
  modalOpen = true;
  const p = b.project;
  document.getElementById('mo-ico').textContent = p.icon;
  document.getElementById('mo-ico').style.background = p.hex + '18';
  document.getElementById('mo-ico').style.border = '1px solid ' + p.hex + '33';
  const catEl = document.getElementById('mo-cat');
  catEl.textContent = p.cat;
  catEl.style.color = p.hex;
  document.getElementById('mo-name').textContent = p.name;
  document.getElementById('mo-stack').textContent = p.stack;
  document.getElementById('mo-desc').textContent = p.desc;
  document.getElementById('mo-tags').innerHTML = p.tags.map(t => '<span class="mo-tag">' + t + '</span>').join('');
  let btns = '';
  if (p.gh)   btns += '<a class="mo-btn-gh" href="' + p.gh + '" target="_blank">View on GitHub</a>';
  if (p.live) btns += '<a class="mo-btn-live" href="' + p.live + '" target="_blank">Live Demo →</a>';
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

// ─────────────────────────────────────────
//  INPUT
// ─────────────────────────────────────────
function bindInput() {
  document.addEventListener('keydown', e => {
    keys[e.key] = true;
    if ((e.key === 'Enter' || e.key === ' ') && nearEntry && !modalOpen) {
      e.preventDefault(); openModal(nearEntry);
    }
    if (e.key === 'Escape' && modalOpen) closeModal();
  });
  document.addEventListener('keyup', e => { keys[e.key] = false; });

  // Mouse camera orbit
  const c = document.getElementById('c');
  c.addEventListener('mousedown', e => {
    isDragging = true; lastMX = e.clientX; lastMY = e.clientY;
  });
  window.addEventListener('mouseup', () => { isDragging = false; });
  window.addEventListener('mousemove', e => {
    if (!isDragging) return;
    const dx = e.clientX - lastMX;
    const dy = e.clientY - lastMY;
    camTheta -= dx * 0.006;
    camPhi = Math.max(0.25, Math.min(1.45, camPhi + dy * 0.006));
    lastMX = e.clientX; lastMY = e.clientY;
  });
  // Touch camera orbit
  let lastTX = 0, lastTY = 0;
  c.addEventListener('touchstart', e => { lastTX = e.touches[0].clientX; lastTY = e.touches[0].clientY; }, {passive:true});
  c.addEventListener('touchmove', e => {
    if (e.touches.length !== 1) return;
    const dx = e.touches[0].clientX - lastTX;
    const dy = e.touches[0].clientY - lastTY;
    camTheta -= dx * 0.006;
    camPhi = Math.max(0.25, Math.min(1.45, camPhi + dy * 0.006));
    lastTX = e.touches[0].clientX; lastTY = e.touches[0].clientY;
  }, {passive:true});
  // Scroll to zoom
  c.addEventListener('wheel', e => {
    camRadius = Math.max(15, Math.min(90, camRadius + e.deltaY * 0.04));
  }, {passive:true});
}

function showToast(msg) {
  const t = document.createElement('div');
  t.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:#4a90d9;color:#fff;border-radius:8px;padding:8px 20px;font-size:11px;font-weight:600;z-index:200;animation:tf 3s ease forwards;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap';
  t.textContent = msg;
  const style = document.createElement('style');
  style.textContent = '@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}10%,75%{opacity:1;transform:translateX(-50%) translateY(0)}100%{opacity:0}}';
  document.head.appendChild(style);
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3100);
}
</script>
</body>
</html>"""

components.html(HTML, height=760, scrolling=False)
