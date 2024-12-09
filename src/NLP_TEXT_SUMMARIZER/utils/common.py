import os
from box.exceptions import BoxValueError
import yaml
from NLP_TEXT_SUMMARIZER.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Lit un fichier YAML et le retourne

    Args:
        path_to_yaml (str): chemin d'entrée

    Raises:
        ValueError: si le fichier YAML est vide
        e: fichier vide

    Returns:
        ConfigBox: type ConfigBox
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Fichier YAML : {path_to_yaml} chargé avec succès")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Le fichier YAML est vide")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Crée une liste de répertoires

    Args:
        path_to_directories (list): liste des chemins des répertoires
        verbose (bool, optional): afficher les logs lors de la création. Défaut : True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Répertoire créé à : {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Obtient la taille en Ko

    Args:
        path (Path): chemin du fichier

    Returns:
        str: taille en Ko
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} Ko"