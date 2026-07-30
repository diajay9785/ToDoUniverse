<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My Todo Universe</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Nunito:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="stars" id="stars"></div>
<div class="wrapper">

<div class="header">
  <h1>✨ MY TODO UNIVERSE</h1>
  <p>Smart tasks with auto-suggested units &bull; Daily &bull; Weekly &bull; Monthly &bull; Habits &bull; Grocery &bull; Fitness</p>
</div>

<!-- SUGGEST BANNER -->
<div class="suggest-banner" id="suggest-banner">
  <span>💡 Smart suggest:</span>
  <div id="suggest-chips"></div>
</div>

<!-- TABS -->
<div class="tab-nav">
  <button class="tab-btn active" data-tab="daily"   onclick="switchTab('daily')">🔥 Daily</button>
  <button class="tab-btn"        data-tab="weekly"  onclick="switchTab('weekly')">📅 Weekly</button>
  <button class="tab-btn"        data-tab="monthly" onclick="switchTab('monthly')">🎯 Monthly</button>
  <button class="tab-btn"        data-tab="habit"   onclick="switchTab('habit')">🔄 Habits</button>
  <button class="tab-btn"        data-tab="grocery" onclick="switchTab('grocery')">🛒 Grocery</button>
  <button class="tab-btn"        data-tab="fitness" onclick="switchTab('fitness')">💪 Fitness</button>
</div>

<div id="sections-container"></div>
</div>

<script src="script.js"></script>
</body>
</html>