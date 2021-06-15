from imageai.Detection.Custom import DetectionModelTrainer
import tensorflow as tf
# from tensorflow import
# from tensorflow import InteractiveSession
# config = ConfigProto()
# config.gpu_options.allow_growth = True
# session = InteractiveSession(config=config)
'''
模型训练
'''
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="identity_card")
trainer.setTrainConfig(object_names_array=["identity card"], batch_size=16, num_experiments=64, train_from_pretrained_model="./pretrained-yolov3.h5")
trainer.trainModel()
