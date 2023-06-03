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
---
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
C) Launch AWS DynamoDB

1. Search for " AWS DynamoDB "
2. Click on "Dashboard" (in left navigation panel)
3. Click on "Create Table"
4. Create Table:
      - Table Details:
          - Table Name: ex. student-database
          - Partition key: ex. rollno (String)  
          - Sort key - optional
          
      - Table Settings:
          - Customzie settings
       
      - Table class:
           - DynamoDB Standard
          
      - Read/write capacity settings:
           - Capacity mode: Provisioned
           - Read capacity: 
                - Auto scaling: Off
                - Provisioned capacity units: 10
           - Write capacity: 
                - Auto scaling: Off
                - Provisioned capacity units: 10
               
![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/12d546ee-0e44-4147-8cc1-b445b2898909)
 
--- 
D) Trigger "API Gateway" with "AWS Lambda"

1. Search and Go on "API Gateway"
2. Click on recently creted api ex. "my-new-api"
3. Select POST method:
    - Setup:
        - Integration type: Lambda Funtion
        - Use Lambda Proxy integration: Enable (check)
        - Lambda region: By default
        - Lambda function: ex. post-function 
        - Use default timeout: Enable
4. Save and OK

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/709a4762-f864-4deb-837d-e3af4aa2d3a3)

5. Do same for other methods (patch,put,delete)
6. Click on "\" 
7. Go in "Action"
8. Select "Deploy API" 
9. Deployment Stage: Choose New Stage
10. Stage name: dev
11. Save

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/986fa7b3-9c05-4697-949d-bcb9b772e094)

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/80477564-09cc-4744-bb5b-07221e5bf672)

---
E) Give "DynamoDB" full access permission to "AWS Lambda"

1. Search for "Lambda"
2. Click on "post-function"
3. Click on "Configuration" (scroll down) 
4. Select "Permissions" 

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/b33feda0-684b-4a44-9ad6-a5fdf29945cd)

5. Click on "Role name" (under Execution Role)
6. Go on "Add Permissions" 
7. Click on "Attach policies"
8. Search for "AmazonDynamoDBFullAccess" and "AWSLambda_FullAccess".
9. Add permission. 

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/ce0479ee-402c-4b93-bc69-940de769a85b)

11. Copy and Paste "post_data_in_db_using_lambda.py" file code
12. Deploy
    - Note: Change table name as per your created table name and change primary key and other key as per your your value.

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/5e9db3ab-9639-4682-b6e8-dabf664aa8bf)

13. Do same for other 3 functions (patch-function,put-function,delete-function).
  
---
F) Log in on Postman (https://www.postman.com/)

 ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/4e5a3d9c-aedf-4582-a0d7-b3276f49f999)

1. Click on "Workspaces" (on left panel)
2. Click on "create workspace"
    - Create workspace:
        - Name: ex. new-space
        - Summary: Optional
        - Visibility: Team   
   
    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/14185d2f-d529-44e8-9a03-69bde6e60158)

3. Click on "New" (on top left corner)
4. Choose "HTTP"

![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/c3842ed8-4997-4ecd-adfc-6811c2d71341)

---
G) Final stage

1. Go on "API Gateway" select your api ex. "my-new-api"
2. Go in POST method copy Invoke URL 

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/1742042f-fb8a-4b91-990e-6e9fddd48bb6)

3. Go in postman select POST method and paste Invoke URL and provide data through Key and Value
    - Note: Your key should match with your code primary key and secondary key

4. Click on "Send"

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/5ec58719-afb8-4fc0-b63d-4730ddf0111b)

5. Go on "DynamoDB" click on created table ex. "student-database" click on "explore table item"

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/121f02e0-fd0c-4273-81ef-dcb6651e7cab)
    
6. Review "item returned"

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/01054638-8aca-4f7d-9924-bf50c8733ab4)

7. Do same for PATCH, PUT, DELETE
8. PATCH
    
    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/556be4f0-2089-4fd8-969b-c1857cb2e3f3)
    
    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/a2075d87-82c5-4486-847b-15d86c89730f)

9. DELETE

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/8e2841e0-2a28-4338-8240-0fae2e946f8f)
    
    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/0c828a06-1b40-4c73-b96f-f51e178ba39b)

10. PUT

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/4b614b1b-8a3f-4736-b58c-ae9fea4f3dae)

    ![image](https://github.com/lokeshwankhede-star-star/Microservices_project/assets/81281161/036457aa-b185-4a73-869b-595f329cd25d)
    
---
    
