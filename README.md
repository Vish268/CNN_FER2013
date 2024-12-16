# CNN model REPOSITORY

## Problem Statement
The problem in question is to classify images from the FER 2013 Databases into its constituent classes (Emotions).
These being : ['anger','fear','disgust','happy','neutral','sad','surprise']

## Approach
A CNN (convolutional neural network) model is being used in this project since for image classification, it on average has a higher accuaracy.
The various layers of the cnn model were modified randomly for optimization. 
Streamlit was used here as the web interface.

### Web App - Screenshot
![Web App](https://github.com/Vish268/CNN_FER2013/blob/main/screenshots/Streamlit_app_screenshot.png)

## Results
The average accuracy was 52 % in the testing dataset. Though this seems low, during the actual trial with random pictures from the internet ,it yielded a much better result.
Screenshots of the correctly and incorrectly classified images are given inside the screenshots folder.

Below are a few snapshots of the these results ,

### Training Accuracy
![Training Accuracy](https://github.com/Vish268/CNN_FER2013/blob/main/screenshots/Screenshot%202024-12-16%20094200.png)

### Validation Accuracy
![Validation Accuracy](https://github.com/Vish268/CNN_FER2013/blob/main/screenshots/Screenshot%202024-12-16%20094224.png)

### Classification Report with F1 score
![Classification Report](https://github.com/Vish268/CNN_FER2013/blob/main/screenshots/Screenshot%202024-12-16%20134417.png)

### Confusion Matrix
![Confusion Matrix](https://github.com/Vish268/CNN_FER2013/blob/main/screenshots/Screenshot%202024-12-16%20134804.png)

## Challenges
During the intial stages of testing with the test data set, the accuracy was around 20 %.This might have been because of the lack of resolution in the pictures (48x48) in the dataset.


## NOTE
Currently only jpg/jpeg images are supported.
