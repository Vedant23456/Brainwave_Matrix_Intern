from flask import Flask, render_template, request
from markupsafe import escape
import re
from urllib.parse import urlparse

app = Flask(__name__)

def is_phishing_url(url):
    
    phishing_patterns = [
        r'http://',  
        r'https?://[^/]+@',  
        r'https?://.*\.?\d+\.\d+\.\d+\.\d+', 
    ]
    
    domain = urlparse(url).netloc

    
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain):
        return True

    
    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True

    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = escape(request.form['url'])  
    if is_phishing_url(url):
        result = f"Phishing URL detected: {url}"
    else:
        result = f"Safe URL: {url}"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
