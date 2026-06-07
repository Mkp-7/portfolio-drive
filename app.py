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
[data-testid="stAppViewContainer"] {background: #0d1117;}
iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100vh;overflow:hidden;background:#0d1117;font-family:'Segoe UI',system-ui,sans-serif}

/* INTRO */
#intro{position:fixed;inset:0;background:#0d1117;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;gap:5px;overflow-y:auto;padding:20px 0}
#intro .ca{font-size:52px;animation:bob 1.2s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
#intro h1{font-size:36px;font-weight:700;background:linear-gradient(120deg,#58a6ff,#bc8cff,#39d353);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-top:8px}
#intro .sub{font-size:13px;color:#7d8590;margin-bottom:3px}
#intro .badge{font-size:11px;color:#58a6ff;background:rgba(88,166,255,.1);border:1px solid rgba(88,166,255,.25);border-radius:20px;padding:3px 13px;margin-bottom:16px}
#intro .legend{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:540px;width:90%;margin-bottom:16px}
#intro .leg{display:flex;align-items:center;gap:6px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:8px;padding:5px 10px;font-size:11px;color:#7d8590}
#intro .leg .dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
#intro .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-width:420px;width:90%;margin-bottom:20px}
#intro .card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:12px;text-align:center}
#intro .card .ci{font-size:18px;margin-bottom:4px}
#intro .card .ct{font-size:10px;color:#7d8590;line-height:1.4}
#intro button{background:linear-gradient(135deg,#58a6ff,#bc8cff);border:none;border-radius:12px;color:#fff;font-size:15px;font-weight:600;padding:12px 42px;cursor:pointer;box-shadow:0 4px 20px rgba(88,166,255,.3);transition:transform .15s}
#intro button:hover{transform:translateY(-2px)}

canvas{display:block}

/* HUD */
#hud{position:fixed;top:14px;left:14px;background:rgba(13,17,23,.93);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:12px 16px;z-index:50;min-width:185px;backdrop-filter:blur(10px);display:none}
.hn{font-size:13px;font-weight:600;color:#e6edf3}.hr{font-size:10px;color:#58a6ff;margin-bottom:9px}
.hs{font-size:9px;color:#484f58;margin-bottom:3px}.hb{height:3px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden;margin-bottom:9px}
.hf{height:100%;background:linear-gradient(90deg,#39d353,#58a6ff);border-radius:2px;transition:width .1s;width:0%}
.hn2{font-size:10px;color:#7d8590}.hn2 span{color:#e3b341}

/* MINIMAP */
#mm{position:fixed;bottom:14px;right:14px;background:rgba(13,17,23,.93);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:9px;z-index:50;display:none}
.ml{font-size:9px;color:#484f58;text-transform:uppercase;letter-spacing:1px;text-align:center;margin-bottom:4px}

/* HINT */
#hint{position:fixed;bottom:14px;left:14px;background:rgba(13,17,23,.85);border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:6px 12px;z-index:50;font-size:10px;color:#484f58;display:none}

/* MODAL */
#ov{position:fixed;inset:0;background:rgba(0,0,0,.75);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(8px)}
#mo{background:#161b22;border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:24px;max-width:440px;width:92%;position:relative;animation:su .22s ease;max-height:90vh;overflow-y:auto}
@keyframes su{from{transform:translateY(18px);opacity:0}to{transform:translateY(0);opacity:1}}
.mh{display:flex;align-items:flex-start;gap:12px;margin-bottom:12px}
.mi{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}
.mt2{font-size:16px;font-weight:600;color:#e6edf3;margin-bottom:4px;line-height:1.3}
.ml2{font-size:10px;padding:2px 9px;border-radius:20px;display:inline-block}
.mcat{font-size:10px;color:#484f58;margin-top:3px}
.md{font-size:12px;color:#7d8590;line-height:1.65;margin-bottom:12px}
.mtags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:14px}
.mtag{font-size:10px;color:#7d8590;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:6px;padding:2px 9px}
.mbtns{display:flex;gap:8px;flex-wrap:wrap}
.bgh{flex:1;min-width:100px;padding:9px;border-radius:10px;font-size:12px;font-weight:500;text-align:center;text-decoration:none;background:rgba(255,255,255,.06);color:#e6edf3;border:1px solid rgba(255,255,255,.1);cursor:pointer;display:block;transition:background .15s}
.bgh:hover{background:rgba(255,255,255,.1)}
.bli{flex:1;min-width:100px;padding:9px;border-radius:10px;font-size:12px;font-weight:600;text-align:center;text-decoration:none;background:linear-gradient(135deg,#58a6ff,#bc8cff);color:#fff;border:none;cursor:pointer;display:block}
.bli.disabled{background:rgba(255,255,255,.08);color:#484f58;pointer-events:none}
.bcl{position:absolute;top:14px;right:14px;width:30px;height:30px;border-radius:8px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);color:#7d8590;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.bcl:hover{background:rgba(255,255,255,.1);color:#e6edf3}

/* DPAD */
#dp{position:fixed;right:14px;bottom:128px;z-index:50;display:none;grid-template-areas:'. u .' 'l . r' '. d .';grid-template-columns:repeat(3,40px);grid-template-rows:repeat(3,40px);gap:3px}
.db{background:rgba(22,27,34,.92);border:1px solid rgba(255,255,255,.1);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px;color:#e6edf3;cursor:pointer;user-select:none;-webkit-user-select:none;touch-action:none;transition:background .1s}
.db.on{background:rgba(88,166,255,.35);border-color:#58a6ff}
#dpu{grid-area:u}#dpd{grid-area:d}#dpl{grid-area:l}#dpr{grid-area:r}

/* TOAST */
.toast{position:fixed;top:14px;left:50%;transform:translateX(-50%);background:rgba(57,211,83,.88);color:#fff;border-radius:20px;padding:6px 16px;font-size:11px;font-weight:500;z-index:200;animation:tf 2.6s ease forwards;white-space:nowrap}
@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}12%,78%{opacity:1;transform:translateX(-50%) translateY(0)}100%{opacity:0}}
</style>
</head>
<body>

<div id="intro">
  <div class="ca">🚗</div>
  <h1>Portfolio Drive</h1>
  <div class="sub">GitHub: Mkp-7 &nbsp;·&nbsp; Data Scientist & AI Engineer</div>
  <div class="badge">🤖 AI · Analytics · Streamlit · Tableau · Power BI · Looker</div>

  <div class="legend">
    <div class="leg"><div class="dot" style="background:#58a6ff"></div>Streamlit Apps</div>
    <div class="leg"><div class="dot" style="background:#e3b341"></div>Tableau Dashboards</div>
    <div class="leg"><div class="dot" style="background:#f78166"></div>Power BI Dashboards</div>
    <div class="leg"><div class="dot" style="background:#bc8cff"></div>ML / Python Projects</div>
    <div class="leg"><div class="dot" style="background:#39d353"></div>Looker / GA4</div>
    <div class="leg"><div class="dot" style="background:#ff7b72"></div>Visualization</div>
  </div>

  <div class="cards">
    <div class="card"><div class="ci">🎮</div><div class="ct">WASD or Arrow keys to drive</div></div>
    <div class="card"><div class="ci">🏢</div><div class="ct">Drive near a glowing building</div></div>
    <div class="card"><div class="ci">⏎</div><div class="ct">Press Enter or Space to open</div></div>
  </div>
  <button onclick="startGame()">Start Driving →</button>
</div>

<canvas id="c"></canvas>

<div id="hud">
  <div class="hn">Mkp-7</div>
  <div class="hr">Data Scientist & AI Engineer</div>
  <div class="hs">SPEED</div>
  <div class="hb"><div class="hf" id="sf"></div></div>
  <div class="hn2" id="hn">Drive to a glowing building</div>
</div>

<div id="mm"><div class="ml">Map</div><canvas id="mc" width="110" height="110"></canvas></div>
<div id="hint">WASD / Arrow keys &nbsp;·&nbsp; Mobile: D-pad &nbsp;·&nbsp; Enter = open project</div>

<div id="ov">
  <div id="mo">
    <button class="bcl" onclick="closeM()">×</button>
    <div class="mh">
      <div class="mi" id="micon"></div>
      <div>
        <div class="mt2" id="mtitle"></div>
        <div class="ml2" id="mlang2"></div>
        <div class="mcat" id="mcat"></div>
      </div>
    </div>
    <div class="md" id="mdesc"></div>
    <div class="mtags" id="mtags"></div>
    <div class="mbtns" id="mbtns"></div>
  </div>
</div>

<div id="dp">
  <div class="db" id="dpu">↑</div>
  <div class="db" id="dpl">←</div>
  <div class="db" id="dpr">→</div>
  <div class="db" id="dpd">↓</div>
</div>

<script>
// ── ALL PROJECTS WITH REAL LINKS ──
const PROJECTS = [
  // STREAMLIT APPS
  {
    name:"Revenue Intelligence Agent",icon:"🚗",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · Groq LLM · GitHub Actions",
    desc:"Autonomous multi-agent AI pipeline monitoring competitor car rental pricing across 8 competitors and 10 US airports. Integrates real-time flight, event, and weather demand signals. Reduces manual analysis from 3 hours to 15 minutes. Features 5-tab Streamlit dashboard with anomaly flagging (≥20% price change) and urgency-ranked pricing recommendations.",
    tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","Revenue Ops","REST APIs","SQLite"],
    gh:"https://github.com/Mkp-7/Revenue-Management-Agent",
    live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"
  },
  {
    name:"AI Pricing Intelligence Agent",icon:"🤖",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · Claude API",
    desc:"AI-powered competitive pricing agent using Claude API automating real-time price monitoring across Amazon, Walmart, and specialty retailers for 20+ SKUs. Reduced manual analysis from 8 hrs/week to 15 minutes at 95% accuracy. Identified 12–15% margin improvement opportunities on underpriced items.",
    tags:["Claude API","Price Monitoring","SQLite","Streamlit","Competitive Intel","ML"],
    gh:"https://github.com/Mkp-7/AI-Pricing-Agent",
    live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"
  },
  {
    name:"EcoRoute Optimizer",icon:"🌿",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · Gemini AI · OR-Tools",
    desc:"Logistics optimization platform generating carbon-optimized shipping routes across 60+ US cities. Analyzes diesel truck, EV, and rail freight using EPA SmartWay carbon methodology. Integrates OpenRouteService + OpenWeatherMap APIs, SQLite route caching, and NLP conversational interface for real-time cost, time, and carbon footprint analysis.",
    tags:["Gemini AI","OR-Tools","Carbon Optimization","REST APIs","NLP","Streamlit","Logistics"],
    gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",
    live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"
  },
  {
    name:"Banking Risk Intelligence",icon:"🏦",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · FDIC API · FRED",
    desc:"Queried FDIC data for 4,500+ banks, calculated 5 operational risk KRIs (Capital Adequacy, NPL, ROA, LDR) against Basel III/CCAR thresholds. Applied Logistic Regression, Random Forest (AUC=0.84), and Gradient Boosting for bank failure risk prediction. Integrated Fed Funds Rate and yield curve from FRED.",
    tags:["Basel III","FDIC API","FRED","Random Forest","AUC=0.84","CCAR","Risk Modeling"],
    gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",
    live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"
  },
  {
    name:"Retail Intelligence Platform",icon:"🛒",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · Groq · Yelp Data",
    desc:"AI-native customer intelligence platform turning public customer review data into actionable insights. Modules: Voice of Customer AI (theme clustering, anomaly detection, executive summaries), Store Pulse Map (benchmarking vs regional peers), Test & Learn Autopilot (statistical significance), and Analyst Copilot (plain-English Q&A chatbot).",
    tags:["Groq LLM","Yelp Dataset","NLP","Streamlit","Plotly","A/B Testing","Customer Analytics"],
    gh:"https://github.com/Mkp-7/retail-intelligence-platform",
    live:"https://retail-intelligence-platform-zvdrhjrf6hcmsuwgnvurd9.streamlit.app/?page=home"
  },
  {
    name:"Medmedia Analytics Hub",icon:"🏥",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
    category:"Streamlit App",lang:"Python · LLMs · REST APIs",
    desc:"End-to-end healthcare media analytics platform integrating ClinicalTrials.gov, PubMed, and NIH databases. Analyzed 470,000+ active clinical trials and 35M+ biomedical publications via NLP. Enables pharma advertiser identification, HCP audience segmentation across 10 clinical specialties, and AI-generated content strategy.",
    tags:["Healthcare","NLP","ClinicalTrials.gov","PubMed","LLMs","HCP Segmentation","Streamlit"],
    gh:"https://github.com/Mkp-7/Medmedia-Analytics-Hub",
    live:"https://medmedia-analytics-app-qdbzvc6gctzvtcyn5936dg.streamlit.app/"
  },
  // TABLEAU
  {
    name:"Sales & Demand Forecasting",icon:"📊",color:"#e3b341",bg:"rgba(227,179,65,.12)",tc:"#e3b341",
    category:"Tableau Dashboard",lang:"Python · ARIMA · SARIMA · Tableau",
    desc:"Fine-tuned ARIMA and SARIMA models to forecast 6-month revenue for 25,432 products across 12 regions at 94% accuracy. Identified top 20% customers driving 62% of total revenue. Built interactive Tableau and Power BI dashboards visualizing revenue trends, seasonal patterns, and KPIs for data-driven pricing and promotions.",
    tags:["ARIMA","SARIMA","Forecasting","Tableau","Power BI","94% Accuracy","25K+ Products"],
    gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",
    live:"https://public.tableau.com/app/profile/om4032/viz/SalseForecastingAnalysis/Dashboard1"
  },
  {
    name:"MSU Collaboratory Dashboard",icon:"🎓",color:"#e3b341",bg:"rgba(227,179,65,.12)",tc:"#e3b341",
    category:"Tableau Dashboard",lang:"Tableau · 3D Network Graph",
    desc:"3D visualization of activities conducted at Montclair State University with different community partner organizations. Also includes a public Tableau dashboard surfacing Collaboratory data insights. Companion network graph hosted on GitHub Pages showing cross-organization collaboration patterns.",
    tags:["Tableau","3D Network Graph","MSU","Community Partners","Data Viz","GitHub Pages"],
    gh:"https://mkp-7.github.io/Network-Graph/",
    live:"https://public.tableau.com/app/profile/mukund.patel7859/viz/Collaboratory_Data_Insights_Mukund-2/Dashboard1"
  },
  {
    name:"MSU Student Happiness Study",icon:"😊",color:"#e3b341",bg:"rgba(227,179,65,.12)",tc:"#e3b341",
    category:"Tableau Dashboard",lang:"Python · Statistics · Tableau",
    desc:"Tracked 70 MSU students for 21 days collecting daily activities, timing, social context, location, and self-reported happiness (0–10) at 30-minute intervals. Cleaned 210 Excel sheets, performed hypothesis testing (t-tests, ANOVA, regression). Tableau dashboard analyzing weekly happiness patterns by activity category.",
    tags:["Survey Analysis","Hypothesis Testing","ANOVA","Regression","Tableau","Python","Behavioral Analytics"],
    gh:"",
    live:"https://public.tableau.com/app/profile/mukundkumar.patel/viz/python1/Dashboard1?publish=yes"
  },
  // POWER BI
  {
    name:"Banking Metrics Client Analysis",icon:"💳",color:"#f78166",bg:"rgba(247,129,102,.12)",tc:"#f78166",
    category:"Power BI Dashboard",lang:"Power BI · SQL · Python",
    desc:"Structured and transformed dataset of 3,000 banking clients integrating portfolio, relationship, and product-level data. Power BI dashboard monitoring client accounts and portfolio metrics — identified high-fee accounts (~51% of deposits), Private Bank loans (~$0.9B), and variations across client segments for risk assessment and regulatory reporting.",
    tags:["Power BI","Banking","Portfolio Analytics","Client Segmentation","Risk Assessment","Regulatory"],
    gh:"https://github.com/Mkp-7/Banking-Metrics-Client-Analysis-Power-BI-Dashboard",
    live:""
  },
  {
    name:"Supply Chain Analytics BI",icon:"📦",color:"#f78166",bg:"rgba(247,129,102,.12)",tc:"#f78166",
    category:"Power BI Dashboard",lang:"Power BI · Power Query · DAX",
    desc:"Integrated and cleaned 10 raw Excel supply chain datasets using Power Query (ETL), built a star schema data model, and developed an interactive Power BI dashboard. Created 12+ DAX measures for KPIs: closing stock, inventory turnover, stock aging, on-time delivery %, and reorder alerts. Includes logistics maps and drill-through.",
    tags:["Power BI","DAX","Power Query","Star Schema","ETL","Supply Chain","Inventory"],
    gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",
    live:""
  },
  {
    name:"Insurance Claims Analysis",icon:"🛡️",color:"#f78166",bg:"rgba(247,129,102,.12)",tc:"#f78166",
    category:"Power BI + ML",lang:"R · SQL Server · Power BI",
    desc:"Processed 58,000+ insurance policy records in SQL Server, engineered features, and developed Random Forest and Logistic Regression models in R achieving 94% accuracy for 6-month claim likelihood prediction. Power BI dashboards track predicted claim probability by car segment, fuel type, transmission, and policyholder age.",
    tags:["Random Forest","Logistic Regression","94% Accuracy","SQL Server","R","Power BI","Insurance"],
    gh:"https://github.com/Mkp-7/Insurance-Claims-Analysis",
    live:""
  },
  {
    name:"Workforce Utilization Analytics",icon:"👥",color:"#f78166",bg:"rgba(247,129,102,.12)",tc:"#f78166",
    category:"Power BI Dashboard",lang:"Power BI · DAX · HR Data",
    desc:"Power BI dashboard analyzing workforce attendance for 80 employees over 3 months tracking presence, WFH utilization, and leave patterns. Computed KPIs: attendance rate, WFH utilization, sick leave. Identified mid-month attendance dips, increased WFH toward end of June, and peak day shifts from Fridays to Mondays.",
    tags:["Power BI","HR Analytics","Workforce Planning","DAX","Attendance","WFH","Talent Insights"],
    gh:"https://github.com/Mkp-7/Workforce-Utilization-Analytics",
    live:""
  },
  // ML / PYTHON
  {
    name:"Retail Customer Analytics",icon:"🛍️",color:"#bc8cff",bg:"rgba(188,140,255,.12)",tc:"#bc8cff",
    category:"ML / Python Project",lang:"Python · Scikit-learn · Excel",
    desc:"Analyzed 25,000+ product records and 10,000+ customer transactions using K-Means clustering (5 segments) and repeat-rate modeling. Identified top 20% customers driving 60% of revenue. Built automated Excel reporting dashboard tracking 10+ KPIs (spend/day, purchase frequency, repeat interval), reducing manual analysis time by 40%.",
    tags:["K-Means","Scikit-learn","Pandas","NumPy","Customer Segmentation","Excel Automation","RFM"],
    gh:"https://github.com/Mkp-7/Retail-Customer-Analytics-Reporting-System",
    live:""
  },
  {
    name:"COVID-19 Global Impact Analysis",icon:"🦠",color:"#bc8cff",bg:"rgba(188,140,255,.12)",tc:"#bc8cff",
    category:"ML / Python Project",lang:"Python · EDA · WHO Data",
    desc:"Analyzed COVID-19 global impact using WHO data (~450,000 records). Performed EDA and Python visualization to uncover pandemic spread patterns. Covered mortality comparisons across WHO regions, global daily cases/deaths over time, country-level outbreaks on peak days, and regional disparities in case fatality rates.",
    tags:["EDA","WHO Data","Matplotlib","Seaborn","Epidemiology","Data Storytelling","Python"],
    gh:"https://github.com/Mkp-7/COVID-19-Global-Impact-Analysis",
    live:""
  },
  {
    name:"Diabetes Prediction Model",icon:"🩺",color:"#bc8cff",bg:"rgba(188,140,255,.12)",tc:"#bc8cff",
    category:"ML / Python Project",lang:"Python · Scikit-learn · SVM",
    desc:"Diabetes prediction system using data from 769 patients. Performed preprocessing, EDA, and feature selection. Evaluated Logistic Regression, Random Forest, and Decision Tree. Achieved peak 80% accuracy with SVM. Used Pandas, NumPy, Matplotlib, and Seaborn throughout.",
    tags:["SVM","Random Forest","Logistic Regression","Feature Selection","Scikit-learn","Healthcare ML"],
    gh:"https://github.com/Mkp-7/Diabetes-Prediction-Model",
    live:""
  },
  {
    name:"Smart Reads: Book Recommender",icon:"📚",color:"#bc8cff",bg:"rgba(188,140,255,.12)",tc:"#bc8cff",
    category:"ML / Python Project",lang:"Python · TF-IDF · SVD",
    desc:"Analyzed 10,000 books and 1M+ ratings using ML (Linear Kernel), TF-IDF with Cosine Similarity, and SVD for personalized recommendations. Mitigated cold start, scalability, and relevance challenges to deliver accurate recommendations across diverse user preferences.",
    tags:["TF-IDF","SVD","Cosine Similarity","Collaborative Filtering","Recommendation Engine","1M+ Ratings"],
    gh:"https://github.com/Mkp-7/Book_Recommendation",
    live:""
  },
  // LOOKER
  {
    name:"E-Commerce GA4 Analytics Pipeline",icon:"📈",color:"#39d353",bg:"rgba(57,211,83,.12)",tc:"#39d353",
    category:"Looker / dbt / BigQuery",lang:"dbt · BigQuery · GA4 · Looker Studio",
    desc:"5-model dbt pipeline on BigQuery covering GA4 event schema modeling, behavioral segmentation across 269K users, and cross-source identity resolution. Identified 9,630 cart abandonment targets via GA4 UNNEST queries. Simulated Klaviyo-style A/B recovery campaign projecting 23% recovery vs 8% baseline and $25K incremental revenue.",
    tags:["dbt","BigQuery","GA4","Looker Studio","A/B Testing","Cart Abandonment","CDP","$25K Revenue Impact"],
    gh:"https://github.com/Mkp-7/ga4-funnel-intelligence",
    live:"https://datastudio.google.com/u/0/reporting/0c2a2ec1-8858-4b92-adc1-422b4e13f989/page/ohbyF"
  }
];

// ── WORLD ──
const W=1800,H=1800;

// Grid layout: 4 columns x 5 rows = 20 slots for 18 projects
const COLS=4,ROWS=5;
const MARGIN_X=220,MARGIN_Y=200;
const STEP_X=(W-MARGIN_X*2)/(COLS-1);
const STEP_Y=(H-MARGIN_Y*2)/(ROWS-1);
const SLOTS=[];
for(let r=0;r<ROWS;r++) for(let c=0;c<COLS;c++) SLOTS.push({x:MARGIN_X+c*STEP_X,y:MARGIN_Y+r*STEP_Y});

// Roads between grid rows/cols
const ROAD_Y=[],ROAD_X=[];
for(let r=0;r<ROWS;r++) ROAD_Y.push(MARGIN_Y+r*STEP_Y);
for(let c=0;c<COLS;c++) ROAD_X.push(MARGIN_X+c*STEP_X);

let buildings=[],car={x:W/2,y:H/2,angle:0,speed:0},cam={x:W/2,y:H/2};
let keys={},dp={up:0,down:0,left:0,right:0},near=null,modal=false;
let particles=[],frame=0,canvas,ctx,mc,mctx;

function placeBuildings(){
  buildings=PROJECTS.map((p,i)=>({
    ...p,x:SLOTS[i].x,y:SLOTS[i].y,w:100,h:100,
    lit:Array.from({length:16},()=>Math.random()>.4)
  }));
}

function startGame(){
  document.getElementById('intro').style.display='none';
  document.getElementById('hud').style.display='block';
  document.getElementById('mm').style.display='block';
  document.getElementById('hint').style.display='block';
  document.getElementById('dp').style.display='grid';
  canvas=document.getElementById('c');ctx=canvas.getContext('2d');
  mc=document.getElementById('mc');mctx=mc.getContext('2d');
  resize();window.addEventListener('resize',resize);
  placeBuildings();bindKeys();bindDpad();loop();
  toast('Drive near a building and press Enter to explore! 🏢');
}

function resize(){canvas.width=window.innerWidth;canvas.height=window.innerHeight;}

function shadeHex(hex,amt){
  hex=hex.replace('#','');
  const n=parseInt(hex.length===3?hex.split('').map(x=>x+x).join(''):hex,16);
  const r=Math.max(0,Math.min(255,(n>>16)+amt));
  const g=Math.max(0,Math.min(255,((n>>8)&255)+amt));
  const b=Math.max(0,Math.min(255,(n&255)+amt));
  return 'rgb('+r+','+g+','+b+')';
}

function drawWorld(){
  ctx.fillStyle='#0d1117';ctx.fillRect(0,0,W,H);
  // grid bg
  ctx.strokeStyle='rgba(33,45,60,.4)';ctx.lineWidth=.5;
  for(let x=0;x<W;x+=80){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
  for(let y=0;y<H;y+=80){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
  // horizontal roads
  ROAD_Y.forEach(ry=>{
    ctx.fillStyle='#161b22';ctx.fillRect(0,ry-44,W,88);
    ctx.setLineDash([24,16]);ctx.strokeStyle='#21262d';ctx.lineWidth=2;
    ctx.beginPath();ctx.moveTo(0,ry);ctx.lineTo(W,ry);ctx.stroke();
    ctx.setLineDash([]);
  });
  // vertical roads
  ROAD_X.forEach(rx=>{
    ctx.fillStyle='#161b22';ctx.fillRect(rx-44,0,88,H);
    ctx.setLineDash([24,16]);ctx.strokeStyle='#21262d';ctx.lineWidth=2;
    ctx.beginPath();ctx.moveTo(rx,0);ctx.lineTo(rx,H);ctx.stroke();
    ctx.setLineDash([]);
  });
  // intersection highlights
  ROAD_Y.forEach(ry=>ROAD_X.forEach(rx=>{
    ctx.fillStyle='#1c2128';ctx.fillRect(rx-44,ry-44,88,88);
  }));
}

function drawBuilding(b){
  const bx=b.x-b.w/2,by=b.y-b.h/2,isN=near===b;
  const pulse=isN?Math.sin(frame*.07)*.4+.7:1;
  // sidewalk
  ctx.fillStyle='#131924';ctx.beginPath();ctx.roundRect(bx-10,by-10,b.w+20,b.h+20,8);ctx.fill();
  // glow
  if(isN){ctx.shadowColor=b.color;ctx.shadowBlur=28*pulse;}
  ctx.fillStyle=isN?b.color:shadeHex(b.color,-65);
  ctx.beginPath();ctx.roundRect(bx,by,b.w,b.h,10);ctx.fill();
  ctx.shadowBlur=0;
  // accent bar
  ctx.fillStyle=b.color;ctx.globalAlpha=.55;
  ctx.beginPath();ctx.roundRect(bx,by,b.w,12,[10,10,0,0]);ctx.fill();
  ctx.globalAlpha=1;
  // windows
  for(let r=0;r<4;r++) for(let c=0;c<4;c++){
    const wx=bx+10+c*20,wy=by+18+r*18,lit=b.lit[r*4+c];
    ctx.fillStyle=lit?'#ffd700':'rgba(120,180,255,.1)';
    ctx.globalAlpha=lit?(isN?1:.75):.35;
    ctx.fillRect(wx,wy,11,8);ctx.globalAlpha=1;
  }
  // icon
  ctx.font='16px serif';ctx.textAlign='center';ctx.fillText(b.icon,b.x,by-12);
  // label
  const short=b.name.length>16?b.name.slice(0,16)+'…':b.name;
  ctx.font=(isN?'600':'500')+' 10px system-ui';
  ctx.fillStyle=isN?'#e6edf3':'rgba(170,185,205,.7)';
  ctx.fillText(short,b.x,by+b.h+16);
  // category label
  ctx.font='9px system-ui';ctx.fillStyle=b.color;ctx.globalAlpha=isN?1:.6;
  ctx.fillText(b.category,b.x,by+b.h+28);ctx.globalAlpha=1;
  // enter hint
  if(isN){
    ctx.font='700 9px system-ui';ctx.fillStyle='#e3b341';
    ctx.globalAlpha=pulse;ctx.fillText('PRESS ENTER',b.x,by-26);ctx.globalAlpha=1;
  }
}

function drawCar(){
  const cw=22,ch=36;
  ctx.save();ctx.translate(car.x,car.y);ctx.rotate(car.angle);
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(2,5,cw/2+4,7,0,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#f0c000';ctx.beginPath();ctx.roundRect(-cw/2,-ch/2,cw,ch,6);ctx.fill();
  ctx.fillStyle='#c87000';ctx.fillRect(-cw/2,-ch/2,cw,10);
  ctx.fillStyle='rgba(140,220,255,.72)';ctx.fillRect(-cw/2+3,-ch/2+2,cw-6,7);
  ctx.fillStyle='rgba(255,248,180,.95)';ctx.fillRect(-cw/2+2,-ch/2+1,4,3);ctx.fillRect(cw/2-6,-ch/2+1,4,3);
  ctx.fillStyle='#e74c3c';ctx.fillRect(-cw/2+2,ch/2-5,4,3);ctx.fillRect(cw/2-6,ch/2-5,4,3);
  if(Math.abs(car.speed)>2.5){
    ctx.strokeStyle='rgba(255,255,255,.12)';ctx.lineWidth=1;
    for(let i=0;i<4;i++){ctx.beginPath();ctx.moveTo(-cw/2+3+i*5,ch/2);ctx.lineTo(-cw/2+1+i*5,ch/2+10);ctx.stroke();}
  }
  ctx.restore();
  if(Math.abs(car.speed)>1&&frame%3===0){
    particles.push({x:car.x-Math.sin(car.angle)*18+(Math.random()-.5)*5,y:car.y+Math.cos(car.angle)*18+(Math.random()-.5)*5,life:1,r:2.5});
  }
}

function drawParticles(){
  particles=particles.filter(p=>p.life>0);
  particles.forEach(p=>{
    ctx.globalAlpha=p.life*.3;ctx.fillStyle='#8b949e';
    ctx.beginPath();ctx.arc(p.x,p.y,p.r*p.life,0,Math.PI*2);ctx.fill();
    p.life-=.07;
  });ctx.globalAlpha=1;
}

function drawMini(){
  const mw=110,mh=110,sx=mw/W,sy=mh/H;
  mctx.fillStyle='#0d1117';mctx.fillRect(0,0,mw,mh);
  mctx.fillStyle='#161b22';
  ROAD_Y.forEach(ry=>mctx.fillRect(0,(ry-44)*sy,mw,88*sy));
  ROAD_X.forEach(rx=>mctx.fillRect((rx-44)*sx,0,88*sx,mh));
  buildings.forEach(b=>{mctx.fillStyle=b.color;mctx.beginPath();mctx.arc(b.x*sx,b.y*sy,3.5,0,Math.PI*2);mctx.fill();});
  mctx.fillStyle='#f0c000';mctx.beginPath();mctx.arc(car.x*sx,car.y*sy,4,0,Math.PI*2);mctx.fill();
  // viewport rect
  const vx=(cam.x-canvas.width/2)*sx,vy=(cam.y-canvas.height/2)*sy;
  const vw=canvas.width*sx,vh=canvas.height*sy;
  mctx.strokeStyle='rgba(255,255,255,.18)';mctx.lineWidth=1;
  mctx.strokeRect(Math.max(0,vx),Math.max(0,vy),Math.min(mw,vw),Math.min(mh,vh));
}

const ACCEL=.22,FRIC=.87,MSPD=6,TURN=.052;
function update(){
  if(modal)return;frame++;
  const U=keys['ArrowUp']||keys['w']||keys['W']||dp.up;
  const D=keys['ArrowDown']||keys['s']||keys['S']||dp.down;
  const L=keys['ArrowLeft']||keys['a']||keys['A']||dp.left;
  const R=keys['ArrowRight']||keys['d']||keys['D']||dp.right;
  if(U)car.speed=Math.min(car.speed+ACCEL,MSPD);
  else if(D)car.speed=Math.max(car.speed-ACCEL,-MSPD*.5);
  else car.speed*=FRIC;
  if(Math.abs(car.speed)>.15){const d=car.speed>0?1:-1;if(L)car.angle-=TURN*d;if(R)car.angle+=TURN*d;}
  car.x+=Math.sin(car.angle)*car.speed;car.y-=Math.cos(car.angle)*car.speed;
  car.x=Math.max(20,Math.min(W-20,car.x));car.y=Math.max(20,Math.min(H-20,car.y));
  cam.x+=(car.x-cam.x)*.1;cam.y+=(car.y-cam.y)*.1;
  near=null;
  let bestD=9999;
  for(const b of buildings){const dx=car.x-b.x,dy=car.y-b.y,d=Math.sqrt(dx*dx+dy*dy);if(d<85&&d<bestD){near=b;bestD=d;}}
  document.getElementById('sf').style.width=(Math.abs(car.speed)/MSPD*100).toFixed(0)+'%';
  document.getElementById('hn').innerHTML=near?'Near: <span>'+near.name+'</span>':'Drive to a glowing building';
}

function render(){
  const cw=canvas.width,ch=canvas.height;
  ctx.clearRect(0,0,cw,ch);
  ctx.save();ctx.translate(-cam.x+cw/2,-cam.y+ch/2);
  drawWorld();drawParticles();buildings.forEach(drawBuilding);drawCar();
  ctx.restore();drawMini();
}

function loop(){update();render();requestAnimationFrame(loop);}

function openM(b){
  modal=true;
  document.getElementById('micon').textContent=b.icon;
  document.getElementById('micon').style.background=b.bg;
  document.getElementById('mtitle').textContent=b.name;
  const ll=document.getElementById('mlang2');
  ll.textContent=b.lang;
  ll.style.cssText='background:'+b.bg+';color:'+b.tc+';border:1px solid '+b.color+'44';
  document.getElementById('mcat').textContent=b.category;
  document.getElementById('mdesc').textContent=b.desc;
  document.getElementById('mtags').innerHTML=b.tags.map(t=>'<span class="mtag">'+t+'</span>').join('');
  // buttons — only show if link exists
  let btns='';
  if(b.gh) btns+='<a class="bgh" href="'+b.gh+'" target="_blank">⑂ GitHub</a>';
  if(b.live) btns+='<a class="bli" href="'+b.live+'" target="_blank">🚀 Live Demo</a>';
  if(!b.gh&&!b.live) btns='<span style="font-size:12px;color:#484f58">No live link available</span>';
  document.getElementById('mbtns').innerHTML=btns;
  document.getElementById('ov').style.display='flex';
}
function closeM(){document.getElementById('ov').style.display='none';modal=false;}
document.getElementById('ov').addEventListener('click',e=>{if(e.target===document.getElementById('ov'))closeM();});

function bindKeys(){
  document.addEventListener('keydown',e=>{
    keys[e.key]=true;
    if((e.key==='Enter'||e.key===' ')&&near&&!modal){e.preventDefault();openM(near);}
    if(e.key==='Escape'&&modal)closeM();
  });
  document.addEventListener('keyup',e=>{keys[e.key]=false;});
}
function bindDpad(){
  [['dpu','up'],['dpd','down'],['dpl','left'],['dpr','right']].forEach(([id,dir])=>{
    const el=document.getElementById(id);
    const on=()=>{dp[dir]=1;el.classList.add('on');};
    const off=()=>{dp[dir]=0;el.classList.remove('on');};
    el.addEventListener('pointerdown',e=>{e.preventDefault();on();});
    el.addEventListener('pointerup',off);el.addEventListener('pointerleave',off);
  });
}
function toast(msg){
  const t=document.createElement('div');t.className='toast';t.textContent=msg;
  document.body.appendChild(t);setTimeout(()=>t.remove(),2800);
}
</script>
</body>
</html>"""

components.html(HTML, height=750, scrolling=False)
