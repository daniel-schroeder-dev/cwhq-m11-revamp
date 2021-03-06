from wizardlib import *

def add_mission_control():
    document.querySelector("#mission-control").style.display = "flex";


def add_rocket():
    rocket = add_image("rocket.png", 100)
    fire = add_image("fire.png", 100)
    position_element(rocket, 500, -300)
    position_element(fire, 500, -258)


def set_land_code(land_code):
    document.querySelector("#land-code-input").dataset.landCode = land_code


add_background("bg.jpg")
add_rocket()



# HW 1
add_mission_control()
set_land_code("django")













