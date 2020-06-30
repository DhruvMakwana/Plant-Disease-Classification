# importing libraries
import requests, zipfile, io

"""
	Download images folder from given url, move it to dataset folder.
"""

#url for data without augmentation
#url = "https://data.mendeley.com/datasets/tywbtsjrjv/1/files/d5652a28-c1d8-4b76-97f3-72fb80f94efc/Plant_leaf_diseases_dataset_without_augmentation.zip?dl=1"

# url for data with augmentation
url = "https://data.mendeley.com/datasets/tywbtsjrjv/1/files/b4e3a32f-c0bd-4060-81e9-6144231f2520/Plant_leaf_diseases_dataset_with_augmentation.zip?dl=1"
response = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(response.content))
z.extractall()