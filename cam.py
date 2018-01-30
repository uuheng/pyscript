import cv2
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from time import time

def get_img():
    cap = cv2.VideoCapture(0)
    while(1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            fname = str(int(time())) + '.jpeg'
            cv2.imwrite(fname, frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return fname

def send_img(fname):
    user = '1293662421@qq.com'
    pwd = 'yuwqgxdthiuifgbi'
    with open(fname, 'rb') as fd:
        data = fd.read()
    msg = MIMEMultipart()
    msg['Subject'] = 'cam_img'
    msg['From'] = user
    msg['To'] = user
    jpegpart = MIMEApplication(data)
    jpegpart.add_header('Content-Disposition', 'attachment', filename=fname)
    msg.attach(jpegpart)
    
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(user, pwd)
    s.sendmail(user, user, msg.as_string())
    s.close()
    return

def main():
    fname = get_img()
    send_img(fname)

if __name__ == '__main__':
    main()

