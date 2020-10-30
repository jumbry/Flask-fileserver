# Flask-fileserver

 This folder contains code for deploying a simple web fileserver using Python, gunicorn and Flask on a Google Compute Engine instance.

 It builds from the sample code for the [Deploying to Google Compute Engine][tutorial-gce] tutorial. 
 
 The original code is at: https://github.com/GoogleCloudPlatform/getting-started-python.git

Please refer to the tutorial for full instructions on configuring, running, and deploying the sample code. 

A brief summary for deploying the code from this folder follows:

1. In the Google Cloud Console, select or create a project and note YOUR_PROJECT_ID
2. Enable the Compute Engine API https://console.cloud.google.com/flows/enableapi?apiid=compute
(you can usually ignore the subsequent questions about credentials)
3. In the Google Cloud Console, open Cloud Shell
4. In Cloud Shell, clone this repository by entering: cloudshell_open --repo_url "https://github.com/jwrbarnes/Flask-fileserver"

   (steps 3 & 4 can be executed automatically by clicking: https://cloud.google.com/console/cloudshell/open?git_repo=https://github.com/jwrbarnes/Flask-fileserver)
5. If you wish, edit <b>deploy.sh</b> to enter your preferred values for MY_INSTANCE_NAME and ZONE
   (these values set the name of the virtual machine and the datacentre in which it is deployed)
6. In Cloud Shell select your chosen project by entering: gcloud config set project YOUR_PROJECT_ID
7. Make <b>deploy.sh</b> executable by entering the command: chmod +x deploy.sh
8. Run <b>deploy.sh</b> by entering the command: ./deploy.sh
9. <b>deploy.sh</b> creates the new VM instance, runs <b>startup-script.sh</b> to setup the instance, and opens the firewall to allow access to port 8080
10. the public IP address of the web server can be found in the Compute Engine dashboard

For information, <b>startup-script.sh</b> does the following to setup the instance (using the sample code from the tutorial):
* installs the Stackdriver logging agent to collect logs from syslog so they can be viewed from the Google Cloud dashboard
* installs Python 3 and Pip
* installs Supervisor to run the Python app as a daemon
* installs the Python modules listed in <b>requirements.txt</b>
* configures the Python environment to run in virtualenv 

The installation is placed in /opt/app. Configuration for the Python environment is set in <b>python-app.conf</b>

This uses honcho to run the gunicorn web server with the Python code <b>main.py</b> configured in the <b>procfile</b>

<b>main.py</b> uses Flask to provide a simple web fileserver that enables users to:
* upload a file using the url /upload/filename
* list all files that have been uploaded using the url /list
* download a file by clicking the link from /list

<b>Notes:</b> 
* As usual in Flask, <b>main.py</b> uses html templates located in /opt/app/templates
* If you extend <b>main.py</b> to do more (and that's the idea!), remember to add any additional modules to <b>requirements.txt</b> 
and also install them with pip to ensure they are available
* Every time you modify <b>main.py</b>, your changes will not take effect until Supervisor updates to run the Python app. To force this, enter the commands:

supervisorctl reread

supervisorctl update


 [tutorial-gce]: https://cloud.google.com/python/tutorials/getting-started-on-compute-engine
