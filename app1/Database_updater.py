from app1.models import User, Request
import json
import logging
import os


# PATH CONSTANTS
absPath = os.getcwd()
usersPath = os.path.join(absPath, "app1/ProcessManager/Files/")
pathReq = "/Requests/"
pathInProgress = "/InProgress/"
pathFinish = "/Finished/"

# Logging configuration
logging.basicConfig(filename='web_page.log',
                    level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def check_processes():

    try:
        # Update database with the file system
        files_to_delete = []
        for usr_directory in enumerate(os.listdir(usersPath)):
            for files_directory in enumerate(os.listdir(os.path.join((usr_directory, pathInProgress)))):
                for file in enumerate(os.listdir(files_directory)):
                    if os.path.isfile(file):
                        with open(file, 'w') as f:
                            req = json.load(f)
                            try:
                                db_req = Request.objects.filter(id=req['id'])
                                if not db_req.status == 'S':
                                    req['status'] = 'F'
                                    with open(os.path.join(usr_directory, pathFinish, str(req['id'])+'/', str(file)), 'w') as g:
                                        json.dump(req, g)
                                    files_to_delete.append(file)
                            except Request.DoesNotExist:
                                req['status'] = 'E'  # ERROR

            for fi in files_to_delete:
                os.remove(fi)

    except IOError:
        logging.fatal("There was a I/O problem updating the processes of User: " + user.user_name)
