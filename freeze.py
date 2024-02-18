from flask_frozen import Freezer
from app import App

freezer = Freezer(App)

if __name__ == '__main__':
    freezer.freeze()