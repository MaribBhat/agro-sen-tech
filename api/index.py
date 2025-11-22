import os
import sys

# Add the backend directory to sys.path so we can import server and its dependencies
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))

from server import app
