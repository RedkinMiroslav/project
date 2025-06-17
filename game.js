const levels = [
    { id: 1, name: "Новачок", description: "Зроби 10 кліків для переходу на наступний рівень!", target: 10 },
    { id: 2, name: "Аматор", description: "Потрібно 25 кліків для переходу далі!", target: 25 },
    { id: 3, name: "Досвідчений", description: "50 кліків до наступного рівня!", target: 50 },
    { id: 4, name: "Експерт", description: "100 кліків - серйозний виклик!", target: 100 },
    { id: 5, name: "Майстер", description: "Вітаємо! Ви досягли максимального рівня!", target: Infinity }
];

function getCurrentScore(){
    return localStorage.getItem("score") ? 
    parseInt(localStorage.getItem("score")) : 0;
}

function getCurrentLevel(){
    return localStorage.getItem("level") ? 
    parseInt(localStorage.getItem("level")) : 1;
}

function getLevelData(levelId) {
    return levels.find(level => level.id === levelId) || levels[0];
}

function updateScore(){
    const score = getCurrentScore();
    document.getElementById("counter").innerText = score;
}

function updateLevelDisplay() {
    const currentLevelId = getCurrentLevel();
    const levelData = getLevelData(currentLevelId);
    const score = getCurrentScore();
    
    document.getElementById("current-level").innerText = `Рівень ${levelData.id}`;
    document.getElementById("level-name").innerText = levelData.name;
    document.getElementById("level-description").innerText = levelData.description;
    
    if (levelData.target === Infinity) {
        document.getElementById("progress-bar").style.width = "100%";
        document.getElementById("progress-text").innerText = `${score} (МАКСИМУМ)`;
    } else {
        const progress = (score / levelData.target) * 100;
        document.getElementById("progress-bar").style.width = Math.min(progress, 100) + "%";
        document.getElementById("progress-text").innerText = `${score} / ${levelData.target}`;
    }
}

function checkLevelUp() {
    const currentLevelId = getCurrentLevel();
    const levelData = getLevelData(currentLevelId);
    const score = getCurrentScore();
    
    if (score >= levelData.target && levelData.target !== Infinity) {
        const newLevelId = currentLevelId + 1;
        const newLevelData = getLevelData(newLevelId);
        
        if (newLevelData) {
            localStorage.setItem("level", newLevelId);
            localStorage.setItem("score", 0);
            
            showLevelUpMessage(newLevelData);
            updateScore();
            updateLevelDisplay();
        }
    }
}

function showLevelUpMessage(levelData) {
    const message = document.getElementById("level-up-message");
    message.innerHTML = `🎉 Вітаємо! Ви перейшли на рівень ${levelData.id}: ${levelData.name}!`;
    message.style.display = "block";
    
    setTimeout(() => {
        message.style.display = "none";
    }, 3000);
}

document.getElementById("click_button").addEventListener("click", function() {
    let score = getCurrentScore();
    score += 1;
    localStorage.setItem("score", score);
    updateScore();
    updateLevelDisplay();
    checkLevelUp();
});

window.onload = function() {
    updateScore();
    updateLevelDisplay();
};

localStorage.setItem("Ivan", "39");
let score = localStorage.getItem("Ivan");
console.log(score);
console.log(localStorage);