import socket
from flask import Flask

def get_ip():
    """ Returns a tuple where the 0 index is the local address,
        and the 1 index is an error if it has occured. """
    err = None
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(0)
        try:
            # Random values, they do not matter, however address must be valid otherwise
            # `127.0.0.1` will be returned.
            s.connect(('1.3.3.7', 1337))
            IP = s.getsockname()[0]
        except (socket.error, OverflowError) as e:
            IP = '127.0.0.1'
            err = e
    return (IP, err)

app = Flask(__name__)
local_ip = get_ip()

@app.route("/")
def home_page():
    if local_ip[1] is None:
        return f"<h3>Local IP address of the container is: {local_ip[0]}</h3>"
    else:
        return f"<h3>Local IP address of the container is: {local_ip[0]}, error is: {local_ip[1]}</h3>"

if __name__ == '__main__':
    app.run('0.0.0.0')