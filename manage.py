#!/usr/bin/env python3
import os
from radio.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.manager.run(debug=True)
