# Plant-Disease-Classification

### Demo of application
<img src="static/images/plantdisease.gif">

### Blog
For more detail explanation and working of this please visit blog [here](https://dhruvmakwana.github.io/2020-07-03/Plant-Disease-Classification)

## Dataset
Here we have used the plant village dataset. The PlantVillage dataset consists of 61,486 healthy and unhealthy leaf images divided into 39 categories by species and disease.

Dataset can be found [here](https://data.mendeley.com/datasets/tywbtsjrjv/1)

The classes uses in dataset are:
<pre>
1. Apple_scab                                                     2. Apple_black_rot
3. Apple_cedar_apple_rust                                         4. Apple_healthy
5. Background_without_leaves                                      6. Blueberry_healthy
7. Cherry_powdery_mildew                                          8. Cherry_healthy
9. Corn_gray_leaf_spot                                            10. Corn_common_rust
11. Corn_northern_leaf_blight                                     12. Corn_healthy
13. Grape_black_rot                                               14. Grape_black_measles
15. Grape_leaf_blight                                             16. Grape_healthy
17. Orange_haunglongbing                                          18. Peach_bacterial_spot
19. Peach_healthy                                                 20. Pepper_bacterial_spot
21. Pepper_healthy                                                22. Potato_early_blight
23. Potato_healthy                                                24. Potato_late_blight
25. Raspberry_healthy                                             26. Soybean_healthy
27. Squash_powdery_mildew                                         28. Strawberry_healthy
29. Strawberry_leaf_scorch                                        30. Tomato_bacterial_spot
31. Tomato_early_blight                                           32. Tomato_healthy
33. Tomato_late_blight                                            34. Tomato_leaf_mold
35. Tomato_septoria_leaf_spot                                     36. Tomato_spider_mites_two-spotted_spider_mite
37. Tomato_target_spot                                            38. Tomato_mosaic_virus
39. Tomato_yellow_leaf_curl_virus
</pre>

There are two versions of dataset one without augmentation and other with augmentation where augmentation is performed with 6 different techniques (flipping, Gamma correction, noise injection, PCA color augmentation, rotation, and Scaling).

<pre>
Consider This file structure
-plantdisease
	-dataset
	-input
		-Apple_black_rot.jpg
		-Apple_cedar_apple_rust.jpg
		-Apple_healthy.jpg
		-Apple_scab.jpg
		-Background_without_leaves.jpg
		-Blueberry_healthy.jpg
	-models
		-rn.h5
	-src
		-dataset.py
		-train.py
		-predict.py
	-static
		-images
			-image_1.jpg
			-image_2.jpg
			-image_3.jpg
			-image_4.jpg
	-templates
		-index.html
		-result.html
	-upload
	-main.py
	-requirements.txt
</pre>

### Dependency

To install all Dependency run `pip install -r requirements.txt` 

### Prepare dataset

First, we need to download the dataset and place it under the dataset folder. For downloading dataset run `src/dataset.py` file. To run dataset.py file execute `python dataset.py`.

### Train Model

Train ResNet152V2 model for 10 epochs with early stopping. To run this file, execute `python train.py` command.

Output of training is given below
  
  Epoch 1/10<br>
	3074/3074 [==============================] - 794s 258ms/step - loss: 0.7289 - accuracy: 0.7813 - val_loss: 0.5274 - val_accuracy: 0.8464<br>
	Epoch 2/10<br>
	3074/3074 [==============================] - 791s 257ms/step - loss: 0.2194 - accuracy: 0.9288 - val_loss: 0.2383 - val_accuracy: 0.9264<br>
	Epoch 3/10<br>
	3074/3074 [==============================] - 803s 261ms/step - loss: 0.1427 - accuracy: 0.9531 - val_loss: 0.1081 - val_accuracy: 0.9674<br>
	Epoch 4/10<br>
	3074/3074 [==============================] - 803s 261ms/step - loss: 0.1065 - accuracy: 0.9653 - val_loss: 0.1219 - val_accuracy: 0.9585<br>
	Epoch 5/10<br>
	3074/3074 [==============================] - 799s 260ms/step - loss: 0.0835 - accuracy: 0.9730 - val_loss: 0.1150 - val_accuracy: 0.9653<br>
	Epoch 6/10<br>
	3074/3074 [==============================] - ETA: 0s - loss: 0.0670 - accuracy: 0.9778<br>
	Reached 97% accuracy so cancelling training!<br>
	3074/3074 [==============================] - 793s 258ms/step - loss: 0.0670 - accuracy: 0.9778 - val_loss: 0.0773 - val_accuracy: 0.9769<br>

### Test Model

Test the model by uploading a single picture and predicting its class. To run this file, execute `python train.py` command.

Make a call to function build with image path if a call is made externally. To run this file execute `python predict.py` command.

### Run flask app

To run this, file execute `python main.py` command. Congratulations, you have made a plant disease classification flask app.
