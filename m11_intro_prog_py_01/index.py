from wizardlib import *

add_background("bg.jpg")


def add_mission_control():
    document.querySelector("#mission-control").style.display = "flex";


def add_rocket():
    rocket = add_image("rocket.png", 100)
    fire = add_image("fire.png", 100)
    position_element(rocket, 500, 500)
    position_element(fire, 500, 542)


def set_launch_code(launch_code):
    document.querySelector("#launch-code-input").dataset.launchCode = launch_code



def set_countdown_time(countdown_time):
    document.querySelector("#countdown").dataset.countdownTime = countdown_time



# This is the in-class assignment
add_rocket()
add_mission_control()
set_launch_code("django")


# This is the bonus
#set_countdown_time(5)





