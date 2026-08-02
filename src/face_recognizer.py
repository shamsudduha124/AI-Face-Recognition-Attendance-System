import face_recognition

class FaceRecognizer:
    def encode_face(self, image):
        encodings = face_recognition.face_encodings(image)
        return encodings[0] if encodings else None