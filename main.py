import webview
import threading
from app.app import app


def server():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    t = threading.Thread(target=server)
    t.daemon = True
    t.start()

    window =webview.create_window(
        'LawranMD',
        'http://localhost:5000/',
        width=1200,
        height=600,
        resizable=True,
        text_select=True
    )
    webview.start()