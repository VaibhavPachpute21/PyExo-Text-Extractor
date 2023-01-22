from flask import Flask
from flask import Flask, render_template, request
from PyExo import PyExo
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

cloudinary.config(
  cloud_name = "dvvzlzude",
  api_key = "819426927953279",
  api_secret = "JAPvS4ZO-hlUtSipa6-BzpRfg8M"
)

app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ProcessDoc', methods=['POST'])
def ProcessDoc():
    obj = request.get_json()
    print(obj)
    url = obj['URL']
    public_id=obj['public_id']
    print("URL:",url)
    # Download the PDF
    pdf_url = cloudinary.utils.cloudinary_url(public_id, format="pdf")[0]
    response = requests.get(pdf_url)
    # Save the PDF to a local file
    with open("downloaded_pdf.pdf", "wb") as f:
        f.write(response.content)
    return request.data

 
if __name__=='__main__':
    app.run(debug = True)