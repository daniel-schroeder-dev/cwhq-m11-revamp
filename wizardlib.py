element_id = 0

def get_next_id():
    global element_id
    element_id += 1
    return element_id


def add_text(text, size=18):
    element = document.createElement("p")
    element.textContent = text
    element.style.fontSize = size + "px"
    element.id = get_next_id()
    document.body.appendChild(element)
    return element.id


def add_image(filename, size=None):
    element = document.createElement("img")
    element.src = filename
    element.id = get_next_id()
    if size:
        element.style.width = size + "px"
    document.body.appendChild(element)
    return element.id


def add_background(filename):
    document.querySelector("html").style.backgroundImage = f"url({filename})"


def clear():
    document.body.innerHTML = ""


def click(element_id, callback):
    element = document.getElementById(element_id)
    element.addEventListener("click", callback.bind(None, element_id))
    

def move_down(element_id, distance, time=2):
    element = document.getElementById(element_id)
    element.style.transition = f"{time}s linear transform"
    setTimeout(translate_y.bind(None, element, distance), 400)
    

def move_up(element_id, distance, time=2):
    element = document.getElementById(element_id)
    element.style.transition = f"{time}s linear transform"
    setTimeout(translate_y.bind(None, element, -distance), 400)


def position_element(element_id, x, y):
    element = document.getElementById(element_id)
    element.style.position = "absolute"
    element.style.top = y + "px"
    element.style.left = x + "px"

    
def set_text_color(element_id, color):
    element = document.getElementById(element_id)
    element.style.color = color


def translate_y(element, distance):
    element.style.transform = f"translateY({distance}px)"


def update_text(element_id, new_text):
    element = document.getElementById(element_id)
    element.textContent = new_text


def remove_element(element):
    element.remove()


def vanish(element_id):
    element = document.getElementById(element_id)
    element.classList.add("fade-out")
    setTimeout(remove_element.bind(None, element), 2000)    



