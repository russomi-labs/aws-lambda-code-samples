import json
import subprocess
import os


def lambda_handler(event, context):

    # Get current working directory
    print("Lambda's default working directory: ")
    print(os.environ['LAMBDA_TASK_ROOT'])

    # Switch to /tmp dir, list its contents and total size of it
    os.chdir('/tmp')

    print(f"/tmp contents: {os.listdir('/tmp')}")
    print("\n")
    ######################
    # Get size of /tmp directory in MBs
    statvfs = os.statvfs('.')

    # Size of filesystem in bytes
    print(f"Size of filesystem in MegaBytes: {statvfs.f_frsize * statvfs.f_blocks/(1024*1024)}")

    # Actual number of free bytes
    print(f"Actual number of free MegaBytes: {statvfs.f_frsize * statvfs.f_bfree/(1024*1024)}")

    # Number of free bytes
    print(f"Number of free MegaBytes: {statvfs.f_frsize * statvfs.f_bavail/(1024*1024)}")
    ######################

    print("\n")
    # Get more info about the underlying processor
    print("cat /etc/os-release: ")
    print(subprocess.check_output(['cat', '/etc/os-release']).decode("utf-8"))

    print("uname -a: ")
    print(subprocess.check_output(['uname', '-a']).decode("utf-8"))

    print("\n")

    print("cat /proc/cpuinfo: ")
    print(subprocess.check_output(["cat", "/proc/cpuinfo"]).decode("utf-8"))

    return {
        'statusCode': 200,
        'body': json.dumps("Completed execution.")
    }
