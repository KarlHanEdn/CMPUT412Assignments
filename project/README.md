A training script, datasets and a final model for the detectron2 model we use can be downloaded from my google drive: 
https://drive.google.com/drive/folders/1vwHls5zjBId-5VXJW1eV_gHA5OD75NVZ?usp=share_link

The link should contain these files:
-dataset_gen.bag is a bag for training data
-duckie_dataset.zip is a folder of labelled training data from dataset_gen.bag
-model_final.pth is the trained pytorch model of detectron2
-more_dataset_gen.bag is a bag for testing data
-Detectron2-Duckiebot.ipynb is the google colab script for training and testing the detectron2 model (modified from the detectron2 google colab tutorial)

You should be able to reproduce the model from just the labelled data and the testing bag on the google colab script (change the paths at the top of the script to point to the zip and bag files, and remember to make a copy of the colab script before editing it), let me know if there is any issue (tianming@ualberta.ca).

The object detection node should be run on a separate laptop using -R option before running Pj412 repo, and the object detection node uses the following path to access the final model:
    rospack.get_path("detectron2_duckiebot_node") + "/src/model_final.pth"
so make sure to put the model_final.pth file inside the src folder before running "dts devel build -f". The object detection node will publish its detection results onto an image topic for debugging, as well as in json format to another topic containing information about the bounding boxes.

The Pj412 repo can be built with "dts devel build -f -H csc229XX" and run with "dts devel run -H csc229XX"