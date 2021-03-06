from wizardlib import *

add_background("bg.jpg")


def add_mission_control():
    document.querySelector("#mission-control").style.display = "flex";


def add_rocket():
    rocket = add_image("rocket.png", 100)
    fire = add_image("fire.png", 100)
    position_element(rocket, 500, -200)
    position_element(fire, 500, -158)


def set_land_code(land_code):
    document.querySelector("#land-code-input").dataset.launchCode = land_code




add_mission_control()
set_land_code("django")








