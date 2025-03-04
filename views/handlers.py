from flask import render_template


def main_page():
    return render_template('index.html')