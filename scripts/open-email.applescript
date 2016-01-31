-------------------------------------------------------------------------------
-- Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
-- Released under the [MIT License] (http://opensource.org/licenses/MIT)
-------------------------------------------------------------------------------

on openEmail(myRecipients)
	set mySender to "Ben Blazak <bblazak@fullerton.edu>"
	set mySubject to "[CPSC 121] "
	
	set myContent to "Dear class,



Sincerely,
Ben Blazak"
	
	tell application "Mail"
		set myMessage to make new outgoing message with properties Â
			{visible:true, subject:mySubject, content:myContent, sender:mySender}
		
		tell myMessage
			repeat with myRecipient in myRecipients
				make new bcc recipient at beginning of bcc recipients with properties Â
					{name:name of myRecipient, address:email in myRecipient}
			end repeat
		end tell
	end tell
end openEmail