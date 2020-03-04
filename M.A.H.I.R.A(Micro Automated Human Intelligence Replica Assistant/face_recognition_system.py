import face_recognition
import cv2
import os
import PIL.Image
import PIL.ImageDraw
def Face_Recognition():
    path = os.getcwd()
    image_directory = os.path.join(path+'\\Face Dataset\\Known Faces')
    known_face_encodings = []
    person_name = []
    for i in os.listdir(image_directory):
        image_path = os.path.join(image_directory,i)
        # Load the known images
        person = i.split('.')
        person_name.append(person[0])
        
        image_of_person = face_recognition.load_image_file(image_path)
    
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
    
        #  Create a list of all known face encodings
        known_face_encodings.append(person_face_encoding)
    
    # Load the image we want to check
    
    vidcap = cv2.VideoCapture(0)
    success,image = vidcap.read()
    count = 0
    output_image = os.path.join(path+'\\Face Dataset\\Unknown Faces')
    output_image_path = output_image+'\\frame.png'
    cv2.imwrite(output_image_path,image)
    vidcap.release()
    cv2.destroyAllWindows()
    for i in os.listdir(output_image):
        
        print('Recognizing People in WebCam'.format(i))
        unknown_image = face_recognition.load_image_file(os.path.join(output_image+'\\{}'.format(i)))
        
        # Get face encodings for any people in the picture
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)
        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)
        face_locations = face_recognition.face_locations(unknown_image)
        pil_image = PIL.Image.fromarray(unknown_image)
    
        for face_location in face_locations:
        
            # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
            top,right,bottom,left = face_location
            # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        
            # Let's draw a box around the face
            draw = PIL.ImageDraw.Draw(pil_image)
            draw.rectangle([left, top, right, bottom], outline="red")
        
        # Display the image on screen
        pil_image.show()
        number_of_faces = len(face_landmarks_list)
        # print("I found {} face(s) in this photograph.".format(number_of_faces))
        
        # Load the image into a Python Image Library object so that we can draw on top of it and display it
        pil_image = PIL.Image.fromarray(image)
        
        # Create a PIL drawing object to be able to draw lines later
        draw = PIL.ImageDraw.Draw(pil_image)
    
        # Loop over each face
        for face_landmarks in face_landmarks_list:
        
            # Loop over each facial feature (eye, nose, mouth, lips, etc)
            for name, list_of_points in face_landmarks.items():
        
                # Print the location of each facial feature in this image
                # print("The {} in this face has the following points: {}".format(name, list_of_points))
        
                # Let's trace out each facial feature in the image with a line!
                draw.line(list_of_points,fill='red',width = 2)
        
        pil_image.show()
    
        
        # There might be more than one person in the photo, so we need to loop over each face we found
        for unknown_face_encoding in unknown_face_encodings:
        
            # Test if this unknown face encoding matches any of the three people we know
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.5)
        
            
            count = 0
            len_res = len(results)
            for i,j in enumerate(results):
                
                if j==True:
                    name=person_name[i]
                    print('Found {} in Photo'.format(name))
                else:
                    count = count+1
            if count == len_res:
                print('Found Unknown Person in Photo')
        try:
            return name
        except:
            return 'Person is not Registered in Database'
            
    # print(unknown_face_encodings)
