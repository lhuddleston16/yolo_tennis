python3 train.py --img 640 --batch 10 --epochs 15 --data ../data.yaml  --weights yolov5s.pt --name yolov5s_results  --cache
python3 train.py --img 640 --batch 16 --epochs 3 --data ../data.yaml --weights yolov5s.pt
python3 detect.py --weights runs/train/exp/weights/best.pt --source ../laver_cup_2017_edit.mp4 --view-img
python3 detect.py  --source ../laver_cup_2017_edit.mp4 --view-img    
yolo task=detect mode=predict model=best_02_12.pt conf=0.20 source=videos/clips/sample_atp_rallies/sample_atp_rallies_1.mp4 show=true    
yolo task=detect mode=train  model=yolov8n.pt data=/Users/levihuddleston/Documents/Repos/yolo_tennis/data.yaml epochs=1 imgsz=640
python3 track.py --source ../videos/clips/sample_atp_rallies/sample_atp_rallies_7.mp4 --yolo-weights ../best_02_12.pt --tracking-method strongsort --save-vid