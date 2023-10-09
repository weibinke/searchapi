# searchapi
an simple search wrapper for bing search/google serp/ddg.

# Quick start
1. clone repo
```
git clone https://github.com/weibinke/searchapi
```
2. make a copy of .env.example
```
cd searchapi
cp .env.example .env
```
3. change SEARCH_API_PROXY_PORT & SEARCH_API_PROXY_KEY to your own.
```
# 服务端端口号
SEARCH_API_PROXY_PORT = 5555
# 代理服务的key
SEARCH_API_PROXY_KEY =  ""
```
4. start server
```
sh start.sh
```
5. test in curl
```
curl http://127.0.0.1:5555/search?q=langchain&key=xx
```
6. test in python
```
def custom_search(self,query:str):        
    try:
    	CUSTOM_SEARCH_PROXY_BASE = "http://127.0.0.1:5555/search"
    	CUSTOM_SEARCH_PROXY_KEY = ""
        response = requests.get(
            CUSTOM_SEARCH_PROXY_BASE,
            params={'q': query,'key': CUSTOM_SEARCH_PROXY_KEY},
            headers={}
        )

        return response.json()
    except Exception as e:
        raise e
```
