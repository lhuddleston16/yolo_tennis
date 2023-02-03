## Image detection on Tennis Player
The goal of this analysis is to offer a image detection solution to track players and the ball. We want to be able to track these players so we can create metrics for total distance run,ball speed, and court position.

### Training data
- The current training data is being generated by downloading Youtube videos. These videos are then edited using Adobe Premiere Pro to subset each video based on when the camera angle changes. This generates a series of clips. Clips with camera angles that show rallies from a vantage point are kept, others are discarded. Once the clips are generated we rename the files and convert the MP4s to JPGs. These JPGs are then uploaded to Roboflow and annotated. These annotations include classes: `tennis-players` and `tennis-ball`.
- Once annotations are completed, the data is export out of Roboflow in Yolov5 format. Exports create `test`, `train`, and `valid` folders as well as a `data.yaml` to be passed when training.


### Resources
- https://www.youtube.com/watch?v=QCG8QMhga9k&ab_channel=Roboflow 
- https://github.com/roboflow/notebooks/blob/main/notebooks/how-to-track-football-players.ipynb
- https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/?utm_campaign=Onboarding&utm_content=YOLOv5+welcome&utm_medium=email_action&utm_source=email
- https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov5-object-detection-on-custom-data.ipynb#scrollTo=1NcFxRcFdJ_O