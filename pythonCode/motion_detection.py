import cv2

class motionDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        _, self.prevFrame = self.cap.read()
        self.curFrame = None
        self.text = []
        self.detected = False
    
    def setText(self, text):
        self.text = text

    def motionDetected(self):
        return self.detected

    def run(self):
        self.detected = False
        if self.cap.isOpened():
            _, self.curFrame = self.cap.read()
            diff = cv2.absdiff(self.prevFrame, self.curFrame)
            diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(diff_gray, (5,5), 0)
            _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(threshold, None, iterations=3)
            contours, _ = cv2.findContours(
                dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
            )

            for contour in contours:
                (x,y,w,h) = cv2.boundingRect(contour)
                if cv2.contourArea(contour) < 900:
                    continue
                cv2.rectangle(self.prevFrame, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(self.prevFrame, "status: {}".format("MOTION DETECTED"), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (217,10,10), 2)
                self.detected = True
            if (type(self.text) == list):
                for i in range(len(self.text)):
                    cv2.putText(self.prevFrame, self.text[i], (40, 120+60*i), cv2.FONT_HERSHEY_SIMPLEX, 1, (217,200,10), 2)
            elif (type(self.text) == str):
                cv2.putText(self.prevFrame, self.text, (40, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (217,10,200), 2)
            cv2.imshow("Video", self.prevFrame)
            self.prevFrame = self.curFrame
            
            if cv2.waitKey(50) != 27:
                return True
        return False
        
    def clean(self):
        self.cap.release()
        cv2.destroyAllWindows()