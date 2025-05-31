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
            'sc_percent': sc_result
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
