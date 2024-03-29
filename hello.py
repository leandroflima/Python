from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name	

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, World!'
	
@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'
   
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
	
app.add_url_rule('/', 'hello', hello_world)
	
if __name__ == '__main__':
   app.run('127.0.0.1',1234)
   #app.run('127.0.0.1',1234,true) #debug