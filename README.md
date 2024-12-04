# Fruit Classification and Calorie Estimation using Machine Learning

This project classifies different types of fruits and estimates their calorie content using a Convolutional Neural Network (CNN) model. Built using Python and machine learning libraries, this tool can identify fruits from images and provide a calorie estimation, helping users make informed dietary choices.

## Project Structure

- `training_colab.ipynb`: Jupyter notebook designed for Google Colab, used for training the CNN model on a labeled dataset of fruits with calorie values.
- `checker.py`: A Python script that serves as an interface to input an image and receive the classification and calorie estimation.
- `model.h5`: Trained CNN model saved for efficient inference.
- `test_images/`: Folder containing test images to validate and demo the model's functionality.

> **Note**: The trained `.h5` model file and test data are available on Google Drive. [Download them here](https://drive.google.com/drive/folders/1t4ySAejgjbhTtV8Wx7MjDsHNNtP5Rcwa?usp=sharing).

## Features

- **Fruit Classification**: Identifies various fruit types from input images.
- **Calorie Estimation**: Estimates calorie count per 100g for each identified fruit.
- **User-Friendly Interface**: Accepts an image as input and displays results instantly.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/pymash/fruit-classification-calorie-estimation-ml.git
    cd fruit-classification-calorie-estimation-ml
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the model and test data from Google Drive and place `model.h5` and test images in the appropriate directories.

4. Run `checker.py` to start the interface:
    ```bash
    python checker.py
    ```

## Usage

1. **Training**:
   - Open `training_colab.ipynb` in Google Colab.
   - Run each cell to preprocess the data, train the model, and save the model as `model.h5`.

2. **Prediction**:
   - Use `checker.py` to input an image and get the fruit classification and calorie estimation.

## Dataset

The dataset used for training was obtained from Kaggle. It contains labeled images of various fruits along with calorie values. You can access the dataset [here](https://www.kaggle.com/datasets/shreyapmaher/fruits-dataset-images).

## Results

The CNN model has been trained to classify various fruits with an accuracy of around 95% and provides estimated calorie counts per fruit type.

## Future Enhancements

- Extend the model to include more fruit varieties.
- Improve calorie estimation accuracy with additional dietary information.

## Contributing

Feel free to contribute by creating issues, suggesting features, or making pull requests.


