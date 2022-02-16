from flask import Flask, request
import socket
import datetime

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    now = datetime.datetime.now()
    timenow = now.strftime("%Y-%m-%d %H:%M:%S")
    docker_short_id = socket.gethostname()
    container_msg = " container ID:" + docker_short_id

    browser = request.headers.get('User-Agent')

    msg_resp = browser + " \n"

    if path != '':
        msg_resp = timenow + " Request x path: /" + path + " and reply from " + container_msg + "\n"
        return msg_resp
    msg_resp = timenow + " Reply from x " + container_msg + "\n"
    return msg_resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
