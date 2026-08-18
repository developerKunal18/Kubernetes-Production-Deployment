from flask import Flask, jsonify
import os
app=Flask(__name__)
VERSION=os.getenv('APP_VERSION','1.0')
@app.get('/')
def home(): return jsonify(message='Day 303 Kubernetes API', version=VERSION)
@app.get('/health')
def health(): return jsonify(status='healthy')
@app.get('/ready')
def ready(): return jsonify(status='ready')
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
