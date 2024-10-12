# IBBS - Web Application Metrics

## Overview
The International Billfish Biosampling System (IBBS) Web Application Metrics (WAM) project was developed to provide an automated method to capture performance metrics from the user perspective for a suite of web actions on the IBBS web app.  The IBBS WAM project can be executed in a variety of scenarios for flexibility.  This project is forked from the [Web App Metrics](https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics) and customized for the IBBS web app.  

## Resources
-   IBBS WAM Version Control Information:
    -   URL: https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics-IBBS.git
    -   Version: 1.5 (Git tag: ibbs_web_app_metrics_v1.5)
    -   Forked repository (upstream)
        -   [Web App Metrics README](https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics/blob/main/README.md)
        -   WAM Version Control Information:
            -   URL: git@github.com:noaa-pifsc/PIFSC-Tools-Web-App-Metrics.git
            -   Version: 1.4 (Git tag: web_app_metrics_v1.4)
-   [Detailed/Summary performance metrics](https://docs.google.com/spreadsheets/d/1oDtnMyg9SosxHOoiq4af35_TU_-7dZyE/edit?usp=drive_link&ouid=107579489323446884981&rtpof=true&sd=true)
    -   During the testing window the local/hybrid projects were configured to run on an hourly basis each weekday for 12 hours (7 AM to 7 PM HST)
    -   The [ibbs-web-app-metrics tab](https://docs.google.com/spreadsheets/d/1oDtnMyg9SosxHOoiq4af35_TU_-7dZyE/edit?gid=2021517478#gid=2021517478) contains the detailed information for each web action and the corresponding metrics that were captured
    -   The [Summary tab](https://docs.google.com/spreadsheets/d/1oDtnMyg9SosxHOoiq4af35_TU_-7dZyE/edit?gid=1590693321#gid=1590693321) contains the summarized information with comparisons between the different scenarios

## Scenarios
-   There are multiple scenarios implemented by the docker project:
    -   Local - this scenario deploys the docker container to a local docker host and connects to a local web app in the following network configurations:
        -   PIFSC Ethernet
        -   Pacific VPN
    -   Remote - this scenario deploys the docker container to a remote docker host and connects to a remote web app in the following network configurations:
        -   FishSTOC network
    -   Hybrid - this scenario deploys the docker container to a local docker host and connects to a remote web app in the following network configurations:
        -   PIFSC Ethernet
        -   Pacific VPN
        -   East Coast VPN
        -   West Coast VPN
-   Each scenario has its own set of files used to specify the configuration during the [preparation process](#prepare-the-docker-container)
    -   Configuration files:
        -   Bash script configuration (e.g. [project_scenario_config.pifsc-ethernet.local.sh](./docker/src/sh_scripts/config/project_scenario_config.pifsc-ethernet.local.sh) for the PIFSC Ethernet network/local database scenario)
        -   Python configuration (e.g. [project_scenario_config.pacific-vpn.hybrid.py](./docker/src/py_scripts/lib/project_scenario_config.pacific-vpn.hybrid.py) for the Pacific VPN network/hybrid scenario)
    -   deployment script (e.g. [prepare_docker_project.fishstoc.remote.sh](./deployment_scripts/prepare_docker_project.fishstoc.remote.sh) for the FishSTOC network/remote web app scenario)
        -   The deployment script prepares the working directory for the docker container and renames the corresponding configuration files to make them active

## Setup Procedure
-   ### Web App Setup
    -   Create a user account on the IBBS authentication system that will be used to execute the web actions
        -   FishSTOC test IBBS web application
            -   Login to the [test IBBS web application](https://test-apps-st.fisheries.noaa.gov/foss/f?p=ibbs) with an account that has been granted the IBBS_ADMIN role in the CAM system
            -   Follow the [IBBS CAM Management Instructions](https://drive.google.com/file/d/1G-8IMLQPQMra2R8DBzgqSwWG6VW5NFA3/view?usp=drive_link) to create a user account with permissions to login to the test IBBS web application
        -   PIFSC development IBBS web application
            -   Create an APEX user account on the LHP_INTL_BIO_APP workspace on the PICMIDD server
    -   Create a user account on the IBBS authorization system that will be used to execute the web actions
        -   Login to the appropriate IBBS web application with an account that has been granted to DATA_ADMIN role
        -   In the navigation menu click on Admin -> Authorization -> Auth Users
        -   Create a User record with the with the same username as the user's authentication record
            -   Add two groups for the new user: "DATA_WRITE" and "US"
-   ### Linux
    -   #### Clone the repository
        ```
        # clone the repository into a working directory that will be used to prepare the container for execution:
        git clone https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics-IBBS.git
        ```
    -   #### Prepare the docker container
        -   Set the \$base_docker_directory bash/environment variables to define the base directory location where the docker application will be built and executed
            ```
            # define the $base_docker_directory variable (e.g. /home/webd/docker) to make it easy to execute the preparation and deployment bash scripts:
            base_docker_directory="[PATH TO PREPARATION FOLDER]"

            # define the value of $base_docker_directory as an environment variable
            export base_docker_directory
            ```
        -   Execute the preparation bash script:
            ```
            # execute the preparation script (in this example the FishSTOC network/remote web app scenario):
            bash ./PIFSC-Tools-Web-App-Metrics-IBBS/deployment_scripts/prepare_docker_project.fishstoc.remote.sh
            ```
        -   press the "Enter" key to dismiss the bash script message
    -   #### Specify the web app credentials
        -   In the preparation folder update the login_credentials.py file (e.g. **$base_docker_directory**/ibbs-web-app-metrics-fishstoc-remote/docker/src/py_scripts/lib/login_credentials.py for the FishSTOC network/remote web app scenario)
            -   Specify the web login credentials for the user created in the [Web App Setup](#web-app-setup) procedure
        -   The code below is used for the remote scenario to edit the login_credentials.py configuration file:
            ```
            vim $base_docker_directory/ibbs-web-app-metrics-fishstoc-remote/docker/src/py_scripts/lib/login_credentials.py
            ```
-   ### Windows
    -   #### Clone the repository
        ```
        # clone the repository into a working directory that will be used to prepare the container for execution:
        git clone https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics-IBBS.git
        ```
        -   \*Note: The links in this documentation will work if you are viewing this README from the working directory
    -   #### Prepare the docker container
        -   Execute the appropriate docker preparation script stored in the [deployment_scripts](./deployment_scripts) folder to prepare the docker container for deployment in a new preparation folder
            -   For example use the [prepare_docker_project.remote.sh](./deployment_scripts/prepare_docker_project.fishstoc.remote.sh) bash script to prepare the docker container for deployment in the FishSTOC network/remote web app scenario
        -   When prompted specify the base directory where the project will be prepared (e.g. /c/docker for Windows), this will set the value of **$base_docker_directory** used within the preparation script
        -   The preparation script will clone the project into a new preparation folder based on the value of **$base_docker_directory** (e.g. **$base_docker_directory**/ibbs-web-app-metrics-fishstoc-remote preparation folder for the FishSTOC network/remote web app scenario) and configure the docker project
        -   This preparation folder will be used to build and execute the docker container
    -   #### Specify the web app credentials
        -   In the preparation folder update the login_credentials.py file (e.g. **$base_docker_directory**/ibbs-web-app-metrics-fishstoc-remote/docker/src/py_scripts/lib/login_credentials.py for the FishSTOC network/remote web app scenario)
            -   Specify the web login credentials for the user created in the [Web App Setup](#web-app-setup) procedure
-   \*Note: more information about the setup procedure for this forked project is available in the [Web App Metrics README](https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics/blob/main/README.md#forked-repository-implementation)

## Building/Running Container
-   In the preparation folder execute the appropriate build and deploy script for the given scenario
    -   ### Linux
        -   On Linux this bash script can be used to automate the execution of the docker container on a timer using cron
            ```
            # execute the build/deploy script (in this example the FishSTOC network/remote web app scenario)
            bash $base_docker_directory/ibbs-web-app-metrics-fishstoc-remote/deployment_scripts/build_deploy_project.sh
            ```
    -   ### Windows
        -   On Windows the batch script can be used to automate the execution of the docker container on a timer using Scheduled Tasks (e.g. **$base_docker_directory**/ibbs-web-app-metrics-fishstoc-remote/deployment_scripts/build_deploy_project.bat for the remote scenario)

## Docker Application Processing
-   \*Note: more information about the docker application processing for this forked project is available in the [Web App Metrics README](https://github.com/noaa-pifsc/PIFSC-Tools-Web-App-Metrics/blob/main/README.md#docker-application-processing)

## Checking Results
-   Open the docker volume ibbs-web-app-metrics-logs to view the log files for the different executions of the docker container
    -   The log files will have the following names: query_metrics_log_YYYYMMDD.log with the date in the UTC timezone (e.g. query_metrics_log_20241007.log for a script that began running on 10/7/2024 in the UTC timezone)
-   Open the docker volume ibbs-web-app-metrics-data to view the exported data files for the different queries
    -   Open the ibbs_web_performance_metrics.csv to view the metrics that were captured for each query execution

## Standard Metrics/Information Logging
-   The following metrics and information is captured for each web action in a .csv file:
    -   App Name - The name of the application (IBBS APEX app)
    -   Metrics App Location - is the location of the IBBS WAM docker container (local or remote)
    -   Web App Location - is the location of the IBBS web application (local or remote)
    -   Network - is the network configuration for the docker container (e.g. PIFSC Ethernet, FishSTOC, Pacific VPN, etc.)
    -   Date/Time (UTC) - The Date/Time the given web action was started in the UTC time zone in MM/DD/YYYY HH:MI:SS AM/PM format
    -   Date/Time (HST) - The Date/Time the given web action was started in the Hawaii Standard time zone in MM/DD/YYYY HH:MI:SS AM/PM format
    -   Page Name - The page the web action was executed on
    -   Action - The type of web action
    -   \# Files - The total number of web resource files (e.g. image, css, JavaScript file, etc.) downloaded for the given web action
    -   Total File Size (KB) - The total size in kilobytes of the web resource files downloaded for the given web action
    -   Total Response Time (s) - The total number of seconds for the web action to complete and the app is ready to accept user interactions
    -   Screenshot File - the name of the screenshot file saved in the data volume for the given web action

## Implemented Web Actions
1.  Load Login Page
2.  Login to web application/Load Full Sampling Report Page
3.  Update the Region select element to filter the Full Sampling Report Page
4.  Open the View All Specimens Page
5.  Open the View/Edit Specimen Page
6.  Submit the specimen form to create a new record
7.  Submit the specimen form to update an existing record
8.  Download the specimen .csv file
9. Load Regional Sampling Charts
10. Filter/Reload Regional Sampling Charts

## License
See the [LICENSE.md](./LICENSE.md) for details

## Disclaimer
This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code is provided on an ‘as is’ basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.
