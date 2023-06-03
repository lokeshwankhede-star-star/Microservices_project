# Microservices project
Create an API Gateway with post,patch,put and delete method backend on lambda and connect database with DynamoDB connect to Postman

### API Gateway:
---
AWS Gateway is a service provided by Amazon Web Services (AWS) that acts as a bridge or intermediary between different systems or services. 
- It enables communication and data exchange between different components in a secure and scalable manner. 
- AWS Gateway as a gateway or doorway that connects different parts of your software or infrastructure together. 
- It allows you to integrate and interact with various AWS services, such as AWS Lambda, AWS DynamoDB, or AWS S3, as well as external systems or APIs.
- AWS Gateway offers different types, such as AWS API Gateway, which allows you to create, manage, and publish APIs for your applications, and AWS Storage Gateway, which helps 
connect your on-premises data storage to the AWS cloud.
- It make easy to scale and build API.

### AWS Lambda:
---
AWS Lambda is a compute service provided by Amazon Web Services (AWS) 
- It allows you to run your code without the need to provision or manage servers. 
- It enables you to execute your code in a serverless environment.

### AWS DynamoDB:
---
- It is a fully managed NoSQL database service provided by Amazon Web Services (AWS). 
- It is a database that allows you to store and retrieve large amounts of data in a highly scalable and efficient manner.

## Steps:
A) Launch API Gateway

1. Log in to your AWS Console. (https://aws.amazon.com/)
2. Search for " API Gateway " 
3. Go on " Create API "
4. Build " REST API "
5. Choose 
    - Choose the Protocol: REST
    - Create new API: New API
    - Settings: 
      - API name: ex. my-new-api 
      - Description (optional)
      - Endpoint type: Regional
6. Click on "/"
7. Go in " Actions " 
8. Create Resources 
      - Resource Name : Student-data
9. Select Student-data 
10. Go in " Actions " and create 4 more resources as:
    - Note: Make sure every time while creating a resources your "Student-data" resource should selected create this 4 resources under that
   
      - Add-student-data
      - Replace-student-data
      - Update-student-data
      - Delete-student-data
      
11. Select "Add-student-data" resource and Go in "Action" Click on "Create Method" choose option as "POST".
12. Select "Replace-student-data" resource and Go in "Action" Click on "Create Method" choose option as "PUT". 
13. Select "Update-student-data" resource and Go in "Action" Click on "Create Method" choose option as "PATCH".
14. Select "Delete-student-data" resource and Go in "Action" Click on "Create Method" choose option as "DELETE". 

![img7](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/b3bd9e0f-3ebf-4f2c-9f6d-5d45571cc980)

---
B) Launch AWS Lambda Function

1. Search for " AWS Lambda "
2. Click on " Create function "
3. Create Function:
      - Author from scratch:
          - Function Name: ex. post-function
          - Runtime: ex. python 3.10  
4. In same way create more 3 function as name following with runtime python 3.10 
      - patch-function
      - delete-function
      - put-function
      
  ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/90349aa4-1659-499b-80ae-b67674b58063)

---
