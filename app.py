from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.ouuxnkr.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,    
    }
    db.team.insert_one(doc)
    
    return jsonify({'msg':'저장완료!'})

@app.route("/guestbook", methods=["GET"])
def mars_get():
    team_data = list(db.team.find({},{'_id':False}))
    return jsonify({'result':team_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)