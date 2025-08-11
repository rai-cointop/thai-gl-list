from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# CSV読み込み
individual_df = pd.read_csv('./data/individual_data.csv')
cp_df = pd.read_csv('./data/cp_data.csv')

@app.route('/api/individuals')
def get_individuals():
    return jsonify(individual_df.to_dict(orient='records'))

@app.route('/api/details/<cp_name>')
def get_details(cp_name):
    cp_info = cp_df[cp_df['CP名'] == cp_name].to_dict(orient='records')
    individuals = individual_df[individual_df['CP名'] == cp_name].to_dict(orient='records')
    return jsonify({
        'cp': cp_info[0] if cp_info else {},
        'individuals': individuals
    })

# フロントエンドのルーティング（index.htmlを返す）
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
