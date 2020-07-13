# Bry Power Lab 3

 The following is this lab 3 app functionality broken up by available routes. 
 The app can be found here: https://tranquil-ridge-26786.herokuapp.com/

- / : view a list of all users
- /adduser : add a new user. Navigate by clicking "add new user" button on the bottom on the index page
- /adduser/{first_name}/{age} : add a user using url get parameters.
- '/user/{id}' : view a single user. Navigate here by clicking any users name in the index page.
- '/confirm/<action>/{id}' : return a page for the user to confirm they want to perform an action on a specific user, such as delete. Used when a user clicks 'delete' next to a user on the index page.
- '/user/delete/{id}' : Delete a user with the specified id. Can only be called by clicking to confirm the delete on the confirmation page.
- '/user/edit/{id}' : Edit a user with the specified id. Navigate here by clicking edit next to a user on the index page.
- '/seed/{rows}' : Create the specified number of rows, populated with mock data, in the users table.