# Internship
 * A platform for offering internship programs


0. The web app has 3 register apps accessible in the admin panel. 
    - Internship app
    - Internship auth
    - Internship profile

1. Internship auth
    - The user model is extended. 
    - The registration is through email and password.
    - The users are able to change their credentials
    
2. Internship profile 
   - There are 3 types of profile: Candidate profile and Company Profile, Admin profile(superuser). Also, we have Anonymous user by default
   - Candidate Profile
     
        - is able to update personal information such as: first and last name CV and photo img. 
        - is able to access all register companies and their ads.
        - is able to apply for a certain position
        - is able to apply with his/her uploaded CV оr to upload new one
        - is able to apply multiple times if he or she wants to
        - is able to review his/her applied ads in his/her profile
        - is able to delete his/her profile
        - is able to filter or search ads
        - is able to search companies
     
   - Company Profile
     
      - is able to update company information: logo, web address, phone etc,
      - the company has to complete its profile to be able to create ads.
      - when the company complete the profile it is visible in company catalog view.
      - also is able to create an ads.
      - all company ads are available in Advertisements view as well as in company profile
      - the owner of the ad can create update delete format and deactivate/activate the ad.
      - also, the company has access to all candidates applied for certain position
      - is able to filter or search ads
      - is able to search companies
    
3. Internship app

    - Two models: Internship_add and AppliedTracking
    - the ads are visible for all time of users but only register candidates are able to apply for them
    - International app has relation one to many  to Company Profile
    - AppliedTracing has relation one to many  to Candidate profile ,  International Add
    - Contain when the candidate is applied and the path to his/her CВ
    
Additional functionality

- admin panel
- search 
- filter
- paginator
- bot catcher mixin
- debug toolbar
- profile completion message

Libraries:

asgiref==3.4.1
beautifulsoup4==4.9.3
bootstrap4==0.1.0
Django==3.2.5
django-bootstrap-form==3.4
django-bootstrap4==3.0.1
django-crispy-forms==1.12.0
django-debug-toolbar==3.2.1
django-summernote==0.8.11.6
Pillow==8.3.1
psycopg2==2.9.1
pytz==2021.1
soupsieve==2.2.1
sqlparse==0.4.1


