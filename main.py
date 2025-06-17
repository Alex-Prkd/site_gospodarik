from flask import Flask

from db import database
from views.register_handlers import pages


def main() -> None:
    app = Flask(__name__)
    database.create_db_and_tables()
    pages(app)
    # app.run(host='192.168.1.106')
    app.run(debug=True)


if __name__ == '__main__':
    main()