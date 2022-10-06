# Deep Classifier Project

# Work flow
1. update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. test run pipe stage
9. run tox for testing your package
10. update dvc.yaml
11. run "dvc repo" for running all the stages in pipeline

STEP 1: Set the environment variable. | Get it from DagsHUB -> remote tab -> Mlflow tab
MLFLOW_TRACKING_URI=https://dagshub.com/Amir47/deep_CNN_Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=Amir47 \
MLFLOW_TRACKING_PASSWORD=dfee1f40f1d2823707d621541d08df26445c3a53 \
python script.py

STEP 2: Install Mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of flow to start run and then log metrics, params and models
