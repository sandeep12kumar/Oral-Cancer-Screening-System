# AI Powered Oral Cancer Screening System

This project focuses on developing an AI-based system for early detection and classification of oral cancer using deep learning. We used the **MobileNetV3** architecture to classify images into three categories: **Benign**, **Healthy**, and **OPMD (Oral Potentially Malignant Disorder)**.


## Objective

To build a lightweight and efficient deep learning model that can assist in the automated classification of oral cancer using clinical images, thereby supporting early diagnosis and treatment.


## Dataset

- **Source:** Zenodo
- **Images:** 2,190 (730 per class)
- **Augmentation:** Performed to balance and increase dataset variability
- **Classes:**
  - **Benign**
  - **Healthy**
  - **OPMD**


## Model Details

- **Architecture:** MobileNetV3 (pretrained with fine-tuning)
- **Input Shape:** 224x224 RGB
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam
- **Metrics:** Accuracy, Precision, Recall, F1 Score


## Web Interface

A Flask-based web app allows users to upload an image and get instant predictions:

- **Frontend:** HTML + Bootstrap
- **Backend:** Python (Flask)
- **Model:** Loaded using TensorFlow/Keras


## Contact

If you have any questions, suggestions, or collaboration opportunities, please feel free to reach out to me at sandeepkumarptkm@gmail.com.
