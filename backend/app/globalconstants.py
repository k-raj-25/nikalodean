import os


current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

ques_path = "{}/static/sys/qa.json".format(current_path)
fun_msg_path = "{}/static/sys/mm.json".format(current_path)