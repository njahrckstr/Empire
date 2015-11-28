

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Invoke-SSHCommand',

            'Author': ['@424f424f'],

            'Description': ('Executes a command on a remote host via SSH.'),

            'Background' : True,

            'OutputExtension' : None,
            
            'NeedsAdmin' : False,

            'OpsecSafe' : True,

            'MinPSVersion' : '2',
            
            'Comments': [
                'Open Source is the Best Source'
            ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'IP' : {
                'Description'   :   'Address of the target server.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Username' : {
                'Description'   :   'The username to login with.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Password' : {
                'Description'   :   'The password to login with.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Command' : {
                'Description'   :   'The command to run on the remote host.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }
        # save off a copy of the mainMenu object to access external functionality
        #   like listeners/agent handlers/etc.
        self.mainMenu = mainMenu

        for param in params:
            # parameter format is [Name, Value]
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value

    def generate(self):

        moduleSource = self.mainMenu.stagers.installPath + "/data/module_source/lateral_movement/Invoke-SSHCommand.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode

        script += "\nInvoke-SSHCommand"

        return script