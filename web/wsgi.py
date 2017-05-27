import os
from colab_server import create_app

application = create_app(os.environ.get('COLAB_CONFIG', 'production'))
