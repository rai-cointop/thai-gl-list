import os
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# CSV読み込み
individual_df = pd.read_csv('./data/individual_data.csv')
cp_df = pd.read_csv('./data/cp_data.csv')

@app.route('/api/individuals', methods=['GET'])
def get_individuals():
    return jsonify(individual_df.to_dict(orient='records'))

@app.route('/api/details/<cp_name>', methods=['GET'])
def get_details(cp_name):
    cp_info = cp_df[cp_df['CP名'] == cp_name].to_dict(orient='records')
    individuals = individual_df[individual_df['CP名'] == cp_name].to_dict(orient='records')
    return jsonify({
        'cp': cp_info[0] if cp_info else {},
        'individuals': individuals
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)