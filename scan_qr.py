import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        for code in decode(frame):
            device_info = code.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return device_info
        cv2.imshow('Scan QR', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return None
