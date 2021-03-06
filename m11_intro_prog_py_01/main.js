const missionControl = document.querySelector("#mission-control");
const launchCodeInput = document.querySelector("#launch-code-input");
const launchCodeError = document.querySelector("#launch-code-error");
const launchButton = document.querySelector("#launch-button");
const launchCodeInputLabel = document.querySelector("#launch-code-input-label");
const countdown = document.querySelector("#countdown");

let countdownTime;
let tickInterval;

let fire;

setTimeout(() => {
    fire = document.querySelector("img[src='fire.png']");
}, 500);

function launchRocket() {
    const rocket = document.querySelector("#element1");
    fire.style.display = "block";
    rocket.style.animation = "3s cubic-bezier(0.5, 0, 1, 1) forwards takeoff";
    fire.style.animation = "3s cubic-bezier(0.5, 0, 1, 1) forwards takeoffFire";
}

function tick() {
    if (!countdownTime) {
        launchRocket();
        clearInterval(tickInterval);
        return;
    };
    countdownTime--;
    countdown.textContent = countdownTime;
}

missionControl.addEventListener("submit", e => {
    e.preventDefault();

    const enteredLaunchCode = launchCodeInput.value;
    const correctLaunchCode = launchCodeInput.dataset.launchCode;

    if (enteredLaunchCode === correctLaunchCode) {
        launchCodeError.style.display = "none";
        launchCodeInput.style.display = "none";
        launchButton.style.display = "none";
        launchCodeInputLabel.style.display = "none";
        countdown.style.display = "block";
        countdownTime = countdown.dataset.countdownTime;
        countdown.textContent = countdownTime;
        tickInterval = setInterval(tick, 1000);
    } else {
        launchCodeError.style.display = "block";
    }
});
