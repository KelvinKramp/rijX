# Install requirements
Install python and pip

# Clone repository
git clone https://github.com/KelvinKramp/flask-assembly.git

# Install requirements
pip install -r requirements.txt

# Setup sqlite database
python app.py

# Setup similarity search algorithm to answer questions
git clone https://github.com/KelvinKramp/flask-searchform-elasticsearch
pip install -r requirements.txt (in the directory)
install Docker if you don't have it
run "python server.py" to launch docker 
run "python backend.py" to start elastic search backend server

# Run this flask webapplication
in the directory of flask-assembly run "python main.py" 

# To run the price search 
git clone https://github.com/KelvinKramp/scrape-driverse-license-medical-check-prices.git
pip install -r requirements.txt (in the directory)
run dash_app.py
-> you should be able to do a price search from the flask webapplication in the former step.