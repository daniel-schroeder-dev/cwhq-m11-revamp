# M11 Transcrypt

Messing around with re-implementing Wizardlib using Transcrypt

## Installation

Make sure you are running Python 3.7! If you're using Linux, follow the excellent instructions [here](https://hackersandslackers.com/multiple-versions-python-ubuntu/) to get multiple installs of Python playing nice together.

Once you are running Python 3.7, clone this repo and enter the directory:

```bash
git clone https://github.com/daniel-schroeder-dev/m11-transcrypt
cd m11-transcrypt
```

Create a virtual environment and activate it (again, make sure you're running Python 3.7):

```bash
➜  m11-transcrypt python --version
Python 3.7.9
➜  m11-transcrypt python -m venv .venv
➜  m11-transcrypt source .venv/bin/activate
```

Now, install the dependencies:

```bash
pip install -r requirements.txt
```

Fire up an http server (note that this will block this terminal, so you'll need to open another tab and make sure to re-activate the virtual environment):

```bash
python -m http.server
```

You should be able to navigate to `http://localhost:8000/index.html` and see the output from `index.py`. 


Everytime you make a change in `index.py`, you need to run the `build.py` script. Change into the directory of the course you want to work with:

```bash
cd m11_intro_prog_py_01/
```

Open the `build.py` file and change the shebang to point to your Python's venv interpreter.

On my system, it's this:

```bash
(.venv) ➜  m11_intro_prog_py_01 which python
/home/daniel/Public/cwhq/curriculum/m11-revamp/m11/.venv/bin/python
```

So, my shebang is the same as the output above. Yours will be different, so you have to change this line:

```python
#!/home/daniel/Public/cwhq/curriculum/m11-revamp/m11/.venv/bin/python

import os

os.system("cp ../wizardlib.py ./")
os.system(f"python -m transcrypt -b -m -n index.py")
```

Then, make sure it has execute priviledges, and then you can run it everytime you change a Python file:

```bash
chmod +x build.py
./build.py
```

If you want to get fancy, you can install `entr` and have it watch the directory (note that this will block this terminal, so you'll need to open another tab and make sure to re-activate the virtual environment):

```bash
sudo apt-get install entr
ls | entr ./build.py
```

## Usage

If you want to test out the functions as you're working on them, work in `index.py`: 

```python
# index.py
from wizardlib import *

text_element = add_text("Hello, world!")
image_element = add_image("doggo.jpg")

distance = 200
speed = 300

move_left(image_element, distance, speed)
```

Make sure to run the `build` commmand after each edit (or have `entr` do it for you):

```bash
./build.py
```

The `wizardlib.py` file is where you can work on wizardlib. You have access to the DOM, and can use JS libraries. For example:

```python
def add_text(text):
    element = document.createElement("p")
    element.textContent = text
    element.id = get_next_id()
    document.body.appendChild(element)
    return element.id
```

Weird, but cool, right? Happy hacking!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

I would really love some better CSS styling for these, so that would be a great first contribution! Adding documentation is also appreciated.


## License
[MIT](https://choosealicense.com/licenses/mit/)
