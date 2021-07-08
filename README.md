
*** README and demo for COSC3506 - STAFFCHAT ***
*** Written by Paul Wilson on July 7, 2021   ***


To run the server:

	(1) $ pip install flask

	(2) $ pip install jsonpickle

	(3) $ python ServerMain.py

you may want to delete the ./database/server_database.txt file to start another database from scratch -- if not, the server database will be loaded from the file. 


Try creating a ClientNode object to interact with the server. In a new Command line window:

	(1) $ python

	(2) >>> from ClientNode import ClientNode

	(3) >>> node = ClientNode( "**paste home address of server**", "**your_name**", "**your_password**")

	(4) >>> node.register_user()

	True

	(5) >>> node.login()			#remember to logout later!

	True

Now create another user. You can do this on a different terminal window, even on a different computer as long as they are on the same wi-fi network as the server!

	(6) >>> node2 = ClientNode( "**paste home address of server**", "**second_name**", "**your_password**")

	(7) >>> node2.register_user()

	(8) >>> node2.login()

Now, you can create a message object and send it from one user to the other:

	(9) >>> from Message import Message

	(10) >>> m = Message(sender = '**your_name**', recipients = ['**second_name**'], content = 'hello')

	(11) >>> node.send_message(m)

If it is successful, it will print true. Then, you can see it by checking the second node's inbox!

	(12) >>> node2.get_inbox()

This is the end of the demo for now

	(13) >>> node.logout()

	(14) >>> node2.logout()

I encourage everyone to read through the documentation of the ClientNode class. This class will be the connection between the GUI and the backend.












