import os
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
def GetImagesWithID(path):
    # All Images name with their Locations
    ImagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    # creating empty variable
    faces = []
    ID = []
    for ImagePath in ImagePaths:
        faceimage = Image.open(ImagePath).convert('L');
        facenp = np.array(faceimage,'uint8')
        Id = int(os.path.split(ImagePath)[-1].split('.')[1])
        faces.append(facenp)
        ID.append(Id)
        # cv2.imshow('Training',facenp)
        # cv2.waitKey(100)
    return faces,ID


faces,ID = GetImagesWithID(path)
with open('labels.pickle','wb') as f:
    pickle.dump(ID,f)
recognizer.train(faces,np.array(ID))
recognizer.save("train.yml")
cv2.destroyAllWindows()