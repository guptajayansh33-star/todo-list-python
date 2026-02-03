// HEALTH TRACKER
function saveHealth() {
  const data = {
    water: document.getElementById("water").value,
    exercise: document.getElementById("exercise").value,
    sleep: document.getElementById("sleep").value
  };

  localStorage.setItem("health", JSON.stringify(data));
  displayHealth();
}

function displayHealth() {
  const data = JSON.parse(localStorage.getItem("health"));
  if (!data) return;

  document.getElementById("healthData").innerText =
    `Water: ${data.water}, Exercise: ${data.exercise} min, Sleep: ${data.sleep} hrs`;
}

displayHealth();


// GOAL TRACKER
let goals = JSON.parse(localStorage.getItem("goals")) || [];

function addGoal() {
  const name = document.getElementById("goalName").value;
  const target = document.getElementById("goalTarget").value;

  goals.push({ name, target });
  localStorage.setItem("goals", JSON.stringify(goals));
  renderGoals();
}

function renderGoals() {
  const list = document.getElementById("goalList");
  list.innerHTML = "";

  goals.forEach(goal => {
    const li = document.createElement("li");
    li.innerText = `${goal.name} - Target: ${goal.target}`;
    list.appendChild(li);
  });
}

renderGoals();
