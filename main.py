import sys
import os
import logging
# GAE Flask code
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages'))

from flask import Flask, render_template, jsonify, send_file,request, url_for, redirect, Response, abort, make_response

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        print e
        raise e

@app.route("/download")
def resume_download():
    try:
        resume_type = ""
        resume_type = request.args.get("type")
        if resume_type == "one_page":
            return send_file("./static/assets/pdf/MANIKANDANS_Single_Page_Resume.pdf", as_attachment=True)

        return send_file("./static/assets/pdf/ManikandanS_Software_Engineer.pdf", as_attachment=True)
    except Exception as e:
        print e
        raise e


if __name__ == "__main__":
    app.run()