from website import creat_app
import os
port = int(os.environ.get('PORT', 5000))
app = creat_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)