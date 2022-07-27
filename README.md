For the Love of Food - The food blog
==================================

* * *

ABOUT THE WEBSITE:
------------------

* * * 

[Link to deployed site](https://for-the-love-of-food1.herokuapp.com/)



_For the Love of Food_ is a public online blog-styled platford where users can create a profile and digitalize their own recipes. Users can also view other users recipes, comment, like and favourite them! This interactive platform is designed to provide a a rich online community as users interact with each others recipe posts.

<img src="assets/images/am-i-responsive.png" width="500px">

<img src="assets/images/homescreen.png" width="500px">

* * * 


## TARGET AUDIENCE:

* * *

The beauty of this platform, is that it targets anyone who has ever needed to set food in a kitchen. From the food lovers, to those finding a quick meal fix... "For the Love of Food" serves as your own digitalized cookbook. The advantage - this cookbook never ceases to grow and evolve.

*   Children 13+ (safe to be in a kitchen)
*   Adults

  
* * *

USER STORIES:
-------------

* * *

1. As a Site User I can view a paginated list of posts so that easily select a post to view.
2. As a Site User I can register an account so that I can View, post, comment, favourite and like recipes.
3. As a Site User I can click on a recipe post so that I can view its content.
4. As a Site User I can click the like button on a recipe so that I can like/unlike recipes.
5. As a Site User I can comment on a recipe so that I can interact with the content and other site users.
6. As a Site User I can favourite a recipe so that collect recipes to easily view them on my _Favourites Page_ when needed to.
7. As a Admin User I can create a recipe template so that site users can post their recipes easily.
8. As a Admin User I can Create, Read, Update and Delete recipes so that I can manage the sites content.
9. As a Admin/Site User I can view a list of recipes so that I can browse and select one to read.
10. As a Admin/Site User I can view the number of likes, favourites and posts so that I can track the recipe's popularity.
11. As a Admin User I can create, read, update and delete recipes so that I can manage the blog content.
12. As a user I can click on the favourites so I can view my list of favourite recipes.




* * * 


STRATEGY:
---------

* * *

Create an aesthetically pleasing and easy to navigate open source recipe database. The site is in the style of a Food Blog. It allows users to create their profile, and upload their own recipes from our recipe template. Users can also view and interact with other users recipes: liking, commenting and saving as favourites. Their favourites will all be displayed in their favourites page.


The site will allow for user authentification, and basic CRUD functionality.


The goal is to create a code that is clear and allows you to update with ease. 

* * * 

STRUCTURE:
----------

* * *

### Initial Home Page

* * *


*   LANDING PAGE: This is the page that initially loads when you first arrive at the site. 
    * Navbar: FontAweseom Icon & Home, Register, and Login.
    * Header: "For the Love of Food"
    * Search feature. !!!!!?????
    * You can immeditaley view the paginated list of recipe Posts (authenticated or not).

<img src="assets/images/homescreen.png" width="500px">

*   Depending on wether the user is authenticated and logged in or not navbar may display: 
    * FontAweseom Icon & Home, Register, and Login 
    * FontAweseom Icon & Home, Favourites, and Logout 
  


* * * 

### Recipe Details Page 

* * *

When user clicks a specific Recipe Post:

* Nav Bar and Header continues at the top.
* Recipe Title
* Recipe Category
* Recipe Author, date of publication and time.
* View number of likes, comments and favourotes. User may click on like and favourite button here.
* Recipe Image
* Ingredients
* Instructions
* Comments section below: user may view comments (oldest at the top, scrolling down to newest), and comment posting as user name.


<img src="assets/images/menu.png" width="500px">

* * * 
  
### Favourites Page 

* * *

When clicking favourites, the user can view all their favourite posts.

* NavBar and Header
* Sub-Header "Favourites"
* Paginated list of favourite posts. Similar to the landing home page.

<img src="assets/images/instructions.png" width="500px">

* * * 


### Create Recipe Page

* * *

User can click on "Create Recipe" , which leads them to the following section..

* NavBar and Header
* Sub-Header "Favourites"
* Form to fill out creating recipe.


<img src="assets/images/exit1.png" width="500px">
  



## SKELETON:

-----------

### WIREFRAMES:


* * * 

## THE CODE:

* * *
Prior to commencing to write my code out, I planned out the ERD.

<img src="./static/images/diagram.png" width="1000px">

The User Model ---> Django default User Model. We will use user (PK), Email and Password.

Recipe Model --> Is our main model. It contains all the required fields for our recipe: recipe_id(PK), title, category(FK), slug, author(FK-User), created_on, image, ingredients, directions, likes, favourites, status and user. 


Categories Model --> Containing the categories_id(PK), category field.

Comments Model --> Containing, comment_id(PK), User(FK), recipe_id, body, created_on.

Favourites Model --> Contains favourtites_id, recipe_id, user, likes.


IMPORTANT RELATIONSHIPS BETWEEN TABLES:
* One to many relationship between the User and the Recipe model.
* One to many relationship between the User and the Favouries model.
* One to many relationship between the User and the Comments model.
* One to many relartionships between Category and Recipe's.
* One to many relationships between Recipe and Comments model.


* * * 

## SURFACE

* * *
* When initially planning this site, I knew it would be clean, light and minimalistic. 
* The recipes should read easily, and the pop of color will come from the images and perhaps a few buttons. Most would be in black and white.

* My initial wireframes...

<img src="./assets/images/wireframes-visual.png" width="800px">
<img src="./assets/images/wireframe-grid-size.png" width="260px">

* * *

### Colors

* * *

Mostly white, black, grey and a pop of green in afew buttons. Most of the color will come from the images uploaded by uses. 

<img src="./assets/images/retro-terminal.png" width="800px">


* * * 

### Typography

* * *

Light, spaced, delicate and clean font. 
*  Montserrat
*  Use of letter-spacing



<img src="assets/images/spaces-letters-font.png" width="500px">

### Images and Icons

* * *

Use of a few font-awesome black icons to add some charater.
Still very minimalistic!


<img src="assets/images/grid.png" width="500px">

* * * 

FEATURES:
---------

* * *

### Current features

*   HOME PAGE: (index.html) This is the page that initially loads when you first arrive at the site. 
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * You can immeditaley view the recipes listed. 
    * Without having set up an authenticated user log, the user can view the recipe details. They can just click on the title and will be redirected to the recipe_detail.html page.


  <img src="assets/images/name-1.png" width="500px"> 
  <img src="assets/images/name-2.png" width="500px"> 


*   RECIPE DETAIL: (recipe_detail.html) User can view the recipe details. 
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Recipe Title
    * Recipe Category
    * Recipe author / Created_on date and time
    * Like button (and number of likes), Comments image (and number of comments), favourite button (and number of favourites)
    * Recipe ingredients
    * Recipe Image
    * Recipe instructions
    

 <img src="assets/images/error.png" width="500px"> 

*   REGISTER - (account/signup.html)
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Sign Up Title - and instructions to sign in if you already have an account.
    * Input fields:
        * Username
        * Email (optional)
        * Passoword
        * Passoword (again)
        * Submit button --> Sign Up

 <img src="assets/images/error-2.png" width="500px"> 

 When registered and logged in you will be able to view the following in the nav bar: Home, Favourites, Drafts, Logout, Create Recipe, and the listed recipes.
 Before this you will only see: Home, Register, and Login.

* LOGIN - (account/login.html)
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Sign IN Title - and instructions to register if you haven't already got an account.
    * Input fields:
        * Username
        * Email (optional)
        * Remember me optional checkbox (optional)
        * Submit button --> Sign In

 <img src="assets/images/error-3.png" width="500px"> 

When logged in you will be able to view the following in the nav bar: Home, Favourites, Drafts, Logout, Create Recipe, and the listed recipes.

* LOGOUT - (account/logout.html)
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Sign OUT Title 
    * Message - are yu sure you wnat to sign out?
    * Submit button --> Sign Out

 <img src="assets/images/gameover.png" width="500px"> 
 Once logged out you will only bew able to view: Home, Register, and Login.

* FAVOURITES - (recipe_favourites.html) -> This is the page that will load, from an authenticated logged in user, when clicking on Favourites.
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * You can immeditaley view the favourited recipes by this user. 
    * User cna click onto the recipe title to get the recipe details.

<img src="assets/images/error-4.png" width="500px"> 


* DRAFTS - (recipe_drafts.html) -> This is the page that will load, from an authenticated logged in user, when clicking on Drafts. It will display all the recipes that have not been published yet.
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * You can immeditaley view the drafted recipes by this user. 
    * User can click onto the recipe title to get the recipe details.


<img src="assets/images/error-5.png" width="500px"> 

* CREATE RECIPE - (create_recipe.html) - this is the page where autheticated users can create their own recipe, filling in a simple form.
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Create your Recipe - sub header 
    * Form: fields (title, category, author, ingredients, instructions, image, status)
    * Post button.


<img src="assets/images/error-6.png" width="500px"> 


* EDIT RECIPE - (update_recipe.html) - this is the page where autheticated users can edit their own recipe, filling in a simple form. User can only edit the posts they created!
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Edit your Recipe - sub header 
    * Form: fields (title, category, author, ingredients, instructions, image, status)
    * Post button.
    * Delete recipe button
    
<img src="assets/images/round-3.png" width="500px"> 
    

* DELETE RECIPE - (delete_recipe.html) - this is the page where autheticated users can delet their own recipe. User can only delete the posts they created! This pops up after clicking on the delete this post button on the edit_recipe.html
    * Navbar: FontAweseom Icon & Home, Register, and Login
    * Header: "For the Love of Food"
    * Delete your Recipe - sub header 
    * Security: are you sure you want to delete this recipe?
    * Delete button.


<img src="assets/images/final-score.png" width="500px"> 


* * * 

### Future features

* Prepopulated author of recipe = authenticated user name. This prevents the user to be able to use someone else's name as author. 
* When creating recipe, the user can either input the category or sleect one from the dropdown menu. At the moment the user is limited to selecting from a limited amount.


* * * 

## LANGUAGES:

* * *

*   PYTHON
*   CSS
*   HTML
*   JavaScript


* * * 

## OTHER TECHNOLOGIES, FRAMEWORKS & LIBRARIES:


* * *

*   [Django](https://www.djangoproject.com/
*   [GitHub](https://github.com/)
*   [GitPod](https://www.gitpod.io/)
*   [Heroku](https://id.heroku.com/login)
*   [Stack Overflow](https://stackoverflow.com/)
*   [Code beautify](https://codebeautify.org/html-to-markdown)
*   [Balsamiq](https://balsamiq.com/wireframes/desktop/#)
*   [Pep8](http://pep8online.com/)
*   [Cloudinary](https://cloudinary.com/)
*   [PostgreSQL](https://www.postgresql.org/)
*   [Bootstrap](https://getbootstrap.com/)



* * * 

## TESTING, BUGS & FIXES:


* * *

For testing I used the following sources:

* * * 

### Tests

* * *

#### [Pep8](http://pep8online.com/)

Tested and no errors found.

<img src="assets/images/no-errors.png" width="800px">

* * *

#### Manual testing 

* * * 

Testing this site manually was a long and very detailed process. No errors were found.

* * *




* * * 


###### BUGS & FIXES: 

* 

* * * 

#### Unresolved bug 

* * * 
I would like to resolve the following issue. 

* CSS styling not loading in my deployed heroku app.
* When a user creates a recipe, they have the option of selecting any author. This is not good user experience. The author should automatically be pre-filled as the verified authenticated user. This allows for more issues. For example: if the user accidentally creates a post using the ertong authot name, they no longer have the ability to edit/delete this post.
* When creating recipe, the user can only select an option from a dropdown meny that has been preset. They cannot add their own category (in the case that they needed to).

<img src="assets/images/victory-bug.png" width="200px">


* * * 

#### Testing User Stories 

* * * 

1. As a Site User I can view a paginated list of posts so that easily select a post to view.


2. As a Site User I can register an account so that I can View, post, comment, favourite and like recipes.


3. As a Site User I can click on a recipe post so that I can view its content.


4. As a Site User I can click the like button on a recipe so that I can like/unlike recipes.


5. As a Site User I can comment on a recipe so that I can interact with the content and other site users.


6. As a Site User I can favourite a recipe so that collect recipes to easily view them on my _Favourites Page_ when needed to.


7. As a Admin User I can create a recipe template so that site users can post their recipes easily.


8. As a Admin User I can Create, Read, Update and Delete recipes so that I can manage the sites content.


9. As a Admin/Site User I can view a list of recipes so that I can browse and select one to read.


10. As a Admin/Site User I can view the number of likes, favourites and posts so that I can track the recipe's popularity.


11. As a Admin User I can create, read, update and delete recipes so that I can manage the blog content.


12. As a user I can click on the favourites so I can view my list of favourite recipes.

* * *

## DEPLOYMENT:

* * *

### Forking The GitHub Repository

* * *

You can Fork the Repository. This makes a copy of the original repository on our Github account so you can make changes without affecting the original repository.
1. Log into GitHub and locate the GitHub repository you want.
2. Click on the "Fork" button which is located in the top right corner.
3. You will now have a copy of the original repository in your GitHub account.

* * * 

### Cloning the Project.
* * *
1. Log into GitHub and locate the GitHub repository you want.
2. Under the repository name, click "Code" button which will come up with a dropdown menu.
3. Where it says Clone, copy the link below.

* * * 


### Using Code Institute's mock terminal for Heroku

* * *

This site was deployed using the following steps:

1. Make sure that the project has been created using Code Institute Python template.
2. Make sure all python scripts have a new line character at the end of the text inside.
3. With installing packages type in command: 'pip3 freeze > requirements.txt'. This will allow them to work in Heroku, and the Code Institute template will be updated automatically.
4. Commit and push changes to GitHub
5. Create Heroku Account
6. In Heroku dashboard: go to Create new app.
7. Give your app a unique name
8. Select region
9. Click create App.
10. Go to the Settings tab, scroll down to Config Vars and select Reveal Config Vars.
11. Confid Vars enter:
    1. Key: PORT
    2. Value: 8000
12. Go to Buildpacks and click Add Buildpack.
13. Select Python and save changes.
14. Add NodeJS and save changes (Python on top and NodeJS below. You can drag the to re-order)
15. Scroll to Deploy Tab, select Github and confirm Connect to Github.
16. Search for your repository and click Connect.
17. Select Deploy Branch and deploy in master/main.
18. Your deployed app is live!

[Link to deployed site](https://battlefields-blast.herokuapp.com/)

* * *


CREDITS: 
--------

* * *

### Content & Code
* A couple of the code institute tutors helped me with some issues I was having. 
    * I encountered a bug: When finishing a game and wanting to launch game again, my X's and -'s remained displayed on the board. Sean from Code Institute helped me solve this, and suggested I use the following code:
    
    <img src="assets/images/sean-bug.png" width="1000px">
    <img src="assets/images/sean-bug-2.png" width="1000px">

* Coming up with how to create my grid was a challenge! After brainstorming, I researched a few different ways people had achieved this. Some of the tutorials I looked at:
    * [Code Academy](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605)
    * [Python for begginers](https://bigmonty12.github.io/battleship)       
    * [Stack Exchange](https://codereview.stackexchange.com/questions/122970/python-simple-battleship-game)
* My peers at Code Institute Slack were also incredibly helpful!
* My mentor Chris helped me better understand how to best validate my code.


       




