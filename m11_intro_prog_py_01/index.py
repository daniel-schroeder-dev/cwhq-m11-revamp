from wizardlib import *

add_background("bg.jpg")


def add_mission_control():
    document.querySelector("#mission-control").style.display = "flex";


def add_rocket():
    rocket = add_image("rocket.png", 100)
    position_element(rocket, 500, 500)


def set_launch_code(launch_code):
    document.querySelector("#launch-code-input").dataset.launchCode = launch_code




add_rocket()
add_mission_control()
set_launch_code("django")



