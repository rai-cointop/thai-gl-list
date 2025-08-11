from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# CSV読み込み
individual_df = pd.read_csv('./data/individual_data.csv')
cp_df = pd.read_csv('./data/cp_data.csv')

# トップページ（index.html）を返す
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# 静的ファイルのルーティング（Vueのルーティングに対応）
@app.route('/<path:path>')
def static_proxy(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# APIエンドポイント
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

# Render 対応: ポート設定
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
