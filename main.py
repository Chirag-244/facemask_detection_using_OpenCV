'''       Developed By Chirag Bajaj       '''
# import the Video Camera Class from the 
from camera import VideoCamera
from flask import Flask, render_template, Response
app=Flask(__name__)
output=[]
# app at the home page
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output)
# creating the function that captures the video
def gen(camera):
    while True:
        data= camera.get_frame()
        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)



