from main import app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app, use_debugger=True, use_reloader=True)