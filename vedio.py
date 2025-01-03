import librosa
from aip import AipSpeech
import os
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image


def get_audio(text, audio_path):
    global APP_ID
    global API_KEY
    global SECRET_KEY
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)  # 配置百度语音客户端
    res = client.synthesis(text, "zh", 1, {
        'spd': 4,
        'pit': 5,
        'vol': 5,
        'per': 5118})
    # 配置个性化语音
    # print(res)
    if not isinstance(res, dict):
        with open(audio_path, 'wb') as f:
            f.write(res)
    audio, freq = librosa.load(audio_path)
    audio_time = len(audio) / freq
    return audio_time


def get_video(audio_time0, image_folder_dir, video_path):
    def resize(image_r, new_w, new_h):
        new_image = cv2.resize(image_r, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
        return new_image

    fps = 20  # fps: frame per seconde 每秒帧数，数值可根据需要进行调整
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码为 mp4v 格式，注意此处字母为小写，大写会报错

    image_list = sorted([image_folder_dir + "/" + name for name in os.listdir(image_folder_dir) if
                         name.endswith('.png')])  # 获取文件夹下所有格式为 jpg 图像的图像名，并按时间戳进行排序
    num_fig = int(audio_time0 * fps / len(image_list))
    # w_h = 1
    # w_f = 550
    # for i in image_list:
    #     w0, h0 = Image.open(i).size
    #     if w0/h0
    #     w_h = min(w_h, h0)
    video = cv2.VideoWriter(filename=video_path, fourcc=fourcc, fps=fps, isColor=True, frameSize=(550, 550))
    for i in range(len(image_list)):
        image = cv2.imread(image_list[i])
        image0 = resize(image, 550, 550)
        for j in range(num_fig):
            video.write(image0)
    video.release()
    cv2.destroyAllWindows()


APP_ID = '62798439'
API_KEY = "wEGCE1nOZOK9QMgZlmyRmCs5"  # ak,控制台内创建app获取
SECRET_KEY = "zhzFWii933JrqMwzd822fqdPoyoS492s"  # sk,控制台内创建app获取
audio_path0 = "theme_audio.mp3"
video_path0 = "theme_video.mp4"
text = "The main idea presented in the context is the significance of traditional CMOS technology in integrated circuits, emphasizing the importance of scaling essential dimensions, overcoming challenges in lithography, transistor scaling, interconnections, and circuit design to drive the industry forward. It also highlights the need for progress in materials, transistor configurations, and lithography to continuously enhance CMOS technology performance. The text discusses the advantages of CMOS technology, challenges in scaling critical dimensions, and the impact of CMOS technology on microelectronics. Additionally, it mentions ongoing research efforts in traditional CMOS technology focusing on exploring new materials and transistor structures to sustain performance enhancements and anticipate significant alterations in lithography for further size reduction."
pic0 = 'vedio'
output_video_path = 'output_video0.mp4'
t = get_audio(text, audio_path0)
get_video(t, pic0, video_path0)

video_clip = VideoFileClip(video_path0)  # 替换为您的视频文件
audio_clip = AudioFileClip(audio_path0)  # 替换为您的音轨文件
# 将音轨添加到视频
video_clip = video_clip.set_audio(audio_clip)

# 保存合并后的视频
video_clip.write_videofile(output_video_path, codec='libx264')

# 关闭视频和音轨文件
video_clip.close()
audio_clip.close()

print(f"已将音轨成功合并到视频并保存为 {output_video_path}")
