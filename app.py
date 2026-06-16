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
  display:flex;flex-direction:column;
  overflow:hidden;
}

/* Animated particle canvas behind intro */
#particle-canvas{position:absolute;inset:0;z-index:0;pointer-events:none}

/* Glowing grid lines */
#intro::before{
  content:'';position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(74,144,217,.06) 1px,transparent 1px),
    linear-gradient(90deg,rgba(74,144,217,.06) 1px,transparent 1px);
  background-size:60px 60px;
  animation:gridScroll 20s linear infinite;
  z-index:1;pointer-events:none;
}
@keyframes gridScroll{from{background-position:0 0}to{background-position:60px 60px}}

/* Radial spotlight */
#intro::after{
  content:'';position:absolute;inset:0;z-index:2;
  background:radial-gradient(ellipse 70% 60% at 50% 45%,rgba(74,144,217,.08) 0%,transparent 70%);
  pointer-events:none;
}

/* NAV */
#lnav{position:absolute;top:0;left:0;right:0;z-index:20;height:52px;
  display:flex;align-items:center;justify-content:space-between;padding:0 28px;
  background:rgba(4,8,15,.88);border-bottom:1px solid rgba(74,144,217,.1);
  backdrop-filter:blur(16px)}
.lnav-logo{font-size:14px;font-weight:700;color:#eef2ff;letter-spacing:.5px}
.lnav-logo span{color:#4a90d9}
.lnav-links{display:flex;gap:2px}
.lnav-link{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#3a4d68;
  padding:6px 11px;border-radius:6px;cursor:pointer;transition:all .2s;
  border:none;background:none;font-family:inherit}
.lnav-link:hover,.lnav-link.active{color:#c8d8f0;background:rgba(74,144,217,.1)}
.lnav-cta{font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
  background:#4a90d9;color:#fff;border:none;border-radius:6px;
  padding:7px 15px;cursor:pointer;transition:all .2s;font-family:inherit}
.lnav-cta:hover{background:#5aa0e9}

/* SCROLLABLE */
#lscroll{position:absolute;inset:0;top:52px;overflow-y:auto;overflow-x:hidden;z-index:10}

/* SECTIONS */
.lsec{min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:60px 24px 40px;position:relative}
.lsec-inner{width:100%;max-width:820px;margin:0 auto}
.lsec-eye{font-size:10px;letter-spacing:3px;color:#4a90d9;text-transform:uppercase;margin-bottom:8px}
.lsec-title{font-size:clamp(24px,4vw,36px);font-weight:700;color:#eef2ff;letter-spacing:-1px;margin-bottom:8px}
.lsec-div{width:32px;height:2px;background:#4a90d9;margin:0 0 26px;
  transform:scaleX(0);transform-origin:left;transition:transform .6s .2s ease}

/* Scroll-reveal base state */
.reveal{opacity:0;transform:translateY(32px);transition:opacity .65s ease,transform .65s ease}
.reveal.in{opacity:1;transform:translateY(0)}
.reveal-left{opacity:0;transform:translateX(-32px);transition:opacity .65s ease,transform .65s ease}
.reveal-left.in{opacity:1;transform:translateX(0)}
.reveal-scale{opacity:0;transform:scale(.94);transition:opacity .55s ease,transform .55s ease}
.reveal-scale.in{opacity:1;transform:scale(1)}
/* stagger children */
.stagger>*{opacity:0;transform:translateY(20px);transition:opacity .5s ease,transform .5s ease}
.stagger.in>*{opacity:1;transform:translateY(0)}
.stagger.in>*:nth-child(1){transition-delay:.05s}
.stagger.in>*:nth-child(2){transition-delay:.15s}
.stagger.in>*:nth-child(3){transition-delay:.25s}
.stagger.in>*:nth-child(4){transition-delay:.35s}
.stagger.in>*:nth-child(5){transition-delay:.45s}
.stagger.in>*:nth-child(6){transition-delay:.55s}
/* div bar animation trigger */
.lsec-inner.in .lsec-div{transform:scaleX(1)}

/* SUMMARY LINE */
.lsummary,.hero-summary{font-size:13.5px;color:#4a6080;line-height:1.82;max-width:640px;
  margin:0 auto 24px;animation:fadeUp .9s .25s ease both}
.lsummary strong,.hero-summary strong{color:#7a9ab8;font-weight:500}

/* CARDS */
.l2col{display:grid;grid-template-columns:1fr 1fr;gap:14px;width:100%}
@media(max-width:580px){.l2col{grid-template-columns:1fr}}
.lcard{background:rgba(255,255,255,.025);border:1px solid rgba(255,255,255,.07);
  border-radius:12px;padding:20px}
.lcard-head{font-size:10px;letter-spacing:2px;color:#4a90d9;text-transform:uppercase;margin-bottom:14px}
.lfield{margin-bottom:12px}.lfield:last-child{margin-bottom:0}
.lfield-lbl{font-size:9px;letter-spacing:1px;color:#2e4058;text-transform:uppercase;margin-bottom:3px}
.lfield-lbl.lfield-title{font-size:13px;letter-spacing:.2px;color:#c8d8f0;text-transform:none;font-weight:600;margin-bottom:4px}
.lfield-val{font-size:12.5px;color:#7a9ab8;line-height:1.6}
.lfield-val strong{color:#c8d8f0;font-weight:500}
.lchips{display:flex;flex-wrap:wrap;gap:5px;margin-top:5px}
.lchip{font-size:10px;color:#4a7096;background:rgba(74,144,217,.07);
  border:1px solid rgba(74,144,217,.14);border-radius:4px;padding:3px 8px}
.lchip-bright{font-size:10px;color:#c8d8f0;background:rgba(74,144,217,.07);
  border:1px solid rgba(74,144,217,.14);border-radius:4px;padding:3px 8px;font-weight:500}
.lchip-link{font-size:10px;color:#c8d8f0;background:rgba(74,144,217,.07);
  border:1px solid rgba(74,144,217,.14);border-radius:4px;padding:3px 8px;font-weight:500;
  text-decoration:none;display:inline-flex;align-items:center;gap:4px;transition:all .15s}
.lchip-link:hover{background:rgba(74,144,217,.16);border-color:rgba(74,144,217,.35);color:#fff}
.lchip-link::after{content:'↗';font-size:9px;opacity:.6}

/* EXPERIENCE */
.lexp{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.07);
  border-radius:12px;padding:18px 20px;margin-bottom:12px;border-left:3px solid #4a90d9}
.lexp-hd{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;gap:12px}
.lexp-role{font-size:14px;font-weight:600;color:#eef2ff;margin-bottom:3px}
.lexp-org{font-size:11px;margin-bottom:7px}
.lexp-date{font-size:9px;letter-spacing:1px;color:#2e4058;text-transform:uppercase;white-space:nowrap;padding-top:3px}
.lexp-tags{margin-bottom:4px}
.letag{display:inline-block;font-size:9px;letter-spacing:.5px;border-radius:3px;
  padding:2px 7px;margin-right:4px;margin-bottom:3px;text-transform:uppercase;border:1px solid}
.lexp-ul{list-style:none;padding:0}
.lexp-ul li{font-size:12px;color:#4a6080;line-height:1.72;padding-left:14px;
  position:relative;margin-bottom:4px}
.lexp-ul li::before{content:'→';position:absolute;left:0;color:#4a90d9;font-size:9px;top:4px}

/* CONTACT */
.lcont-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;width:100%}
.lcont-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.07);
  border-radius:12px;padding:18px;text-align:center;transition:all .2s;
  text-decoration:none;display:block;color:inherit}
.lcont-card:hover{background:rgba(74,144,217,.06);border-color:rgba(74,144,217,.22);transform:translateY(-2px)}
.lcont-icon{font-size:24px;margin-bottom:9px}
.lcont-lbl{font-size:9px;letter-spacing:2px;color:#2e4058;text-transform:uppercase;margin-bottom:4px}
.lcont-val{font-size:12px;color:#7a9ab8;font-weight:500}
.lexplore-banner{background:rgba(74,144,217,.07);border:1px solid rgba(74,144,217,.18);
  border-radius:12px;padding:24px;text-align:center;margin-top:18px;width:100%}

/* BACK BUTTON (in game) */
#back-btn{position:fixed;top:14px;right:14px;z-index:300;display:none;
  background:rgba(4,8,15,.9);border:1px solid rgba(74,144,217,.2);border-radius:8px;
  color:#4a90d9;font-size:10px;font-weight:600;padding:8px 14px;cursor:pointer;
  letter-spacing:.5px;text-transform:uppercase;font-family:inherit;transition:all .2s}
#back-btn:hover{background:rgba(74,144,217,.1)}

.intro-content{
  position:relative;z-index:10;
  display:flex;flex-direction:column;align-items:center;
  max-width:780px;width:90%;text-align:center;
  padding:30px 0 20px;
}

/* Availability pill */
/* Profile photo */
.profile-photo{
  width:118px;height:118px;border-radius:50%;
  object-fit:cover;object-position:center top;
  border:3px solid rgba(74,144,217,.35);
  box-shadow:0 0 0 6px rgba(74,144,217,.06), 0 8px 30px rgba(0,0,0,.4);
  margin-bottom:20px;
  animation:fadeDown .8s ease both;
}

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

.dist-row{
  display:flex;flex-wrap:wrap;justify-content:center;gap:8px;
  animation:fadeUp .9s .6s ease both;
}
.dist-chip{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;
  padding:8px 16px;border-radius:8px;border:1px solid;
  transition:all .22s;cursor:default;
}
.dist-chip:hover{transform:translateY(-2px);filter:brightness(1.18)}
.dist-pip{width:8px;height:8px;border-radius:50%;flex-shrink:0}

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

/* HINT (desktop only - see media query above) */

/* ════ DEVICE-ADAPTIVE CONTROLS ════ */
#dpad{display:none!important}
/* mcontrols wrapper hidden — individual elements positioned separately */
#mcontrols{display:none!important}

/* ── Steering wheel — bottom-left ── */
#steering-wrap{
  position:fixed;left:12px;bottom:12px;z-index:60;
  display:none; /* shown by JS on touch devices */
  flex-direction:column;align-items:center;gap:3px;
}
#mc-wheel{
  width:100px;height:100px;border-radius:50%;
  background:rgba(4,8,15,.92);
  border:3px solid rgba(74,144,217,.45);
  position:relative;
  cursor:grab;user-select:none;-webkit-user-select:none;touch-action:none;
}
#mc-wheel::before{
  content:'';position:absolute;inset:6px;border-radius:50%;
  border:1px solid rgba(74,144,217,.18);pointer-events:none;
}
#mc-wheel-spoke{
  position:absolute;top:50%;left:50%;
  width:68px;height:3px;background:rgba(74,144,217,.65);border-radius:2px;
  transform:translate(-50%,-50%);
  pointer-events:none;
}
#mc-wheel-hub{
  position:absolute;top:50%;left:50%;
  width:14px;height:14px;border-radius:50%;
  background:#4a90d9;transform:translate(-50%,-50%);
  pointer-events:none;box-shadow:0 0 8px #4a90d9;
}
#mc-wheel-marker{
  position:absolute;top:5px;left:50%;
  width:7px;height:12px;border-radius:3px;
  background:#4a90d9;transform:translateX(-50%);
  pointer-events:none;
}
#mc-wheel-lbl{
  font-size:9px;letter-spacing:1.5px;color:#2a3d52;text-transform:uppercase;
}

/* ── Pedals — bottom-right ── */
#pedals{
  position:fixed;right:12px;bottom:12px;z-index:60;
  display:none; /* shown by JS on touch devices */
  flex-direction:row;gap:8px;align-items:flex-end;
}
.mc-btn{
  background:rgba(4,8,15,.9);
  border-radius:12px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:2px;
  font-size:22px;color:#4a6a8a;cursor:pointer;
  user-select:none;-webkit-user-select:none;touch-action:none;
  transition:background .1s,border-color .1s;
}
#mc-brake{width:60px;height:60px;border:2px solid rgba(232,85,85,.4);color:#e85555}
#mc-brake.on{background:rgba(232,85,85,.22);border-color:#e85555;color:#fff}
#mc-accel{width:60px;height:60px;border:2px solid rgba(62,207,142,.4);color:#3ecf8e}
#mc-accel.on{background:rgba(62,207,142,.22);border-color:#3ecf8e;color:#fff}

/* Hint box — desktop only */
#hint-box{position:fixed;bottom:16px;left:16px;display:none;background:rgba(4,8,15,.88);border:1px solid rgba(255,255,255,.06);border-radius:8px;padding:7px 13px;font-size:10px;color:#2e4058;z-index:50;line-height:2}

/* ════ RESPONSIVE LANDING PAGE ════ */
@media(max-width:640px){
  /* Nav */
  #lnav{padding:0 14px;height:48px}
  .lnav-links{display:none}
  .lnav-logo{font-size:13px}
  .lnav-cta{font-size:10px;padding:6px 12px}
  /* Hero text — tighter for mobile */
  .profile-photo{width:88px;height:88px;margin-bottom:14px}
  .intro-name{font-size:clamp(30px,9vw,48px);letter-spacing:-1px}
  .intro-role{font-size:12px;margin-bottom:16px}
  .lsummary,.hero-summary{font-size:12px;padding:0 4px;margin-bottom:16px}
  .domain-row{gap:4px;margin-bottom:16px}
  .domain-tag{font-size:9.5px;padding:3px 8px}
  .stats-row{flex-wrap:wrap}
  .stat-item{min-width:50%;border-bottom:1px solid rgba(255,255,255,.06)}
  .stat-num{font-size:18px}
  .stat-lbl{font-size:9px}
  .cta-row{flex-wrap:wrap;gap:7px;justify-content:center;margin-bottom:18px}
  .btn-primary,.btn-outline,.btn-enter{font-size:11px;padding:10px 14px;gap:5px}
  .dist-row{gap:4px;margin-top:12px}
  .dist-chip{font-size:9.5px;padding:5px 9px;gap:5px}
  .scroll-hint{margin-top:14px;font-size:9px}
  /* Sections */
  .lsec{padding:36px 12px 24px}
  .lsec-title{font-size:clamp(19px,5vw,26px)}
  .lsec-eye{font-size:9px}
  .l2col{grid-template-columns:1fr}
  .lcard{padding:12px}
  .lfield-val{font-size:12px}
  /* Experience */
  .lexp{padding:12px 12px}
  .lexp-role{font-size:12.5px}
  .lexp-ul li{font-size:11px;line-height:1.6}
  /* Contact grid */
  .lcont-grid{grid-template-columns:1fr 1fr}
  .lcont-card{padding:14px 10px}
  .lcont-icon{font-size:20px;margin-bottom:6px}
  .lcont-val{font-size:11px}
  /* Game UI — mobile adjustments */
  #mm-wrap{top:10px;right:10px;bottom:auto} /* minimap top-right on mobile */
  .mm-lbl{display:none} /* hide label to save space */
  #mm{width:90px;height:90px}
  #hud{min-width:150px;max-width:55vw}
  .hud-box{padding:8px 10px}
  .hud-val{font-size:11px}
  .hud-lbl{font-size:8px}
  .hud-enter{display:none!important}
}
@media(min-width:641px){
  /* Desktop: force-hide all mobile controls */
  #steering-wrap{display:none!important}
  #pedals{display:none!important}
}

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

<!-- ════════════ LANDING ════════════ -->
<div id="intro">
<canvas id="particle-canvas"></canvas>

<!-- NAV -->
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

<!-- SCROLLABLE BODY -->
<div id="lscroll">

<!-- HERO -->
<section class="lsec" id="s-hero">
  <div class="intro-content">
    <img class="profile-photo" src="data:image/jpeg;base64,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" alt="Mukund Patel">
    <div class="avail-pill"><span class="avail-dot"></span>Open to full-time opportunities</div>
    <div class="intro-name">Mukund <span class="accent">Patel</span></div>
    <div class="intro-role"><strong>Data Scientist</strong> &nbsp;·&nbsp; <strong>AI Engineer</strong> &nbsp;·&nbsp; <strong>Analytics Professional</strong></div>
    <div class="lsummary">MS Data Science graduate from <strong>Montclair State University</strong> (GPA 4.0) with hands-on experience at the <strong>MTA New York</strong> building data pipelines, and BI dashboards. I build end-to-end analytics solutions — from SQL pipelines and ML models to deployed AI applications — across transportation, finance, healthcare, retail, and logistics.</div>
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
      <a class="btn-outline" href="https://www.linkedin.com/in/mukund-patel7" target="_blank">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a class="btn-outline" href="https://github.com/Mkp-7" target="_blank">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
        GitHub
      </a>
      <a class="btn-outline" href="https://raw.githubusercontent.com/Mkp-7/portfolio-drive/main/Resume_Mukund_Patel.pdf" download="Mukund_Patel_Resume.pdf">&#8595; Resume</a>
      <button class="btn-primary" onclick="startGame()">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Explore Portfolio
      </button>
    </div>
    <div class="dist-row">
      <div class="dist-chip" style="color:#7eb8f7;background:rgba(74,144,217,.12);border-color:rgba(74,144,217,.4)"><div class="dist-pip" style="background:#4a90d9;box-shadow:0 0 8px #4a90d9"></div>Retail &amp; Commerce</div>
      <div class="dist-chip" style="color:#f08080;background:rgba(232,85,85,.12);border-color:rgba(232,85,85,.4)"><div class="dist-pip" style="background:#e85555;box-shadow:0 0 8px #e85555"></div>Finance &amp; Banking</div>
      <div class="dist-chip" style="color:#f5c878;background:rgba(245,166,35,.12);border-color:rgba(245,166,35,.4)"><div class="dist-pip" style="background:#f5a623;box-shadow:0 0 8px #f5a623"></div>Operations &amp; Logistics</div>
      <div class="dist-chip" style="color:#6ee8b4;background:rgba(62,207,142,.12);border-color:rgba(62,207,142,.4)"><div class="dist-pip" style="background:#3ecf8e;box-shadow:0 0 8px #3ecf8e"></div>Healthcare &amp; Life Sci.</div>
      <div class="dist-chip" style="color:#c4a8ff;background:rgba(155,109,255,.12);border-color:rgba(155,109,255,.4)"><div class="dist-pip" style="background:#9b6dff;box-shadow:0 0 8px #9b6dff"></div>Research &amp; Education</div>
    </div>
    <div class="scroll-hint">&#8595; &nbsp; scroll to explore &nbsp; &#8595;</div>
  </div>
</section>

<!-- ABOUT -->
<section class="lsec" id="s-about">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">About</div>
    <div class="lsec-title reveal">Who Am I</div>
    <div class="lsec-div"></div>
    <div class="l2col stagger">
      <div class="lcard">
        <div class="lcard-head">Education</div>
        <div class="lfield"><div class="lfield-lbl lfield-title">Master of Science &middot; Data Science</div><div class="lfield-val"><strong>Montclair State University</strong></div><div class="lfield-val">New Jersey, USA &nbsp;&middot;&nbsp; GPA 4.0 / 4.0</div><div class="lfield-val">Sep 2024 &ndash; May 2026</div></div>
        <div class="lfield"><div class="lfield-lbl lfield-title">Bachelor of Engineering &middot; Information Technology</div><div class="lfield-val"><strong>CVM University, India</strong></div><div class="lfield-val">GPA 3.58 / 4.0 &nbsp;&middot;&nbsp; Jun 2020 &ndash; Mar 2024</div></div>
        <div class="lfield"><div class="lfield-lbl">Location</div><div class="lfield-val">Clifton, New Jersey, USA</div></div>
      </div>
      <div class="lcard">
        <div class="lcard-head">Technical Skills</div>
        <div class="lfield"><div class="lfield-lbl">Languages</div><div class="lchips"><span class="lchip-bright">Python</span><span class="lchip-bright">SQL</span><span class="lchip-bright">R</span><span class="lchip-bright">DAX</span><span class="lchip-bright">Power Query</span></div></div>
        <div class="lfield"><div class="lfield-lbl">BI &amp; Visualization</div><div class="lchips"><span class="lchip-bright">Tableau</span><span class="lchip-bright">Power BI</span><span class="lchip-bright">Looker Studio</span><span class="lchip-bright">ArcGIS</span></div></div>
        <div class="lfield"><div class="lfield-lbl">Data &amp; Cloud</div><div class="lchips"><span class="lchip-bright">BigQuery</span><span class="lchip-bright">dbt</span><span class="lchip-bright">PostgreSQL</span><span class="lchip-bright">MySQL</span><span class="lchip-bright">GCP</span></div></div>
        <div class="lfield"><div class="lfield-lbl">AI &amp; ML</div><div class="lchips"><span class="lchip-bright">Scikit-learn</span><span class="lchip-bright">TensorFlow</span><span class="lchip-bright">Claude API</span><span class="lchip-bright">Groq</span><span class="lchip-bright">Gemini</span><span class="lchip-bright">Streamlit</span></div></div>
      </div>
      <div class="lcard" style="grid-column:1/-1">
        <div class="lcard-head">Certifications</div>
        <div class="lchips">
          <a class="lchip-link" href="https://www.coursera.org/account/accomplishments/certificate/TSJ4R9S9BTAF" target="_blank" rel="noopener">Data Science Fundamentals &middot; Databricks</a>
          <a class="lchip-link" href="https://www.coursera.org/account/accomplishments/specialization/certificate/MPYTC1Z5RWS0" target="_blank" rel="noopener">Microsoft 365 Fundamentals</a>
          <a class="lchip-link" href="https://www.coursera.org/account/accomplishments/verify/CH8C35WNNSKS" target="_blank" rel="noopener">Machine Learning with Python &middot; IBM</a>
          <a class="lchip-link" href="https://www.coursera.org/account/accomplishments/certificate/SEM77V2P57A7" target="_blank" rel="noopener">Applied Business Analytics &middot; Univ. of Illinois</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- EXPERIENCE -->
<section class="lsec" id="s-exp">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">Career</div>
    <div class="lsec-title reveal">Professional Experience</div>
    <div class="lsec-div"></div>
    <div class="stagger">
    <div class="lexp" style="border-left-color:#4a90d9">
      <div class="lexp-hd"><div><div class="lexp-role">Data Analyst Intern</div><div class="lexp-org" style="color:#4a90d9">MTA &mdash; Metropolitan Transportation Authority &middot; New York, NY</div><div class="lexp-tags"><span class="letag" style="color:#4a90d9;background:rgba(74,144,217,.08);border-color:rgba(74,144,217,.2)">Computer Vision</span><span class="letag" style="color:#4a90d9;background:rgba(74,144,217,.08);border-color:rgba(74,144,217,.2)">ArcGIS</span><span class="letag" style="color:#4a90d9;background:rgba(74,144,217,.08);border-color:rgba(74,144,217,.2)">Tableau</span><span class="letag" style="color:#4a90d9;background:rgba(74,144,217,.08);border-color:rgba(74,144,217,.2)">Python ETL</span><span class="letag" style="color:#4a90d9;background:rgba(74,144,217,.08);border-color:rgba(74,144,217,.2)">SQL</span></div></div><div class="lexp-date">Oct 2025 &ndash; May 2026</div></div>
      <ul class="lexp-ul"><li>Automated data processing and validation for 8,500+ events using Python and Office Scripts, improving data quality.</li><li>Managed master data for 1,400+ bus routes via SQL and Excel; ArcGIS spatial analysis to identify route overlaps.</li><li>Built computer vision pipeline detecting bus lane violations from 900+ cameras at 92% accuracy; integrated with Tableau dashboards.</li><li>Developed ETL workflow processing driver trip logs to calculate pull-in/pull-out counts per depot at 30-minute intervals.</li></ul>
    </div>
    <div class="lexp" style="border-left-color:#9b6dff">
      <div class="lexp-hd"><div><div class="lexp-role">Graduate Research Assistant</div><div class="lexp-org" style="color:#9b6dff">Montclair State University &middot; New Jersey</div><div class="lexp-tags"><span class="letag" style="color:#9b6dff;background:rgba(155,109,255,.08);border-color:rgba(155,109,255,.2)">SQL</span><span class="letag" style="color:#9b6dff;background:rgba(155,109,255,.08);border-color:rgba(155,109,255,.2)">Tableau</span><span class="letag" style="color:#9b6dff;background:rgba(155,109,255,.08);border-color:rgba(155,109,255,.2)">Data Governance</span></div></div><div class="lexp-date">Aug 2025 &ndash; May 2026</div></div>
      <ul class="lexp-ul"><li>Standardized institution-wide student master data (8,000+ records) using SQL for federal compliance and regulatory reporting.</li><li>Created Tableau dashboards analyzing 5+ years of enrollment, financial aid, and academic outcome data for leadership stakeholders.</li></ul>
    </div>
    <div class="lexp" style="border-left-color:#f5a623">
      <div class="lexp-hd"><div><div class="lexp-role">Data Analyst</div><div class="lexp-org" style="color:#f5a623">Montclair State University &middot; New Jersey</div><div class="lexp-tags"><span class="letag" style="color:#f5a623;background:rgba(245,166,35,.08);border-color:rgba(245,166,35,.2)">Power BI</span><span class="letag" style="color:#f5a623;background:rgba(245,166,35,.08);border-color:rgba(245,166,35,.2)">Python Maps</span></div></div><div class="lexp-date">Apr 2025 &ndash; Aug 2025</div></div>
      <ul class="lexp-ul"><li>Streamlined data cleaning, reducing processing time by 30%; structured raw data into partner and population segments.</li><li>Developed interactive Python map and Power BI dashboards analyzing 150+ community investment activities.</li></ul>
    </div>
    <div class="lexp" style="border-left-color:#3ecf8e">
      <div class="lexp-hd"><div><div class="lexp-role">Research Volunteer</div><div class="lexp-org" style="color:#3ecf8e">Montclair State University &middot; New Jersey</div></div><div class="lexp-date">Nov 2024</div></div>
      <ul class="lexp-ul"><li>Processed NJ weather data (1915&ndash;2024) contributing to research showing ARIMA/SARIMA outperform deep learning for time-series forecasting.</li></ul>
    </div>
  </div><!-- end stagger -->
  </div>
</section>

<!-- CONTACT -->
<section class="lsec" id="s-contact">
  <div class="lsec-inner">
    <div class="lsec-eye reveal">Get In Touch</div>
    <div class="lsec-title reveal">Contact</div>
    <div class="lsec-div"></div>
    <div class="lcont-grid stagger">
      <a class="lcont-card" href="mailto:mkpatel4102@gmail.com"><div class="lcont-icon">&#9993;&#65039;</div><div class="lcont-lbl">Email</div><div class="lcont-val">mkpatel4102@gmail.com</div></a>
      <a class="lcont-card" href="https://www.linkedin.com/in/mukund-patel7" target="_blank"><div class="lcont-icon">&#128188;</div><div class="lcont-lbl">LinkedIn</div><div class="lcont-val">linkedin.com/in/mukund-patel7</div></a>
      <a class="lcont-card" href="https://github.com/Mkp-7" target="_blank"><div class="lcont-icon">&#128187;</div><div class="lcont-lbl">GitHub</div><div class="lcont-val">github.com/Mkp-7</div></a>
      <div class="lcont-card" style="cursor:default"><div class="lcont-icon">&#128205;</div><div class="lcont-lbl">Location</div><div class="lcont-val">Clifton, New Jersey, USA</div></div>
    </div>
    <div class="lexplore-banner reveal">
      <div style="font-size:17px;font-weight:600;color:#eef2ff;margin-bottom:8px">Explore Projects Interactively</div>
      <div style="font-size:13px;color:#4a6080;margin-bottom:16px;line-height:1.7">Drive through a 3D city where each building is a project. Pull into any glowing entrance and press Enter to view details, live demo, and GitHub.</div>
      <button class="btn-primary" onclick="startGame()">&#9654; &nbsp;Enter Portfolio City</button>
    </div>
  </div>
</section>

</div><!-- end #lscroll -->
</div><!-- end #intro -->

<!-- BACK BUTTON -->
<button id="back-btn" onclick="backToPortfolio()">&#8592; Portfolio</button>

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

<!-- MOBILE CONTROLS (touch devices only) -->
<div id="dpad" style="display:none"></div>
<div id="mcontrols" style="display:none"></div>
<!-- Steering wheel — bottom-left -->
<div id="steering-wrap">
  <div id="mc-wheel">
    <div id="mc-wheel-spoke"></div>
    <div id="mc-wheel-marker"></div>
    <div id="mc-wheel-hub"></div>
  </div>
  <div id="mc-wheel-lbl">STEER</div>
</div>
<!-- Pedals: brake left, accel right — bottom-right -->
<div id="pedals">
  <div class="mc-btn" id="mc-brake">▼<br><span style="font-size:8px;letter-spacing:1px;opacity:.75">BRK</span></div>
  <div class="mc-btn" id="mc-accel">▲<br><span style="font-size:8px;letter-spacing:1px;opacity:.75">GAS</span></div>
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

const DIST_ORDER=['research','health','ops','finance','retail'];
const ROW_COLS={retail:5,finance:3,ops:4,health:2,research:4};

// ════════════════════════════════════
//  SCENE STATE
// ════════════════════════════════════
let scene,camera,renderer,clock;
let carGroup,carWheels=[];
let buildings=[];
let nearEntry=null,modalOpen=false;
let keys={},dpadState={up:0,down:0,left:0,right:0};
let carPos=new THREE.Vector3(0,0,105);
let carAngle=Math.PI,carSpeed=0;
let frame=0;
let mmCanvas,mmCtx;
let visitedSet=new Set();
let allParticleGroups=[];
let audioCtx=null,engineOsc=null,engineGain=null;
let lastNearEntry=null;

const CAM_BACK=11,CAM_UP=5.5,CAM_LAG=0.09;
let camPos=new THREE.Vector3(0,8,117);
// Matrix layout: alternating building columns/rows and road columns/rows
// BW=building slot, RW=road width, STEP=BW+RW
const BW=18, RW=16, STEP=BW+RW; // step=34
const CITY_H=115;
// Building col centres (5): -68,-34,0,34,68
// Road col centres (6):     -85,-51,-17,17,51,85
function bColX(col){ return -68+col*STEP; }
function bRowZ(row){ return -68+row*STEP; }
function rColX(col){ return -85+col*STEP; }
function rRowZ(row){ return -85+row*STEP; }

// District row assignments (car starts at +Z, drives -Z; row 0 = nearest = most +Z)


// NAV SCROLL + SCROLL REVEAL
function navTo(id){
  const el=document.getElementById(id);
  const sc=document.getElementById('lscroll');
  if(!el||!sc)return;
  sc.scrollTo({top:el.offsetTop,behavior:'smooth'});
}
document.addEventListener('DOMContentLoaded',()=>{
  const sc=document.getElementById('lscroll');
  if(!sc)return;

  // Nav active state
  const secs=['s-hero','s-about','s-exp','s-contact'];
  const links=document.querySelectorAll('.lnav-link');
  sc.addEventListener('scroll',()=>{
    const st=sc.scrollTop+80;
    secs.forEach((id,i)=>{
      const el=document.getElementById(id);
      if(!el)return;
      if(el.offsetTop<=st&&el.offsetTop+el.offsetHeight>st){
        links.forEach(l=>l.classList.remove('active'));
        if(links[i])links[i].classList.add('active');
      }
    });
  });

  // Scroll reveal via IntersectionObserver
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('in');
        // Also trigger lsec-inner for div bar
        const inner=e.target.closest('.lsec-inner');
        if(inner)inner.classList.add('in');
      }
    });
  },{root:sc,threshold:0.15});

  // Observe all reveal elements and stagger containers
  sc.querySelectorAll('.reveal,.reveal-left,.reveal-scale,.stagger').forEach(el=>obs.observe(el));
});
// ════════════════════════════════════
function startGame(){
  document.getElementById('intro').style.display='none';
  const cv2=document.getElementById('c');
  cv2.style.display='block';
  cv2.style.width='100%';
  cv2.style.height=window.innerHeight+'px';
  window.addEventListener('resize',()=>{ cv2.style.height=window.innerHeight+'px'; });
  window.addEventListener('orientationchange',()=>setTimeout(()=>{ cv2.style.height=window.innerHeight+'px'; },200));
  document.getElementById('back-btn').style.display='block';
  ['hud','mm-wrap'].forEach(id=>document.getElementById(id).style.display='block');
  document.getElementById('dpad').style.display='none';
  // Show mobile controls only on touch-capable devices
  const isTouchDevice=('ontouchstart' in window)||navigator.maxTouchPoints>0;
  if(isTouchDevice){
    document.getElementById('steering-wrap').style.display='flex';
    document.getElementById('pedals').style.display='flex';
    document.getElementById('hint-box').style.display='none';
  } else {
    document.getElementById('steering-wrap').style.display='none';
    document.getElementById('pedals').style.display='none';
    document.getElementById('hint-box').style.display='block';
  }
  mmCanvas=document.getElementById('mm');
  mmCanvas.width=140; mmCanvas.height=140;
  mmCtx=mmCanvas.getContext('2d');
  init3D();buildCity();buildCar();bindInput();initAudio();
  clock=new THREE.Clock();loop();
  showToast('Drive into a glowing zone · Press Enter to open a project');
}
function backToPortfolio(){
  document.getElementById('intro').style.display='flex';
  document.getElementById('c').style.display='none';
  document.getElementById('back-btn').style.display='none';
  ['hud','mm-wrap','hint-box'].forEach(id=>document.getElementById(id).style.display='none');
  document.getElementById('dpad').style.display='none';
  document.getElementById('mcontrols').style.display='none';
  document.getElementById('steering-wrap').style.display='none';
  document.getElementById('pedals').style.display='none';
  document.getElementById('hint-box').style.display='none';
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
  function onResize(){
    const W=window.innerWidth, H=window.innerHeight;
    camera.aspect=W/H;
    camera.updateProjectionMatrix();
    renderer.setSize(W,H,false);
  }
  window.addEventListener('resize',onResize);
  window.addEventListener('orientationchange',()=>setTimeout(onResize,200));
  screen.orientation && screen.orientation.addEventListener('change',()=>setTimeout(onResize,200));
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
  // Centre each district within col 0-4 range
  const startCol=Math.floor((5-cols)/2);
  // Building at matrix building column (bColX) and building row (bRowZ)
  return {
    x: bColX(startCol+col),
    z: bRowZ(row)
  };
}

function buildCity(){
  // Ground
  const ground=new THREE.Mesh(new THREE.PlaneGeometry(CITY_H*2.5,CITY_H*2.5),
    new THREE.MeshLambertMaterial({color:0x060a10}));
  ground.rotation.x=-Math.PI/2;ground.receiveShadow=true;scene.add(ground);
  scene.add(new THREE.GridHelper(CITY_H*2.4,110,0x0d1420,0x090f18));
  makeRoads();makeDistrictZones();placeBuildings();makeDistrictSigns();
}

function makeRoads(){
  const rM=new THREE.MeshLambertMaterial({color:0x0a0e18});
  const lM=new THREE.MeshLambertMaterial({color:0x1e2e48,emissive:0x102030,emissiveIntensity:0.4});
  const sM=new THREE.MeshLambertMaterial({color:0x111c2c});
  const len=200; // road length covers full city

  // 6 horizontal roads (rows 0-5) running along X
  for(let r=0;r<=5;r++){
    const rz=rRowZ(r);
    const road=new THREE.Mesh(new THREE.PlaneGeometry(len,RW),rM);
    road.rotation.x=-Math.PI/2; road.position.set(0,0.05,rz); road.receiveShadow=true;
    scene.add(road);
    // Kerbs
    [-RW/2+0.3,RW/2-0.3].forEach(oz=>{
      const k=new THREE.Mesh(new THREE.BoxGeometry(len,0.16,0.3),sM);
      k.position.set(0,0.08,rz+oz); scene.add(k);
    });
    // Centre dashes
    for(let x=-len/2+3;x<len/2;x+=7){
      const d=new THREE.Mesh(new THREE.PlaneGeometry(3.2,0.2),lM);
      d.rotation.x=-Math.PI/2; d.position.set(x,0.07,rz); scene.add(d);
    }
  }

  // 6 vertical roads (cols 0-5) running along Z
  for(let cc=0;cc<=5;cc++){
    const rx=rColX(cc);
    const road=new THREE.Mesh(new THREE.PlaneGeometry(RW,len),rM);
    road.rotation.x=-Math.PI/2; road.position.set(rx,0.05,0); road.receiveShadow=true;
    scene.add(road);
    [-RW/2+0.3,RW/2-0.3].forEach(ox=>{
      const k=new THREE.Mesh(new THREE.BoxGeometry(0.3,0.16,len),sM);
      k.position.set(rx+ox,0.08,0); scene.add(k);
    });
    for(let z=-len/2+3;z<len/2;z+=7){
      const d=new THREE.Mesh(new THREE.PlaneGeometry(0.2,3.2),lM);
      d.rotation.x=-Math.PI/2; d.position.set(rx,0.07,z); scene.add(d);
    }
  }
}


function makeDistrictZones(){
  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[dk];
    const startCol=Math.floor((5-cols)/2);
    // Zone covers building cols for this district row
    const leftX  = bColX(startCol) - BW/2;
    const rightX = bColX(startCol+cols-1) + BW/2;
    const cx     = (leftX+rightX)/2;
    const w      = rightX - leftX;
    const zone=new THREE.Mesh(
      new THREE.PlaneGeometry(w, BW),
      new THREE.MeshLambertMaterial({color:dist.color,transparent:true,opacity:0.04})
    );
    zone.rotation.x=-Math.PI/2;
    zone.position.set(cx,0.055,bRowZ(row));
    scene.add(zone);
  });
}


function makeDistrictSigns(){
  // N buildings per district row → N-1 holding bars connecting adjacent pairs.
  // Each bar spans from right edge of building[i] to left edge of building[i+1].
  // No poles. Floats just above tallest building in that row.
  // Front (+Z) and back (-Z) faces show district label in district colour.
  const BH_LIST=[9,13,10,14,8,12,11,9,13,10,14,8,12,11,9,13,10,14];
  const bBody=12; // building body width

  DIST_ORDER.forEach((dk,row)=>{
    const dist=DISTRICTS[dk];
    const cols=ROW_COLS[dk];
    const startCol=Math.floor((5-cols)/2);
    const rowZ=bRowZ(row);

    // Bar passes through buildings — slightly below the shortest building in this row
    const idxs=PROJECTS.map((p,i)=>p.district===dk?i:-1).filter(i=>i>=0);
    const minH=Math.min(...idxs.map(i=>BH_LIST[i%18]));
    const barY=minH*0.7+1.9; // passes through buildings at user-specified height
    const barH=0.82;

    for(let i=0;i<cols-1;i++){
      const lx=bColX(startCol+i);    // left building centre
      const rx=bColX(startCol+i+1);  // right building centre
      const hLeft  = lx+bBody/2;     // right edge of left building
      const hRight = rx-bBody/2;     // left edge of right building
      const hW     = hRight-hLeft;
      const hCX    = (hLeft+hRight)/2;

      // Structural beam runs along the BOTTOM edge of the label — not through its centre
      const beamY = barY - barH/2 - 0.09;  // just below the label face
      const beam=new THREE.Mesh(
        new THREE.BoxGeometry(hW,0.12,0.12),
        new THREE.MeshLambertMaterial({color:dist.color,emissive:dist.color,emissiveIntensity:0.6})
      );
      beam.position.set(hCX,beamY,rowZ);
      scene.add(beam);

      // Connector brackets where bar meets building walls
      [hLeft+0.07, hRight-0.07].forEach(ex=>{
        const brk=new THREE.Mesh(
          new THREE.BoxGeometry(0.2,barH+0.3,0.2),
          new THREE.MeshLambertMaterial({color:dist.color,emissive:dist.color,emissiveIntensity:0.7})
        );
        brk.position.set(ex,barY,rowZ);
        scene.add(brk);
      });

      // Label texture (canvas)
      function mkTex(){
        const cw=512, ch=76;
        const can=document.createElement('canvas');
        can.width=cw; can.height=ch;
        const ctx=can.getContext('2d');
        ctx.fillStyle='#06101c'; ctx.fillRect(0,0,cw,ch);
        ctx.fillStyle=dist.hex;
        ctx.fillRect(0,0,cw,6); ctx.fillRect(0,ch-6,cw,6);
        ctx.font='bold 30px Segoe UI,Arial';
        ctx.fillStyle=dist.hex;
        ctx.textAlign='center'; ctx.textBaseline='middle';
        let lbl=dist.name.toUpperCase();
        while(ctx.measureText(lbl).width>cw-16&&lbl.length>3) lbl=lbl.slice(0,-1);
        ctx.fillText(lbl,cw/2,ch/2);
        const tex=new THREE.CanvasTexture(can);
        tex.anisotropy=renderer.capabilities.getMaxAnisotropy();
        return tex;
      }

      const mat=new THREE.MeshBasicMaterial({map:mkTex(),transparent:true,depthWrite:false});

      // Front face (+Z)
      const fm=new THREE.Mesh(new THREE.PlaneGeometry(hW,barH),mat);
      fm.position.set(hCX,barY,rowZ-0.09); fm.rotation.y=0;
      scene.add(fm);

      // Back face (-Z)
      const bm=new THREE.Mesh(new THREE.PlaneGeometry(hW,barH),mat.clone());
      bm.position.set(hCX,barY,rowZ+0.09); bm.rotation.y=Math.PI;
      scene.add(bm);

      // Subtle glow
      const pl=new THREE.PointLight(dist.color,0.45,hW+6);
      pl.position.set(hCX,barY+0.6,rowZ);
      scene.add(pl);
    }
  });
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
  const BH_LIST=[9,13,10,14,8,12,11,9,13,10,14,8,12,11,9,13,10,14];
  const bH=BH_LIST[idx%18];
  const bW=12, bD=12; // fits BW=18 slot with 3-unit gap to road
  const g=new THREE.Group();g.position.set(bx,0,bz);

  // Pavement
  const pave=new THREE.Mesh(new THREE.BoxGeometry(bW+4,0.2,bD+4),
    new THREE.MeshLambertMaterial({color:0x0e1826}));
  pave.position.y=0.1;pave.receiveShadow=true;g.add(pave);

  // Solid body — clean dark concrete, no style variations
  const body=new THREE.Mesh(new THREE.BoxGeometry(bW,bH,bD),
    new THREE.MeshLambertMaterial({color:0x111824}));
  body.position.y=bH/2+0.2;body.castShadow=true;body.receiveShadow=true;g.add(body);

  // Colored top cap — category color, full width
  const cap=new THREE.Mesh(new THREE.BoxGeometry(bW+0.1,0.6,bD+0.1),
    new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.5}));
  cap.position.y=bH+0.5;g.add(cap);

  // Thin colored ledge at base
  const base=new THREE.Mesh(new THREE.BoxGeometry(bW+0.2,0.25,bD+0.2),
    new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.2}));
  base.position.y=0.32;g.add(base);

  makePoster(g,p,dist,bW,bH,bD);

  // Category glow light above cap
  const rL=new THREE.PointLight(hc,0.8,30);rL.position.set(0,bH+3,0);g.add(rL);

  // Particles
  const pg=makeParticles(p.district,hc,bW,bH);
  g.add(pg);allParticleGroups.push({group:pg,building:null});

  // ── PERIMETER ENTRANCE ZONE ──
  // Full rectangle around building — glowing floor plane
  const zoneW=bW+10,zoneD=bD+10;
  const eMat=new THREE.MeshBasicMaterial({color:hc,transparent:true,opacity:0.08,depthWrite:false});
  const ePlane=new THREE.Mesh(new THREE.PlaneGeometry(zoneW,zoneD),eMat);
  ePlane.rotation.x=-Math.PI/2;ePlane.position.set(0,0.12,0);g.add(ePlane);

  // Border lines (4 edges of the zone)
  const bMat=new THREE.MeshBasicMaterial({color:hc,transparent:true,opacity:0.5});
  const hw2=zoneW/2,hd2=zoneD/2;
  [[zoneW,0.12,0,-hd2],[zoneW,0.12,0,hd2],[0.12,zoneD,-hw2,0],[0.12,zoneD,hw2,0]].forEach(([fw,fd,fx,fz2])=>{
    const line=new THREE.Mesh(new THREE.PlaneGeometry(fw,fd),bMat.clone());
    line.rotation.x=-Math.PI/2;line.position.set(fx,0.13,fz2);g.add(line);
  });

  // Corner posts (4 corners)
  const pstM=new THREE.MeshLambertMaterial({color:hc,emissive:hc,emissiveIntensity:0.7});
  for(const[px2,pz2]of[[-hw2,-hd2],[hw2,-hd2],[-hw2,hd2],[hw2,hd2]]){
    const post=new THREE.Mesh(new THREE.CylinderGeometry(0.1,0.1,1.4,8),pstM.clone());
    post.position.set(px2,0.7,pz2);g.add(post);
    const ball=new THREE.Mesh(new THREE.SphereGeometry(0.16,8,8),pstM.clone());
    ball.position.set(px2,1.5,pz2);g.add(ball);
  }

  // Entrance light at centre
  const eL=new THREE.PointLight(hc,0,18);eL.position.set(0,0.5,0);g.add(eL);

  const entranceWorld=new THREE.Vector3(bx,0,bz);
  const bbox=new THREE.Box2(
    new THREE.Vector2(bx-bW/2-0.5,bz-bD/2-0.5),
    new THREE.Vector2(bx+bW/2+0.5,bz+bD/2+0.5)
  );
  scene.add(g);
  return{
    group:g,bbox,entranceWorld,project:p,eMat,eLight:eL,
    visited:false,distHex:dist.hex,particleGroup:pg,
    cx:bx,cz:bz,hw:bW/2+5,hd:bD/2+5  // perimeter half-dims for detection
  };
}

function makePoster(g,p,dist,bW,bH,bD){
  const PX=96;
  const cw=Math.round(bW*PX), ch=Math.round(bH*PX);

  function buildCanvas(){
    const can=document.createElement('canvas');
    can.width=cw; can.height=ch;
    const ctx=can.getContext('2d');

    // Solid background matching body
    ctx.fillStyle='#111824'; ctx.fillRect(0,0,cw,ch);
    // Coloured top strip (matches cap)
    ctx.fillStyle=dist.hex; ctx.fillRect(0,0,cw,ch*0.055);

    ctx.textAlign='center'; ctx.textBaseline='top';
    const pad=cw*0.08;
    const maxW=cw-pad*2;

    // Text wrapping helper
    function wrap(text,font,mW){
      ctx.font=font;
      const words=text.split(' ');
      const lines=[];let line='';
      words.forEach(w=>{
        const t=line?line+' '+w:w;
        if(ctx.measureText(t).width>mW&&line){lines.push(line);line=w;}
        else line=t;
      });
      if(line)lines.push(line);
      return lines;
    }

    // Start drawing from 18% down so text sits in lower portion
    let y=ch*0.18;

    // Project name — bold white, wrapped
    const nameSz=cw*0.082;
    const nameFont=`900 ${nameSz}px Segoe UI,Arial`;
    const nameLines=wrap(p.name,nameFont,maxW);
    ctx.font=nameFont; ctx.fillStyle='#f0f4ff';
    const nameLineH=nameSz*1.28;
    nameLines.forEach((line,i)=>{ ctx.fillText(line,cw/2,y+i*nameLineH); });
    y+=nameLines.length*nameLineH+nameSz*0.5;

    // Thin divider
    ctx.fillStyle=dist.hex; ctx.globalAlpha=0.4;
    ctx.fillRect(pad,y,maxW,2); ctx.globalAlpha=1;
    y+=nameSz*0.55;

    // Category — district colour, wrapped
    const catSz=nameSz*0.62;
    const catFont=`700 ${catSz}px Segoe UI,Arial`;
    const catLines=wrap(p.cat,catFont,maxW);
    ctx.font=catFont; ctx.fillStyle=dist.hex;
    const catLineH=catSz*1.3;
    catLines.forEach((line,i)=>{ ctx.fillText(line,cw/2,y+i*catLineH); });

    const tex=new THREE.CanvasTexture(can);
    tex.anisotropy=renderer.capabilities.getMaxAnisotropy();
    return tex;
  }

  const eps=0.05;
  const mat=new THREE.MeshBasicMaterial({map:buildCanvas(),transparent:true,depthWrite:false});
  const mat2=new THREE.MeshBasicMaterial({map:buildCanvas(),transparent:true,depthWrite:false});

  // FRONT (+Z)
  const front=new THREE.Mesh(new THREE.PlaneGeometry(bW,bH),mat);
  front.position.set(0,bH/2+0.2,bD/2+eps); g.add(front);

  // BACK (-Z)
  const back=new THREE.Mesh(new THREE.PlaneGeometry(bW,bH),mat2);
  back.position.set(0,bH/2+0.2,-bD/2-eps);
  back.rotation.y=Math.PI; g.add(back);
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
    wg.position.set(wx,wy,wz);
    wg.userData.isWheel=true;

    // Inner spin group — this is what we rotate to spin the wheel
    const spin=new THREE.Group();
    wg.add(spin);
    wg.userData.spin=spin;

    // Tyre — cylinder lying on its side (axis along X = car width)
    const tyre=new THREE.Mesh(new THREE.CylinderGeometry(0.42,0.42,0.26,20),yM);
    tyre.rotation.z=Math.PI/2; tyre.castShadow=true; spin.add(tyre);

    // Rim
    const rim=new THREE.Mesh(new THREE.CylinderGeometry(0.27,0.27,0.27,10),rM);
    rim.rotation.z=Math.PI/2; spin.add(rim);

    // 5 spokes
    for(let s=0;s<5;s++){
      const spk=new THREE.Mesh(new THREE.BoxGeometry(0.05,0.52,0.05),rM);
      spk.rotation.z=Math.PI/2;
      spk.rotation.x=(s/5)*Math.PI*2;
      spk.position.y=Math.sin((s/5)*Math.PI*2)*0.14;
      spk.position.z=Math.cos((s/5)*Math.PI*2)*0.14;
      spin.add(spk);
    }

    carGroup.add(wg);
    carWheels.push(wg);
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
const ACCEL=0.038,FRIC=0.88,MAX_SPD=0.36,TURN=0.034,BOOST_SPD=1.1,BOOST_ACCEL=0.12;

// Mouse orbit
let isDrag=false,lastMX=0,lastMY=0,camTheta=0,camPhi=0.38,camOrbit=false;
const CAM_R=13;

function loop(){
  requestAnimationFrame(loop);frame++;clock.getDelta();

  if(!modalOpen){
    const U=keys['ArrowUp']  ||keys['w']||keys['W']||dpadState.up;
    const D=keys['ArrowDown'] ||keys['s']||keys['S']||dpadState.down;
    const L=keys['ArrowLeft'] ||keys['a']||keys['A']||dpadState.left;
    const R=keys['ArrowRight']||keys['d']||keys['D']||dpadState.right;
    const boost=keys['Shift']||keys['Control'];
    const mspd=boost?BOOST_SPD:MAX_SPD;
    const macc=boost?BOOST_ACCEL:ACCEL;

    if(U)carSpeed=Math.min(carSpeed+macc,mspd);
    else if(D)carSpeed=Math.max(carSpeed-macc,-mspd*.5);
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
    if(Math.abs(nx)>CITY_H||Math.abs(nz)>CITY_H)blocked=true;
    if(!blocked){carPos.x=nx;carPos.z=nz;}else{carSpeed*=-.25;}

    carGroup.position.x=carPos.x;carGroup.position.z=carPos.z;carGroup.rotation.y=carAngle;
    // Spin wheels — rotate the inner spin group around Z axis (wheel's roll axis)
    carWheels.forEach(wg=>{
      if(wg.userData.spin) wg.userData.spin.rotation.x+=carSpeed*2.5;
    });

    if(engineOsc&&audioCtx){
      engineOsc.frequency.value=55+Math.abs(carSpeed)/mspd*80;
      engineGain.gain.value=Math.abs(carSpeed)>.01?.04:0;
    }
  }

  // Camera: mouse-orbit or third-person follow
  if(camOrbit){
    // Orbit around car
    const r=CAM_R+8;
    camera.position.set(
      carPos.x+r*Math.sin(camPhi)*Math.sin(camTheta+carAngle),
      carPos.y+r*Math.cos(camPhi),
      carPos.z+r*Math.sin(camPhi)*Math.cos(camTheta+carAngle)
    );
    camera.lookAt(carPos.x,1.5,carPos.z);
  } else {
    const behind=new THREE.Vector3(
      carPos.x-Math.sin(carAngle)*CAM_BACK,CAM_UP,
      carPos.z-Math.cos(carAngle)*CAM_BACK
    );
    camPos.lerp(behind,CAM_LAG);
    camera.position.copy(camPos);
    camera.lookAt(carPos.x+Math.sin(carAngle)*4,1.2,carPos.z+Math.cos(carAngle)*4);
  }

  // Entrance detection + glow — perimeter zone around whole building
  nearEntry=null;let bestD=9999;
  buildings.forEach(b=>{
    const dx=carPos.x-b.cx,dz=carPos.z-b.cz;
    // Distance to building perimeter (not centre) — use Chebyshev distance to rectangle
    const px=Math.max(0,Math.abs(dx)-b.hw),pz=Math.max(0,Math.abs(dz)-b.hd);
    const d=Math.sqrt(px*px+pz*pz); // 0 when inside perimeter ring
    const inZone=d<5.5;
    const pulse=Math.abs(Math.sin(frame*.07));
    if(inZone){
      b.eMat.opacity=.48+pulse*.32;b.eLight.intensity=2.0+pulse*1.2;
      if(d<bestD){nearEntry=b;bestD=d;}
    }else if(d<10){
      const t=1-(d-5.5)/4.5;b.eMat.opacity=.10+t*.12;b.eLight.intensity=t*.4;
    }else{b.eMat.opacity=.06;b.eLight.intensity=0;}
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
  const scale=mw/(CITY_H*2.1),ox=mw/2,oz=mh/2;
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
  mmCtx.save();mmCtx.translate(cpx,cpz);
  // carAngle=0 → moving +Z → down canvas. carAngle=PI → moving -Z → up canvas.
  // carAngle=PI → car faces -Z → up on canvas (-Y). Arrow tip at (0,-6.5) = up.
  // rotate(0) keeps tip pointing up. So rotate(carAngle - PI).
  mmCtx.rotate(-carAngle+Math.PI);
  mmCtx.fillStyle='#f5c842';
  mmCtx.beginPath();
  mmCtx.moveTo(0,-6.5);   // tip = forward (car faces -Z = up canvas when angle=PI)
  mmCtx.lineTo(4,5);mmCtx.lineTo(0,2.5);mmCtx.lineTo(-4,5);
  mmCtx.closePath();mmCtx.fill();
  mmCtx.fillStyle='#fff';mmCtx.beginPath();mmCtx.arc(0,0,1.8,0,Math.PI*2);mmCtx.fill();
  mmCtx.restore();
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

  // Mouse orbit
  const cv=document.getElementById('c');
  cv.addEventListener('mousedown',e=>{isDrag=true;lastMX=e.clientX;lastMY=e.clientY;camOrbit=true;});
  window.addEventListener('mouseup',()=>{isDrag=false;});
  window.addEventListener('mousemove',e=>{
    if(!isDrag)return;
    const dx=e.clientX-lastMX,dy=e.clientY-lastMY;
    camTheta-=dx*0.008;
    camPhi=Math.max(0.1,Math.min(1.4,camPhi+dy*0.006));
    lastMX=e.clientX;lastMY=e.clientY;
  });
  // Double-click to reset to follow cam
  cv.addEventListener('dblclick',()=>{camOrbit=false;camTheta=0;camPhi=0.38;});
  // Touch orbit
  cv.addEventListener('touchstart',e=>{if(e.touches.length===1){lastMX=e.touches[0].clientX;lastMY=e.touches[0].clientY;camOrbit=true;}},{passive:true});
  cv.addEventListener('touchmove',e=>{
    if(e.touches.length!==1)return;
    const dx=e.touches[0].clientX-lastMX,dy=e.touches[0].clientY-lastMY;
    camTheta-=dx*0.008;camPhi=Math.max(0.1,Math.min(1.4,camPhi+dy*0.006));
    lastMX=e.touches[0].clientX;lastMY=e.touches[0].clientY;
  },{passive:true});

  // ── Mobile pedal buttons ──
  function mcBind(id, dir){
    const el=document.getElementById(id);
    if(!el) return;
    const on=()=>{ dpadState[dir]=1; el.classList.add('on'); if(audioCtx&&audioCtx.state==='suspended') audioCtx.resume(); };
    const off=()=>{ dpadState[dir]=0; el.classList.remove('on'); };
    el.addEventListener('pointerdown',e=>{e.preventDefault();on();});
    el.addEventListener('pointerup',off);
    el.addEventListener('pointerleave',off);
  }
  mcBind('mc-accel','up');
  mcBind('mc-brake','down');

  // ── 360 steering wheel ──
  // Wheel rotation drives steering: rotating CW = steer right, CCW = steer left.
  // Threshold: ±15 degrees from start angle activates steer.
  const wh=document.getElementById('mc-wheel');
  const spoke=document.getElementById('mc-wheel-spoke');
  if(wh){
    let wheelActive=false, startAngle=0, currentAngle=0, wheelCX=0, wheelCY=0;
    const STEER_THRESH=15; // degrees to activate steering

    function getAngle(cx,cy,ex,ey){
      return Math.atan2(ey-cy,ex-cx)*180/Math.PI;
    }
    function applyWheelAngle(ang){
      currentAngle=ang;
      // Clamp visual rotation to ±90 deg
      const vis=Math.max(-90,Math.min(90,ang));
      wh.style.transform='rotate('+vis+'deg)';
      // Steer based on threshold
      if(ang>STEER_THRESH){ dpadState.right=1; dpadState.left=0; }
      else if(ang<-STEER_THRESH){ dpadState.left=1; dpadState.right=0; }
      else { dpadState.left=0; dpadState.right=0; }
    }
    function wheelStart(ex,ey){
      const r=wh.getBoundingClientRect();
      wheelCX=r.left+r.width/2; wheelCY=r.top+r.height/2;
      startAngle=getAngle(wheelCX,wheelCY,ex,ey)-currentAngle;
      wheelActive=true;
      wh.style.cursor='grabbing';
      if(audioCtx&&audioCtx.state==='suspended') audioCtx.resume();
    }
    function wheelMove(ex,ey){
      if(!wheelActive) return;
      const ang=getAngle(wheelCX,wheelCY,ex,ey)-startAngle;
      applyWheelAngle(ang);
    }
    function wheelEnd(){
      if(!wheelActive) return;
      wheelActive=false;
      wh.style.cursor='grab';
      // Spring back to centre
      const spring=setInterval(()=>{
        currentAngle*=0.75;
        const vis=Math.max(-90,Math.min(90,currentAngle));
        wh.style.transform='rotate('+vis+'deg)';
        if(Math.abs(currentAngle)<0.5){
          currentAngle=0; wh.style.transform='';
          dpadState.left=0; dpadState.right=0;
          clearInterval(spring);
        } else {
          if(currentAngle>STEER_THRESH){ dpadState.right=1; dpadState.left=0; }
          else if(currentAngle<-STEER_THRESH){ dpadState.left=1; dpadState.right=0; }
          else { dpadState.left=0; dpadState.right=0; }
        }
      },16);
    }
    // Pointer events
    wh.addEventListener('pointerdown',e=>{e.preventDefault();wh.setPointerCapture(e.pointerId);wheelStart(e.clientX,e.clientY);});
    wh.addEventListener('pointermove',e=>{e.preventDefault();wheelMove(e.clientX,e.clientY);});
    wh.addEventListener('pointerup',e=>{e.preventDefault();wheelEnd();});
    wh.addEventListener('pointercancel',e=>{e.preventDefault();wheelEnd();});
  }
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
