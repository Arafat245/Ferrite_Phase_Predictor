from flask import Flask, request, jsonify, render_template
from our import our_calc
from sc import sc_calc

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form input and convert to floats
        inputs = {k: float(request.form[k]) for k in ['C', 'N', 'Mn', 'Ni', 'Cr', 'Mo', 'Si', 'Cu', 'Nb']}
        our_result, oNieq, oCreq = our_calc(**inputs)
        sc_result,  sNieq, sCreq = sc_calc(**inputs)
        return jsonify({
            'ferrite_percent': our_result,
            'sc_percent': sc_result,
            'oNieq': oNieq,
            'oCreq': oCreq,
            'sNieq': sNieq,
            'sCreq': sCreq,
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
=======
from flask import send_file, Flask, request, jsonify, render_template
from our import our_calc
from sc import sc_calc
import io
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form input and convert to floats
        inputs = {k: float(request.form[k]) for k in ['C', 'N', 'Mn', 'Ni', 'Cr', 'Mo', 'Si', 'Cu', 'Nb']}
        our_result, oNieq, oCreq = our_calc(**inputs)
        sc_result,  sNieq, sCreq = sc_calc(**inputs)
        return jsonify({
            'ferrite_percent': our_result,
            'sc_percent': sc_result,
            'oNieq': oNieq,
            'oCreq': oCreq,
            'sNieq': sNieq,
            'sCreq': sCreq,
        })
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/plot.png')
def plot_image():
    try:
        oCreq = float(request.args.get('oCreq'))
        oNieq = float(request.args.get('oNieq'))
        sCreq = float(request.args.get('sCreq'))
        sNieq = float(request.args.get('sNieq'))

        fig, ax = plt.subplots(figsize=(10, 6))
        img = plt.imread("static/schaeffler_nogrid_2x.png")
        ax.imshow(img, extent=[0, 40, 0, 30])
        ax.grid(color='k', linestyle='--', linewidth=0.2)
        ax.plot(oCreq, oNieq, marker='o', color='red', linestyle='None', label='Our Model')
        ax.plot(sCreq, sNieq, marker='d', color='blue', linestyle='None', label='Schaeffler')
        ax.set_xlabel('Chromium Equivalent (%)')
        ax.set_ylabel('Nickel Equivalent (%)')
        ax.legend(loc="upper left")

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close(fig)
        return send_file(buf, mimetype='image/png')
    except Exception as e:
        return f"Plot error: {str(e)}", 400

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
