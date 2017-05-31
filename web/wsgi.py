from colab_server import create_app
from config import create_configuration

# Get a configuration
configuration = create_configuration()
application = create_app(configuration=configuration)
