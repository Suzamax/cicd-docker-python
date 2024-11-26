# CI/CD pipelines using Python containers
 
## Preparation on host

Create a virtual env with
```bash
python -m venv .venv
```
Activate it on host and install all requirements with
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Run this.

```bash
echo "export PROJECT_DIR=${PWD}" >> .env
```

## Run on container

Run:

```bash
source .env
./run.sh
```
