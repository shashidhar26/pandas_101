#!/usr/bin/env python3
"""
Main module of the server file
"""

from flask import render_template
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")
app.add_api('swagger.yml', base_path='/api')


if __name__ == "__main__":
    app.run(debug=True)