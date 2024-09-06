## Camera Classifier

### Overview

This project is a simple camera-based classifier using Python, OpenCV, and Tkinter. The system allows you to classify images captured from a camera into two different classes, train a model on the collected data, and then use the trained model to predict the class of new images in real time.

### Project Structure

- **main.py**: The entry point of the application. Initializes the app and starts the camera classifier.
- **model.py**: Contains the `Model` class, which handles training and prediction using a linear support vector machine (SVM).
- **camera.py**: Handles camera operations, including capturing frames from the webcam.
- **app.py**: Manages the graphical user interface (GUI) using Tkinter and handles interactions between the camera, model, and user.

### Requirements

- Python 3.x
- OpenCV
- Tkinter
- scikit-learn
- PIL (Pillow)
