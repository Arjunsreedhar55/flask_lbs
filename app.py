from flask import Flask, render_template, request
import weight
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='POST':
        height=request.form['height']
        print(height)
        weigh=weight.prediction([[float(height)]])
        return render_template('index.html',hei=height, wei=weigh)
    return render_template('index.html')

if __name__ == "__main__":
      app.run(port=8001)
