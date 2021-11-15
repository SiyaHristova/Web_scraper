from app import app

if __name__ == "__main__":
    """
    set different options when the flask is run (debug mode, not the default port, etc)
    """
    app.run(debug=True)