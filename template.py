import logging
import os
from pathlib import Path
list_of_file=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/componenets/data_indegestion.py",
    "src/componenets/data_transformation.py",
    "src/componenets/model_trainer.py",
    "src/componenets/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/Exception/Exception",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file: {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass #create an empty file



