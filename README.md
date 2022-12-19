**Todo_Api(and webapp)**
===============================================
version 1.0 18/12/2022 <br>


REQUIREMENTS FOR TOOL :
--------------------------------------------------------------------
- Python3
- MongoDB (mongodb on local machine) -> Default
- Mongo Atlas Cluster (An External cluster with username and password) → Modify in api.py → <br>&nbsp; &nbsp; → line-17 → MongoClient("<_your connection string here_>")
--------------------------------------------------------------------


HOW TO USE :
--------------------------------------------------------------------
- **Install requirements :** </br>
      <pre>
         ```python
           pip install -r requirements.txt
          ```
      </pre>

- **Start the API server :** </br>
         _After installing dependencies start the server using command -_
         <pre>
         uvicorn api:app --reload
         </pre>
         

- **Run the Flask app :** </br>
        _Run the main webapp (or webpage) when python3 installed using -_
        <pre>
            python3 app.py
        </pre>
        _If command doesn't works-_
        <pre>
            py app.py
        </pre>
--------------------------------------------------------------------


CREATE A TODO:
--------------------------------------------------------------------
- step 1 →> After running Flask app open 'http://127.0.0.1:5000' on your browser
- step 2 →> Create a Todo Title and Description
- step 3 →> Submit the Form and it will be saved in Mongo Database
<!-- -------------------------------------------------------------------- -->
