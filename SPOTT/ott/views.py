from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import subprocess
import face_recognition
import cv2
import numpy as np

face_det=False

# Create your views here.
def device(request):
    
    device_def="""USB:

    USB 3.1 Bus:

      Host Controller Driver: AppleT8103USBXHCI

    USB 3.1 Bus:

      Host Controller Driver: AppleT8103USBXHCI

"""
    result = subprocess.run(["system_profiler", "SPUSBDataType"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    device_details=result.stdout
    yell = 10
    if device_details==device_def:
        device_flag=True

    else:
        device_flag=False


    return JsonResponse({'device_flag':device_flag})

def audio(request):

    result = subprocess.run(["system_profiler", "SPAudioDataType"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    audio_devices=result.stdout 
    target_device="Salil’s AirPods Pro"
    if (audio_devices.find(target_device) == -1):
        audio_flag=False
    else:
        audio_flag=True  


    return JsonResponse({'audio_flag':audio_flag})



#FACE DETECTION

def face(request):
    global face_det
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("safuwan.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    akshay_image = face_recognition.load_image_file("akshay.jpg")
    akshay_face_encoding = face_recognition.face_encodings(akshay_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,akshay_face_encoding
    ]
    known_face_names = [
        "Obama","Akshay"
    ]

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if name in known_face_names:
                    face_det=True
            else:
                    face_det=False
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

def flagcall(request):
    global face_det
    flag=face_det
    return JsonResponse({'face_flag':flag})

def home(request):
	return render(request, "home.html")

def login(request):
	return render(request, "login.html")

def play(request):
	return render(request, "play.html")


def blocked(request):
	return render(request, "blocked.html")

def start(request):
	return render(request, "start.html")
