#!flask/bin/python
from app import app


if __name__ == "__main__":
    global temperature
    app.run(
        host='0.0.0.0',
        debug=True,
        threaded=True
    )
