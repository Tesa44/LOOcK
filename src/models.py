from facenet_pytorch import MTCNN, InceptionResnetV1

# Initialize face detection (MTCNN) and recognition model (InceptionResnetV1)
detector = MTCNN(keep_all=True)
resnet = InceptionResnetV1(pretrained='vggface2').eval()