from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)  # Frozen to ensure immutability
class PrepareBaseModelConfig:
    root_dir: Path                      # Directory to store model artifacts
    base_model_path: Path               # Path for the base model file
    updated_base_model_path: Path       # Path for the updated model file
    params_image_size: list[int]        # List of image dimensions, e.g., [224, 224, 3]
    params_learning_rate: float         # Learning rate for the optimizer
    params_include_top: bool            # Whether to include the top layer in the model
    params_weights: str                  # Pre-trained weights
    params_classes: int   


@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    trained_model_path: Path
    updated_base_model_path:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_is_agumentation:bool
    params_image_size:list

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model : Path
    training_data: Path
    all_params:dict
    mlflow_uri : str
    params_image_size:list
    params_batch_size:int