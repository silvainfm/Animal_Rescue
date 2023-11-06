# Animal Rescue Management System

## Overview

This project aims to build an animal rescue management system to help animal shelters and rescue organizations efficiently manage their operations. The system will use MongoDB to store data on rescued animals and provide a Flask interface for users to interact with the data.

## Key features:

* Store animal data like name, breed, age, adoption status etc in MongoDB
* CRUD operations on animal records via Flask interface
* Search/filter animals by criteria
* Manage adoption applications
* Match animals to potential adopters using ML

## Data

The data will consist of records for 20 dogs and 20 cats scraped from the Nashville Humane Association website.

Each animal record will contain:
* Type
* Name
* ID
* Picture
* Birthdate
* Weight
* Breed
* Adoption status
* Sex
* Adoption fee
* Additional notes
* MongoDB is chosen for its flexibility in storing semi-structured and evolving data.
* Usage

The Flask interface will allow users to:
* Create new animal records
* Retrieve an animal's profile
* Update an animal's information
* Provide endpoints for adopters to apply for adoption/fostering

Some example queries:
```
# Retrieve all available animals
db.animals.find({ status: "available" })

# Search for animals by species and age 
db.animals.find({ species: "Dog", age: { $gte: 1, $lte: 5 } })

# Find available animals in a city
db.animals.find({ location: "Nashville", status: "available" })  

# Update adoption status from available to pending
db.animals.updateOne({ _id: ObjectId("animal_id") }, 
                     { $set: { status: "pending" } })

# Apply for adoption
db.adoptionApplications.insert({
  animal_id: "animal_id",
  applicant_name: "Hunter Dawley",
  applicant_phone: "757-323-6133",
  applicant_email: "hunter.b.dawley@vanderbilt.edu",
  application_status: "pending"  
})
```

## Timeline
* Week 1: Submit proposal, create dataset
* Week 2: Test MongoDB, run sample queries
* Week 3: Work on Flask interface
* Week 4: Final touches and deliverables

## Expected Output
The project will showcase available animals for adoption in the Nashville area and allow rescue staff to manage and update animal records and adoption applications.

## Additional Scope
* Web scraping to expand dataset
* CLI interface for queries
* REST API endpoints
* Researching use of MongoDB with machine learning
