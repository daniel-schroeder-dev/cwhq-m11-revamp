const missionControl = document.querySelector("#mission-control");
const launchCodeInput = document.querySelector("#launch-code-input");
const launchCodeError = document.querySelector("#launch-code-error");

missionControl.addEventListener("submit", e => {
    e.preventDefault();

    const enteredLaunchCode = launchCodeInput.value;
    const correctLaunchCode = launchCodeInput.dataset.launchCode;

    if (enteredLaunchCode === correctLaunchCode) {
        launchCodeError.style.display = "none";
    } else {
        launchCodeError.style.display = "block";
    }
});
