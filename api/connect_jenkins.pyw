import time
import jenkins

jenkins_server_url='http://10.1.1.100/'
user_id='wangqing'
api_token='ys@123456'
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
server.build_job('10.1.1.99-fk-client-gs')
time.sleep(7)
server.get_job_info('10.1.1.99-fk-client-gs')
build_number=server.get_job_info('10.1.1.99-fk-client-gs')['lastBuild']['number']#获取最后次构建号
print(build_number)

result_state = server.get_build_info('10.1.1.99-fk-client-gs', build_number)['result']#获取构建的执行结果状态
print(result_state)

isbuiding = server.get_build_info('10.1.1.99-fk-client-gs', build_number)['building']#判断是否还在构建中
print(isbuiding)



while isbuiding==True:
    time.sleep(5)
    isbuiding = server.get_build_info('10.1.1.99-fk-client-gs', build_number)['building']
    print(isbuiding)
time.sleep(2)
result_state = server.get_build_info('10.1.1.99-fk-client-gs', build_number)['result']  # 获取构建的执行结果状态
print(result_state)
if result_state=='SUCCESS':
    print(result_state)
    print(1)

