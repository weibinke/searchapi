python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
nohup python searchapi/search.py > log.txt &

