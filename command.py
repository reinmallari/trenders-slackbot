class Command(object):


    def __init__(self):
        self.commands = { 
            "Hi!" : self.jump,
            "help" : self.help,
        }
 
    def handle_command(self, user, command):
        response = "<@" + user + ">: "
     
        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
        return response
         
    def jump(self):

        response += "Hello! " + user + ". " + self.jump()
        
        print response

    def help(self):
        response = "Currently I support the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response