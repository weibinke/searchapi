import os
import requests
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from flask import Flask, jsonify, request

load_dotenv()
SEARCH_API_PROXY_PORT = os.getenv('SEARCH_API_PROXY_PORT')
SEARCH_API_PROXY_KEY = os.getenv('SEARCH_API_PROXY_KEY')
app = Flask(__name__)

def validate_key(key):
    # 在此处添加您的密钥验证逻辑
    # 您可以根据需要自定义密钥验证方法
    return key == SEARCH_API_PROXY_KEY

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    key = request.args.get('key')

    if not validate_key(key):
        return jsonify({'error': 'Invalid API key'}), 401
    
    # # Bing Search
    # try:
    #     response = requests.get(
    #         'https://api.bing.microsoft.com/v7.0/search',
    #         params={'q': query},
    #         headers={'Ocp-Apim-Subscription-Key': BING_API_KEY}
    #     )
    #     response.raise_for_status()
    #     return jsonify(response.json())
    # except requests.HTTPError:
    #     pass

    # # Google Search
    # try:
    #     response = requests.get(
    #         'https://www.googleapis.com/customsearch/v1',
    #         params={'key': GOOGLE_API_KEY, 'cx': GOOGLE_CX, 'q': query}
    #     )
    #     response.raise_for_status()
    #     return jsonify(response.json())
    # except requests.HTTPError:
    #     pass

    # DuckDuckGo Search
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
        print("search query:%s results:%s" % (query, results))

    return results

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=SEARCH_API_PROXY_PORT)
