import os
import subprocess


def deploy(cluster_name, region, max_nodes, min_nodes, projet_name):
    process = subprocess.run(["./cloud-helm-charts/master-script.sh", cluster_name, region, max_nodes, min_nodes, projet_name])
    return process.returncode == 0


def getip(cluster_name):
    try:
        process = subprocess.check_output(["./cloud-helm-charts/get-ip.sh", cluster_name])
        return str(process, 'utf-8').splitlines()[-1]
    except:
        return None


def check(cluster_name, region, max_nodes, min_nodes, projet_name):
    output = {}
    exit_codes = []

    check1_process = subprocess.run(["./cloud-helm-charts/cluster-status.sh", cluster_name, region])
    exit_codes.append(check1_process.returncode == 0)

    check2_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-BackendServices.sh")
    exit_codes.append(check2_process.returncode == 0)

    check3_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-Certs.sh")
    exit_codes.append(check3_process.returncode == 0)

    check4_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-OtherServices.sh")
    exit_codes.append(check4_process.returncode == 0)

    output['result'] = exit_codes
    return output
