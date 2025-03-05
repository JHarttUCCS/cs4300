# Homework 2 Jacob Hartt
## Project Structure
The key components of the project structure are as follows:
```
homework2
├── Bookings
│   ├── Bookings
│   ├── BookingsApp
│   │   ├── migrations
│   │   ├── templates
│   │   └── tests
│   └── manage.py
├── README.md
└── requirements.txt
```

## Setup
1. Navigate to the `homework2/` folder
2. Make a venv: `python -m venv myvenv`
3. Source the venv: `source /myvenv/bin/activate`
4. Run `pip install -r requirements.txt`

## Running 
1. Navigate to the `homework2/` folder
2. Source the venv: `source /myvenv/bin/activate`
3. Navigate to the `homework2/Bookings/` subfolder
4. Run `python manage.py runserver 0.0.0.0:3000`

## Testing
1. Start the server.
2. Start a **seperate** terminal
2. Navigate to the `homework2/Bookings/` subfolder
3. Run `python manage.py test -v 2`
