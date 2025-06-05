from flask import Flask

from views.register_handlers import pages


def main() -> None:
    app = Flask(__name__)

    pages(app)
    # app.run(host='192.168.1.106')
    app.run(debug=True)


if __name__ == '__main__':
    main()