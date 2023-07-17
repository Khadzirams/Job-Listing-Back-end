from flask import Flask, request, redirect, url_for, flash
from flask_cors import CORS


from db import db

app = Flask(__name__)
CORS(app)



@app.route('/')
def main():
    return"Job_listing_API"


@app.route('/job_listing', methods=["POST"])
def job_listing():
    data = request.get_json()
    job_title=data["job_title"]
    address=data["address"]
    about_company=data["about_company"]
    employement=data["employement"]
    roles_responsibilities=data["roles_responsibilities"]
    qualification=data["qualification"]
    experience=data["experience"]
    
    job_listing_instance = db('job_lisiting')

    job_listing_instance.insert(job_title,address,about_company,employement,roles_responsibilities,qualification,experience)

    return {'name':'Job posted'}

@app.route('/listing',methods=['GET'])
def listing():
    listing_instance = db('job_lisiting')

    listing = []

    rows = listing_instance.select()

    for row in rows:
        list_item = {
            "id": row[0],
            "job_title":row[1],
             "address":row[2],
             "about_company":row[3],
             "employement":row[4],
             "roles_responsibilities":row[5],
             "qualification": row[6],
             "experience": row[7]
        }

        listing.append(list_item)

        listing_dict = {
        "job_listing":listing
    }
    return listing_dict 

   