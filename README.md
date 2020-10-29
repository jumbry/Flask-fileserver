# Flask-fileserver

 This folder contains code for deploying a simple Flask web fileserver on a virtual machine in
 Google Compute Engine.

 It builds from the sample code for the [Deploying to Google Compute Engine][tutorial-gce] tutorial. 
 
 The original code is at: https://github.com/GoogleCloudPlatform/getting-started-python.git

Please refer to the tutorial for full instructions on configuring, running,
and deploying the sample code. A brief summary for deploying the code from this folder follows:

1. In the Google Cloud Console, select or create a project and note the project ID
2. Enable the Compute Engine API
3. In the Google Cloud Console, open Cloud Shell
4. In Cloud Shell, clone this repository by entering: cloudshell_open --repo_url "https://github.com/jwrbarnes/Flask-fileserver"
5. If you wish, edit deploy.sh to enter your preferred values for MY_INSTANCE_NAME and ZONE
(these values set the name of virtual machine and the datacentre in which it is deployed)
5. In Cloud Shell select your chosen project by entering: gcloud config set project YOUR_PROJECT_ID
6. 


https://cloud.google.com/console/cloudshell/open?git_branch=master&git_repo=https://github.com/jwrbarnes/Flask-fileserver

 [tutorial-gce]: https://cloud.google.com/python/tutorials/getting-started-on-compute-engine
