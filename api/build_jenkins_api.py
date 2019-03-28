import flask, json
import jenkins
import time
from tkinter import *
from wsgiref.simple_server import make_server
server = flask.Flask(__name__)  # 实例化server，把当前这个python文件当作一个服务，__name__代表当前这个python文件
@server.route('/index', methods=['get'])  # 'index'是接口路径，methods不写，则默认get请求
# 装饰器，下面的函数变为一个接口

def index():
    #'10.1.1.99-fk-client-gs'
    name = flask.request.values.get('name')
    jenkins_server_url = 'http://10.1.1.100/'
    user_id = 'wangqing'
    api_token = 'ys@123456'
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    last_build_number = server.get_job_info(name)['lastBuild']['number']
    print(last_build_number)
    server.build_job(name)
    now_build_number=last_build_number+1
    time.sleep(10)

    start_result_state = server.get_build_info(name, now_build_number)['result']  # 获取构建的执行结果状态

    print(start_result_state)
    while start_result_state==None:
        time.sleep(2)
        start_result_state = server.get_build_info(name, now_build_number)['result']

    isbuiding = server.get_build_info(name, now_build_number)['building']  # 判断是否还在构建中
    print(isbuiding)
    a=1
    while isbuiding == True:
        time.sleep(5)
        isbuiding = server.get_build_info(name, now_build_number)['building']
        print(isbuiding)
        print('第',a,'次等待')
        a +=1
    time.sleep(2)
    result_state = server.get_build_info(name, now_build_number)['result']  # 获取构建的执行结果状态
    print(result_state)

    if result_state=='SUCCESS':
        res = {'msg': result_state,'build_number':now_build_number, 'msg_code': '0000'}
    else:
        res = {'msg': result_state, 'build_number':now_build_number,'msg_code': '0001'}

    return json.dumps(res, ensure_ascii=False)
    # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False

server.run(port=8888, debug=True, host='10.1.1.187')  # 启动服务
# debug=True,改了代码后，不用重启，它会自动重启
