import speech_recognition as sr #加载包
r = sr.Recognizer()
with sr.WavFile("D:\\hhhh.wav") as source:  #请把引号内改成你自己的音频文件路径
    audio = r.record(source) 
IBM_USERNAME = 'fa928d54-4210-49c8-989d-b0734c62007c'  
IBM_PASSWORD= 'TkpyJI1H6iaF'  
text = r.recognize_ibm(audio, username = IBM_USERNAME, password = IBM_PASSWORD, language = 'zh-CN')
print(text)
# from aip import AipSpeech

# """ 你的 APPID AK SK """
# APP_ID = '11434936'
# API_KEY = 'Fh1DCbfp1tXhVfhexBqSaEGa'
# SECRET_KEY = 'KFcLexuoYzOyFXywMXNB3neW5yom22wV'

# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# # 读取文件
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# # 识别本地文件
# a = client.asr(get_file_content('D:\\hhhh.wav'), 'pcm', 16000, {
#     'dev_pid': 1536,
# })
# print(a)