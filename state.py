import time

class Path:
    def __init__(self):
        self.__dict__["_data"] = {}

    def __getattr__(self, name):
        if name not in self._data:
            self._data[name] = Path()
        return self._data[name]

    def __setattr__(self, name, value):
        self._data[name] = value

    def __repr__(self):
        return f"Path({self._data})"
st = Path()

#Eating Path Variables
st.eat.eatClock = 1200
st.eat.ranout = ""
st.eat.food = True
st.eat.starving = False
st.eat.lastEatTime = time.time()
st.eat.eatInterval = 20

#Button Path Variables
st.gui.buttons.branstorm.onScreen = True
st.gui.buttons.berries.onScreen = True
st.gui.buttons.research.onScreen = False

