import os
import requests
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    
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
        print(results)

    return results

if __name__ == '__main__':
    load_dotenv()
    SEARCH_API_PROXY_PORT = os.getenv('SEARCH_API_PROXY_PORT')
    app.run(debug=True, port=SEARCH_API_PROXY_PORT)
