python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
ps aux | grep search.py | awk '{print $2}' | xargs kill -9
nohup python searchapi/search.py > log.txt &
