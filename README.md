## Request For questions (RFQ) System:-
- ####Introduction:-
  The RFQ (Request For Quotation) system we're building is a web application that facilitates the quotation process between clients and vendors. In this system:
    - **Clients** can manage a list of items they need.
    - Clients can create an **RFQ** by selecting one or more items from their list.
    - **Vendors** can view these RFQs and submit quotations for them.
    - Clients can review the quotations and approve the one with the lowest estimate.
    
- ####Installation
   1. Clone the Repository by run this command 
       ```
        git clone https://github.com/shantiNaser/RFQ_system.git
        cd RFQ_system
       ```
   2. Run the Application with Docker Compose
        ```
        docker-compose up
       ```
   3. Access the Application
        ```
        http://localhost:8000/
       ```
   #### **Congratulations!, Your Django application should now be running.**
   
   #### Important Notes:
    - Database: The application uses SQLite as the database, which is included in the repository.
    - Virtual Environment: The virtual environment (venv) is already created and included in the repository, so you don't need to create one.
    
   #### In Order to use the website you can create a new user or just use the existing one that stored in the sqllite database
    - Client User
       - username:- client
       - password:- client123456
   - vendor User1
       - username:- vendor
       - password:- vendor123456
   - vendor User2:-
       - username:- NaserVendor
       - password:- naser123456789
       
   #### How you can use the application
       
    
       

    