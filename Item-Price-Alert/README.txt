This is a README file for Item-Price-Alert

This program is a Python web application that allows users to track the prices of items from websites.
It then sends out users an alert if the price point they desire is reached for that item.


Some currently known problems with this program:

-Currently if there are discrepencies between the _id of items and alerts in the DB program will throw a NoneType error.
  *This can be solved by checking for nonetype or discprencies, and if there is one to send user to add new alert.
  
-Program is asking technical data from user, which is not ideal.
  *Change the way the data is collected from the user, using a different method on obtaining the information from websites.
  Exploring the options on how to do this.
  
-The program does not work if there is javascript dynamically altering the price of an item after page construction
  *There is a way to obtain the price if this is the case, but it would need to be approached differently.
  
-After the creation of an item in our DB we lose the item ID so we lose the ability to send it to our alerts in DB

-The point of the program currently is to add things into the program, when really the point the user wants to use it for is to
get things out of the program.
  *We need to ask the user what item it is they want, for what price they want the item. And for the program to do the rest.
  We need to consolidate our two forms into one, and not require the user to know our database IDS which are hidden. We can accomplish they
  by not allowing the user to create items and instead only be able to create alerts. Stores will be added to the application, we will
  save the store alongside the rest of the information associated to that store, and then use that store's tag_name and query to access
  the information.
