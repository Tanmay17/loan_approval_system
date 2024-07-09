from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.loan_applications

def save_application(application_id, application, risk_score, is_approved):
    db.applications.insert_one({
        "application_id": application_id,
        "application": application.dict(),
        "risk_score": risk_score,
        "approved": is_approved
    })

def get_application(application_id):
    return db.applications.find_one({"application_id": application_id})

def update_application_status(application_id, approved):
    db.applications.update_one({"application_id": application_id}, {"$set": {"approved": approved}})
