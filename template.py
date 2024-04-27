import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    '.github/workflow/.gitkeep',
    f'frc/{project_name}/__init__.py',
    f'frc/{project_name}/components/__init__.py',
    f'frc/{project_name}/utils/__init__.py',
    f'frc/{project_name}/utils/common.py',
    f'frc/{project_name}/logging/__init__.py',
    f'frc/{project_name}/config/__init__.py',
    f'frc/{project_name}/config/configuration.py',
    f'frc/{project_name}/pipeline/__init__.py',
    f'frc/{project_name}/entity/__init__.py',
    f'frc/{project_name}/constants/__init__.py',
    "config/config.yaml",
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'resource/trails.ipynb',
    'test.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent  # Get the directory of the file
    os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist
    filename = filepath.name  # Get the name of the file

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File: {filepath} already exists and is not empty")
