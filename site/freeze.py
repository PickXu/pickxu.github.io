from flask_frozen import Freezer
from serve import app

# Build a static snapshot of the site

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
