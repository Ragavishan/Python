import sys
def cli_parser(command):
    switcher={
            'start':"starting the program",
            'stop':"stoping the program",
            'restart':"restarting the program"
            }
    return switcher.get(command,"unknown command")
if len(sys.argv)>1:
    print(cli_parser(sys.argv[1]))
else:
    print("No command provided")