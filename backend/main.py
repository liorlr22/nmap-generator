from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    target = request.form.get('target')
    subnet = request.form.get('subnet_type')
    ports = request.form.get('ports')
    scan_type = request.form.get('scan_type')

    if ports == "" or ports == "*" or ports == " ":
        ports = "-"
    else:
        ports = f" {ports}"

    nmap_command = f"nmap {scan_type} -p{ports} {target}{subnet}"

    return render_template('result.html', nmap_command=nmap_command)


if __name__ == '__main__':
    app.run(debug=True)
