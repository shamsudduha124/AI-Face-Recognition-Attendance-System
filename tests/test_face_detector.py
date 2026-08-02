from src.face_detector import FaceDetector

def test_detector_initialization():
    detector = FaceDetector()
    assert detector is not None