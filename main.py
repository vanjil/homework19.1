from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

if __name__ == '__main__':
    # Открываем браузер Chrome при запуске приложения
    webbrowser.get('chrome').open('http://127.0.0.1:5000')
    app.run(debug=True)
