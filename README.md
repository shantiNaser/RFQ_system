## Request For questions (RFQ) System:-
- #### Introduction:-
  The RFQ (Request For Quotation) system we're building is a web application that facilitates the quotation process between clients and vendors. In this system:
    - **Clients** can manage a list of items they need.
    - Clients can create an **RFQ** by selecting one or more items from their list.
    - **Vendors** can view these RFQs and submit quotations for them.
    - Clients can review the quotations and approve the one with the lowest estimate.
    
- #### Installation
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
    - Client user page 

        - Home Page

          <img width="723" alt="Screenshot 2024-11-03 at 8 01 49 PM" src="https://github.com/user-attachments/assets/51db9698-d273-43cd-9492-b4dc44482c73">

        - RFQs Page

          <img width="560" alt="image" src="https://github.com/user-attachments/assets/dcaab2d8-b1a7-4423-8dd8-9695f0fbd8f1">

        - RFQ detail

          <img width="823" alt="Screenshot 2024-11-03 at 8 08 24 PM" src="https://github.com/user-attachments/assets/df322bcf-9835-494f-a706-a26d8deeaa61">


    - Vendor user page

        - Home Page

          <img width="714" alt="Screenshot 2024-11-03 at 8 11 40 PM" src="https://github.com/user-attachments/assets/fb9eb143-4b16-4361-a005-dcf8ad93e441">

        - Approved RFQ for this user

          <img width="574" alt="Screenshot 2024-11-03 at 8 13 20 PM" src="https://github.com/user-attachments/assets/1b14198c-8fa2-4642-a25e-b57bb720a258">





        
       
    
       

    
