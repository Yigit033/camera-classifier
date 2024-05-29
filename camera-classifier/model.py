from sklearn.svm import LinearSVC
import numpy as np
import cv2
import PIL

class Model:
  def __init__(self):
    self.model = LinearSVC()

  def train_model(self, counters):
    img_list = np.array([])
    class_list = np.array([])


    for i in range(1, counters[0]):
      img = cv2.imread(f"1/frame{1}.jpg")[:,:,0]
      img= img.reshape(16800)
      img_list = np.append(img_list, img)
      class_list = np.append(class_list, 1)

    for i in range(1, counters[1]):
      img = cv2.imread(f"2/frame{1}.jpg")[:,:,0]  # 2 is the folder number for the second class of images  
      img= img.reshape(16800)
      img_list = np.append(img_list, img)
      class_list = np.append(class_list, 2)
    
    img_list = img_list.reshape(counters[0] - 1 + counters[1] - 1, 16800)
    self.model.fit(img_list, class_list)
    print("The Model successfully trained!")


  def predict(self, frame):
    frame = frame[1]
    cv2.imread("frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
    img = PIL.Image.open("frame.jpg")
    img.thumbnail((150, 150), PIL.Image.LANCZOS)
    img.save("frame.jpg")


    img = cv2.imread("frame.jpg")[:,:,0]
    img = img.reshape(16800)
    prediction = self.predict([img])

    return prediction[0]
  

