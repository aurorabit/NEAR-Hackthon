
#encoding:utf-8
#!/usr/bin/env python
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
import os
import base64
import random
import datetime
import json
from flask_cors import CORS


app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
def create_uuid(): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
    randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum)
    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum
 

@app.route('/upload')
def upload_test():
    return render_template('test.html')
 
 
# 上传文件
CORS(app, resources=r'/*')
@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = create_uuid() + '.' + ext
        f.save(os.path.join(file_dir, new_filename))

        nft_dict = {"nft_name": request.form.get('nft_name'),
                    "creator_name": request.form.get('creator_name'),
                    "description": request.form.get('description'),
                    "type": request.form.get('type'),
                    "style": request.form.get('style'),
                    "date": request.form.get('date'),
                    "number": request.form.get('number'),
                    "theme": request.form.get('theme'),
                    "serial_number": request.form.get('serial_number')}

        print(nft_dict)
        nft_json = json.dumps(nft_dict)
        json_filename = new_filename + '_json'
        json_file = open(os.path.join(file_dir, json_filename), 'w', encoding='utf-8')
        json_file.write(nft_json)
        json_file.close()

        return jsonify({"success": 0, "msg": "success", "photo_url": new_filename, "json_url": json_filename})
    else:
        return jsonify({"error": 1001, "msg": "fail"})
 
CORS(app, resources=r'/*')
@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        pass
    
# show photo
CORS(app, resources=r'/*')
@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass
 
 
if __name__ == '__main__':
    app.run(debug=True)
