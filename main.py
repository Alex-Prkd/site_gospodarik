from flask import Flask, request
from flask_wtf import CSRFProtect

from admin.create_admin import admin_pages
from db import database
from db.create_default_data import first_data_creation
from views.register_handlers import pages






def main() -> None:
    app = Flask(__name__)
    app.secret_key = "secret_key"
    # app.config["SECRET_KEY"] = "12345"
    csrf = CSRFProtect()
    csrf.init_app(app)
    database.create_db_and_tables()
    first_data_creation()
    pages(app)
    admin_pages(app)
    # app.run(host='192.168.1.106')
    app.run(debug=True)


if __name__ == '__main__':
    main()