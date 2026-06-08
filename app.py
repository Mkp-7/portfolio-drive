import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfolio | Mkp-7", page_icon="🚗", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"]{background:#060a12}
iframe{border:none!important}
</style>""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100vh;overflow:hidden;background:#060a12;font-family:'Segoe UI',system-ui,sans-serif}

/* INTRO */
#intro{position:fixed;inset:0;background:#060a12;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;padding:24px}
.i-eye{font-size:10px;letter-spacing:4px;color:#4a90d9;text-transform:uppercase;margin-bottom:10px}
.i-name{font-size:44px;font-weight:700;color:#eef2ff;letter-spacing:-1px;margin-bottom:5px}
.i-role{font-size:12px;color:#5a6e90;letter-spacing:2px;text-transform:uppercase;margin-bottom:28px}
.i-div{width:36px;height:2px;background:#4a90d9;margin:0 auto 24px}
.i-districts{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:520px;margin-bottom:20px}
.i-dist{display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:6px;padding:6px 12px;font-size:11px;color:#6b7fa8}
.i-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.i-hint{font-size:11px;color:#3a4d68;text-align:center;line-height:2;margin-bottom:22px;max-width:380px}
.i-btn{background:#4a90d9;border:none;border-radius:8px;color:#fff;font-size:13px;font-weight:600;padding:12px 36px;cursor:pointer;letter-spacing:1px;text-transform:uppercase;transition:all .18s}
.i-btn:hover{background:#5aa0e9;transform:translateY(-1px)}

/* CANVAS */
#c{display:block;width:100%;height:100vh}

/* HUD */
#hud{position:fixed;top:18px;left:18px;display:none;z-index:50;min-width:196px}
.hud-box{background:rgba(6,10,18,.9);border:1px solid rgba(74,144,217,.15);border-radius:12px;padding:13px 16px;backdrop-filter:blur(16px);margin-bottom:6px}
.hud-lbl{font-size:9px;letter-spacing:2px;color:#2e3f5c;text-transform:uppercase;margin-bottom:1px}
.hud-val{font-size:12px;font-weight:600;color:#c8d8f0}
.hud-acc{color:#4a90d9}
.hud-sep{height:1px;background:rgba(255,255,255,.05);margin:8px 0}
.hud-bar{height:2px;background:rgba(255,255,255,.06);border-radius:1px;overflow:hidden;margin:5px 0 8px}
.hud-bfill{height:100%;background:#4a90d9;border-radius:1px;transition:width .08s;width:0%}
.hud-proj{font-size:10px;color:#3a4d68;min-height:13px}
.hud-proj span{font-weight:600}
.hud-enter{font-size:11px;font-weight:700;color:#f5c842;margin-top:4px;display:none;animation:blink .9s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.4}}
.hud-visited{font-size:10px;color:#3ecf8e;margin-top:5px}

/* MINIMAP */
#mm-wrap{position:fixed;bottom:18px;right:18px;display:none;z-index:50}
.mm-lbl{font-size:9px;letter-spacing:2px;color:#2e3f5c;text-transform:uppercase;text-align:center;margin-bottom:4px}
#mm{border-radius:10px;border:1px solid rgba(74,144,217,.15)}

/* HINT */
#hint-box{position:fixed;bottom:18px;left:18px;display:none;background:rgba(6,10,18,.85);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:8px 14px;font-size:10px;color:#3a4d68;z-index:50;line-height:2}

/* MODAL */
#ov{position:fixed;inset:0;background:rgba(0,0,0,.82);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(14px)}
#mo{background:#0b1120;border:1px solid rgba(74,144,217,.18);border-radius:16px;padding:26px;max-width:480px;width:92%;position:relative;max-height:88vh;overflow-y:auto;animation:moin .2s ease}
@keyframes moin{from{transform:translateY(14px);opacity:0}to{transform:translateY(0);opacity:1}}
.mo-close{position:absolute;top:14px;right:14px;width:28px;height:28px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);color:#6b7fa8;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}
.mo-close:hover{background:rgba(255,255,255,.1);color:#eef2ff}
.mo-head{display:flex;align-items:flex-start;gap:13px;margin-bottom:14px}
.mo-ico{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0}
.mo-eye{font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}
.mo-name{font-size:16px;font-weight:700;color:#eef2ff;line-height:1.3;margin-bottom:4px}
.mo-stack{font-size:10px;color:#6b7fa8}
.mo-dist{display:inline-block;font-size:9px;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px}
.mo-desc{font-size:12.5px;color:#8a9bb8;line-height:1.78;margin-bottom:14px}
.mo-tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:16px}
.mo-tag{font-size:10px;color:#6b7fa8;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:4px;padding:3px 9px}
.mo-btns{display:flex;gap:8px;flex-wrap:wrap}
.mo-gh{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:600;text-align:center;text-decoration:none;background:rgba(255,255,255,.05);color:#c8d8f0;border:1px solid rgba(255,255,255,.1);display:block;transition:background .15s;letter-spacing:.5px;text-transform:uppercase}
.mo-gh:hover{background:rgba(255,255,255,.1)}
.mo-live{flex:1;min-width:110px;padding:10px;border-radius:8px;font-size:11px;font-weight:700;text-align:center;text-decoration:none;background:#4a90d9;color:#fff;border:none;display:block;letter-spacing:.5px;text-transform:uppercase;transition:opacity .15s}
.mo-live:hover{opacity:.88}
</style>
</head>
<body>
<div id="intro">
  <div class="i-eye">Interactive Portfolio</div>
  <div class="i-name">Mkp-7</div>
  <div class="i-role">Data Scientist &amp; AI Engineer</div>
  <div class="i-div"></div>
  <div class="i-districts">
    <div class="i-dist"><div class="i-dot" style="background:#4a90d9"></div>Retail &amp; Commerce</div>
    <div class="i-dist"><div class="i-dot" style="background:#e85555"></div>Finance &amp; Banking</div>
    <div class="i-dist"><div class="i-dot" style="background:#f5a623"></div>Operations &amp; Logistics</div>
    <div class="i-dist"><div class="i-dot" style="background:#3ecf8e"></div>Healthcare &amp; Life Sciences</div>
    <div class="i-dist"><div class="i-dot" style="background:#9b6dff"></div>Research &amp; Education</div>
  </div>
  <div class="i-hint">
    <strong style="color:#c8d8f0">W A S D</strong> / Arrows — Drive &nbsp;·&nbsp; City is divided into <strong style="color:#c8d8f0">5 districts</strong><br>
    Drive into the <strong style="color:#c8d8f0">glowing zone</strong> in front of each building<br>
    Press <strong style="color:#c8d8f0">Enter</strong> to open the project · Explore all <strong style="color:#c8d8f0">18</strong>
  </div>
  <button class="i-btn" onclick="startGame()">Enter Portfolio</button>
</div>

<canvas id="c"></canvas>

<div id="hud">
  <div class="hud-box">
    <div class="hud-lbl">Portfolio</div>
    <div class="hud-val hud-acc">Mkp-7</div>
    <div class="hud-sep"></div>
    <div class="hud-lbl">Speed</div>
    <div class="hud-bar"><div class="hud-bfill" id="spd-fill"></div></div>
    <div class="hud-proj" id="hud-proj">Navigate to a project</div>
    <div class="hud-enter" id="hud-enter">⏎ Press Enter to open</div>
    <div class="hud-visited" id="hud-visited">0 / 18 explored</div>
  </div>
</div>

<div id="mm-wrap">
  <div class="mm-lbl">City Map</div>
  <canvas id="mm" width="140" height="140"></canvas>
</div>

<div id="hint-box">
  <span style="color:#c8d8f0">W A S D</span> / Arrows — Drive &nbsp;·&nbsp; <span style="color:#c8d8f0">Enter</span> — Open project
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
// ─── DISTRICTS ───────────────────────────────────────────────
const DISTRICTS = {
  retail:    {name:"Retail & Commerce",      color:0x4a90d9, hex:"#4a90d9", particles:"retail"},
  finance:   {name:"Finance & Banking",      color:0xe85555, hex:"#e85555", particles:"finance"},
  ops:       {name:"Operations & Logistics", color:0xf5a623, hex:"#f5a623", particles:"ops"},
  health:    {name:"Healthcare & Life Sci.", color:0x3ecf8e, hex:"#3ecf8e", particles:"health"},
  research:  {name:"Research & Education",   color:0x9b6dff, hex:"#9b6dff", particles:"research"},
};

// ─── PROJECTS ────────────────────────────────────────────────
const PROJECTS = [
  // RETAIL & COMMERCE (5) — col 0-4, row 0
  {name:"AI Pricing Intelligence",      icon:"🤖", district:"retail",   stat:"20+ SKUs · 95% accuracy",   cat:"Streamlit Application",  stack:"Python · Claude API",              desc:"Competitive pricing agent using the Claude API to automate real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Surfaced 12–15% margin improvement opportunities.",                                                                                                                                                                       tags:["Claude API","Price Monitoring","Competitive Intel","ML"],                          gh:"https://github.com/Mkp-7/AI-Pricing-Agent",                                       live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"Retail Intelligence Platform", icon:"🛒", district:"retail",   stat:"4 AI modules · Live app",   cat:"Streamlit Application",  stack:"Python · Groq LLM · Yelp Dataset", desc:"AI-native customer intelligence platform converting public review data into operational insights. Four modules: Voice of Customer AI, Store Pulse Map (regional benchmarking), Test & Learn Autopilot (A/B statistical significance), and Analyst Copilot (plain-English Q&A chatbot).",                                                                                                                                                              tags:["Groq LLM","NLP","Plotly","A/B Testing","Customer Analytics"],                     gh:"https://github.com/Mkp-7/retail-intelligence-platform",                           live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"},
  {name:"Retail Customer Analytics",    icon:"🛍️", district:"retail",   stat:"25K products · -40% time",  cat:"ML & Python",            stack:"Python · Scikit-learn · K-Means",  desc:"Analyzed 25,000+ product records and 10,000+ customer transactions. K-Means clustering (5 segments) identified top 20% of customers contributing 60% of revenue. Automated Excel reporting dashboard tracking 10+ KPIs, reducing manual analysis time by 40%.",                                                                                                                                                                                       tags:["K-Means","Customer Segmentation","RFM","Pandas","Excel Automation"],               gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",              live:""},
  {name:"E-Commerce Funnel Analytics",  icon:"📈", district:"retail",   stat:"269K users · $25K revenue", cat:"Looker · dbt · BigQuery", stack:"dbt · BigQuery · GA4 · Looker",   desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling and behavioral segmentation across 269K users. Identified 9,630 cart abandonment targets. Simulated email recovery campaign projecting 23% recovery rate vs 8% baseline and $25K incremental revenue.",                                                                                                                                                                          tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","$25K Revenue"],               gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",                                live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"},
  {name:"Sales & Demand Forecasting",   icon:"📊", district:"retail",   stat:"94% accuracy · 25K SKUs",   cat:"Tableau Dashboard",      stack:"Python · ARIMA · SARIMA · Tableau",desc:"Fine-tuned ARIMA and SARIMA models forecasting 6-month revenue for 25,432 products across 12 regions at 94% accuracy. Identified top 20% of customers contributing 62% of revenue. Interactive Tableau and Power BI dashboards for pricing and promotion strategy.",                                                                                                                                                                                 tags:["ARIMA","SARIMA","94% Accuracy","Tableau","Power BI"],                              gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",                             live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"},
  // FINANCE & BANKING (3) — col 0-2, row 1
  {name:"Banking Risk Intelligence",    icon:"🏦", district:"finance",  stat:"4500+ banks · AUC 0.84",    cat:"Streamlit Application",  stack:"Python · FDIC API · FRED",         desc:"Operational risk monitoring platform querying FDIC data for 4,500+ banks. Calculates 5 risk KRIs against Basel III and CCAR thresholds. Applies Random Forest (AUC = 0.84) and Gradient Boosting for bank failure prediction. Integrates Fed Funds Rate and yield-curve signals from FRED.",                                                                                                                                                     tags:["Basel III","FDIC API","FRED","Random Forest AUC=0.84","CCAR"],                    gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",                                 live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Banking Client Analysis",      icon:"💳", district:"finance",  stat:"3000 clients · $0.9B loans", cat:"Power BI Dashboard",    stack:"Power BI · SQL · Python",          desc:"Structured 3,000 banking client records integrating portfolio, relationship, and product-level dimensions. Dashboard identifies high-fee accounts (~51% of deposits), Private Bank loan exposure (~$0.9B), and cross-segment variation for risk assessment and regulatory reporting.",                                                                                                                                                              tags:["Power BI","Client Segmentation","Portfolio Analytics","Risk Assessment"],          gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",     live:""},
  {name:"Insurance Claims Prediction",  icon:"🛡️", district:"finance",  stat:"58K records · 94% accuracy", cat:"Power BI + ML",         stack:"R · SQL Server · Power BI",        desc:"Processed 58,000+ insurance policy records in SQL Server. Random Forest and Logistic Regression in R achieving 94% accuracy for 6-month claim likelihood prediction. Power BI dashboard tracks predicted claim probability by vehicle segment, fuel type, and policyholder demographics.",                                                                                                                                                        tags:["Random Forest","94% Accuracy","SQL Server","R","Power BI"],                        gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",                              live:""},
  // OPERATIONS & LOGISTICS (4) — col 0-3, row 2
  {name:"Revenue Intelligence Agent",   icon:"🚗", district:"ops",      stat:"10 airports · -3hrs→15min", cat:"Streamlit Application",  stack:"Python · Groq LLM · GitHub Actions",desc:"Autonomous multi-agent pipeline monitoring competitor car-rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals. Reduces analyst workflow from 3 hours to 15 minutes. 5-tab Streamlit dashboard with anomaly flagging and urgency-ranked pricing recommendations.",                                                                                                                   tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","SQLite"],                      gh:"https://github.com/Mkp-7/Revenue-Management-Agent",                               live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"EcoRoute Optimizer",           icon:"🌿", district:"ops",      stat:"60+ US cities · EPA method", cat:"Streamlit Application",  stack:"Python · Gemini AI · OR-Tools",    desc:"Logistics optimization platform generating carbon-minimized shipping routes across 60+ US cities. Evaluates diesel, EV, and rail freight via EPA SmartWay carbon methodology. Integrates OpenRouteService and OpenWeatherMap APIs, SQLite route caching, and a natural-language query interface.",                                                                                                                                                  tags:["Gemini AI","OR-Tools","Carbon Optimization","NLP","REST APIs"],                    gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",                                     live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Supply Chain Analytics",       icon:"📦", district:"ops",      stat:"10 datasets · 12+ KPIs",     cat:"Power BI Dashboard",     stack:"Power BI · Power Query · DAX",     desc:"Integrated 10 raw Excel supply chain datasets via Power Query ETL and built a star schema data model. Created 12+ DAX measures for KPIs including inventory turnover, stock aging, on-time delivery %, and reorder alerts. Includes logistics maps and drill-through analysis.",                                                                                                                                                                tags:["Power BI","DAX","Power Query","Star Schema","ETL","Inventory"],                    gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",                              live:""},
  {name:"Workforce Utilization",        icon:"👥", district:"ops",      stat:"80 employees · 3 months",    cat:"Power BI Dashboard",     stack:"Power BI · DAX · HR Analytics",    desc:"Dashboard analyzing attendance for 80 employees over 3 months, tracking presence, WFH utilization, and leave patterns. KPIs: attendance rate, WFH utilization, sick leave frequency. Identified mid-month attendance dips and a shift in peak days from Fridays to Mondays.",                                                                                                                                                                tags:["Power BI","HR Analytics","DAX","WFH Utilization","Workforce Planning"],            gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",                        live:""},
  // HEALTHCARE (2) — col 0-1, row 3
  {name:"Medmedia Analytics Hub",       icon:"🏥", district:"health",   stat:"470K trials · 35M papers",  cat:"Streamlit Application",  stack:"Python · LLMs · ClinicalTrials.gov",desc:"Healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables HCP audience segmentation across 10 clinical specialties and AI-generated content strategy.",                                                                                                                                                         tags:["Healthcare NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation"],         gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",                                 live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"},
  {name:"Diabetes Risk Prediction",     icon:"🩺", district:"health",   stat:"769 patients · 80% accuracy",cat:"ML & Python",           stack:"Python · SVM · Scikit-learn",      desc:"Multi-model diabetes prediction system trained on clinical data from 769 patients. Evaluated Logistic Regression, Decision Tree, Random Forest, and SVM. Achieved peak predictive accuracy of 80% with SVM. Applied feature selection and exploratory analysis throughout.",                                                                                                                                                                    tags:["SVM","Random Forest","Logistic Regression","Healthcare ML","Feature Selection"],   gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",                              live:""},
  // RESEARCH & EDUCATION (4) — col 0-3, row 4
  {name:"COVID-19 Global Impact",       icon:"🦠", district:"research", stat:"450K records · WHO data",   cat:"Exploratory Data Analysis",stack:"Python · EDA · WHO Data",         desc:"Global COVID-19 analysis using WHO data (~450,000 records). Covers mortality comparisons across WHO regions, global daily case and death trajectories, country-level outbreaks on peak days, and regional disparities in case fatality rates.",                                                                                                                                                                                               tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology","Data Storytelling"],        gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",                        live:""},
  {name:"MSU Collaboratory",            icon:"🎓", district:"research", stat:"3D network · MSU partners", cat:"Tableau Dashboard",      stack:"Tableau · 3D Network Graph",       desc:"3D network visualization of interdisciplinary activities and partnerships at Montclair State University. Tableau dashboard surfacing Collaboratory data insights across community partner organizations. Companion network graph on GitHub Pages showing cross-organizational collaboration topology.",                                                                                                                                              tags:["Tableau","3D Network Graph","MSU","Community Partners","GitHub Pages"],             gh:"https://mkp-7.github.io/Network-Graph/",                                          live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"},
  {name:"Student Wellbeing Study",      icon:"📋", district:"research", stat:"70 students · 21 days",     cat:"Tableau Dashboard",      stack:"Python · Statistics · Tableau",    desc:"Longitudinal study tracking 70 MSU students over 21 days. Collected daily activities, social context, location, and self-reported happiness (0–10) at 30-minute intervals. Conducted hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard identifies happiness patterns by activity category.",                                                                                                                                    tags:["Hypothesis Testing","ANOVA","Regression","Tableau","Behavioral Analytics"],        gh:"",                                                                                live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"},
  {name:"Book Recommendation Engine",   icon:"📚", district:"research", stat:"10K books · 1M+ ratings",   cat:"ML & Python",            stack:"Python · TF-IDF · SVD",            desc:"Recommendation engine trained on 10,000 books and 1M+ ratings. Employs TF-IDF with Cosine Similarity and SVD for personalized recommendations. Addresses cold start, scalability, and relevance challenges for accurate suggestions across diverse reader profiles.",                                                                                                                                                                          tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering","1M+ Ratings"],        gh:"https://github.com/Mkp-7/Book_Recommendation",                                    live:""},
];

// District row assignments
const DISTRICT_ROWS = {retail:0, finance:1, ops:2, health:3, research:4};
const ROW_COLS      = {0:5,       1:3,       2:4,   3:2,      4:4};
const ROW_STARTS    = {}; // computed below

// ─── SCENE STATE ────────────────────────────────────────────
let scene, camera, renderer, clock;
let carGroup, carWheels=[];
let buildings=[];
let nearEntry=null, modalOpen=false;
let keys={};
let carPos=new THREE.Vector3(0,0,110);
let carAngle=Math.PI, carSpeed=0;
let frame=0;
let mmCanvas,mmCtx;
let visitedSet=new Set();
let allParticles=[];

// Audio context
let audioCtx=null;
let engineOsc=null, engineGain=null;

// Camera
const CAM_BACK=11, CAM_UP=5.5, CAM_LAG=0.09;
let camPos=new THREE.Vector3(0,8,122);

// Layout constants
const BLK_X=24, BLK_Z=28, ROAD_W=10;
const CITY_H=150;

// ─── START ──────────────────────────────────────────────────
function startGame(){
  document.getElementById('intro').style.display='none';
  ['hud','mm-wrap','hint-box'].forEach(id=>document.getElementById(id).style.display='block');
  mmCanvas=document.getElementById('mm'); mmCtx=mmCanvas.getContext('2d');
  computeLayout();
  init3D();
  buildCity();
  buildCar();
  bindInput();
  initAudio();
  clock=new THREE.Clock();
  loop();
  toast('Drive into a glowing zone · Press Enter to explore a project');
}

// ─── LAYOUT ─────────────────────────────────────────────────
function computeLayout(){
  const ROWS=5;
  // centre each row
  for(let r=0;r<ROWS;r++){
    const cols=ROW_COLS[r];
    ROW_STARTS[r]=-((cols-1)*BLK_X)/2;
  }
}

function projectPos(p){
  const dist=p.district;
  const row=DISTRICT_ROWS[dist];
  // find index within district
  const distProjects=PROJECTS.filter(x=>x.district===dist);
  const col=distProjects.indexOf(p);
  const cols=ROW_COLS[row];
  const startX=ROW_STARTS[row];
  const startZ=-((5-1)*BLK_Z)/2; // 5 rows total
  return {x:startX+col*BLK_X, z:startZ+row*BLK_Z};
}

// ─── THREE INIT ─────────────────────────────────────────────
function init3D(){
  scene=new THREE.Scene();
  scene.background=new THREE.Color(0x060a12);
  scene.fog=new THREE.FogExp2(0x060a12,0.007);

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
  sun.position.set(60,100,40);
  sun.castShadow=true;
  sun.shadow.mapSize.set(4096,4096);
  sun.shadow.camera.near=1; sun.shadow.camera.far=400;
  sun.shadow.camera.left=sun.shadow.camera.bottom=-200;
  sun.shadow.camera.right=sun.shadow.camera.top=200;
  sun.shadow.bias=-0.0004;
  scene.add(sun);
  scene.add(new THREE.DirectionalLight(0x2233aa,0.3).position.set(-60,30,-60));
}

// ─── CITY ───────────────────────────────────────────────────
function buildCity(){
  // Ground
  const ground=new THREE.Mesh(
    new THREE.PlaneGeometry(CITY_H*2.5,CITY_H*2.5),
    new THREE.MeshLambertMaterial({color:0x080e1a})
  );
  ground.rotation.x=-Math.PI/2; ground.receiveShadow=true;
  scene.add(ground);
  scene.add(new THREE.GridHelper(CITY_H*2.4,110,0x0f1828,0x0a1120));

  makeRoads();
  makeDistrictZones();
  placeBuildings();
  makeDistrictSigns();
  placeLamps();
}

function makeRoads(){
  const rMat=new THREE.MeshLambertMaterial({color:0x0b0f18});
  const lMat=new THREE.MeshLambertMaterial({color:0x243050,emissive:0x152840,emissiveIntensity:0.45});
  const sMat=new THREE.MeshLambertMaterial({color:0x141d2c});

  const ROWS=5;
  const startZ=-((ROWS-1)*BLK_Z)/2;

  // Horizontal road per row + one before/after
  for(let r=-1;r<=ROWS;r++){
    const rz=startZ+r*BLK_Z-BLK_Z/2+BLK_Z/2;
    makeHRoad(rz,rMat,lMat,sMat);
  }
  // Vertical roads for max cols (5)
  const startX=-((5-1)*BLK_X)/2;
  for(let c=-1;c<=5;c++){
    const rx=startX+c*BLK_X-BLK_X/2+BLK_X/2;
    makeVRoad(rx,rMat,lMat,sMat);
  }
}

function makeHRoad(rz,rMat,lMat,sMat){
  const len=CITY_H*2.2;
  const r=new THREE.Mesh(new THREE.PlaneGeometry(len,ROAD_W),rMat);
  r.rotation.x=-Math.PI/2; r.position.set(0,0.05,rz); r.receiveShadow=true; scene.add(r);
  for(const oz of [-ROAD_W/2+0.3,ROAD_W/2-0.3]){
    const k=new THREE.Mesh(new THREE.BoxGeometry(len,0.16,0.32),sMat);
    k.position.set(0,0.08,rz+oz); scene.add(k);
  }
  for(let x=-len/2+3;x<len/2;x+=7){
    const d=new THREE.Mesh(new THREE.PlaneGeometry(3.2,0.2),lMat);
    d.rotation.x=-Math.PI/2; d.position.set(x,0.07,rz); scene.add(d);
  }
}

function makeVRoad(rx,rMat,lMat,sMat){
  const len=CITY_H*2.2;
  const r=new THREE.Mesh(new THREE.PlaneGeometry(ROAD_W,len),rMat);
  r.rotation.x=-Math.PI/2; r.position.set(rx,0.05,0); r.receiveShadow=true; scene.add(r);
  for(const ox of [-ROAD_W/2+0.3,ROAD_W/2-0.3]){
    const k=new THREE.Mesh(new THREE.BoxGeometry(0.32,0.16,len),sMat);
    k.position.set(rx+ox,0.08,0); scene.add(k);
  }
  for(let z=-len/2+3;z<len/2;z+=7){
    const d=new THREE.Mesh(new THREE.PlaneGeometry(0.2,3.2),lMat);
    d.rotation.x=-Math.PI/2; d.position.set(rx,0.07,z); scene.add(d);
  }
}

// Subtle colored ground zones per district
function makeDistrictZones(){
  const ROWS=5;
  const startZ=-((ROWS-1)*BLK_Z)/2;
  const distKeys=['retail','finance','ops','health','research'];
  distKeys.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[row];
    const startX=ROW_STARTS[row];
    const zoneW=cols*BLK_X+4, zoneD=BLK_Z-ROAD_W-1;
    const zone=new THREE.Mesh(
      new THREE.PlaneGeometry(zoneW,zoneD),
      new THREE.MeshLambertMaterial({color:dist.color,transparent:true,opacity:0.04})
    );
    zone.rotation.x=-Math.PI/2;
    zone.position.set(startX+(cols-1)*BLK_X/2, 0.06, startZ+row*BLK_Z);
    scene.add(zone);
  });
}

// District entry signs at top of each district zone
function makeDistrictSigns(){
  const ROWS=5;
  const startZ=-((ROWS-1)*BLK_Z)/2;
  const distKeys=['retail','finance','ops','health','research'];
  distKeys.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[row];
    const startX=ROW_STARTS[row];
    const cx=startX+(cols-1)*BLK_X/2;
    const rz=startZ+row*BLK_Z-BLK_Z/2+1;
    makeSignAt(cx,rz,dist.name,dist.color);
  });
}

function makeSignAt(x,z,label,color){
  const g=new THREE.Group();
  g.position.set(x,0,z);

  // Two poles
  const pMat=new THREE.MeshLambertMaterial({color:0x444d60});
  for(const ox of [-3,3]){
    const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.1,0.12,4,8),pMat);
    pole.position.set(ox,2,0); g.add(pole);
  }
  // Sign board
  const board=new THREE.Mesh(new THREE.BoxGeometry(7,1.1,0.18),
    new THREE.MeshLambertMaterial({color:0x0b1220}));
  board.position.set(0,4.15,0); g.add(board);

  // Colored top strip
  const strip=new THREE.Mesh(new THREE.BoxGeometry(7,0.18,0.22),
    new THREE.MeshLambertMaterial({color,emissive:color,emissiveIntensity:0.6}));
  strip.position.set(0,4.74,0); g.add(strip);

  // Canvas label
  const can=document.createElement('canvas');
  can.width=512; can.height=80;
  const ctx=can.getContext('2d');
  ctx.clearRect(0,0,512,80);
  ctx.font='bold 32px Segoe UI, Arial';
  ctx.fillStyle='#c8d8f0';
  ctx.textAlign='center'; ctx.textBaseline='middle';
  ctx.fillText(label.toUpperCase(),256,40);
  const tex=new THREE.CanvasTexture(can);
  const sign=new THREE.Mesh(new THREE.PlaneGeometry(6.5,0.9),
    new THREE.MeshBasicMaterial({map:tex,transparent:true}));
  sign.position.set(0,4.15,0.1); g.add(sign);

  // Glow light
  const pl=new THREE.PointLight(color,0.5,14);
  pl.position.set(0,4.5,1); g.add(pl);

  scene.add(g);
}

// ─── BUILDINGS ──────────────────────────────────────────────
function placeBuildings(){
  PROJECTS.forEach((p,i)=>{
    const {x,z}=projectPos(p);
    const bld=makeBuilding(p,x,z,i);
    buildings.push(bld);
  });
}

function makeBuilding(p,bx,bz,idx){
  const dist=DISTRICTS[p.district];
  const hexColor=dist.color;
  const style=idx%4;
  const bH=9+(idx%7)*3.2;
  const bW=7.5, bD=6.5;

  const g=new THREE.Group();
  g.position.set(bx,0,bz);

  // Pavement
  const pave=new THREE.Mesh(new THREE.BoxGeometry(bW+3,0.2,bD+3),
    new THREE.MeshLambertMaterial({color:0x101828}));
  pave.position.y=0.1; pave.receiveShadow=true; g.add(pave);

  // Main body
  const body=new THREE.Mesh(new THREE.BoxGeometry(bW,bH,bD),
    new THREE.MeshLambertMaterial({color:0x0e1626}));
  body.position.y=bH/2+0.2; body.castShadow=true; body.receiveShadow=true; g.add(body);

  // Style details
  if(style===0){
    const gMat=new THREE.MeshLambertMaterial({color:hexColor,emissive:hexColor,emissiveIntensity:0.06,transparent:true,opacity:0.78});
    const s=new THREE.Mesh(new THREE.BoxGeometry(bW-1,bH,0.09),gMat);
    s.position.set(0,bH/2+0.2,bD/2+0.05); g.add(s);
    const s2=s.clone(); s2.position.z=-bD/2-0.05; g.add(s2);
  } else if(style===1){
    for(let b=1;b<Math.floor(bH/2.8);b++){
      const band=new THREE.Mesh(new THREE.BoxGeometry(bW+0.1,0.16,bD+0.1),
        new THREE.MeshLambertMaterial({color:hexColor,emissive:hexColor,emissiveIntensity:0.14}));
      band.position.y=0.2+b*2.8; g.add(band);
    }
  } else if(style===2){
    const cMat=new THREE.MeshLambertMaterial({color:0x1a2840});
    for(const [cx,cz] of [[-bW/2+0.4,-bD/2+0.4],[bW/2-0.4,-bD/2+0.4],[-bW/2+0.4,bD/2-0.4],[bW/2-0.4,bD/2-0.4]]){
      const col=new THREE.Mesh(new THREE.BoxGeometry(0.65,bH,0.65),cMat);
      col.position.set(cx,bH/2+0.2,cz); g.add(col);
    }
  } else {
    const top=new THREE.Mesh(new THREE.BoxGeometry(bW*0.62,bH*0.38,bD*0.62),
      new THREE.MeshLambertMaterial({color:0x0e1626}));
    top.position.y=bH+bH*0.38/2-0.4; top.castShadow=true; g.add(top);
    const ledge=new THREE.Mesh(new THREE.BoxGeometry(bW+0.3,0.28,bD+0.3),
      new THREE.MeshLambertMaterial({color:hexColor,emissive:hexColor,emissiveIntensity:0.22}));
    ledge.position.y=bH+0.2; g.add(ledge);
  }

  addWindows(g,bW,bH,bD);

  // Rooftop bar
  const roofBar=new THREE.Mesh(new THREE.BoxGeometry(bW,0.3,bD),
    new THREE.MeshLambertMaterial({color:hexColor,emissive:hexColor,emissiveIntensity:0.55}));
  roofBar.position.y=bH+0.38; g.add(roofBar);
  const roofLight=new THREE.PointLight(hexColor,0.65,22);
  roofLight.position.set(0,bH+2,0); g.add(roofLight);

  // ── BUILDING POSTER ──
  makePoster(g,p,dist,bW,bH,bD);

  // ── FLOATING PARTICLES ──
  const particleGroup=makeParticles(p.district,hexColor,bW,bH);
  particleGroup.position.set(0,0,0);
  g.add(particleGroup);
  allParticles.push(particleGroup);

  // ── ENTRANCE ZONE ──
  const eZ=bD/2+3.6;

  // Road label
  const labelTex=makeRoadTex(p.name,dist.hex);
  const label=new THREE.Mesh(new THREE.PlaneGeometry(9.5,2),
    new THREE.MeshBasicMaterial({map:labelTex,transparent:true,depthWrite:false}));
  label.rotation.x=-Math.PI/2; label.position.set(0,0.11,eZ+3.8); g.add(label);

  // Entrance plane
  const eMat=new THREE.MeshBasicMaterial({color:hexColor,transparent:true,opacity:0.14,depthWrite:false});
  const ePlane=new THREE.Mesh(new THREE.PlaneGeometry(5.5,3.2),eMat);
  ePlane.rotation.x=-Math.PI/2; ePlane.position.set(0,0.12,eZ); g.add(ePlane);

  // Entrance border lines
  const fMat=new THREE.MeshBasicMaterial({color:hexColor,transparent:true,opacity:0.5});
  [[5.5,0.1,0,eZ-1.6],[5.5,0.1,0,eZ+1.6],[0.1,3.2,-2.75,eZ],[0.1,3.2,2.75,eZ]].forEach(([fw,fh,fx,fz_])=>{
    const line=new THREE.Mesh(new THREE.PlaneGeometry(fw,fh),fMat.clone());
    line.rotation.x=-Math.PI/2; line.position.set(fx,0.13,fz_); g.add(line);
  });

  // Corner posts
  const postMat=new THREE.MeshLambertMaterial({color:hexColor,emissive:hexColor,emissiveIntensity:0.65});
  for(const [px,pz_] of [[-2.5,eZ-1.4],[2.5,eZ-1.4],[-2.5,eZ+1.4],[2.5,eZ+1.4]]){
    const post=new THREE.Mesh(new THREE.CylinderGeometry(0.07,0.07,1.0,8),postMat.clone());
    post.position.set(px,0.5,pz_); g.add(post);
    const ball=new THREE.Mesh(new THREE.SphereGeometry(0.11,8,8),postMat.clone());
    ball.position.set(px,1.1,pz_); g.add(ball);
  }

  // Entrance light
  const eLight=new THREE.PointLight(hexColor,0,12);
  eLight.position.set(0,0.4,eZ); g.add(eLight);

  const entranceWorld=new THREE.Vector3(bx,0,bz+eZ);
  const bbox=new THREE.Box2(
    new THREE.Vector2(bx-bW/2-0.5,bz-bD/2-0.5),
    new THREE.Vector2(bx+bW/2+0.5,bz+bD/2+0.5)
  );

  scene.add(g);
  return {group:g, bbox, entranceWorld, project:p,
          eMat, eLight, visited:false,
          distColor:hexColor, distHex:dist.hex};
}

// ── POSTER ON BUILDING FACE ──────────────────────────────────
function makePoster(g,p,dist,bW,bH,bD){
  const can=document.createElement('canvas');
  can.width=512; can.height=320;
  const ctx=can.getContext('2d');

  // Background
  ctx.fillStyle='#0b1220';
  ctx.fillRect(0,0,512,320);

  // Top color bar
  ctx.fillStyle=dist.hex;
  ctx.fillRect(0,0,512,12);

  // Icon
  ctx.font='56px serif';
  ctx.textAlign='center';
  ctx.fillText(p.icon,256,86);

  // Project name
  ctx.font='bold 32px Segoe UI, Arial';
  ctx.fillStyle='#eef2ff';
  ctx.textAlign='center';
  ctx.textBaseline='top';
  let name=p.name;
  if(ctx.measureText(name).width>480) name=name.slice(0,22)+'…';
  ctx.fillText(name,256,110);

  // Stat line
  ctx.font='22px Segoe UI, Arial';
  ctx.fillStyle=dist.hex;
  ctx.fillText(p.stat,256,162);

  // District label
  ctx.font='16px Segoe UI, Arial';
  ctx.fillStyle='rgba(200,216,240,0.5)';
  ctx.fillText(dist.name.toUpperCase(),256,205);

  // Bottom bar
  ctx.fillStyle=dist.hex;
  ctx.globalAlpha=0.25;
  ctx.fillRect(0,308,512,12);
  ctx.globalAlpha=1;

  const tex=new THREE.CanvasTexture(can);
  // Front face poster
  const poster=new THREE.Mesh(
    new THREE.PlaneGeometry(bW*0.82,bH*0.48),
    new THREE.MeshBasicMaterial({map:tex,transparent:true})
  );
  poster.position.set(0,bH*0.52,bD/2+0.08); g.add(poster);
  // Rear poster
  const poster2=poster.clone();
  poster2.position.z=-bD/2-0.08;
  poster2.rotation.y=Math.PI; g.add(poster2);
}

// ── FLOATING DOMAIN PARTICLES ────────────────────────────────
function makeParticles(districtKey,color,bW,bH){
  const group=new THREE.Group();
  const count=18;
  const mat=new THREE.MeshBasicMaterial({color,transparent:true,opacity:0.0});

  for(let i=0;i<count;i++){
    let geo;
    // Different shapes per district
    if(districtKey==='retail')       geo=new THREE.BoxGeometry(0.18,0.18,0.18);      // data cubes
    else if(districtKey==='finance') geo=new THREE.ConeGeometry(0.12,0.28,4);        // trend arrows (diamonds)
    else if(districtKey==='ops')     geo=new THREE.CylinderGeometry(0.06,0.06,0.3,6);// pipeline tubes
    else if(districtKey==='health')  geo=new THREE.SphereGeometry(0.12,8,8);         // cell spheres
    else                             geo=new THREE.TetrahedronGeometry(0.14);         // research nodes

    const mesh=new THREE.Mesh(geo,mat.clone());
    // Random spread around building
    const angle=Math.random()*Math.PI*2;
    const radius=2+Math.random()*3.5;
    mesh.position.set(
      Math.cos(angle)*radius,
      1.5+Math.random()*bH*0.85,
      Math.sin(angle)*radius
    );
    mesh.userData={
      baseAngle:angle,
      radius,
      speed:0.004+Math.random()*0.006,
      ySpeed:0.008+Math.random()*0.01,
      yBase:mesh.position.y,
      yAmp:0.6+Math.random()*1.2,
      phase:Math.random()*Math.PI*2,
      color,
    };
    group.add(mesh);
  }
  group.userData.isParticleGroup=true;
  return group;
}

// ── ROAD LABEL TEXTURE ───────────────────────────────────────
function makeRoadTex(text,hexColor){
  const can=document.createElement('canvas');
  can.width=512; can.height=112;
  const ctx=can.getContext('2d');
  ctx.clearRect(0,0,512,112);
  ctx.font='bold 34px Segoe UI, Arial';
  ctx.fillStyle=hexColor;
  ctx.textAlign='center'; ctx.textBaseline='middle';
  let label=text;
  while(ctx.measureText(label).width>490&&label.length>4) label=label.slice(0,-1);
  if(label!==text) label=label.trim()+'…';
  ctx.fillText(label,256,56);
  return new THREE.CanvasTexture(can);
}

// ── WINDOWS ─────────────────────────────────────────────────
function addWindows(g,bW,bH,bD){
  const litMat=new THREE.MeshLambertMaterial({color:0xfff0b0,emissive:0xfff0b0,emissiveIntensity:0.65});
  const darkMat=new THREE.MeshLambertMaterial({color:0x0a1020});
  const cols=3, rows=Math.max(2,Math.floor((bH-1.5)/2.2));
  const gapX=(bW-1.8)/(cols-1);
  const gapY=(bH-1.5)/(rows+1);
  for(let r=0;r<rows;r++){
    for(let c=0;c<cols;c++){
      const wx=-bW/2+0.9+c*gapX;
      const wy=0.2+gapY+r*gapY;
      const lit=Math.random()>0.32;
      const wf=new THREE.Mesh(new THREE.BoxGeometry(0.62,0.82,0.07),lit?litMat:darkMat);
      wf.position.set(wx,wy,bD/2+0.04); g.add(wf);
      const wb=wf.clone(); wb.position.z=-bD/2-0.04; g.add(wb);
    }
  }
}

// ── LAMPS ────────────────────────────────────────────────────
function placeLamps(){
  const pMat=new THREE.MeshLambertMaterial({color:0x606878});
  const bMat=new THREE.MeshLambertMaterial({color:0xffeedd,emissive:0xffeedd,emissiveIntensity:1});
  const ROWS=5;
  const startZ=-((ROWS-1)*BLK_Z)/2;
  for(let c=-1;c<=5;c++){
    for(let r=-1;r<=ROWS;r++){
      const lx=ROW_STARTS[0]+c*BLK_X-BLK_X/2;
      const lz=startZ+r*BLK_Z-BLK_Z/2;
      const lg=new THREE.Group();
      lg.position.set(lx,0,lz);
      const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.07,0.09,5,8),pMat);
      pole.position.y=2.5; lg.add(pole);
      const arm=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.07,1.1),pMat);
      arm.position.set(0,5.1,0.55); lg.add(arm);
      const head=new THREE.Mesh(new THREE.BoxGeometry(0.34,0.15,0.55),bMat);
      head.position.set(0,4.98,1.0); lg.add(head);
      const pl=new THREE.PointLight(0xfff0e0,0.28,16);
      pl.position.set(0,4.9,1.0); lg.add(pl);
      scene.add(lg);
    }
  }
}

// ── CAR ──────────────────────────────────────────────────────
function buildCar(){
  carGroup=new THREE.Group();
  const bMat=new THREE.MeshLambertMaterial({color:0x1a3060});
  const dkMat=new THREE.MeshLambertMaterial({color:0x080c14});
  const chMat=new THREE.MeshLambertMaterial({color:0xaab4c0,emissive:0x606870,emissiveIntensity:0.2});
  const glMat=new THREE.MeshLambertMaterial({color:0x4477aa,transparent:true,opacity:0.55,emissive:0x223366,emissiveIntensity:0.05});
  const hlMat=new THREE.MeshLambertMaterial({color:0xfffff0,emissive:0xfffff0,emissiveIntensity:2.2});
  const tlMat=new THREE.MeshLambertMaterial({color:0xff2000,emissive:0xff2000,emissiveIntensity:1.8});
  const riMat=new THREE.MeshLambertMaterial({color:0xc0c8d4,emissive:0x808898,emissiveIntensity:0.2});
  const tyMat=new THREE.MeshLambertMaterial({color:0x111111});

  const lo=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.52,4.8),bMat);
  lo.position.y=0.56; lo.castShadow=true; carGroup.add(lo);

  for(const sx of [-1.21,1.21]){
    const sk=new THREE.Mesh(new THREE.BoxGeometry(0.09,0.26,4.5),dkMat);
    sk.position.set(sx,0.43,0); carGroup.add(sk);
  }
  const cab=new THREE.Mesh(new THREE.BoxGeometry(2.05,0.68,2.6),bMat);
  cab.position.set(0,1.28,-0.15); cab.castShadow=true; carGroup.add(cab);

  const roof=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.1,2.4),dkMat);
  roof.position.set(0,1.68,-0.15); carGroup.add(roof);

  const wf=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.6,0.09),glMat);
  wf.position.set(0,1.3,1.12); wf.rotation.x=-0.28; carGroup.add(wf);
  const wr=new THREE.Mesh(new THREE.BoxGeometry(1.95,0.55,0.09),glMat);
  wr.position.set(0,1.27,-1.48); wr.rotation.x=0.26; carGroup.add(wr);
  for(const sx of [-1.04,1.04]){
    const ws=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.48,1.85),glMat);
    ws.position.set(sx,1.32,-0.15); carGroup.add(ws);
  }

  const hood=new THREE.Mesh(new THREE.BoxGeometry(2.3,0.09,1.55),bMat);
  hood.position.set(0,0.9,1.88); hood.rotation.x=0.05; carGroup.add(hood);
  const trunk=new THREE.Mesh(new THREE.BoxGeometry(2.1,0.09,0.9),bMat);
  trunk.position.set(0,0.9,-2.1); trunk.rotation.x=-0.04; carGroup.add(trunk);

  const bf=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.28,0.18),chMat);
  bf.position.set(0,0.46,2.43); carGroup.add(bf);
  const br=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.28,0.18),chMat);
  br.position.set(0,0.46,-2.43); carGroup.add(br);
  const grille=new THREE.Mesh(new THREE.BoxGeometry(1.5,0.2,0.08),dkMat);
  grille.position.set(0,0.52,2.44); carGroup.add(grille);

  for(const hx of [-0.74,0.74]){
    const hl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),hlMat);
    hl.position.set(hx,0.74,2.45); carGroup.add(hl);
    const beam=new THREE.SpotLight(0xffffff,0.9,28,Math.PI*0.1,0.5);
    beam.position.set(hx,0.74,2.5);
    beam.target.position.set(hx*1.1,-2,15);
    carGroup.add(beam); carGroup.add(beam.target);
  }
  for(const tx of [-0.74,0.74]){
    const tl=new THREE.Mesh(new THREE.BoxGeometry(0.48,0.17,0.08),tlMat);
    tl.position.set(tx,0.74,-2.45); carGroup.add(tl);
  }
  for(const sx of [-1.23,1.23]){
    const mir=new THREE.Mesh(new THREE.BoxGeometry(0.08,0.13,0.32),chMat);
    mir.position.set(sx,1.1,0.65); carGroup.add(mir);
  }

  const wps=[[-1.14,0.42,1.52],[1.14,0.42,1.52],[-1.14,0.42,-1.52],[1.14,0.42,-1.52]];
  wps.forEach(([wx,wy,wz])=>{
    const wg=new THREE.Group();
    const tyre=new THREE.Mesh(new THREE.CylinderGeometry(0.42,0.42,0.26,20),tyMat);
    tyre.rotation.z=Math.PI/2; tyre.castShadow=true; wg.add(tyre);
    const rim=new THREE.Mesh(new THREE.CylinderGeometry(0.27,0.27,0.27,10),riMat);
    rim.rotation.z=Math.PI/2; wg.add(rim);
    for(let s=0;s<5;s++){
      const spk=new THREE.Mesh(new THREE.BoxGeometry(0.05,0.52,0.05),riMat);
      spk.rotation.z=Math.PI/2;
      spk.rotation.x=(s/5)*Math.PI*2;
      spk.position.y=Math.sin((s/5)*Math.PI*2)*0.14;
      spk.position.z=Math.cos((s/5)*Math.PI*2)*0.14;
      wg.add(spk);
    }
    wg.position.set(wx,wy,wz);
    wg.userData.isWheel=true;
    carGroup.add(wg);
    carWheels.push(wg);
  });

  carGroup.position.copy(carPos);
  scene.add(carGroup);
}

// ─── AUDIO ──────────────────────────────────────────────────
function initAudio(){
  try{
    audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    engineGain=audioCtx.createGain();
    engineGain.gain.value=0;
    engineGain.connect(audioCtx.destination);
    engineOsc=audioCtx.createOscillator();
    engineOsc.type='sawtooth';
    engineOsc.frequency.value=55;
    const filter=audioCtx.createBiquadFilter();
    filter.type='lowpass'; filter.frequency.value=200;
    engineOsc.connect(filter);
    filter.connect(engineGain);
    engineOsc.start();
  }catch(e){}
}

function playChime(){
  if(!audioCtx) return;
  try{
    const osc=audioCtx.createOscillator();
    const gain=audioCtx.createGain();
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.frequency.value=880;
    osc.type='sine';
    gain.gain.setValueAtTime(0.18,audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.55);
    osc.start(); osc.stop(audioCtx.currentTime+0.55);
    // Second note
    setTimeout(()=>{
      const o2=audioCtx.createOscillator();
      const g2=audioCtx.createGain();
      o2.connect(g2); g2.connect(audioCtx.destination);
      o2.frequency.value=1100; o2.type='sine';
      g2.gain.setValueAtTime(0.12,audioCtx.currentTime);
      g2.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.4);
      o2.start(); o2.stop(audioCtx.currentTime+0.4);
    },120);
  }catch(e){}
}

function playOpen(){
  if(!audioCtx) return;
  try{
    [440,554,660].forEach((freq,i)=>{
      setTimeout(()=>{
        const osc=audioCtx.createOscillator();
        const gain=audioCtx.createGain();
        osc.connect(gain); gain.connect(audioCtx.destination);
        osc.frequency.value=freq; osc.type='sine';
        gain.gain.setValueAtTime(0.1,audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+0.3);
        osc.start(); osc.stop(audioCtx.currentTime+0.3);
      },i*80);
    });
  }catch(e){}
}

let lastNearEntry=null;

// ─── MAIN LOOP ───────────────────────────────────────────────
const ACCEL=0.05, FRIC=0.88, MAX_SPD=0.5, TURN=0.036;

function loop(){
  requestAnimationFrame(loop);
  frame++; clock.getDelta();

  if(!modalOpen){
    const U=keys['ArrowUp']  ||keys['w']||keys['W'];
    const D=keys['ArrowDown'] ||keys['s']||keys['S'];
    const L=keys['ArrowLeft'] ||keys['a']||keys['A'];
    const R=keys['ArrowRight']||keys['d']||keys['D'];

    if(U) carSpeed=Math.min(carSpeed+ACCEL,MAX_SPD);
    else if(D) carSpeed=Math.max(carSpeed-ACCEL,-MAX_SPD*0.5);
    else carSpeed*=FRIC;

    if(Math.abs(carSpeed)>0.004){
      const dir=carSpeed>0?1:-1;
      if(L) carAngle+=TURN*dir;
      if(R) carAngle-=TURN*dir;
    }

    const nx=carPos.x+Math.sin(carAngle)*carSpeed;
    const nz=carPos.z+Math.cos(carAngle)*carSpeed;
    const pt=new THREE.Vector2(nx,nz);
    let blocked=false;
    for(const b of buildings){ if(b.bbox.containsPoint(pt)){blocked=true;break;} }
    if(Math.abs(nx)>CITY_H-2||Math.abs(nz)>CITY_H-2) blocked=true;

    if(!blocked){ carPos.x=nx; carPos.z=nz; }
    else{ carSpeed*=-0.25; }

    carGroup.position.x=carPos.x;
    carGroup.position.z=carPos.z;
    carGroup.rotation.y=carAngle;
    carWheels.forEach(wg=>{ wg.children[0].rotation.x+=carSpeed*2.2; });

    // Engine audio
    if(engineOsc&&audioCtx){
      engineOsc.frequency.value=55+Math.abs(carSpeed)/MAX_SPD*80;
      engineGain.gain.value=Math.abs(carSpeed)>0.02?0.04:0;
    }
  }

  // Third-person camera
  const behind=new THREE.Vector3(
    carPos.x-Math.sin(carAngle)*CAM_BACK,
    CAM_UP,
    carPos.z-Math.cos(carAngle)*CAM_BACK
  );
  camPos.lerp(behind,CAM_LAG);
  camera.position.copy(camPos);
  camera.lookAt(
    carPos.x+Math.sin(carAngle)*4,
    1.2,
    carPos.z+Math.cos(carAngle)*4
  );

  // ── ENTRANCE DETECTION ──
  nearEntry=null;
  let bestD=9999;
  buildings.forEach(b=>{
    const dx=carPos.x-b.entranceWorld.x;
    const dz=carPos.z-b.entranceWorld.z;
    const d=Math.sqrt(dx*dx+dz*dz);
    const inZone=d<3.5;
    const pulse=Math.abs(Math.sin(frame*0.07));

    if(inZone){
      // Strong glow + pulse
      b.eMat.opacity=0.48+pulse*0.32;
      b.eLight.intensity=2.0+pulse*1.2;
      if(d<bestD){ nearEntry=b; bestD=d; }
    } else if(d<9){
      // Soft approach glow
      const t=1-(d-3.5)/5.5;
      b.eMat.opacity=0.14+t*0.12;
      b.eLight.intensity=t*0.4;
    } else {
      b.eMat.opacity=0.10;
      b.eLight.intensity=0;
    }
  });

  // Chime when first entering a zone
  if(nearEntry&&nearEntry!==lastNearEntry) playChime();
  lastNearEntry=nearEntry;

  // ── PARTICLE ANIMATION ──
  buildings.forEach(b=>{
    const pg=b.group.children.find(c=>c.userData.isParticleGroup);
    if(!pg) return;
    const isNear=nearEntry===b;
    pg.children.forEach((mesh,i)=>{
      const ud=mesh.userData;
      if(!ud.speed) return;
      // Orbit + float
      ud.baseAngle+=ud.speed;
      mesh.position.x=Math.cos(ud.baseAngle)*ud.radius;
      mesh.position.z=Math.sin(ud.baseAngle)*ud.radius;
      mesh.position.y=ud.yBase+Math.sin(frame*ud.ySpeed+ud.phase)*ud.yAmp;
      mesh.rotation.x+=0.02;
      mesh.rotation.y+=0.015;
      // Opacity: dim normally, bright when near
      const targetOpacity=isNear?0.75:0.18;
      mesh.material.opacity+=(targetOpacity-mesh.material.opacity)*0.05;
      mesh.material.color.setHex(ud.color);
    });
  });

  // HUD
  document.getElementById('spd-fill').style.width=(Math.abs(carSpeed)/MAX_SPD*100).toFixed(0)+'%';
  const projEl=document.getElementById('hud-proj');
  const enterEl=document.getElementById('hud-enter');
  if(nearEntry){
    projEl.innerHTML='<span style="color:'+nearEntry.distHex+'">'+nearEntry.project.name+'</span>';
    enterEl.style.display='block';
  } else {
    projEl.textContent='Navigate to a project entrance';
    enterEl.style.display='none';
  }
  document.getElementById('hud-visited').textContent=visitedSet.size+' / 18 explored';

  drawMinimap();
  renderer.render(scene,camera);
}

// ─── MINIMAP ─────────────────────────────────────────────────
function drawMinimap(){
  const mw=140,mh=140;
  mmCtx.fillStyle='#060a12';
  mmCtx.fillRect(0,0,mw,mh);
  const scale=mw/(CITY_H*2);
  const ox=mw/2,oz=mh/2;

  buildings.forEach(b=>{
    const px=ox+b.entranceWorld.x*scale;
    const pz=oz+b.entranceWorld.z*scale;
    const isN=b===nearEntry;
    const isV=b.visited;
    mmCtx.globalAlpha=isN?1:isV?0.55:0.4;
    mmCtx.fillStyle=isV?'#3ecf8e':b.distHex;
    mmCtx.beginPath();
    mmCtx.arc(px,pz,isN?5:3,0,Math.PI*2);
    mmCtx.fill();
    if(isV){
      mmCtx.strokeStyle='#3ecf8e';
      mmCtx.lineWidth=1;
      mmCtx.beginPath();
      mmCtx.arc(px,pz,4.5,0,Math.PI*2);
      mmCtx.stroke();
    }
    mmCtx.globalAlpha=1;
  });

  // Car arrow
  const cpx=ox+carPos.x*scale;
  const cpz=oz+carPos.z*scale;
  mmCtx.save();
  mmCtx.translate(cpx,cpz);
  mmCtx.rotate(-carAngle);
  mmCtx.fillStyle='#ffffff';
  mmCtx.beginPath();
  mmCtx.moveTo(0,-5.5);
  mmCtx.lineTo(3.2,4);
  mmCtx.lineTo(0,2);
  mmCtx.lineTo(-3.2,4);
  mmCtx.closePath();
  mmCtx.fill();
  mmCtx.restore();

  mmCtx.strokeStyle='rgba(74,144,217,.15)';
  mmCtx.lineWidth=1;
  mmCtx.strokeRect(0,0,mw,mh);
}

// ─── MODAL ───────────────────────────────────────────────────
function openModal(b){
  modalOpen=true;
  if(!b.visited){
    b.visited=true;
    visitedSet.add(b.project.name);
  }
  const p=b.project;
  const dist=DISTRICTS[p.district];
  document.getElementById('mo-ico').textContent=p.icon;
  document.getElementById('mo-ico').style.cssText='background:'+dist.hex+'18;border:1px solid '+dist.hex+'30;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0';
  const catEl=document.getElementById('mo-cat');
  catEl.textContent=p.cat; catEl.style.color=dist.hex;
  document.getElementById('mo-name').textContent=p.name;
  document.getElementById('mo-stack').textContent=p.stack;
  const distEl=document.getElementById('mo-dist');
  distEl.textContent=dist.name;
  distEl.style.cssText='background:'+dist.hex+'18;color:'+dist.hex+';border:1px solid '+dist.hex+'30;display:inline-block;font-size:9px;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border-radius:4px;margin-top:4px';
  document.getElementById('mo-desc').textContent=p.desc;
  document.getElementById('mo-tags').innerHTML=p.tags.map(t=>'<span class="mo-tag">'+t+'</span>').join('');
  let btns='';
  if(p.gh)   btns+='<a class="mo-gh"   href="'+p.gh+'"   target="_blank">View on GitHub</a>';
  if(p.live) btns+='<a class="mo-live" href="'+p.live+'" target="_blank">Live Demo →</a>';
  if(!p.gh&&!p.live) btns='<span style="font-size:11px;color:#3a4d68">No live link available</span>';
  document.getElementById('mo-btns').innerHTML=btns;
  document.getElementById('ov').style.display='flex';
  playOpen();
}

function closeModal(){
  document.getElementById('ov').style.display='none';
  modalOpen=false;
}
document.getElementById('ov').addEventListener('click',e=>{
  if(e.target===document.getElementById('ov')) closeModal();
});

// ─── INPUT ───────────────────────────────────────────────────
function bindInput(){
  document.addEventListener('keydown',e=>{
    keys[e.key]=true;
    if((e.key==='Enter'||e.key===' ')&&nearEntry&&!modalOpen){
      e.preventDefault(); openModal(nearEntry);
    }
    if(e.key==='Escape'&&modalOpen) closeModal();
    // Unlock audio on first key
    if(audioCtx&&audioCtx.state==='suspended') audioCtx.resume();
  });
  document.addEventListener('keyup',e=>{ keys[e.key]=false; });
}

// ─── TOAST ───────────────────────────────────────────────────
function toast(msg){
  const style=document.createElement('style');
  style.textContent='@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}10%,75%{opacity:1;transform:translateX(-50%)}100%{opacity:0}}';
  document.head.appendChild(style);
  const t=document.createElement('div');
  t.style.cssText='position:fixed;top:18px;left:50%;transform:translateX(-50%);background:#4a90d9;color:#fff;border-radius:8px;padding:8px 20px;font-size:11px;font-weight:600;z-index:300;animation:tf 3.2s ease forwards;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap';
  t.textContent=msg;
  document.body.appendChild(t);
  setTimeout(()=>t.remove(),3300);
}
</script>
</body>
</html>"""

components.html(HTML, height=760, scrolling=False)
