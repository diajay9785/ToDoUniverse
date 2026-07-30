const TABS=[
  {id:'daily',  label:'Daily',  emoji:'🔥',icon:'☀️',ph:'e.g. Morning run, Water 8 glasses, Take medicine...'},
  {id:'weekly', label:'Weekly', emoji:'📅',icon:'📅',ph:'e.g. Gym 3x, Read 100 pages, Call family...'},
  {id:'monthly',label:'Monthly',emoji:'🎯',icon:'🎯',ph:'e.g. Lose 2kg, Save 5000, Run 100km...'},
  {id:'habit',  label:'Habit',  emoji:'🔄',icon:'🌱',ph:'e.g. Meditate daily, No sugar, 10k steps...'},
  {id:'grocery',label:'Grocery',emoji:'🛒',icon:'🛍',ph:'e.g. Milk 2L, Rice 2kg, Apples 500g...'},
  {id:'fitness',label:'Fitness',emoji:'💪',icon:'🏋',ph:'e.g. Bench press 60kg, Run 5km, 100 pushups...'},
];

const UNIT_MAP={
  none:     {l:'— None —',       u:[]},
  time:     {l:'⏱ Time',         u:['min','hr','sec','hr:min','days']},
  weight:   {l:'⚖️ Weight',       u:['kg','g','lb','mg','oz']},
  distance: {l:'📍 Distance',     u:['km','m','miles','steps','cm','laps']},
  count:    {l:'🔢 Count',        u:['times','sets','reps','pages','glasses','cups','pieces','items','doses']},
  money:    {l:'💰 Money',        u:['₹','$','€','£','¥','k₹','k$']},
  calories: {l:'🔥 Calories',     u:['kcal','cal','kJ','g protein','g carbs','g fat']},
  temp:     {l:'🌡 Temperature',  u:['°C','°F','K']},
  custom:   {l:'✏️ Custom',       u:['units','batches','sessions','drops','sprays','tablets']},
};

const BADGE={time:'badge-time',weight:'badge-weight',distance:'badge-dist',count:'badge-count',
  money:'badge-money',calories:'badge-cal',temp:'badge-temp',custom:'badge-custom'};
const UICON={time:'⏱',weight:'⚖️',distance:'📍',count:'🔢',money:'💰',calories:'🔥',temp:'🌡',custom:'✏️'};

const SMART=[
  {kw:['run','jog','walk','hike','cycle','swim','lap','treadmill'],       t:'distance',u:'km'},
  {kw:['steps','pedometer'],                                               t:'distance',u:'steps'},
  {kw:['water','juice','milk','drink','glass','bottle','fluid'],           t:'count',   u:'glasses'},
  {kw:['protein','calorie','kcal','diet','nutrition','macro'],            t:'calories', u:'kcal'},
  {kw:['weight','lose','gain','fat','bmi','body'],                        t:'weight',   u:'kg'},
  {kw:['bench','squat','deadlift','press','curl','row','lift'],           t:'weight',   u:'kg'},
  {kw:['pushup','pullup','situp','crunch','rep','set','burpee','plank'],  t:'count',    u:'reps'},
  {kw:['read','page','book','chapter'],                                   t:'count',    u:'pages'},
  {kw:['save','spend','budget','invest','expense','₹','dollar','money'],  t:'money',    u:'₹'},
  {kw:['meditate','sleep','study','work','focus','practice','yoga'],      t:'time',     u:'min'},
  {kw:['temperature','fever','temp','bp','pulse'],                        t:'temp',     u:'°C'},
  {kw:['medicine','pill','tablet','vitamin','supplement','dose'],         t:'count',    u:'doses'},
  {kw:['rice','flour','sugar','salt','spice','vegetable','fruit','meat'], t:'weight',   u:'kg'},
  {kw:['oil','sauce','syrup','liquid','ml','liter','litre'],              t:'count',    u:'cups'},
];

const RECUR_OPTS=['—','Daily','Weekdays','Weekly','Monthly'];

let tasks={};
let filters={};
TABS.forEach(t=>{tasks[t.id]=[];filters[t.id]='all';});

// ── BUILD SECTIONS ──────────────────────────────────────────────────
function buildSections(){
  const c=document.getElementById('sections-container');
  c.innerHTML=TABS.map((t,i)=>{
    const pid=t.id[0];
    const isHabit=t.id==='habit';
    const unitOpts=Object.entries(UNIT_MAP).map(([k,v])=>`<option value="${k}">${v.l}</option>`).join('');
    const recurOpts=RECUR_OPTS.map(r=>`<option value="${r}">${r}</option>`).join('');
    return `
<div class="tab-section section-${t.id} ${i===0?'active':''}" id="section-${t.id}">
  <div class="accentLine"></div>
  <div class="stats">
    <div class="stat-card"><div class="stat-num" id="${pid}-total">0</div><div class="stat-lbl">Total</div></div>
    <div class="stat-card"><div class="stat-num" id="${pid}-done">0</div><div class="stat-lbl">Done</div></div>
    <div class="stat-card"><div class="stat-num" id="${pid}-left">0</div><div class="stat-lbl">Left</div></div>
    ${isHabit?`<div class="stat-card"><div class="stat-num" id="h-streak" style="color:#f59e0b">0🔥</div><div class="stat-lbl">Streak</div></div>`:''}
  </div>
  <div class="progress-label"><span>${t.label} Progress</span><span id="${pid}-pct">0%</span></div>
  <div class="progress-bar-wrap"><div class="progress-bar-fill" id="${pid}-bar" style="width:0%"></div></div>

  <div class="add-form">
    <div class="form-row">
      <div style="flex:2;min-width:155px">
        <label class="form-label">Task Name</label>
        <input class="inp" id="${t.id}-name" placeholder="${t.ph}"
          oninput="smartSuggest(this.value,'${t.id}')"
          onkeydown="if(event.key==='Enter')addTask('${t.id}')"/>
      </div>
      <div>
        <label class="form-label">Priority</label>
        <select class="inp inp-sm" id="${t.id}-priority">
          <option value="high">🔴 High</option>
          <option value="medium" selected>🟡 Medium</option>
          <option value="low">🟢 Low</option>
        </select>
      </div>
      <div>
        <label class="form-label">Recurring</label>
        <select class="inp inp-sm" id="${t.id}-recur">${recurOpts}</select>
      </div>
    </div>
    <div class="form-row">
      <div>
        <label class="form-label">Unit Type</label>
        <select class="inp inp-sm" id="${t.id}-utype" onchange="updateUnits('${t.id}')">${unitOpts}</select>
      </div>
      <div>
        <label class="form-label">Target Value</label>
        <input class="inp inp-xs" id="${t.id}-val" type="number" placeholder="0" min="0" step="any"/>
      </div>
      <div>
        <label class="form-label">Unit</label>
        <select class="inp inp-xs" id="${t.id}-unit"><option value="">—</option></select>
      </div>
      <div>
        <label class="form-label">Due Date</label>
        <input class="inp inp-sm" id="${t.id}-due" type="date" style="color-scheme:dark"/>
      </div>
      <div>
        <label class="form-label">Time</label>
        <input class="inp inp-xs" id="${t.id}-time" type="time" style="color-scheme:dark"/>
      </div>
    </div>
    <div class="form-row">
      <div style="flex:1">
        <label class="form-label">Notes (optional)</label>
        <input class="inp" id="${t.id}-note" placeholder="Extra details, reminders..."/>
      </div>
      <div style="display:flex;align-items:flex-end">
        <button class="add-btn" onclick="addTask('${t.id}')">+ ADD</button>
      </div>
    </div>
  </div>

  <div class="filter-bar">
    <button class="filter-btn on" onclick="setFilter('${t.id}','all',this)">All</button>
    <button class="filter-btn" onclick="setFilter('${t.id}','active',this)">Active</button>
    <button class="filter-btn" onclick="setFilter('${t.id}','done',this)">Done</button>
    <button class="filter-btn" onclick="setFilter('${t.id}','high',this)">🔴 High</button>
  </div>
  <div class="task-list" id="${t.id}-list"></div>
</div>`;
  }).join('');
}

// ── SWITCH TAB ──────────────────────────────────────────────────────
function switchTab(tab){
  TABS.forEach(t=>{
    document.getElementById('section-'+t.id).classList.toggle('active',t.id===tab);
  });
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.toggle('active',b.dataset.tab===tab));
  hideSuggest();
}

// ── UNIT DROPDOWN ───────────────────────────────────────────────────
function updateUnits(tid){
  const type=document.getElementById(tid+'-utype').value;
  const sel =document.getElementById(tid+'-unit');
  sel.innerHTML='<option value="">—</option>';
  (UNIT_MAP[type]?.u||[]).forEach(u=>{
    const o=document.createElement('option');
    o.value=u;o.textContent=u;sel.appendChild(o);
  });
  if(UNIT_MAP[type]?.u?.length) sel.selectedIndex=1;
}

// ── SMART SUGGEST ───────────────────────────────────────────────────
function smartSuggest(val,tid){
  const lower=val.toLowerCase();
  const matches=[];
  SMART.forEach(rule=>{
    if(rule.kw.some(k=>lower.includes(k))){
      if(!matches.find(m=>m.t===rule.t)) matches.push(rule);
    }
  });
  const banner=document.getElementById('suggest-banner');
  const chips =document.getElementById('suggest-chips');
  if(matches.length && val.length>2){
    chips.innerHTML=matches.slice(0,4).map(m=>`
      <span class="suggest-chip" onclick="applySuggest('${tid}','${m.t}','${m.u}')">
        ${UICON[m.t]} ${UNIT_MAP[m.t].l.replace(/[^\w\s]/g,'').trim()} → ${m.u}
      </span>`).join('');
    banner.classList.add('show');
  } else {
    hideSuggest();
  }
}
function hideSuggest(){
  document.getElementById('suggest-banner').classList.remove('show');
}
function applySuggest(tid,type,unit){
  document.getElementById(tid+'-utype').value=type;
  updateUnits(tid);
  document.getElementById(tid+'-unit').value=unit;
  hideSuggest();
  document.getElementById(tid+'-val').focus();
}

// ── ADD TASK ─────────────────────────────────────────────────────────
function addTask(tid){
  const name=document.getElementById(tid+'-name').value.trim();
  if(!name){
    const el=document.getElementById(tid+'-name');
    el.style.borderColor='#ff4757';
    el.style.animation='shake 0.3s';
    setTimeout(()=>{el.style.borderColor='';el.style.animation='';},800);
    return;
  }
  const utype =document.getElementById(tid+'-utype').value;
  const val   =document.getElementById(tid+'-val').value;
  const unit  =document.getElementById(tid+'-unit').value;
  const prio  =document.getElementById(tid+'-priority').value;
  const recur =document.getElementById(tid+'-recur').value;
  const due   =document.getElementById(tid+'-due').value;
  const dtime =document.getElementById(tid+'-time').value;
  const note  =document.getElementById(tid+'-note').value.trim();

  const task={
    id:Date.now()+Math.random(),
    name,utype,val:val||null,unit:unit||null,
    priority:prio,recur,due,dtime,note,
    done:false,
    streak:Array(7).fill(false),
    created:new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'})
  };
  tasks[tid].unshift(task);
  renderList(tid);
  updateStats(tid);
  // clear
  ['name','val','note'].forEach(f=>document.getElementById(tid+'-'+f).value='');
  document.getElementById(tid+'-due').value='';
  document.getElementById(tid+'-time').value='';
  hideSuggest();
}

// ── TOGGLE DONE ──────────────────────────────────────────────────────
function toggleDone(tid,id){
  const t=tasks[tid].find(x=>x.id===id);
  if(!t)return;
  t.done=!t.done;
  if(t.done) spawnConfetti();
  renderList(tid);
  updateStats(tid);
}

// ── TOGGLE STREAK DOT ────────────────────────────────────────────────
function toggleStreak(tid,id,day){
  const t=tasks[tid].find(x=>x.id===id);
  if(!t)return;
  t.streak[day]=!t.streak[day];
  updateStats(tid);
  renderList(tid);
}

// ── DELETE ───────────────────────────────────────────────────────────
function deleteTask(tid,id,elId){
  const el=document.getElementById(elId);
  if(el){
    el.classList.add('removing');
    setTimeout(()=>{
      tasks[tid]=tasks[tid].filter(x=>x.id!==id);
      renderList(tid);
      updateStats(tid);
    },350);
  }
}

// ── FILTER ───────────────────────────────────────────────────────────
function setFilter(tid,f,btn){
  filters[tid]=f;
  btn.closest('.filter-bar').querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
  renderList(tid);
}

// ── RENDER LIST ──────────────────────────────────────────────────────
const TAB_EMOJIS={daily:'☀️',weekly:'📅',monthly:'🎯',habit:'🌱',grocery:'🛍️',fitness:'🏋️'};
const TAB_MSGS  ={daily:'Add your first daily task!',weekly:'Plan your week!',monthly:'Set your monthly goals!',
  habit:'Build a new habit!',grocery:'Start your shopping list!',fitness:'Log your first workout!'};

function filteredTasks(tid){
  const f=filters[tid];
  return tasks[tid].filter(t=>{
    if(f==='all')   return true;
    if(f==='active')return !t.done;
    if(f==='done')  return t.done;
    if(f==='high')  return t.priority==='high';
    return true;
  });
}

function renderList(tid){
  const c=document.getElementById(tid+'-list');
  const list=filteredTasks(tid);
  if(!tasks[tid].length){
    c.innerHTML=`<div class="empty"><span class="emoji">${TAB_EMOJIS[tid]}</span><p>${TAB_MSGS[tid]}</p></div>`;
    return;
  }
  if(!list.length){
    c.innerHTML=`<div class="empty"><span class="emoji">🔍</span><p>No tasks match this filter.</p></div>`;
    return;
  }
  const isHabit=tid==='habit';
  c.innerHTML=list.map(t=>{
    const uid='t-'+Math.abs(t.id).toString().replace('.','').substring(0,10);
    const pcls={high:'p-high',medium:'p-medium',low:'p-low'}[t.priority];
    let badge='';
    if(t.utype&&t.utype!=='none'&&t.val){
      const bc=BADGE[t.utype]||'badge-custom';
      const bi=UICON[t.utype]||'';
      badge=`<span class="task-badge ${bc}">${bi} ${t.val}${t.unit?' '+t.unit:''}</span>`;
    }
    let dueBadge='';
    if(t.due){
      const now=new Date(); const d=new Date(t.due);
      const over=d<now&&!t.done;
      const fmt=d.toLocaleDateString([],{month:'short',day:'numeric'});
      dueBadge=`<span class="due-badge${over?' overdue':''}">📅 ${fmt}${t.dtime?' '+t.dtime:''}</span>`;
    }
    let recurBadge=t.recur&&t.recur!=='—'?`<span class="recur-badge">🔁 ${t.recur}</span>`:'';
    const note=t.note?`<div class="task-note">💬 ${t.note}</div>`:'';
    const streakGrid=isHabit?`
      <div class="streak-grid">
        ${['M','T','W','T','F','S','S'].map((d,i)=>`
          <div class="streak-dot ${t.streak[i]?'filled':''}" title="${d}" onclick="toggleStreak('${tid}',${t.id},${i})"></div>
        `).join('')}
        <span style="font-size:0.65rem;color:var(--muted);align-self:center;margin-left:4px">${t.streak.filter(Boolean).length}/7 this week</span>
      </div>`:'';
    return `
<div class="task-item ${t.done?'done':''}" id="${uid}">
  <span class="priority-dot ${pcls}"></span>
  <button class="check-btn" onclick="toggleDone('${tid}',${t.id})">${t.done?'✓':''}</button>
  <div class="task-body">
    <div class="task-text">${t.name}</div>
    <div class="task-meta">
      ${badge}${dueBadge}${recurBadge}
      <span>🕐 ${t.created}</span>
    </div>
    ${note}
    ${streakGrid}
  </div>
  <button class="del-btn" onclick="deleteTask('${tid}',${t.id},'${uid}')">🗑</button>
</div>`;
  }).join('');
}

// ── UPDATE STATS ─────────────────────────────────────────────────────
function updateStats(tid){
  const pid=tid[0];
  const all =tasks[tid].length;
  const done=tasks[tid].filter(t=>t.done).length;
  const left=all-done;
  const pct =all?Math.round(done/all*100):0;
  document.getElementById(pid+'-total').textContent=all;
  document.getElementById(pid+'-done').textContent=done;
  document.getElementById(pid+'-left').textContent=left;
  document.getElementById(pid+'-pct').textContent=pct+'%';
  document.getElementById(pid+'-bar').style.width=pct+'%';
  if(tid==='habit'){
    const best=tasks.habit.reduce((mx,t)=>Math.max(mx,t.streak.filter(Boolean).length),0);
    document.getElementById('h-streak').textContent=best+'🔥';
  }
}

// ── CONFETTI ──────────────────────────────────────────────────────────
function spawnConfetti(){
  const colors=['#ff6b6b','#ffd700','#4ecdc4','#a855f7','#ec4899','#22c55e','#ff8e53','#60a5fa'];
  for(let i=0;i<22;i++){
    const el=document.createElement('div');
    el.className='conf';
    const sz=7+Math.random()*9;
    el.style.cssText=`
      left:${15+Math.random()*70}%;top:${25+Math.random()*35}%;
      width:${sz}px;height:${sz}px;
      background:${colors[Math.floor(Math.random()*colors.length)]};
      border-radius:${Math.random()>.5?'50%':'2px'};
      --cd:${0.7+Math.random()*0.9}s;--dl:${Math.random()*0.25}s;`;
    document.body.appendChild(el);
    setTimeout(()=>el.remove(),1800);
  }
}

// ── STARFIELD ─────────────────────────────────────────────────────────
function createStars(){
  const c=document.getElementById('stars');
  const cols=['#ff6b6b','#ffd700','#4ecdc4','#a855f7','#fff','#ec4899','#22c55e'];
  for(let i=0;i<70;i++){
    const s=document.createElement('div');
    const sz=1+Math.random()*2.5;
    s.className='star';
    s.style.cssText=`left:${Math.random()*100}%;top:${Math.random()*100}%;
      width:${sz}px;height:${sz}px;
      background:${cols[Math.floor(Math.random()*cols.length)]};
      --d:${2+Math.random()*4}s;--dl:${-Math.random()*4}s;`;
    c.appendChild(s);
  }
}

// ── INIT ──────────────────────────────────────────────────────────────
buildSections();
createStars();
TABS.forEach(t=>{renderList(t.id);updateStats(t.id);});
console.log('🌈 Todo Universe loaded! Enter key adds tasks quickly.');