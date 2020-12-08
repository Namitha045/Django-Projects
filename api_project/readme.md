Overview:

        This big Corp API is used to pull Employee data for your app along with the offices and department information for each.

Packages Used

        •	Python (3.8.0)
        
        •	Django (3.0.3)
        
        •	Django Rest framework (3.11.1)
        
        •	Django -filter (2.3.0)

Installation:

        pip install django
        
        pip install djangorestframework
        
        pip install django-filter

API Reference

       API Root
        The API root resource links to all other resources available in the API.

       List api root resources
        GET / 
       
       Get links to all other resources available in the API.

       POST, PUT or DELETE methods are not allowed for this app
        
        Get authorized Info:
                GET /Resource Info/{key_id}
                Get information about the requested id for the resource.
                Path parameters:
                Key_id: Required
                Key id is the id of an Employee, office or a department.
                    Example Response:
                        "results": [
                            {
                                "first": "Patricia",
                                "last": "Diaz",
                                "id": 1,
                                "manager": null,
                                "department": "http://localhost:8000/departments/5/",
                                "office": "http://localhost:8000/offices/2/"
                            },
                    Error Response:
                    HTTP 404 Not Found
                    Allow: GET, HEAD, OPTIONS
                    Content-Type: application/json
                    Vary: Accept

                    {
                        "detail": "Not found."
                    }


