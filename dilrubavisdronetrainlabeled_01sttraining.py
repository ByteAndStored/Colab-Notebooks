# -*- coding: utf-8 -*-
"""DilrubaVisDroneTrainLabeled-01stTraining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C1YOAohE244Fbg7kaDAvohcs7_l4exEE
"""

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="tm7r9EMvdRtRwB0BnDkL")
project = rf.workspace("gktay").project("objectdetection-visdronetest")
version = project.version(1)
dataset = version.download("yolov8")

# Valid klasörü oluştur
!mkdir /content/ObjectDetection-VisDroneTEST-1/valid
!mkdir /content/ObjectDetection-VisDroneTEST-1/valid/images
!mkdir /content/ObjectDetection-VisDroneTEST-1/valid/labels

# Train klasöründen 40 görseli validation'a kopyala (örnek)
!cp /content/ObjectDetection-VisDroneTEST-1/train/images/* /content/ObjectDetection-VisDroneTEST-1/valid/images/
!cp /content/ObjectDetection-VisDroneTEST-1/train/labels/* /content/ObjectDetection-VisDroneTEST-1/valid/labels/

!pip install ultralytics
from ultralytics import YOLO

# Modeli yükle
model = YOLO("yolov8n.pt")  # n: nano, s: small, m, l, x seçenekleri

# Eğitim başlat
model.train(data="/content/ObjectDetection-VisDroneTEST-1/data.yaml", epochs=50, imgsz=640, batch=16)

