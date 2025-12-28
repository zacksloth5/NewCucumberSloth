from ourgameresources import *
import state as st
def eat():
    import state as st
    for food_type in st.eat.priorities:
        if getamount(food_type) > 0:
            changeamount(food_type, -1)
            st.eat.food = True
            st.eat.starving = False
            st.eat.lastEatenFood = food_type
            return
    
def havefood():
    if getamount("berries") > 0 or getamount("vegetables") > 0 or getamount("fruits") > 0:
        return True
    else:
        return False
        
