from ultralytics import YOLO
import os
import yaml
import logging
import csv
from scripts.mlops.register_model import register_model
import pdb

def train_model(dataset_dir: str, model: str, epochs: int, batch: int, imgsz: int):
    """Trains a YOLOv8 model using the ultralytics package.

    Args:
        dataset_dir (str): Directory to the dataset
        model (str): Pretrained model name
        epochs (int): Number of epochs during training
        batch (int): Number of images to process in each batch.
        imgsz (int): Size of the images that will be trained on.
    """
    data_path = os.path.join(dataset_dir, "data.yaml")
    logging.info(f"Dataset location: {data_path}")
    device = os.environ.get("INFERENCE_DEVICE", "cpu")
    logging.info(f"Device to run on: {device}")
     # Load a pretrained YOLOv8n model
    model = YOLO(model=model) 
    # Train the model
    model.train(
        data=data_path, epochs=epochs, batch=batch, imgsz=imgsz, device=device
    )  
    # Register the model
    register_model(experiment_name = 'BestTennisDetector', model_name = 'TennisDetector', save_dir = model.trainer.save_dir)       
    


