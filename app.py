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
#intro{position:fixed;inset:0;background:#0d1117;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:999;gap:5px}
#intro .ca{font-size:58px;animation:bob 1.2s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
#intro h1{font-size:40px;font-weight:700;background:linear-gradient(120deg,#58a6ff,#bc8cff,#39d353);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-top:10px}
#intro .sub{font-size:13px;color:#7d8590;margin-bottom:4px}
#intro .badge{font-size:12px;color:#58a6ff;background:rgba(88,166,255,.1);border:1px solid rgba(88,166,255,.25);border-radius:20px;padding:4px 14px;margin-bottom:30px}
#intro .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;max-width:460px;width:90%;margin-bottom:26px}
#intro .card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:14px;text-align:center}
#intro .card .ci{font-size:20px;margin-bottom:5px}
#intro .card .ct{font-size:11px;color:#7d8590;line-height:1.4}
#intro button{background:linear-gradient(135deg,#58a6ff,#bc8cff);border:none;border-radius:12px;color:#fff;font-size:15px;font-weight:600;padding:13px 44px;cursor:pointer;box-shadow:0 4px 20px rgba(88,166,255,.3);transition:transform .15s}
#intro button:hover{transform:translateY(-2px)}
canvas{display:block}
#hud{position:fixed;top:14px;left:14px;background:rgba(13,17,23,.92);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:12px 16px;z-index:50;min-width:188px;backdrop-filter:blur(10px);display:none}
.hn{font-size:14px;font-weight:600;color:#e6edf3}.hr{font-size:11px;color:#58a6ff;margin-bottom:10px}
.hs{font-size:10px;color:#484f58;margin-bottom:3px}.hb{height:4px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden;margin-bottom:10px}
.hf{height:100%;background:linear-gradient(90deg,#39d353,#58a6ff);border-radius:2px;transition:width .1s;width:0%}
.hn2{font-size:11px;color:#7d8590}.hn2 span{color:#e3b341}
#mm{position:fixed;bottom:14px;right:14px;background:rgba(13,17,23,.92);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:10px;z-index:50;display:none}
.ml{font-size:9px;color:#484f58;text-transform:uppercase;letter-spacing:1px;text-align:center;margin-bottom:5px}
#hint{position:fixed;bottom:14px;left:14px;background:rgba(13,17,23,.85);border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:7px 13px;z-index:50;font-size:11px;color:#484f58;display:none}
#ov{position:fixed;inset:0;background:rgba(0,0,0,.72);display:none;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(8px)}
#mo{background:#161b22;border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:26px;max-width:400px;width:90%;position:relative;animation:su .22s ease}
@keyframes su{from{transform:translateY(18px);opacity:0}to{transform:translateY(0);opacity:1}}
.mh{display:flex;align-items:flex-start;gap:13px;margin-bottom:14px}
.mi{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0}
.mt2{font-size:17px;font-weight:600;color:#e6edf3;margin-bottom:4px}
.ml2{font-size:11px;padding:2px 10px;border-radius:20px;display:inline-block}
.md{font-size:13px;color:#7d8590;line-height:1.65;margin-bottom:14px}
.mtags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.mtag{font-size:11px;color:#7d8590;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:6px;padding:3px 10px}
.mbtns{display:flex;gap:8px}
.bgh{flex:1;padding:10px;border-radius:10px;font-size:13px;font-weight:500;text-align:center;text-decoration:none;background:rgba(255,255,255,.06);color:#e6edf3;border:1px solid rgba(255,255,255,.1);cursor:pointer;display:block;transition:background .15s}
.bgh:hover{background:rgba(255,255,255,.1)}
.bli{flex:1;padding:10px;border-radius:10px;font-size:13px;font-weight:600;text-align:center;text-decoration:none;background:linear-gradient(135deg,#58a6ff,#bc8cff);color:#fff;border:none;cursor:pointer;display:block}
.bcl{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:8px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);color:#7d8590;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.bcl:hover{background:rgba(255,255,255,.1);color:#e6edf3}
#dp{position:fixed;right:14px;bottom:128px;z-index:50;display:none;grid-template-areas:'. u .' 'l . r' '. d .';grid-template-columns:repeat(3,42px);grid-template-rows:repeat(3,42px);gap:3px}
.db{background:rgba(22,27,34,.92);border:1px solid rgba(255,255,255,.1);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:17px;color:#e6edf3;cursor:pointer;user-select:none;-webkit-user-select:none;touch-action:none;transition:background .1s}
.db.on{background:rgba(88,166,255,.35);border-color:#58a6ff}
#dpu{grid-area:u}#dpd{grid-area:d}#dpl{grid-area:l}#dpr{grid-area:r}
.toast{position:fixed;top:14px;left:50%;transform:translateX(-50%);background:rgba(57,211,83,.88);color:#fff;border-radius:20px;padding:7px 18px;font-size:12px;font-weight:500;z-index:200;animation:tf 2.6s ease forwards;white-space:nowrap}
@keyframes tf{0%{opacity:0;transform:translateX(-50%) translateY(-8px)}12%,78%{opacity:1;transform:translateX(-50%) translateY(0)}100%{opacity:0}}
</style>
</head>
<body>

<div id="intro">
  <div class="ca">🚗</div>
  <h1>Portfolio Drive</h1>
  <div class="sub">GitHub: Mkp-7 &nbsp;·&nbsp; Data Scientist & AI Engineer</div>
  <div class="badge">🤖 AI Agents · Analytics · Streamlit · Python</div>
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

<div id="mm"><div class="ml">Map</div><canvas id="mc" width="108" height="108"></canvas></div>
<div id="hint">WASD / Arrow keys &nbsp;·&nbsp; Mobile: D-pad</div>

<div id="ov">
  <div id="mo">
    <button class="bcl" onclick="closeM()">×</button>
    <div class="mh">
      <div class="mi" id="micon"></div>
      <div><div class="mt2" id="mtitle"></div><div class="ml2" id="mlang2"></div></div>
    </div>
    <div class="md" id="mdesc"></div>
    <div class="mtags" id="mtags"></div>
    <div class="mbtns">
      <a class="bgh" id="mgh" href="#" target="_blank">⑂ GitHub</a>
      <a class="bli" id="mli" href="#" target="_blank">🚀 Live Demo</a>
    </div>
  </div>
</div>

<div id="dp">
  <div class="db" id="dpu">↑</div>
  <div class="db" id="dpl">←</div>
  <div class="db" id="dpr">→</div>
  <div class="db" id="dpd">↓</div>
</div>

<script>
const PROJECTS=[
  {name:"Revenue Management Agent",icon:"🚗",color:"#58a6ff",bg:"rgba(88,166,255,.12)",tc:"#58a6ff",
   lang:"Python · Groq AI",
   desc:"Autonomous AI agent monitoring competitor car rental pricing across 10 US airports. Uses Groq llama-3.3-70b, GitHub Actions pipeline every 6h, and a 5-tab Streamlit dashboard with anomaly alerts and AI-driven pricing recommendations.",
   tags:["AI Agents","Groq LLM","Streamlit","GitHub Actions","Revenue Ops"],
   gh:"https://github.com/Mkp-7/Revenue-Management-Agent",
   live:"https://revenue-management-agent-rpyqjvfpghplga6ls4gph3.streamlit.app/"},
  {name:"AI Pricing Agent",icon:"🤖",color:"#bc8cff",bg:"rgba(188,140,255,.12)",tc:"#bc8cff",
   lang:"Python · Claude API",
   desc:"AI-powered competitive pricing intelligence system using the Claude API. Monitors competitor prices in real-time, applies ML models to recommend optimal pricing, and delivers explainable AI decisions for business stakeholders.",
   tags:["Claude API","Competitive Intel","ML","Pricing Strategy","Explainable AI"],
   gh:"https://github.com/Mkp-7/AI-Pricing-Agent",
   live:"https://ai-pricing-agent-ev34sy7v4zposplwcc2cyo.streamlit.app/"},
  {name:"EcoRoute Optimizer",icon:"🌿",color:"#39d353",bg:"rgba(57,211,83,.12)",tc:"#39d353",
   lang:"Python · OR-Tools",
   desc:"Sustainable logistics platform optimizing delivery routes to minimize carbon emissions. Uses Google OR-Tools and genetic algorithms with real-time traffic data and environmental impact scoring.",
   tags:["OR-Tools","Optimization","Sustainability","Logistics","Green Tech"],
   gh:"https://github.com/Mkp-7/EcoRoute-Optimizer",
   live:"https://ecoroute-optimizer-9zxsy43vdkaqwlrmo5fafj.streamlit.app/"},
  {name:"Banking Risk Analytics",icon:"🏦",color:"#f78166",bg:"rgba(247,129,102,.12)",tc:"#f78166",
   lang:"Python · Streamlit",
   desc:"Comprehensive banking risk intelligence platform covering credit, market, and operational risk. Features Basel III stress testing, PD/LGD/EAD modeling, and regulatory capital calculation dashboards.",
   tags:["Basel III","Credit Risk","Stress Testing","Finance","Risk Modeling"],
   gh:"https://github.com/Mkp-7/Banking-Risk-Analytics",
   live:"https://banking-risk-analytics-gqfn6y23ifuiuace8tgw5h.streamlit.app/"},
  {name:"Supply Chain Analytics BI",icon:"📦",color:"#e3b341",bg:"rgba(227,179,65,.12)",tc:"#e3b341",
   lang:"Python · Power BI",
   desc:"End-to-end supply chain BI platform with demand forecasting, supplier performance tracking, inventory optimization, and logistics KPI dashboards integrating predictive ML with interactive visualizations.",
   tags:["Supply Chain","BI","Demand Forecasting","Inventory","Power BI"],
   gh:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI",
   live:"https://github.com/Mkp-7/Supply-Chain-Analytics-BI"},
  {name:"Sales Forecasting Analysis",icon:"📈",color:"#79c0ff",bg:"rgba(121,192,255,.12)",tc:"#79c0ff",
   lang:"Python · Tableau",
   desc:"Tableau dashboard analyzing and forecasting sales performance using historical data. Implements time-series forecasting, seasonal decomposition, and interactive drill-down visualizations for sales trend analysis.",
   tags:["Tableau","Time Series","Forecasting","Sales Analytics","Visualization"],
   gh:"https://github.com/Mkp-7/Sales-Forecasting-Analysis",
   live:"https://github.com/Mkp-7/Sales-Forecasting-Analysis"}
];

const W=1400,H=1400;
const SLOTS=[{x:210,y:210},{x:700,y:180},{x:1190,y:210},{x:180,y:700},{x:1220,y:700},{x:210,y:1190},{x:700,y:1220},{x:1190,y:1190}];

let buildings=[],car={x:700,y:700,angle:0,speed:0},cam={x:700,y:700};
let keys={},dp={up:0,down:0,left:0,right:0},near=null,modal=false;
let particles=[],frame=0,canvas,ctx,mc,mctx;

function placeBuildings(){
  buildings=PROJECTS.map((p,i)=>({...p,x:SLOTS[i].x,y:SLOTS[i].y,w:108,h:108,lit:Array.from({length:16},()=>Math.random()>.38)}));
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
  toast('Drive to a glowing building and press Enter!');
}

function resize(){canvas.width=window.innerWidth;canvas.height=window.innerHeight;}

function shadeHex(hex,amt){
  const n=parseInt(hex.replace('#',''),16);
  const r=Math.max(0,Math.min(255,(n>>16)+amt));
  const g=Math.max(0,Math.min(255,((n>>8)&255)+amt));
  const b=Math.max(0,Math.min(255,(n&255)+amt));
  return 'rgb('+r+','+g+','+b+')';
}

function drawWorld(){
  ctx.fillStyle='#0d1117';ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(33,45,60,.5)';ctx.lineWidth=.5;
  for(let x=0;x<W;x+=80){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
  for(let y=0;y<H;y+=80){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
  const roads=[{x:0,y:420,w:W,h:90},{x:0,y:890,w:W,h:90},{x:420,y:0,w:90,h:H},{x:890,y:0,w:90,h:H}];
  roads.forEach(r=>{ctx.fillStyle='#161b22';ctx.fillRect(r.x,r.y,r.w,r.h);});
  ctx.setLineDash([26,18]);ctx.strokeStyle='#21262d';ctx.lineWidth=2;
  [[0,465,W,465],[0,935,W,935],[465,0,465,H],[935,0,935,H]].forEach(([x1,y1,x2,y2])=>{ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();});
  ctx.setLineDash([]);
  [[420,420],[420,890],[890,420],[890,890]].forEach(([x,y])=>{ctx.fillStyle='#1c2128';ctx.fillRect(x,y,90,90);});
}

function drawBuilding(b){
  const bx=b.x-b.w/2,by=b.y-b.h/2,isN=near===b;
  const pulse=isN?Math.sin(frame*.07)*.4+.7:1;
  ctx.fillStyle='#131924';ctx.beginPath();ctx.roundRect(bx-10,by-10,b.w+20,b.h+20,8);ctx.fill();
  if(isN){ctx.shadowColor=b.color;ctx.shadowBlur=30*pulse;}
  ctx.fillStyle=isN?b.color:shadeHex(b.color,-65);
  ctx.beginPath();ctx.roundRect(bx,by,b.w,b.h,10);ctx.fill();
  ctx.shadowBlur=0;
  ctx.fillStyle=b.color;ctx.globalAlpha=.55;
  ctx.beginPath();ctx.roundRect(bx,by,b.w,13,[10,10,0,0]);ctx.fill();
  ctx.globalAlpha=1;
  for(let r=0;r<4;r++) for(let c=0;c<4;c++){
    const wx=bx+11+c*22,wy=by+19+r*19,lit=b.lit[r*4+c];
    ctx.fillStyle=lit?'#ffd700':'rgba(120,180,255,.1)';
    ctx.globalAlpha=lit?(isN?1:.75):.35;
    ctx.fillRect(wx,wy,12,9);ctx.globalAlpha=1;
  }
  ctx.font='18px serif';ctx.textAlign='center';ctx.fillText(b.icon,b.x,by-14);
  const short=b.name.length>17?b.name.slice(0,17)+'…':b.name;
  ctx.font=(isN?'600':'500')+' 11px system-ui';
  ctx.fillStyle=isN?'#e6edf3':'rgba(180,195,215,.7)';
  ctx.fillText(short,b.x,by+b.h+18);
  if(isN){
    ctx.font='700 10px system-ui';ctx.fillStyle='#e3b341';
    ctx.globalAlpha=pulse;ctx.fillText('PRESS ENTER',b.x,by-28);ctx.globalAlpha=1;
  }
}

function drawCar(){
  const cw=24,ch=38;
  ctx.save();ctx.translate(car.x,car.y);ctx.rotate(car.angle);
  ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(2,5,cw/2+4,7,0,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#f0c000';ctx.beginPath();ctx.roundRect(-cw/2,-ch/2,cw,ch,6);ctx.fill();
  ctx.fillStyle='#c87000';ctx.fillRect(-cw/2,-ch/2,cw,11);
  ctx.fillStyle='rgba(140,220,255,.72)';ctx.fillRect(-cw/2+3,-ch/2+2,cw-6,8);
  ctx.fillStyle='rgba(255,248,180,.95)';
  ctx.fillRect(-cw/2+2,-ch/2+1,5,4);ctx.fillRect(cw/2-7,-ch/2+1,5,4);
  ctx.fillStyle='#e74c3c';
  ctx.fillRect(-cw/2+2,ch/2-6,5,4);ctx.fillRect(cw/2-7,ch/2-6,5,4);
  if(Math.abs(car.speed)>2.5){
    ctx.strokeStyle='rgba(255,255,255,.13)';ctx.lineWidth=1;
    for(let i=0;i<4;i++){ctx.beginPath();ctx.moveTo(-cw/2+4+i*6,ch/2);ctx.lineTo(-cw/2+2+i*6,ch/2+11);ctx.stroke();}
  }
  ctx.restore();
  if(Math.abs(car.speed)>1&&frame%3===0){
    particles.push({x:car.x-Math.sin(car.angle)*20+(Math.random()-.5)*6,y:car.y+Math.cos(car.angle)*20+(Math.random()-.5)*6,life:1,r:3});
  }
}

function drawParticles(){
  particles=particles.filter(p=>p.life>0);
  particles.forEach(p=>{
    ctx.globalAlpha=p.life*.35;ctx.fillStyle='#8b949e';
    ctx.beginPath();ctx.arc(p.x,p.y,p.r*p.life,0,Math.PI*2);ctx.fill();
    p.life-=.065;
  });ctx.globalAlpha=1;
}

function drawMini(){
  const s=108/W;
  mctx.fillStyle='#0d1117';mctx.fillRect(0,0,108,108);
  mctx.fillStyle='#161b22';
  [{x:0,y:420,w:W,h:90},{x:0,y:890,w:W,h:90},{x:420,y:0,w:90,h:H},{x:890,y:0,w:90,h:H}]
    .forEach(r=>mctx.fillRect(r.x*s,r.y*s,r.w*s,r.h*s));
  buildings.forEach(b=>{mctx.fillStyle=b.color;mctx.beginPath();mctx.arc(b.x*s,b.y*s,4,0,Math.PI*2);mctx.fill();});
  mctx.fillStyle='#f0c000';mctx.beginPath();mctx.arc(car.x*s,car.y*s,4,0,Math.PI*2);mctx.fill();
}

const ACCEL=.24,FRIC=.87,MSPD=6.5,TURN=.054;
function update(){
  if(modal)return;frame++;
  const U=keys['ArrowUp']||keys['w']||keys['W']||dp.up;
  const D=keys['ArrowDown']||keys['s']||keys['S']||dp.down;
  const L=keys['ArrowLeft']||keys['a']||keys['A']||dp.left;
  const R=keys['ArrowRight']||keys['d']||keys['D']||dp.right;
  if(U) car.speed=Math.min(car.speed+ACCEL,MSPD);
  else if(D) car.speed=Math.max(car.speed-ACCEL,-MSPD*.5);
  else car.speed*=FRIC;
  if(Math.abs(car.speed)>.15){const d=car.speed>0?1:-1;if(L)car.angle-=TURN*d;if(R)car.angle+=TURN*d;}
  car.x+=Math.sin(car.angle)*car.speed;car.y-=Math.cos(car.angle)*car.speed;
  car.x=Math.max(20,Math.min(W-20,car.x));car.y=Math.max(20,Math.min(H-20,car.y));
  cam.x+=(car.x-cam.x)*.1;cam.y+=(car.y-cam.y)*.1;
  near=null;
  for(const b of buildings){const dx=car.x-b.x,dy=car.y-b.y;if(Math.sqrt(dx*dx+dy*dy)<88){near=b;break;}}
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
  document.getElementById('mlang2').textContent=b.lang;
  document.getElementById('mlang2').style.cssText='background:'+b.bg+';color:'+b.tc+';border:1px solid '+b.color+'44';
  document.getElementById('mdesc').textContent=b.desc;
  document.getElementById('mtags').innerHTML=b.tags.map(t=>'<span class="mtag">'+t+'</span>').join('');
  document.getElementById('mgh').href=b.gh;
  document.getElementById('mli').href=b.live;
  document.getElementById('ov').style.display='flex';
}
function closeM(){document.getElementById('ov').style.display='none';modal=false;}
document.getElementById('ov').addEventListener('click',e=>{if(e.target===document.getElementById('ov'))closeM();});

function bindKeys(){
  document.addEventListener('keydown',e=>{
    keys[e.key]=true;
    if((e.key==='Enter'||e.key===' ')&&near&&!modal)openM(near);
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
  document.body.appendChild(t);setTimeout(()=>t.remove(),2700);
}
</script>
</body>
</html>"""

components.html(HTML, height=750, scrolling=False)
