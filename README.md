1. Navigate to your desired project directory:
cd G:\Django-Projects\

2. Create a new Django project:
django-admin startproject SchoolProject

3. Change to the new project directory:
cd SchoolProject

4. Create a virtual environment (if not already done):
python -m venv venv

5. Activate the virtual environment:
.\venv\Scripts\activate

6. pip install django
pip install django

7. python manage.py runserver
python manage.py runserver


Summary
1. Ensure your manage.py file is in the correct project folder.
2. Make sure to activate your virtual environment before running the server.
3. Install Django within the virtual environment if it’s not already installed.

Problem: You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run:  'python manage.py migrate' to apply them.

After that lets configure the database mysql.

Lets Install Mysql
1. pip install pymysql
2. pip install pymysql --upgrade

Next, now you in the Virtual Environment lets install the Django again
pip install django==3.2

StudentApp we have to added in to the setting.py
  'StudentApp.apps.StudentappConfig'

1. After that Create the Model
models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    fee = models.IntegerField()

2. Install the CORS
pip install django-cors-headers

3. Install the Rest Framework
pip install djangorestframework

4. Add the dependencies in to the settings.py inside the INSTALLED_APPS
'corsheaders',
'rest_framework',
'StudentApp.apps.StudentappConfig'

5. in to the settings.py inside the MIDDLEWARE add this dependencies
 'corsheaders.middleware.CorsMiddleware',

6. in to the settings.py you have add CORS_ORIGIN Setting make both as true
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_HEADERS=True

7. Angular Connected Port
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
]

8. After that select StudentApp Folder inside the create the file serializers.py
serializers.py
from rest_framework import serializers
from StudentApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

9. After that lets Configure the Mysql Database into our Django Project

1.  Install the database Url  type by the following command
pip install dj-database-url

2. After that Install the mysqlclient
pip install mysqlclient

3. After that Configure the database connection on settings.py
settings.py

import dj_database_url

DATABASES['default'] = dj_database_url.parse('mysql://root@localhost/kms')

4. After that run the migration command 
python manage.py makemigrations

5. After done successfully. then type following command
python manage.py migrate

then you can see you database table has been created.

6. After that open views.py for generating views
views.py paste the code
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        student = Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(id=id)
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=Student.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

7. Manage the Urls
Urls.py paste the code

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from StudentApp import views

urlpatterns = [
    url(r'^student$',views.studentApi),
    url(r'^student$',views.studentApi),
    url(r'^student/([0-9]+)$',views.studentApi),
    path('admin/', admin.site.urls),
]

8. Run the Project
python manage.py runserver

React
1. Installing React
npx create-react-app front-end

2. After complete the installation and run the project using following command.
npm start

3. Now you see the React Welcome Page of react.After that open the React project into VS code editor.

Add the Bootstrap styles inside the index.html file. inside the head tag

<head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />

    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

    <title>React App</title>
  </head>

4. After that install the axios by typing the following command

npm i axios

5. Create a Folder Component inside folder Create a new Component Student.js 

import {useEffect, useState } from "react";
import axios from 'axios';
function Student()
{

  const [id, setId] = useState('');
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [fee, setFee] = useState("");
  const [students, setUsers] = useState([]);


useEffect(() => {
  (async () => await Load())();
  }, []);
  
  
  async function  Load()
  {
     const result = await axios.get(
         "http://127.0.0.1:8000/student");
         setUsers(result.data);
         console.log(result.data);
  }
    
  
 async function save(event)
    {
        event.preventDefault();
    try
        {
         await axios.post("http://127.0.0.1:8000/student",
        {
        
          name: name,
          address: address,
          fee: fee
        
        });
          alert("Student Registation Successfully");
          setId("");
          setName("");
          setAddress("");
          setFee("");
          Load();

      
        
        }
    catch(err)
        {
          alert("Student Registation Failed");
        }
   }



   async function editStudent(students)
   {
    setName(students.name);
    setAddress(students.address);
    setFee(students.fee);
    setId(students.id);
    
   }
   async function DeleteStudent(id)
   {
      
        await axios.delete("http://127.0.0.1:8000/student/" + id);
        alert("Student deleted Successfully");
        setId("");
        setName("");
        setAddress("");
        setFee("");
        Load();
  
  
   }
   async function update(event)
   {
    event.preventDefault();
   try
       {
        
        await axios.put("http://127.0.0.1:8000/student/"+ students.find(u => u.id === id).id || id,
       {
         id: id,
         name: name,
         address: address,
         fee: fee
      
       });
         alert("Student Updateddddd");
         setId("");
         setName("");
         setAddress("");
         setFee("");
         Load();
      
       }
   catch(err)
       {
         alert(" Student updateddd Failed");
       }
  }
  return (
    <div>
       <h1>Student Details</h1>
       <div class="container mt-4" >
          <form>
              <div class="form-group">

               <label>Student Name</label>
                <input  type="text" class="form-control" id="name"
                value={name}
                onChange={(event) =>
                  {
                    setName(event.target.value);      
                  }}
                />
              </div>

              <div class="form-group">
                <label>Address</label>
                <input  type="text" class="form-control" id="address"
                 value={address}
                  onChange={(event) =>
                    {
                     setAddress(event.target.value);      
                    }}
                />
              </div>
              <div class="form-group">
                <label>Fee</label>
                <input type="text" class="form-control" id="fee"
                  value={fee}
                onChange={(event) =>
                  {
                    setFee(event.target.value);      
                  }}
                />
              </div>
                 <div>
              <button   class="btn btn-primary mt-4"  onClick={save}>Register</button> 
              <button   class="btn btn-warning mt-4"  onClick={update}>Update</button>
              </div>  

              
            </form>
          </div>


<table class="table table-dark" align="center">
  <thead>
    <tr>
      <th scope="col">Student Id</th>
      <th scope="col">Student Name</th>
      <th scope="col">Address</th>
      <th scope="col">Fee</th>
      
      <th scope="col">Option</th>
    </tr>
  </thead>
       {students.map(function fn(student)
       {
            return(
            <tbody>
                <tr>
                <th scope="row">{student.id} </th>
                <td>{student.name}</td>
                <td>{student.address}</td>
                <td>{student.fee}</td>        
                <td>
                    <button type="button" class="btn btn-warning"  onClick={() => editStudent(student)} >Edit</button>  
                    <button type="button" class="btn btn-danger" onClick={() => DeleteStudent(student.id)}>Delete</button>
                </td>
                </tr>
            </tbody>
            );
            })}
            </table>
       </div>
            );
        }
export default Student;

6. Set the out Student.js Component to app.js

import Student from "./compontents/Student";
function App() {
  return (

<div className="App">
    
    <Student/>
  </div>
  );
}

export default App;


Problem 2: Ensure Virtual Environment is Activated in the IDE
Solution:If you're using VS Code or another IDE, ensure that it's using the correct Python interpreter:

In VS Code: Press Ctrl + Shift + P and select Python: Select Interpreter.
Choose the interpreter inside your virtual environment, e.g., G:\Django-Projects\SchoolProject\venv\Scripts\python.exe.
Restart VS Code to apply the changes.


