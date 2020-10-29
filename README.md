# Flask-fileserver

 This folder contains code for deploying a simple Flask web fileserver on a virtual machine in
 Google Compute Engine.

 It builds from the sample code for the [Deploying to Google Compute Engine][tutorial-gce] tutorial. 
 
 The original code is at: https://github.com/GoogleCloudPlatform/getting-started-python.git

Please refer to the tutorial for full instructions on configuring, running,
and deploying the sample code. 

A brief summary for deploying the code from this folder follows:

1. In the Google Cloud Console, select or create a project and note YOUR_PROJECT_ID
2. Enable the Compute Engine API
3. In the Google Cloud Console, open Cloud Shell
4. In Cloud Shell, clone this repository by entering: cloudshell_open --repo_url "https://github.com/jwrbarnes/Flask-fileserver"
   (steps 3 & 4 can be executed automatically by clicking: https://cloud.google.com/console/cloudshell/open?git_repo=https://github.com/jwrbarnes/Flask-fileserver)
5. If you wish, edit <b>deploy.sh</b> to enter your preferred values for MY_INSTANCE_NAME and ZONE
(these values set the name of the virtual machine and the datacentre in which it is deployed)
6. In Cloud Shell select your chosen project by entering: gcloud config set project YOUR_PROJECT_ID
7. RUN <b>deploy.sh</b> - do we need to make it executable first?
8. <b>deploy.sh</b> creates the new instance, runs <b>startup-script.sh</b> to setup the instance, and opens the firewall to allow access to port 8080
9. the public IP address of the web server can be found in the Compute Engine dashboard

For information, startup-script.sh does the following to setup the instance (using the sample code from the tutorial):
* installs the Stackdriver logging agent to collect logs from syslog so they can be viewed from the Google Cloud dashboard
* installs Python 3 and Pip
* installs Supervisor to run the Python app as a daemon
* installs the Python modules listed in <b>requirements.txt</b>
* configures the Python environment to run in virtualenv 

Configuration for the Python environment is set in <b>python-app.conf</b>

This uses honcho to run the gunicorn web server with the Python code <b>main.py</b> configured in the <b>procfile</b>

main.py uses the Flask framework to provide a simple web fileserver that enables users to:
* upload a file using the url /upload/filename
* list all files that have been uploaded using the url /list
* download a file by clicking the link from /list



 [tutorial-gce]: https://cloud.google.com/python/tutorials/getting-started-on-compute-engine
