from app import create_app

if __name__ == "__main__":
    app = create_app()
    # Dev only: run "python main.py" and open http://localhost:8080
    app.run(host="localhost", port=8080, debug=True)
