from .app import st
from .server import run_server, set_elements

def run():
    set_elements(st.get_elements())
    run_server()