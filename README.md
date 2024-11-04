## Request For questions (RFQ) System:-
- ### Introduction:-
  The RFQ (Request For Quotation) system we're building is a web application that facilitates the quotation process between clients and vendors. In this system:
    - **Clients** can manage a list of items they need.
    - Clients can create an **RFQ** by selecting one or more items from their list.
    - **Vendors** can view these RFQs and submit quotations for them.
    - Clients can review the quotations and approve the one with the lowest estimate.
    
- ### Installation
   1. Clone the Repository by run this command 
       ```
        git clone https://github.com/shantiNaser/RFQ_system.git
        cd RFQ_system
       ```
   2. Build and Start the Docker Containers
        ```
        docker-compose up --build
       ```
   3. Open another terminal window and Generate the Migration Files
        ```
        docker-compose exec web python manage.py makemigrations
       ```
   4. Apply Migrations to Set Up the Database Schema
        ```
        docker-compose exec web python manage.py migrate
       ```
   5. Access the Application
        ```
        http://localhost:8000/
       ```
   #### **Congratulations!, Your Django application should now be running.**
  
   
   ### Important Notes:
    - Database: The application uses SQLite as the database, which is included in the repository.
    - Virtual Environment: The virtual environment (venv) is already created and included in the repository, so you don't need to create one.
    
   ### In Order to use the website you can create a new users
   There's two types of users Client, Vendor

   ### explain page in the system
    - **Login Page**

      <img width="913" alt="Screenshot 2024-11-03 at 8 17 34 PM" src="https://github.com/user-attachments/assets/d8ea6a54-1eb1-407c-8cd3-e00ce54b5127">
 
    - **Registration Page**

      <img width="1087" alt="Screenshot 2024-11-03 at 8 17 40 PM" src="https://github.com/user-attachments/assets/3d0a8cf6-2a8e-49d2-a1e5-3233fd772778">


    - **Client user page**

        - **Home Page**

          <img width="723" alt="Screenshot 2024-11-03 at 8 01 49 PM" src="https://github.com/user-attachments/assets/51db9698-d273-43cd-9492-b4dc44482c73">

        - **RFQs Page**

          <img width="560" alt="image" src="https://github.com/user-attachments/assets/dcaab2d8-b1a7-4423-8dd8-9695f0fbd8f1">

        - **RFQ detail**

          <img width="823" alt="Screenshot 2024-11-03 at 8 08 24 PM" src="https://github.com/user-attachments/assets/df322bcf-9835-494f-a706-a26d8deeaa61">


    - **Vendor user page**

        - **Home Page**

          <img width="714" alt="Screenshot 2024-11-03 at 8 11 40 PM" src="https://github.com/user-attachments/assets/fb9eb143-4b16-4361-a005-dcf8ad93e441">

        - **Approved RFQ for this user**

          <img width="574" alt="Screenshot 2024-11-03 at 8 13 20 PM" src="https://github.com/user-attachments/assets/1b14198c-8fa2-4642-a25e-b57bb720a258">





        
       
    
       

    
