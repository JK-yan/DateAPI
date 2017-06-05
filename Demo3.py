import paramiko


# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('192.168.1.41', 1022, username='fulihui', password='p@ssw0rd', timeout=6)
# stdin, stdout, stderr = client.exec_command('ls -l')
# for std in stdout.readlines():
#   print (std)
# client.close()






def connect(hostname='192.168.1.41', port=1022, username='fulihui', password='p@ssw0rd', timeout=6):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, port=port, username=username, password=password, timeout=timeout)
    except Exception as  e:
        print('Error is:' + str(e))
        exit()
    return client


def ssh_exec_cmd(client, _cmd):
    return client.exec_command(_cmd)


def ssh_close(client):
    client.close()


if __name__ == '__main__':
    ssh = connect()
    stdin, stdout, stderr = ssh_exec_cmd(ssh, 'ls')
    # print(stdin.readlines())
    with open(stdin, mode='r') as a:
        for i in a.readlines():
            print(i)
    err_list = stderr.readlines()
    if len(err_list) > 0:
        print('ERROR:' + err_list[0])
        exit()
    for std in stdout.readlines():
        print(std)
