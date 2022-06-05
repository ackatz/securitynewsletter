# Security Newsletter Web Application

This website provides individuals and organizations with boilerplate security awareness newsletters and rotating cybersecurity tips and links. As a security consultant, I have viewed many security awareness training and newsletters that offer dated advice from the mid-2000s when the internet and its risks were vastly different. My goal is to provide advice that end users can understand and is fit for 2022 and beyond.

Every refresh of the site pulls a new set of tips and links from the database. This database contains security advice from industry professionals on Twitter, LinkedIn, and other avenues.

# Installation

1. After cloning this repo, create virtual Python environment in the /securitynewsletter dir

```python3 -m venv venv```  
```source venv/bin/activate```

2. Install required packages

```pip3 install -r requirements.txt```

3. Run webserver

```python3 wsgi.py```

4. Access webserver through http://127.0.0.1:5000
