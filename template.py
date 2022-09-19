import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

package_name="deepClassifier"
list_of_files=[
    ".github/workflows/.gitkeep",
    "src/deepClassifier/__init__.py",
    "src/deepClassifier/components/__init__.py",
    "src/deepClassifier/configs/__init__.py",
    "src/deepClassifier/utils/__init__.py",
    "src/deepClassifier/pipeline/__init__.py",
    "src/deepClassifier/entity/__init__.py",
    "src/deepClassifier/constants/__init__.py",
    "tests/__init__.py"
    "tests/units/__init__.py"
    "tests/integration/__init__.py"
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename= os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file {filedir}")
    #else:
        #logging.info(f"{filename} already exist")