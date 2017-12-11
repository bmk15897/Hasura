from flask import Flask,render_template,request,redirect,send_file
import requests,json

ListOfNames=[]  #for storing subtask 7 logs.

app = Flask(__name__)

#Subtask 1 - A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"

@app.route("/")
def hello():
    return "Hello World - Bharati"


#Subtask 2 - Add a route, for e.g. http://localhost:8080/authors, which:
#a) fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
#b) fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
#c) Respond with only a list of authors and the count of their posts (a newline for each author).

@app.route("/authors")
def tp():
    r = json.loads(requests.get('https://jsonplaceholder.typicode.com/users').content.decode('utf-8'))

    s = json.loads(requests.get('https://jsonplaceholder.typicode.com/posts').content.decode('utf-8'))

    list = {}

    ans = ""
    for t in s:
        if t['userId'] in list:
            list[t['userId']]+=1
        else:
            list[t['userId']]=1

    for u in r:
        ans+=u['name']+"   "+str(list[u['id']])+'<br>'
    return ans


#Subtask 3 - Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

@app.route("/users/setcookie",methods=['GET','POST'])
def setcookie():
    resp = app.make_response(redirect('/'))

    if 'Username' not in request.cookies:
        resp.set_cookie('Username','Bharati')
        print("Username Cookie set")
    if 'Age' not in request.cookies:
        resp.set_cookie('Age','20')
        print("Age Cookie set")

    return resp


#Subtask 4 - Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

@app.route("/users/getcookie",methods=['GET','POST'])
def getcookie():
    users_name = ""
    users_age = ""
    if 'Username' in request.cookies:
        users_name = request.cookies.get('Username')
    if 'Age' in request.cookies:
        users_age = request.cookies.get('Age')

    return users_name+"\t"+users_age


#Subtask 5 - Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

@app.route("/robots.txt",methods=['GET','POST'])
def deny_req():
    return redirect('http://httpbin.org/deny')


#Subtask 6 - Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.
@app.route("/html")
def user_html():
    return render_template('sam.html')

@app.route("/image")
def user_image():
    return send_file('tiger.png')


#Subtask 7 - A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.
@app.route("/input")
def fInput():
    return render_template('sam.html')

@app.route("/input",methods=['POST','GET'])
def fProcess():
    ListOfNames.append(request.form['text'])
    print('Logged Info ',ListOfNames)
    return render_template('sam.html',my_list=ListOfNames)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

