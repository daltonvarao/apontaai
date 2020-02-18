import os
from app import create_app


if __name__ == '__main__':
    app = create_app()
    port = os.getenv('PORT', 5000)
    app.run()
