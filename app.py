from flask import Flask, render_template              
app = Flask(__name__)

@app.route("/")                
def home():                    
    return render_template("homepage.html") 
    
                  
@app.route("/zachholman")                
def zachholman():
    return render_template("zachholman.html")                    
    
if __name__== "__main__":
    app.run(debug=True)