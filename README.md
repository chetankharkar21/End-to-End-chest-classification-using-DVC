# End-to-End-chest-classification-using-DVC

## Workflows 

1. Update config.yaml
2. Update secreats.yaml [optional]
3. Upadte parms.yaml
4. Update the entity
5. Update the configuration manager in src config 
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

clone the repository

```bash

```
### step 01- create virtual enviroment after opening repository
```bash
python -m venv venv_name 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv_name\Scripts\Activate
```

### step 02- install the requirements
```bash
pip install -r requirements.txt
```
### dagshub
[dagshub](https://dagshub.com/)

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/chetankharkar21/End-to-End-chest-classification-using-DVC.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="chetankharkar21"
os.environ["MLFLOW_TRACKING_PASSWORD"]="4d6584b697c03a8d1f682a054efbee4a7264d047"
python script.py

Run this export as env variables:

```bash

$env:MLFLOW_TRACKING_URI = "https://dagshub.com/chetankharkar21/End-to-End-chest-classification-using-DVC.mlflow"

$env:MLFLOW_TRACKING_USERNAME = "chetankharkar21"

$env:MLFLOW_TRACKING_PASSWORD = "4d6584b697c03a8d1f682a054efbee4a7264d047"

```
