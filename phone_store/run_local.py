from waitress import serve
from phone_store.wsgi import application

if __name__ == '__main__':
    print('Starting server on http://localhost:8000')
    serve(application, host='localhost', port=8000)