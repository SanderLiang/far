from website import creat_app
import os

app = creat_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True)