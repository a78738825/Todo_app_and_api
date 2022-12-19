Todo_Api(and webapp) version 1.0 18/12/2022


REQUIREMENTS FOR TOOL:
--------------------------------------------------------------------
- python3
- mongoDB (mongodb on local machine) -> Default
- mongo atlas cluster (An External cluster with username and password) -> Modify in api.py => line-17 => MongoClient("<your connection string here>")
--------------------------------------------------------------------


HOW TO USE:
--------------------------------------------------------------------
- Install requirements:
    _Install dependencies using-_
        ```pip install -r requirements.txt```

- Start the API server:
    "After installing dependencies start the server using command -"
        uvicorn api:app --reload

- Run the Flask app:
    "Run the main webapp (or webpage) when python3 installed using-"
        python3 app.py
    "If command doesn't works-"
        py app.py
--------------------------------------------------------------------


CREATE A TODO:
--------------------------------------------------------------------
- step 1 >> After running Flask app open 'http://127.0.0.1:5000' on your browser
- step 2 >> Create a todo Title and Description
- step 3 >> Submit the Form and it will be saved in mongo database
--------------------------------------------------------------------
