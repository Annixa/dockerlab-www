from flask import Flask, render_template, __version__
import sys, pip

app = Flask(__name__)

@app.route('/')
def index():
    python_version = str(sys.version_info.major)
    python_version = python_version + '.' + str(sys.version_info.minor)
    python_version = python_version + '.' + str(sys.version_info.micro)

    pip_packages = []
    for package in pip.get_installed_distributions():
        split = str(package).split()
        pip_packages.append({
            'name': split[0],
            'version': split[1]
        })

    return render_template('welcome.html',
        flask_version = __version__,
        python_version = python_version,
        pip_packages = pip_packages)

if __name__ == '__main__':
    # retrieve the host, port, and debug values from the args

    if (len(sys.argv) < 3):
        debug = False
        print "No debug value given, using \"{0}\"".format(debug)
    else:
        debug = bool(sys.argv[2])
        print "Using debug: {0}".format(debug)

    if (len(sys.argv) < 2):
        host = "0.0.0.0"
        port = 80
        print "No host/port value given, using \"{0}:{0}\"".format(host, port)
    else:
        hostport = sys.argv[1].split(':')
        host = hostport[0]
        print "Using host: {0}".format(host)
        port = int(hostport[1])
        print "port: {0}".format(port)

    app.run(host = host, port = port, debug = debug)
