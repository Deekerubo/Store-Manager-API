from app import create_app

app = create_app('development')

if __name__ == "__name__":
    app.run()