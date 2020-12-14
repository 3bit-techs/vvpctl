# Ververica Platform Cli (vvpctl)

Cli used to manage Apache Flink® Jobs installed as Ververica Plataform® Deployments through the [Application Manager API](https://docs.ververica.com/user_guide/application_operations/rest_api.html).

**NOTE**: This tool currently only supports [Jar Deployments](https://docs.ververica.com/user_guide/application_operations/deployments/index.html).

## Features

* Delete Deployments
* Declarative way of applying changes on Deployments
* Jar upload to the [Managed Artifact Storage](https://docs.ververica.com/user_guide/application_operations/artifact_management/index.html) (maximum of 50MB) and automatic reference when applying changes
* Drift detection before applying changes
* Automatic old artifacts purge
* Dry run mode
* Automatic Deployment Target creation and reference on the deployment
* Synchronous interactions with the API (waiting for the desired state transition)
* Automatic self-heal a Deployment by cancelling it when the current state is `FAILED`
* Automatic performs a health-check on the deployment after the update/create actions
* Automatic rollback of a Deployment to its previous state (when updating) if the health-check failed or the deployment operation itself failed
* Dumps the installed Deployment json to a file

## Install

```bash
python -m pip install git+https://github.com/3bit-techs/vvpctl.git
```

>Recommended Python version: 3.7+

## Uninstall


```bash
python -m pip uninstall vvpctl
```

## Usage

Example usage:
```bash
vvpctl --server ${VERVERICA_HOST} --apply --file ${PROJECT_NAME}-${GIT_BRANCH}.json --upload ${JAR_FILE} --output target/${PROJECT_NAME}-${GIT_BRANCH}.json --purge --rollback --dry-run
```

Getting help:

```bash
vvpctl -h
```

Example help:

```text
usage: vvpctl [-h] -f FILE -s SERVER [-n NAMESPACE] [-t DEPLOYMENT_TARGET]
              [-a] [-d] [-u UPLOAD] [-r] [-c]
              [--health-check-time HEALTH_CHECK_TIME] [-o OUTPUT]
              [--timeout TIMEOUT] [--dry-run] [--log-level LOG_LEVEL]
              [--purge] [--keep-artifacts KEEP_ARTIFACTS]

Ververica Platform Cli, used to interact with the Application Manager API

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The deployment file
  -s SERVER, --server SERVER
                        The ververica platform server address. E.g:
                        http://localhost:8080
  -n NAMESPACE, --namespace NAMESPACE
                        The ververica platform namespace. Note: This feature
                        is only available in Ververica Platform Stream Edition
                        and above
  -t DEPLOYMENT_TARGET, --deployment-target DEPLOYMENT_TARGET
                        The Deployment target, which corresponds to different
                        Kubernetes namespaces in the same Kubernetes cluster.
                        If the deployment target doesn't exists the cli will
                        attempt to create one
  -a, --apply           Apply a configuration to a deployment
  -d, --delete          Delete a deployment
  -u UPLOAD, --upload UPLOAD
                        Must be used in conjunction with apply, uploads a file
                        to Ververica Platform Artifact Storage (maximum of
                        50MB) and update the deployment with the uploaded file
                        location
  -r, --rollback        Must be used in conjunction with apply, rollback a
                        deployment to its previous state if the update action
                        failed
  -c, --health-check    Performs a health check on the deployment after the
                        update/create action
  --health-check-time HEALTH_CHECK_TIME
                        Used in conjunction with health-check, the length of
                        time in seconds to wait before checking the deployment
                        for a Failing Status
  -o OUTPUT, --output OUTPUT
                        Must be used in conjunction with apply or create,
                        output the installed deployment to disk
  --timeout TIMEOUT     The length of time in seconds to wait before giving up
                        on waiting
  --dry-run             Only simulate actions without submit the request
  --log-level LOG_LEVEL
                        The log level (verbosity), from logging library
  --purge               Used in conjunction with upload, purge old artifacts
                        from artifact storage
  --keep-artifacts KEEP_ARTIFACTS
                        Used in conjunction with purge, specify how many
                        artifacts to keep (from oldest to newest)
```
