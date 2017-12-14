import requests as req
import json
import shelve
from requests.auth import HTTPBasicAuth
import os

url = "http://0.0.0.0:8080/filepath/"
print("==================================================================")
print("\t\tDFS System")
print("==================================================================\n")
print("A.Open and Read Current file ")
print("B.Write on the Current file")
print("C. Delete File\n")
choices = input("Select the choices to:- \n")
if choices =='A':
    filepath = input("File name :")
    url = url+filepath
    response = req.get(url)
    print("reply: ",response.text)
if choices=='B':
    filepath = input("Enter the file name:")
    url = url+filepath
    content = "hello"
    response= req.post(url, content)
    print("reply: ",reply.text)
if choices=='C':
    filepath = input("Enter the file name:")
    url = url+filepath
    response = req.delete(url)
    print("File deleted")

    """
    response = req.get(url, auth=HTTPBasicAuth(username,password))
    #print("File: ",response.json())
    print("Response: ",response.text)
    url = "http://0.0.0.0:8080/filepath/DFS_Test/ex.txt"
    filepath = input("Enter the file name:")
    url = url+filepath
    response = req.get(url)
    print("Response: ",response.text)
    """
