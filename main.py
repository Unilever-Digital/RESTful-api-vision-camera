from app import create_app

if __name__ == "__main__":
    """ main function 
    """
    app = create_app()
    app.run(host="localhost", port=8080, debug=True)
