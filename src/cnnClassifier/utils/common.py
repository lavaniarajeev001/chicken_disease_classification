import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
    if verbose:
        logger.info(f"created directoty at : {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json fie saved at:{path}")

@ensure_annotations
def decode_image(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"w") as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedimagepath):
    with open(croppedimagepath,"rb") as f:
        return base64.b64encode(f.read())
