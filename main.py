from flask import Flask

from views.register_handlers import pages


def main() -> None:
    app = Flask(__name__)
    pages(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()