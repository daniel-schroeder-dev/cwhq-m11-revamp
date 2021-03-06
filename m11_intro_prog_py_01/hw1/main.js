const missionControl = document.querySelector("#mission-control");
const landCodeInput = document.querySelector("#land-code-input");
const landCodeError = document.querySelector("#land-code-error");
const landButton = document.querySelector("#land-button");
const landCodeInputLabel = document.querySelector("#land-code-input-label");

let tickInterval;

let fire;

setTimeout(() => {
    fire = document.querySelector("img[src='fire.png']");
}, 500);

function landRocket() {
    const rocket = document.querySelector("#element1");
    const ignition = document.querySelector("#ignition");
    ignition.play();
    fire.style.display = "block";
    rocket.style.animation = "3s cubic-bezier(0.5, 0, 1, 1) forwards takeoff";
    fire.style.animation = "3s cubic-bezier(0.5, 0, 1, 1) forwards takeoffFire";
}

let = countdownTime = 5;

function tick() {
    if (!countdownTime) {
        landRocket();
        clearInterval(tickInterval);
        return;
    };
    countdownTime--;
    countdown.textContent = countdownTime;
}

missionControl.addEventListener("submit", e => {
    e.preventDefault();

    const enteredlandCode = landCodeInput.value;
    const correctlandCode = landCodeInput.dataset.landCode;

    if (enteredlandCode === correctlandCode) {
        landCodeError.style.display = "none";
        landCodeInput.style.display = "none";
        landButton.style.display = "none";
        landCodeInputLabel.style.display = "none";
        tickInterval = setInterval(tick, 1000);
    } else {
        landCodeError.style.display = "block";
    }
});
