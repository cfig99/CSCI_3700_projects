# Homework 3

## Team Members
- Gurkeerat Bains - Email: bainsg21@students.ecu.edu
- Cristian Figueiredo - Emial: FigueiredoC21@students.ecu.edu

## Quick Start
- $git clone https://github.com/cfig99/CSCI_3700_projects.git
- cd CSCI_3700_projects

- To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```

- Then you can start the server with:
```
python3 Main.py
```

- You should insert a new row (5, 'Cherry') into basket_a by inserting this into broswer
```
127.0.0.1:5000/api/update_basket_a
```

- You should show unique fruits in basket_a and unique fruits in basket_b by inserting this into broswer
```
127.0.0.1:5000/api/unique
```

## Dependencies
- Python
- Flask==2.0.3
- Jinja2==3.1.1
- markupsafe==2.0.1
- psycopg2