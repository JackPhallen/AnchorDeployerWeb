import os
import subprocess


def deploy(cluster_name, region, max_nodes, min_nodes, projet_name):
    wd = os.getcwd()
    process = subprocess.run(["./cloud-helm-charts/master-script.sh", cluster_name, region, max_nodes, min_nodes, projet_name])
    print("test")
    return process.returncode == 0


def getip(cluster_name):
    process = subprocess.check_output(["./cloud-helm-charts/get-ip.sh", cluster_name])
    if process.returncode == 0:
        return str(process, 'utf-8').splitlines()[-1]
    else:
        return None


def check(cluster_name, region, max_nodes, min_nodes, projet_name):
    output = {}
    exit_codes = []

    check1_process = subprocess.run(["./cloud-helm-charts/cluster_status.sh", cluster_name, region])
    exit_codes.append(check1_process.returncode == 0)

    check2_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-BackendServices.sh")
    exit_codes.append(check2_process.returncode == 0)

    check3_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-Certs.sh")
    exit_codes.append(check3_process.returncode == 0)

    check4_process = subprocess.run("./cloud-helm-charts/HealthCheck-07-OtherServices.sh")
    exit_codes.append(check4_process.returncode == 0)

    output['result'] = exit_codes
    return output


if __name__ == "__main__":
    deploy("test", "test", "0", "0", "test")
    print("test")