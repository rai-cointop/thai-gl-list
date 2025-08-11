from flask import Flask, jsonify, render_template
import pandas as pd
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
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

# Vue の SPA を返す
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # /assets/* や /images/* などの静的ファイルは除外されて自動で配信される
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
