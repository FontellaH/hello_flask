from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!, Hello '  # Return the string 'Hello World!' as a response

@app.route('/greeting/<name>')          # 2 The "@" decorator associates this route with the function immediately following can add multiple routes
def greeting(name):
     print(name)
     return f'<h1>Welcome! {name} </h1>' 

@app.route('/template')
def show_temp():
    return render_template("index.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

