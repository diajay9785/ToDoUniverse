*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#07071a;--card:#10102a;--card2:#181838;--border:rgba(255,255,255,0.07);
  --text:#e8e8ff;--muted:#6666aa;
}
body{font-family:'Nunito',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;
  background-image:radial-gradient(ellipse at 10% 10%,rgba(168,85,247,0.12) 0%,transparent 45%),
  radial-gradient(ellipse at 90% 90%,rgba(78,205,196,0.12) 0%,transparent 45%),
  radial-gradient(ellipse at 50% 50%,rgba(255,107,107,0.06) 0%,transparent 55%);}

.stars{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}
.star{position:absolute;border-radius:50%;animation:twinkle var(--d,3s) ease-in-out infinite;animation-delay:var(--dl,0s)}
@keyframes twinkle{0%,100%{opacity:0.1;transform:scale(1)}50%{opacity:0.9;transform:scale(1.4)}}

.wrapper{position:relative;z-index:1;max-width:980px;margin:0 auto;padding:14px 13px 90px}

.header{text-align:center;padding:26px 0 20px;animation:slideDown 0.8s cubic-bezier(.175,.885,.32,1.275)}
@keyframes slideDown{from{opacity:0;transform:translateY(-40px)}to{opacity:1;transform:translateY(0)}}
.header h1{font-family:'Orbitron',sans-serif;font-size:clamp(1.4rem,5vw,2.5rem);font-weight:900;
  background:linear-gradient(135deg,#ff6b6b,#ffd700,#4ecdc4,#a855f7,#ec4899,#22c55e);
  background-size:400% 400%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:gradShift 5s ease infinite;letter-spacing:2px}
@keyframes gradShift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.header p{color:var(--muted);font-size:0.82rem;margin-top:5px}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

/* SUGGEST */
.suggest-banner{display:none;background:rgba(255,215,0,0.07);border:1px solid rgba(255,215,0,0.2);
  border-radius:11px;padding:8px 13px;margin-bottom:10px;font-size:0.8rem;color:#ffd700;gap:8px;align-items:center;flex-wrap:wrap}
.suggest-banner.show{display:flex;animation:fadeIn 0.3s}
.suggest-chip{display:inline-block;background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.3);
  color:#ffd700;border-radius:50px;padding:3px 10px;font-size:0.7rem;font-weight:700;cursor:pointer;transition:all 0.2s;margin:2px}
.suggest-chip:hover{background:rgba(255,215,0,0.25);transform:scale(1.05)}

/* TABS */
.tab-nav{display:flex;gap:5px;margin-bottom:18px;background:var(--card);border-radius:15px;padding:5px;
  border:1px solid var(--border);overflow-x:auto;scrollbar-width:none;animation:fadeIn 0.5s 0.2s both}
.tab-nav::-webkit-scrollbar{display:none}
.tab-btn{flex:1;min-width:82px;padding:10px 5px;border:none;border-radius:10px;
  font-family:'Nunito',sans-serif;font-size:0.75rem;font-weight:700;cursor:pointer;
  transition:all 0.35s cubic-bezier(.175,.885,.32,1.275);background:transparent;color:var(--muted);white-space:nowrap}
.tab-btn:not(.active):hover{color:var(--text);background:var(--card2)}
.tab-btn.active[data-tab=daily]  {background:linear-gradient(135deg,#ff6b6b,#ff8e53);color:#fff;box-shadow:0 4px 18px rgba(255,107,107,0.5);transform:scale(1.04)}
.tab-btn.active[data-tab=weekly] {background:linear-gradient(135deg,#4ecdc4,#44a8d6);color:#fff;box-shadow:0 4px 18px rgba(78,205,196,0.5);transform:scale(1.04)}
.tab-btn.active[data-tab=monthly]{background:linear-gradient(135deg,#a855f7,#ec4899);color:#fff;box-shadow:0 4px 18px rgba(168,85,247,0.5);transform:scale(1.04)}
.tab-btn.active[data-tab=habit]  {background:linear-gradient(135deg,#f59e0b,#fbbf24);color:#000;box-shadow:0 4px 18px rgba(245,158,11,0.5);transform:scale(1.04)}
.tab-btn.active[data-tab=grocery]{background:linear-gradient(135deg,#22c55e,#4ade80);color:#000;box-shadow:0 4px 18px rgba(34,197,94,0.5);transform:scale(1.04)}
.tab-btn.active[data-tab=fitness]{background:linear-gradient(135deg,#f43f5e,#fb923c);color:#fff;box-shadow:0 4px 18px rgba(244,63,94,0.5);transform:scale(1.04)}

.tab-section{display:none}.tab-section.active{display:block;animation:fadeIn 0.4s}

/* ACCENT */
.accentLine{height:3px;border-radius:3px;margin-bottom:16px}
.section-daily   .accentLine{background:linear-gradient(90deg,#ff6b6b,#ff8e53)}
.section-weekly  .accentLine{background:linear-gradient(90deg,#4ecdc4,#44a8d6)}
.section-monthly .accentLine{background:linear-gradient(90deg,#a855f7,#ec4899)}
.section-habit   .accentLine{background:linear-gradient(90deg,#f59e0b,#fbbf24)}
.section-grocery .accentLine{background:linear-gradient(90deg,#22c55e,#4ade80)}
.section-fitness .accentLine{background:linear-gradient(90deg,#f43f5e,#fb923c)}

/* STATS */
.stats{display:flex;gap:9px;margin-bottom:14px;flex-wrap:wrap;animation:fadeIn 0.5s 0.3s both}
.stat-card{flex:1;min-width:75px;background:var(--card);border-radius:13px;padding:10px 13px;border:1px solid var(--border);text-align:center}
.stat-num{font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:700}
.stat-lbl{font-size:0.62rem;color:var(--muted);font-weight:700;letter-spacing:0.5px;text-transform:uppercase;margin-top:2px}
.section-daily   .stat-num{color:#ff6b6b}.section-weekly .stat-num{color:#4ecdc4}
.section-monthly .stat-num{color:#a855f7}.section-habit  .stat-num{color:#f59e0b}
.section-grocery .stat-num{color:#22c55e}.section-fitness.stat-num{color:#f43f5e}

.progress-label{display:flex;justify-content:space-between;font-size:0.72rem;color:var(--muted);margin-bottom:4px;font-weight:600}
.progress-bar-wrap{background:rgba(255,255,255,0.05);border-radius:50px;height:7px;margin-bottom:16px;overflow:hidden}
.progress-bar-fill{height:100%;border-radius:50px;transition:width 0.6s cubic-bezier(.175,.885,.32,1.275)}
.section-daily   .progress-bar-fill{background:linear-gradient(90deg,#ff6b6b,#ffd700)}
.section-weekly  .progress-bar-fill{background:linear-gradient(90deg,#4ecdc4,#44a8d6)}
.section-monthly .progress-bar-fill{background:linear-gradient(90deg,#a855f7,#ec4899)}
.section-habit   .progress-bar-fill{background:linear-gradient(90deg,#f59e0b,#fbbf24)}
.section-grocery .progress-bar-fill{background:linear-gradient(90deg,#22c55e,#4ade80)}
.section-fitness .progress-bar-fill{background:linear-gradient(90deg,#f43f5e,#fb923c)}

/* FORM */
.add-form{background:var(--card);border-radius:16px;padding:16px;border:1px solid var(--border);
  margin-bottom:16px;animation:fadeIn 0.5s 0.4s both;position:relative;overflow:hidden}
.add-form::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.section-daily   .add-form::before{background:linear-gradient(90deg,#ff6b6b,#ff8e53)}
.section-weekly  .add-form::before{background:linear-gradient(90deg,#4ecdc4,#44a8d6)}
.section-monthly .add-form::before{background:linear-gradient(90deg,#a855f7,#ec4899)}
.section-habit   .add-form::before{background:linear-gradient(90deg,#f59e0b,#fbbf24)}
.section-grocery .add-form::before{background:linear-gradient(90deg,#22c55e,#4ade80)}
.section-fitness .add-form::before{background:linear-gradient(90deg,#f43f5e,#fb923c)}

.form-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:9px}.form-row:last-child{margin-bottom:0}
.form-label{font-size:0.65rem;color:var(--muted);font-weight:700;letter-spacing:0.5px;margin-bottom:3px;display:block;text-transform:uppercase}
.inp{flex:1;min-width:120px;background:var(--card2);border:1px solid var(--border);border-radius:10px;
  padding:9px 12px;color:var(--text);font-family:'Nunito',sans-serif;font-size:0.86rem;outline:none;
  transition:border-color 0.3s,box-shadow 0.3s}
.inp:focus{border-color:rgba(255,255,255,0.25);box-shadow:0 0 0 3px rgba(255,255,255,0.05)}
.inp::placeholder{color:var(--muted)}
select.inp option{background:#1a1a35}
.inp-xs{min-width:66px;max-width:85px;flex:0 0 auto}
.inp-sm{min-width:95px;max-width:125px;flex:0 0 auto}

.add-btn{padding:9px 20px;border:none;border-radius:10px;font-family:'Nunito',sans-serif;font-size:0.88rem;font-weight:800;
  cursor:pointer;transition:all 0.3s;flex-shrink:0}
.add-btn:hover{transform:translateY(-2px) scale(1.03)}.add-btn:active{transform:scale(0.97)}
.section-daily   .add-btn{background:linear-gradient(135deg,#ff6b6b,#ff8e53);color:#fff;box-shadow:0 4px 14px rgba(255,107,107,0.4)}
.section-weekly  .add-btn{background:linear-gradient(135deg,#4ecdc4,#44a8d6);color:#fff;box-shadow:0 4px 14px rgba(78,205,196,0.4)}
.section-monthly .add-btn{background:linear-gradient(135deg,#a855f7,#ec4899);color:#fff;box-shadow:0 4px 14px rgba(168,85,247,0.4)}
.section-habit   .add-btn{background:linear-gradient(135deg,#f59e0b,#fbbf24);color:#000;box-shadow:0 4px 14px rgba(245,158,11,0.4)}
.section-grocery .add-btn{background:linear-gradient(135deg,#22c55e,#4ade80);color:#000;box-shadow:0 4px 14px rgba(34,197,94,0.4)}
.section-fitness .add-btn{background:linear-gradient(135deg,#f43f5e,#fb923c);color:#fff;box-shadow:0 4px 14px rgba(244,63,94,0.4)}

/* FILTER */
.filter-bar{display:flex;gap:6px;margin-bottom:13px;flex-wrap:wrap}
.filter-btn{padding:5px 12px;border-radius:50px;border:1px solid var(--border);background:transparent;
  color:var(--muted);font-size:0.72rem;font-weight:700;cursor:pointer;transition:all 0.2s;font-family:'Nunito',sans-serif}
.filter-btn.on{background:rgba(255,255,255,0.1);color:var(--text);border-color:rgba(255,255,255,0.2)}
.filter-btn:hover{color:var(--text)}

/* TASKS */
.task-list{display:flex;flex-direction:column;gap:8px}
.task-item{background:var(--card);border-radius:13px;padding:11px 13px;border:1px solid var(--border);
  display:flex;align-items:flex-start;gap:9px;transition:all 0.4s cubic-bezier(.175,.885,.32,1.275);
  animation:taskIn 0.4s cubic-bezier(.175,.885,.32,1.275);position:relative;overflow:hidden}
@keyframes taskIn{from{opacity:0;transform:translateX(-26px) scale(0.96)}to{opacity:1;transform:translateX(0) scale(1)}}
.task-item:hover{transform:translateX(4px);border-color:rgba(255,255,255,0.12)}
.task-item.done{opacity:0.42}.task-item.done .task-text{text-decoration:line-through;color:var(--muted)}
.task-item.removing{animation:taskOut 0.35s forwards}
@keyframes taskOut{to{opacity:0;transform:translateX(60px) scale(0.85);max-height:0;padding:0;margin:0;border:none}}
.task-item::before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;border-radius:4px 0 0 4px}
.section-daily   .task-item::before{background:linear-gradient(180deg,#ff6b6b,#ff8e53)}
.section-weekly  .task-item::before{background:linear-gradient(180deg,#4ecdc4,#44a8d6)}
.section-monthly .task-item::before{background:linear-gradient(180deg,#a855f7,#ec4899)}
.section-habit   .task-item::before{background:linear-gradient(180deg,#f59e0b,#fbbf24)}
.section-grocery .task-item::before{background:linear-gradient(180deg,#22c55e,#4ade80)}
.section-fitness .task-item::before{background:linear-gradient(180deg,#f43f5e,#fb923c)}

.check-btn{width:23px;height:23px;border-radius:50%;border:2px solid;background:transparent;cursor:pointer;
  flex-shrink:0;margin-top:1px;transition:all 0.3s;display:flex;align-items:center;justify-content:center;font-size:0.72rem}
.section-daily   .check-btn{border-color:#ff6b6b;color:#ff6b6b}
.section-weekly  .check-btn{border-color:#4ecdc4;color:#4ecdc4}
.section-monthly .check-btn{border-color:#a855f7;color:#a855f7}
.section-habit   .check-btn{border-color:#f59e0b;color:#f59e0b}
.section-grocery .check-btn{border-color:#22c55e;color:#22c55e}
.section-fitness .check-btn{border-color:#f43f5e;color:#f43f5e}
.task-item.done .check-btn{color:#22c55e;border-color:#22c55e;background:rgba(34,197,94,0.15)}
.check-btn:hover{transform:scale(1.2)}

.task-body{flex:1;min-width:0}
.task-text{font-size:0.9rem;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.task-meta{font-size:0.7rem;color:var(--muted);margin-top:3px;display:flex;gap:7px;flex-wrap:wrap;align-items:center}
.task-note{font-size:0.72rem;color:var(--muted);margin-top:3px;font-style:italic;opacity:0.75;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}

.task-badge{display:inline-flex;align-items:center;gap:3px;padding:2px 8px;border-radius:50px;font-size:0.66rem;font-weight:700}
.badge-time    {background:rgba(255,215,0,0.12);  color:#ffd700}
.badge-weight  {background:rgba(78,205,196,0.12); color:#4ecdc4}
.badge-dist    {background:rgba(168,85,247,0.12); color:#a855f7}
.badge-count   {background:rgba(255,107,107,0.12);color:#ff6b6b}
.badge-money   {background:rgba(34,197,94,0.12);  color:#22c55e}
.badge-cal     {background:rgba(251,146,60,0.12); color:#fb923c}
.badge-temp    {background:rgba(96,165,250,0.12); color:#60a5fa}
.badge-custom  {background:rgba(236,72,153,0.12); color:#ec4899}

.priority-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;margin-top:7px}
.p-high  {background:#ff4757;box-shadow:0 0 6px #ff4757}
.p-medium{background:#ffa502;box-shadow:0 0 6px #ffa502}
.p-low   {background:#2ed573;box-shadow:0 0 6px #2ed573}

.recur-badge{font-size:0.62rem;background:rgba(255,255,255,0.07);padding:2px 7px;border-radius:50px;color:var(--muted)}
.due-badge  {font-size:0.62rem;background:rgba(255,165,0,0.1);   padding:2px 7px;border-radius:50px;color:#ffa502}
.due-badge.overdue{background:rgba(255,71,87,0.12);color:#ff4757}

.del-btn{background:transparent;border:none;color:var(--muted);cursor:pointer;font-size:0.95rem;
  padding:2px;transition:all 0.2s;border-radius:7px;flex-shrink:0}
.del-btn:hover{color:#ff4757;background:rgba(255,71,87,0.1);transform:scale(1.2)}

/* HABIT STREAKS */
.streak-grid{display:flex;gap:4px;margin-top:6px;flex-wrap:wrap}
.streak-dot{width:13px;height:13px;border-radius:3px;cursor:pointer;transition:all 0.2s;border:1px solid var(--border)}
.streak-dot.filled{background:linear-gradient(135deg,#f59e0b,#fbbf24);border-color:#f59e0b;box-shadow:0 0 6px rgba(245,158,11,0.5)}
.streak-dot:hover{transform:scale(1.3)}

/* EMPTY */
.empty{text-align:center;padding:38px 20px;color:var(--muted);animation:fadeIn 0.5s}
.empty .emoji{font-size:2.8rem;animation:bounce 2s ease-in-out infinite;display:block}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.empty p{margin-top:10px;font-size:0.88rem}

/* CONFETTI */
.conf{position:fixed;pointer-events:none;z-index:9999;border-radius:2px;
  animation:confFall var(--cd,1s) var(--dl,0s) forwards}
@keyframes confFall{
  0%  {transform:translateY(0) rotate(0deg) scale(1);opacity:1}
  100%{transform:translateY(280px) rotate(720deg) scale(0);opacity:0}}