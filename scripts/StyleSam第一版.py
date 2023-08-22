import modules.scripts as scripts
import gradio as gr
import copy
import os
import random
from os import listdir, path
from os.path import isfile, join
from modules.shared import cmd_opts, opts, state
from modules import scripts
from modules.processing import process_images, Processed
import codecs

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResourceDir = os.path.join(scripts.basedir(), f"scripts/Stylepower/")

def FilesInFolder(SourceFolder):
     return [file for file in os.listdir(SourceFolder)]

def FilesInFolderFullPath(SourceFolder):
     return [SourceFolder + file for file in os.listdir(SourceFolder)]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# replace "createSam\大叔动作.txt" with os.path.join("createSam", "大叔动作.txt") and so on for the other files.

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔动作.txt"), 'r+', encoding='utf-8') as tf:
    大叔动作  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔场景.txt"), 'r+', encoding='utf-8') as tf:
    大叔场景  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔职业.txt"), 'r+', encoding='utf-8') as tf:
    大叔职业  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔背景.txt"), 'r+', encoding='utf-8') as tf:
    大叔背景  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔纯色.txt"), 'r+', encoding='utf-8') as tf:
    大叔纯色  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔魔法.txt"), 'r+', encoding='utf-8') as tf:
    大叔魔法  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔皮肤.txt"), 'r+', encoding='utf-8') as tf:
    大叔皮肤  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔头发.txt"), 'r+', encoding='utf-8') as tf:
    大叔头发  = [line.rstrip() for line in tf]

with codecs.open(os.path.join(ResourceDir, "createSam", "大叔眼睛.txt"), 'r+', encoding='utf-8') as tf:
    大叔眼睛  = [line.rstrip() for line in tf]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ResultACDoncept = ["No","Random"]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultType = {
   "No":"", 
   " 🤍 Q版":",Q版|(chibi drawing stytle:1.4),Professional",
   " 🤍 3D渲染":",(3D render:1.3),Professional",
   " 🤍雕塑":",雕塑|(sculpture:1.3)",
   " 🤍 CG风":",CG风|(game cg:1.3),extremely detailed CG unity 8k wallpaper",
   " 🤍绘画":",绘画|(painting:1.3), canvas, ((fine art)), detailed", 
   " 🤍草图":",草图|(((sketch:1.3), drawing)), pencil art, graphite, colored pencil, charcoal art, high contrast, 2  bit", 
   " 🤍阴影":",阴影|(shadows:1.4)",
   " 🤍素描风":",草稿风|(sketch:1.7)(sketch:2)",
   " 🤍像素风":"像素风|(pixel art:1.5)",
   " 🤍科幻风":"科幻风格|(science fiction:1.5)",
   " 🤍水彩风":",水彩风|(Watercolor:1.4)",
   " 🤍维杜塔":",维杜塔绘画|(Veduta painting:1.3)",
   " 🤍湿壁画":",湿壁画|(Fresco painting:1.3)",
   " 🤍水粉画":",水粉画|(Gouache Painting:1.3)",
   " 🤍蛋彩画":",蛋彩画|(Tempera Painting:1.3)",
   " 🤍摄影技巧":",(数字绘画|digital painting:1.3),Bokeh, ((photograph)), highly detailed, sharp focus, 8k, 4k", 
   " 🤍电影风格":",数字艺术|(storybook drawing:1.7)(storybook drawing:1.3)(storybook drawing:1.3))), (digital illustration), 4k, trending  on artstation, trending on cgsociety, cinematic, agfacolor", 
   " 🤍经典漫画":",经典漫画|((storybook drawing, graphic novel, comic book)), Jack Kirby, Frank Miller, Steve Ditko, John Romita , Neal Adams", 
   " 🤍现代漫画":",现代漫画|((comic book)), Jim Lee, john romita jr, Cory Walker, ryan ottley",
   " 🤍复古漫画":",复古漫画|((manga,anime)), Katsuhiro Otomo, Naoki Urasawa, Hiroya Oku, Hiromu Arakawa, Junji Ito,danbooru, zerochan  art, kyoto animation",
   " 🤍纸艺风格":",纸艺风格|paper art{{{paper Figure}}}, origami art, 3d,{{{origami art}}}",
   " 🤍轻小说风":"轻小说风|(art of light novel:1.7)",
   " 🤍色铅笔风":",色铅笔风|(colored pencils style:1.7)",
   " 🤍老照片风":",老照片风|(High resolution scan:1.3)",
   " 🤍向量图像":",向量图像|(vector image:1.3)",
   " 🤍厚涂绘画":",厚涂绘画|(Impasto painting:1.3)",
   " 🤍烟雾绘画":",烟雾绘画|(Sfumato painting:1.3)",
   " 🤍拜占庭绘画":",拜占庭马赛克|(Byzantine mosaic:1.3)",
   " 🤍粉彩绘画":",粉彩画|(pastel painting:1.3)"
}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultTypeNegatives = {
   "No":"", 
   " 🤍 Q版":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech  bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍 3D渲染":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍雕塑":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍 CG风":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍绘画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍草图":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍阴影":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍素描风":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍像素风":",low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍科幻风":",low quality,bad quality,worst quality,error,text,glitch, low  quality,bad quality,worst quality,error ,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍水彩风":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍维杜塔":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,  stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍湿壁画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍水粉画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, (( logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering,  oversaturated, washed out, noisy, low-resolution.",
   " 🤍蛋彩画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,  stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍摄影技巧":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍电影风格":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍经典漫画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍现代漫画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍复古漫画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍纸艺风格":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍轻小说风":",low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍色铅笔风":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍老照片风":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍向量图像":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍厚涂绘画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering, oversaturated, washed out, noisy, low-resolution.",
   " 🤍烟雾绘画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering , oversaturated, washed out, noisy, low- resolution.",
   " 🤍拜占庭绘画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch, ( (logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering, stuttering , oversaturated, washed out, noisy, low-resolution.",
   " 🤍粉彩绘画":", low quality,bad quality,worst quality,error,text,glitch, low quality,bad quality,worst quality,error,text,glitch,  ((logo)), (title), text, speech bubbles, panels, signature, ((barcode)), margin, sticker,grainy, blurred, distorted, flickering,   stuttering, oversaturated, washed out, noisy, low-resolution."


}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultScenarios = {
     "No":"", 
     " 🏙️城市":",城市|(cityscape:1.3)",
     " 🏰城堡":",城堡|(Castle:1.3)",
     " ⛩️神社":",神社|(Shrine:1.3)",
     " 🏞️街景":",街景|(street scenery:1.3)",
     " 🌊海滩":",海滩|(beach:1.3)",
     " 🏞️湖边":",湖边|(lakeside:1.3)",
     " 🏞️河边":",河边|(riverside:1.3)",
     " 🌌星空":",星空|(starry sky:1.3)",
     " 🌾草原":",草原|(grassland:1.3)",
     " 🎆烟火":",烟火|(fireworks:1.3)",
     " 🚽浴室":",浴室|(bathroom:1.3)",
     " 🏢公会":",公会|(guild:1.3)",
     " 🍺酒馆":",酒馆|(Tavern:1.3)",
     " 🏨旅馆":",旅馆|(hostel:1.3)",
     " 🧗 悬崖":",悬崖|(cliff:1.3)",
     " 🍻酒吧":",酒吧|(pub:1.3)",
     " 🚽厕所":",校园厕所|(campus toilet:1.3)",
     " 🚃电车":",电车|(Train:1.3)",
     " ⚔️战场":",战场|(War/Battlefield:1.3)",
     " 🏫学校":",学校/校园|(School/Academy:1.3)",
     " 🔥暖色":",(暖色|warm|:1.3)",
     " 🌕红月亮":",(红月亮|red moon:1.3)",
     " ☀️太阳":",(太阳|sun:1.3)",
     " 🪦墓地":",(墓地|graveyard:1.3)",
     " 🕳️盆地":",(盆地|basin:1.3)",
     " 🏚️地下室":",(地下室|basement:1.3)",
     " 🏋️ 训练场":",训练场|(training course:1.3)",
     " 🏫学校":",学校/学园|(School / Academy:1.3)",
     " 🏮风俗店":",风俗店/泡泡浴|(Sex Industry/Soapland:1.3)",
     " 💼办公室":",办公室/职场|(Office/Workplace:1.3)",
     " ♨️露天温泉":",露天温泉|(openair hot springs:1.3)",
     " 💎豪华大厅":",豪华室内大厅|(magnificent indoor hall:1.3)",
     " 💡吊灯大厅":",吊灯豪华大厅|(magnificent indoor hall with chandelier:1.3)",
     " 🌳梦幻森林":",(梦幻森林|Dreamy forest:1.3)"

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultSpecies = {
   "No":"", 
   " 😀露齿而笑的脸":",( 😀 Grinning Face:1.3)",
   " 😃紧闭嘴巴睁大眼睛的脸":",( 😃 Grinning Face with Big Eyes:1.3)",
   " 😄眼睛眯成一条缝的笑脸":",( 😄 Grinning Face with Smiling Eyes:1.3)",
   " 😁露出大牙齿的笑脸":",( 😁 Beaming Face with Smiling Eyes:1.3)",
   " 😆眯眼大笑的脸":",( 😆 Grinning Squinting Face:1.3)",
   " 😅擦汗的笑脸":",( 😅 Grinning Face with Sweat:1.3)",
   " 🤣大笑躺在地上的脸":",( 🤣 Rolling on the Floor Laughing:1.3)",
   " 😂笑到流泪的脸":",( 😂 Face with Tears of Joy:1.3)",
   " 🙂微笑的脸":",( 🙂 Slightly Smiling Face:1.3)",
   " 🙃上下颠倒的脸":",( 🙃 Upside-Down Face:1.3)",
   " 😉眨眼的脸":",( 😉 Winking Face:1.3)",
   " 😊眼睛眯成一条缝的微笑脸":",( 😊 Smiling Face with Smiling Eyes:1.3)",
   " 😇带着光环微笑的脸":",( 😇 Smiling Face with Halo:1.3)",
   " 🥰带着爱心的微笑脸":",( 🥰 Smiling Face with Hearts:1.3)",
   " 😍眼中含情的微笑脸":",( 😍 Smiling Face with Heart-Eyes:1.3)",
   " 🤩心花怒放的脸":",( 🤩 Star-Struck:1.3)",
   " 😘送出飞吻的脸":",( 😘 Face Blowing a Kiss:1.3)",
   " 😗亲嘴的脸":",( 😗 Kissing Face:1.3)",
   " ☺微笑的脸":",( ☺️ Smiling Face:1.3)",
   " 😚闭着眼睛的亲嘴脸":",( 😚 Kissing Face with Closed Eyes:1.3)",
   " 😙眼睛眯成一条缝的亲嘴脸":",( 😙 Kissing Face with Smiling Eyes:1.3)",
   " 😋舌头舔嘴巴的脸":",( 😋 Face Savoring Food:1.3)",
   " 😛舌头伸出的脸":",( 😛 Face with Tongue:1.3)",
   " 😜眨眼的脸伸出舌头":",( 😜 Winking Face with Tongue:1.3)",
   " 🤪疯狂的脸":",( 🤪 Zany Face:1.3)",
   " 😝眯眼吐舌头的脸":",( 😝 Squinting Face with Tongue:1.3)",
   " 🤑大嘴巴贪钱的脸":",( 🤑 Money-Mouth Face:1.3)",
   " 🤗拥抱的脸":",( 🤗 Hugging Face:1.3)",
   " 🤔思考的脸":",( 🤔 Thinking Face:1.3)",
   " 🤨抬起眉毛的脸":",( 🤨 Face with Raised Eyebrow:1.3)",
   " 😐中立的脸":",( 😐 Neutral Face:1.3)",
   " 😑无表情的脸":",( 😑 Expressionless Face:1.3)",
   " 😶没有嘴巴的脸":",( 😶 Face Without Mouth:1.3)",
   " 😏嘲讽的脸":",( 😏 Smirking Face:1.3)",
   " 😒不开心的脸":",( 😒 Unamused Face:1.3)",
   " 🙄翻白眼的脸":",( 🙄 Face with Rolling Eyes:1.3)",
   " 😬扮鬼脸的":",( 😬 Grimacing Face:1.3)",
   " 😌感到宽慰的脸":",( 😌 Relieved Face:1.3)",
   " 😔沉思的脸":",( 😔 Pensive Face:1.3)",
   " 😪瞌睡的脸":",( 😪 Sleepy Face:1.3)",
   " 🤤流口水的脸":",( 🤤 Drooling Face:1.3)",
   " 😴睡觉的脸":",( 😴 Sleeping Face:1.3)",
   " 😷带着医用口罩的脸":",( 😷 Face with Medical Mask:1.3)",
   " 🤒带着温度计的生病脸":",( 🤒 Face with Thermometer:1.3)",
   " 🤕带着头绷带的受伤脸":",( 🤕 Face with Head-Bandage:1.3)",
   " 🤢想吐的脸":",( 🤢 Nauseated Face:1.3)",
   " 🤮呕吐的脸":",( 🤮 Face Vomiting:1.3)",
   " 🥱打呵欠的脸":",( 🥱 Yawning Face:1.3)",
   " 😯惊讶的脸":",( 😯 Hushed Face:1.3)",
   " 😦张嘴皱眉的脸":",( 😦 Frowning Face with Open Mouth:1.3)",
   " 😧苦恼的脸":",( 😧 Anguished Face:1.3)",
   " 😨害怕的脸":",( 😨 Fearful Face:1.3)",
   " 😰带着汗水的焦虑脸":",( 😰 Anxious Face with Sweat:1.3)",
   " 😥伤心但感到宽慰的脸":",( 😥 Sad but Relieved Face:1.3)",
   " 😢哭泣的脸":",( 😢 Crying Face:1.3)",
   " 😭大声哭泣的脸":",( 😭 Loudly Crying Face:1.3)",
   " 😱惊恐尖叫的脸":",( 😱 Face Screaming in Fear:1.3)",
   " 😖困惑的脸":",( 😖 Confounded Face:1.3)",
   " 😞失望的脸":",( 😞 Disappointed Face:1.3)",
   " 😫疲倦的脸":",( 😫 Tired Face:1.3)",  
   " 😓带着汗水的沮丧脸":",( 😓 Downcast Face with Sweat:1.3)",
   " 🥵发热的脸":",( 🥵 Hot Face:1.3)",
   " 🥶发冷的脸":",( 🥶 Cold Face:1.3)",
   " 😩疲惫的脸":",( 😩 Weary Face:1.3)",
   " 🥺乞求的脸":",( 🥺 Pleading Face:1.3)",
   " 😕困惑的脸":",( 😕 Confused Face:1.3)",
   " 🙁微微皱眉的脸":",( 🙁 Slightly Frowning Face:1.3)",
   " ☹皱眉的脸":",( ☹️ Frowning Face:1.3)",
   " 😟担心的脸":",( 😟 Worried Face:1.3)",
   " 😤喷气的脸":",( 😤 Face with Steam From Nose:1.3)",
   " 😠生气的脸":",( 😠 Angry Face:1.3)",
   " 🤬带着咒骂符号的脸":",( 🤬 Face with Symbols on Mouth:1.3)",
   " 😡噘嘴的脸":",( 😡 Pouting Face:1.3)",
   " 🤯头爆炸的脸":",( 🤯 Exploding Head:1.3)",
   " 🥴头晕的脸":",( 🥴 Woozy Face:1.3)",
   " 🤥说谎的脸":",( 🤥 Lying Face:1.3)",
   " 😎带太阳眼镜的笑脸":",( 😎  Smiling face with sunglasses :1.3)",
   " 🥳庆祝的脸":",( 🥳  Partying face :1.3)",
   " 🤠戴牛仔帽的脸":",( 🤠  Cowboy hat face :1.3)",
   " 🤖机器人的脸":",( 🤖  Robot face :1.3)",
   " 🤫嘘声的脸":",( 🤫  Shushing face :1.3)",
   " 🤭手掩嘴巴的脸":",( 🤭  Face with hand over mouth :1.3)",
   " 🤧打喷嚏的脸":",( 🤧  Sneezing face :1.3)",
   " 🤓书呆子的脸":",( 🤓  Nerd face :1.3)",
   " 😈带角的笑脸":",( 😈  Smiling face with horns :1.3)",
   " 🤐拉链嘴脸":",( 🤐  Zipper-mouth face :1.3)",
   " 🧐单片眼镜脸":",( 🧐  Face with monocle :1.3)",
   " 🤡小丑脸":",( 🤡  Clown face :1.3)",
   " 👽外星人":",( 👽  Alien :1.3)",
   " 🎃南瓜灯笼":",( 🎃  Jack-o-lantern :1.3)",
   " 🤩有趣的":", 🤩有趣的|(Amusing:1.3, 🤩 )",
   " 😠发怒的":", 😠发怒的|(Angry:1.3, 😠 ,)",
   " 🛋舒适的":", 🛋️舒适的|(Cosy:1.3, 🛋 ,)",
   " 😔沮丧的":", 😔沮丧的|(Depressing:1.3, 😔 ,)",
   " 🤢厌恶的":", 🤢厌恶的|(Disgusting:1.3, 🤢 ,)",
   " 😳尴尬的":", 😳尴尬的|(Embarrassing:1.3, 😳 ,)",
   " 👿恶毒的":", 👿恶毒的|(Evil:1.3, 👿 ,)",
   " 😨担心的":", 😨担心的|(Fearful:1.3, 😨 ,)",
   " 👻可怕的":", 👻可怕的|(Frightening:1.3, 👻 ,)",
   " 😬严峻的":", 😬严峻的|(Grim:1.3, 😬 ,)",
   " 😞内疚的":", 😞内疚的|(Guilty:1.3, 😞 ,)",
   " 😊快乐的":", 😊快乐的|(Happy:1.3, 😊 ,)",
   " 💔绝望的":", 💔绝望的|(Hopeless:1.3, 💔 ,)",
   " 😏好色的":", 😏好色的|(Lustful:1.3, 😏 ,)",
   " 😌平静的":", 😌平静的|(Peaceful:1.3, 😌 ,)",
   " 🙌自豪的":", 🙌自豪的|(Proud:1.3, 🙌 ,)",
   " 💕浪漫的":", 💕浪漫的|(Romantic:1.3, 💕 ,)",
   " 😢悲哀的":", 😢悲哀的|(Sad:1.3, 😢 ,)",
   " 🙈可耻的":", 🙈可耻的|(Shameful:1.3, 🙈 ,)",
   " 🤪疯狂的":", 🤪疯狂的|(frantic:1.3, 🤪 ,)",
   " 🤞充满希望的":", 🤞充满希望的|(Hopeful:1.3, 🤞 ,)",
   " 💪精力充沛的":", 💪精力充沛的|(Energetic:1.3, 💪 ,)",
   " 👍令人满意的":", 👍令人满意的|(Satisfying:1.3, 👍 ,)",
   " 😲令人惊讶的" :", 😲  令人惊讶的 |(Surprising:1.3, 😲 ,)",
   " 💫有吸引力的":", 💫  极有吸引力的|(fascinating:1.3, 💫 ,)",
   " 🆘极其严重的":", 🆘  极其严重的|(dire:1.3, 🆘 ,)",
   " 🤔难以捉摸的":", 🤔  难以捉摸|(elusive:1.3), 🤔 ,)"



}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultStyle = {
   "No":"", 
   " 📜虚幻引擎":",虚幻引擎渲染|(unreal engine render:1.3)",
   " 📜 Maya":",在maya中渲染|(rendered in maya:1.3)",
   " 📜 Zbrush":",在zbrush中渲染|(rendered in zbrush:1.3)",
   " 📜 C4d":",在cinema4d中渲染|(rendered in cinema4d:1.3)",
   " 📜 3D VR":",3D VR绘制|(3D VR painting:1.3)",
   " 📜 1950年封面":",1950年代纸浆科幻封面|(1950s pulp sci-fi cover:1.3)",
   " 📜维杜塔绘画":",维杜塔绘画|(Veduta painting:1.3)",
   " 📜苏门答腊画":",苏门答腊州索托(|Sotto In Su:1.3)",
   " 📜 G绘画":",G绘画|(Grisaille painting:1.3)",
   " 📜透视画":",透视画|(Perspective painting:1.3)",
   " 📜异世界":",异世界转生|(Isekai Reincarnation:1.3)",
   " 📜超现实":",超现实|(hyperrealism),(micro details), (surrealism)", 
   " 📜现实的":",现实|((realistic)),(realism)", 
   " 📜写实的":",写实|((photorealism)),detailed", 
   " 📜现代的":",现代艺术|(modern art:1.3)",  
   " 📜抽象的":",抽象的|(abstract art:1.3)", 
   " 📜流行的":",流行艺术|(pop art:1.3)", 
   " 📜印象派":",印象派|(impressionist art:1.3)", 
   " 📜立体的":",立体|(cubism:1.3)", 
   " 📜幻想的":",幻想|(fantasy art:1.3)",
   " 📜女体化":",女体化|(Feminization:1.3)",
   " 📜格斗的":",格斗|(Fighting/Martial Arts:1.3)",
   " 📜搞笑的":",搞笑|(Gag/Joke:1.3)",
   " 📜情侣的":",情侣|(Lovers:1.3)",
   " 📜纯爱的":",纯爱|(Pure Love:1.3)",
   " 📜严肃的":",严肃|(Serious:1.3)",
   " 📜运动的":",运动|(Sports:1.3)",
   " 📜后宫的":",后宫|(Harem:1.3)",
   " 📜暴力的":",暴力|(Violence:1.3)",
   " 📜附身的":",附身|(Possession:1.3)",
   " 📜温馨的":",温馨|(Heartwarming:1.3)",
   " 📜恐怖的":",恐怖|(Horror:1.3)",
   " 📜魔法的":",魔法|(Magic:1.3)",
   " 📜推理的":",推理|(Mystery:1.3)",
   " 📜军武的":",军武|(Military:1.3)",
   " 📜怀孕的":",怀孕/生产|(pregnancy/Childbirth:1.3)",
   " 📜耽美的":",耽美|(Ephebophilia/Shonenai:1.3)",
   " 📜浮世绘":",浮世绘-e|(Ukiyo-e:1.3)",

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ResultColors = {
   "No":"", 
   " ⭐ HDR":",HDR|(HDR:2.4)",
   " ⭐暖色":",暖色|(warm:2.5)",
   " ⭐冷色":",冷色|(cool:2.5)",
   " ⭐剪影":",(silhouette:1.3)",
   " ⭐光环":",光环|(halo:1.3)",
   " ⭐灰度":",灰度|(grayscale:2)",
   " ⭐单色":",单色|(monochrome:1.3)",
   " ⭐背光 ":"(backlight:1.6)",
   " ⭐光亮":",光亮|(light:2.5)",
   " ⭐星光":",(starlight:1.3)",
   " ⭐月光":",(moonlight:1.3)",
   " ⭐色调":",(hue:1.3)",
   " ⭐剪影":",(silhouette:1.3)",
   " ⭐色温":",(colortemperature:1.3)",
   " ⭐黑暗":",(darkness:1.3)",
   " ⭐色差":",色差|chromatic aberration",
   " ⭐互补":",互补|complementary-colors",
   " ⭐饱和的":",饱和的|saturated",
   " ⭐去饱和":",去饱和|desaturated",
   " ⭐黑与白":",黑与白|black and white",
   " ⭐非互补":",非互补|non-complementary colors",
   " ⭐混乱的":",混乱的|chaotic colors",
   " ⭐暗色调":",暗色调|Tenebrism",
   " ⭐哑光漆":",(哑光漆|matte painting:1.3)",
   " ⭐环境光":",(ambientlight:1.3)",
   " ⭐散射光":",(scatteredlight:1.3)",
   " ⭐温柔光":",(gentlelight:1.3)",
   " ⭐边缘灯":",(rimlight:1.3)",
   " ⭐对比度":",(contrast:1.3)",
   " ⭐着色光":",(tintedlight:1.3)",
   " ⭐饱和度":",(saturation:1.3)",
   " ⭐闪光灯":",(strobelight:1.3)",
   " ⭐霓虹灯":",(neonlight:1.3)",
   " ⭐蜡烛光":",(candlelight:1.3)",
   " ⭐火焰光":",(firelight:1.3)",
   " ⭐自然光":",(naturallight:1.3)",
   " ⭐影棚灯":",(studiolight:1.3)",
   " ⭐泛光灯":",(floodlight:1.3)",
   " ⭐轨道灯":",(tracklight:1.3)",
   " ⭐跟踪灯":",(followspot:1.3)",
   " ⭐光影板":",(gobo:1.3)",
   " ⭐星光晕":",(starburst:1.3)",
   " ⭐十字灯":",(crosslight:1.3)",
   " ⭐蝴蝶灯":",(butterflylight:1.3)",
   " ⭐美容盘":",(beautydish:1.3)",
   " ⭐柔光箱":",(softbox:1.3)",
   " ⭐雨伞灯":",(umbrellalight:1.3)",
   " ⭐环形灯":",(ringlight:1.3)",
   " ⭐圆形灯":",(circularlight:1.3)",
   " ⭐光束灯":",(beamlight:1.3)",
   " ⭐洗染灯":",(washlight:1.3)",
   " ⭐烟雾机":",(fogmachine:1.3)",
   " ⭐雾化器":",(hazer:1.3)",
   " ⭐泡泡机":",(bubblemachine:1.3)",
   " ⭐闪光灯":",(strobelight:1.3)",
   " ⭐自然光":",自然光|natural light",
   " ⭐丰富色彩":",丰富色彩|colorful",
   " ⭐低饱和度":",低饱和度|low coloration",
   " ⭐高对比度":",高对比度|high contrast",
   " ⭐轮廓加深":",轮廓加深|contour deepening",
   " ⭐色彩斑澜":",色彩斑澜|colorful",
   " ⭐强烈的光":",(intenselight:1.3)",
   " ⭐明亮的光":",(brightlight:1.3)",
   " ⭐眩目的光":",(blindinglight:1.3)",
   " ⭐炫耀的光":",(glare:1.3)",
   " ⭐镜头光晕":"(lens 135mm,f1.8:1.3)",
   " ⭐边缘照明":",(edgelighting:1.3)",
   " ⭐昏暗的光":",(dimlight:1.3)",
   " ⭐镜头光斑":",(lensflare:1.3)",
   " ⭐太阳光晕":",(sunburst:1.3)",
   " ⭐图案投影":",(patternprojection:1.3)",
   " ⭐影像投影":",(imageprojection:1.3)",
   " ⭐纹理投影":",(textureprojection:1.3)",
   " ⭐断裂纹路":",(breakuppattern:1.3)",
   " ⭐紫外线灯":",(UVlight:1.3)",
   " ⭐舞台灯光":",(stagelight:1.3)",
   " ⭐移动头灯":",(movingheadlight:1.3)",
   " ⭐霓虹圆环灯":",(neonring:1.3)",
   " ⭐八角柔光箱":",(octabox:1.3)",
   " ⭐抛物面反光镜":",(parabolicreflector:1.3)",
   " ⭐雷姆布兰特灯光":",(Rembrandtlighting:1.3)",
   " ⭐椭圆反射器聚光灯":",(ellipsoidalreflectorspotlight:1.3)"

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageView = {
     "No":"", 
     " 🤳自拍 ":"自拍|(selfie:1.3), 🤳 ",
     " 📷侧脸 ":"侧脸|(profile:1.3)",
     " 📷远景":"远景|(wide shot:1.3)",
     " 📷颠倒":"颠倒|(upside-down:1.3)",
     " 📷透视 ":"透视|(perspective:1.3)",
     " 📷全景 ":"全景|(overall view:2.0)",
     " 📷景深 ":"景深|(depth of field:1.3)",
     " 📷特写":"特写|(close up:1.3),worms-eye view",
     " 📷广角":",广角|(wide angle:1.3), 25mm, 35mm, zoomed out, F/5.6, medium distance, sharp", 
     " 📷超广角":",超广角|(super wide angle:1.3), 20mm, zoomed out, F/11.0, far away, sharp", 
     " 📷超长焦":",超长焦|(super telephoto:1.3), F/11.0, 200mm, 300mm, very far away, sharp", 
     " 📷鸟瞰图":"鸟瞰图|(birds-eye view:1.3),distant",
     " 📷电影镜头":"电影镜头|(cinematic angle :1.3)",
     " 📷偷看视角 ":"偷看视角|(peeking:1.2)",
     " 📷臀部焦点 ":"臀部焦点|(hip focus:1.3)",
     " 📷模糊背景 ":"模糊背景|(blurry background:1.3)",
     " 📷运动模糊":"运动模糊|(motion blur:1.3)",
     " 📷斜角镜头 ":"斜角镜头|(dutch angle:1.3)",
     " 📷面朝远方 ":"面朝远方|(facing away:1.3)",
     " 📷强烈镜头 ":"强烈镜头|(intense angle :1.3)",
     " 📷动态镜头 ":"动态镜头|(dynamic angle :1.3)",
     " 📷正前缩距 ":"正前缩距|(foreshortening:1.3)",
     " 📹主观视角   ":"主观视角|(pov:1.3)",
     " 📷人像镜头":",人像镜头|(portrait:1.3), 50mm, F/2.8, 1m away", 
     " 📹背面镜头":",背面镜头|(view from back:2),(exquisite detail:2)", 
     " 📷全身镜头":",全身镜头|(((FULL-BODY:2.5))),(exquisite detail:2)", 
     " 📹侧面镜头":",侧面镜头|(view from the side:2),(exquisite detail:2)", 
     " 📹正面镜头":",正面镜头|(view from the front:2),(exquisite detail:2)", 
     " 📷长焦镜头":",长焦镜头|(telephoto:1.3), 100mm, F/5.6, far away, sharp", 
     " 📷微距镜头":",微距镜头|(macro:1.3), extremely close, extremely detailed",
     " 📷鱼眼镜头":",鱼眼镜头|fisheye, 10mm, zoomed out, F/21.3, very far away, sharp", 
     " 📷三视图进阶  ":"三视图进阶|(concept art:1.3)",
     " 📷戏剧性镜头 ":"戏剧性镜头|(dramatic angle :1.3)",
     " 📷 45度角":"45度角|looking at viewer,(from side:1.2),( head tilt:1.65),(leaning_back:1.25),"
}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageTheme  = {
     "No":"", 
     " 👦高颜质帅哥":", 高质量帅哥|(boy:2.0),(1boy:2.0), 👦 ,Portrait of an attractive young boy,extremely detailed CG  unity 8k wallpaper, Clear picture,photography, masterpiece, best quality, 8K, HDR, highres, (absurdres:1.3), Kodak portra 400, film grain,  blurry background, (bokeh:1.3), lens flare, (vibrant color:1.3),大叔-超逼真系|8 k high definition, insanely detailed, intricate, elegant ,", 
     " 👩高颜质美女":", 高质量美女|(Portrait of an attractive young lady:2.0), 👩 ,extremely detailed CG unity 8k wallpaper,  Clear picture,photography, masterpiece, best quality, 8K, HDR, highres, (absurdres:1.3), Kodak portra 400, film grain, blurry background, (bokeh :1.3), lens flare, (vibrant color:1.3),大叔-超逼真系|photo of a gorgeous anime girl in bikini in the style of stefan  kostic, realistic,body shot, sharp focus, 8 k high definition, insanely detailed, intricate, elegant,",
     " 🐶高颜质动物":",高质量动物|(animal:1.3), 🐶 ,Organism, Living being, Creature, Life form, Species, Flora, Fauna,  Microorganism, Multicellular, Unicellular, Eukaryote, Prokaryote, Mammal, Reptile, Bird, Fish, Insect, Arthropod, Amphibian, Bacteria, Fungi.High quality,, 8K,  pets, many animals, many pets",
     " 🏠高颜质场景":",高质量场景|(Breathtaking:2.0),Elaborate, 🏠 ,Picturesque, Idyllic,  Serene, Enchanting, Breathtaking, Majestic, Pristine, Scenic , Tranquil, Radiant. Intricate, Detailed, Meticulous, Delicate, Nuanced, Complex, Exquisite, Refined, Precise, Ornate, Articulate, Comprehensive, Thorough, Multifaceted",
     " 🎨高颜质画家":",高质量优雅的画|Norman Rockwell, 🎨 , Franz Xaver Winterhalter, Jeremy Mann, Artgerm, Ilya Kuvshinov, Anges Cecile , Michael Garmash",
     " 👾高颜质怪物":",高质量怪物|(monster:1.3), 👾 , ugly, surgery, evisceration, morbid, cut, open, rotten, mutilated,  deformed, disfigured, malformed, missing limbs, extra limbs, bloody, slimy, goo, Richard Estes, Audrey Flack, Ralph Goings, Robert Bechtle, Tomasz  Alen Kopera, HRGiger, Joel Boucquemont, artstation",
     " 👾 Max怪物": "大叔制作怪物|The Laboratory of Underground Monsters, 👾 ,from the Japanese animated series,is cultivating different monsters. There are  many cabinets and jars containing different creatures and monsters that greedily look at you and want to eat you,non-human,spooky,confusion,(incomprehensible) ,(extremely frustrating),extremely detailed,((depressing)),unbearable,((extraordinary)),(hollow eyes),(masterpiece),(highquality),terrified,horrified,huge,gigantic,massive,"

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageThemeNegatives  = {
     "No": "", 
     " 👦高颜质帅哥": ",帅哥负面|(1girl:2.0),Girl, Daughter, Sister, Niece, Cousin (female), Teenager, Young woman,  Woman, Lady, Mother, Wife, Girlfriend, Fiancée, Bride, Widow, Divorcee, Aunt, Grandmother, Great-grandmother, Godmother,young lady,low quality,normal  quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality,error,text,glitch,", 
     " 👩高颜质美女": ",美女负面|lowres, text, error, missing fingers, (bad anatomy), extra digit, fewer digits, cropped , worst quality, low quality, jpeg artifacts, signature, watermark, extra fingers, mutated hands, (multiple penises), (disembodied), (poorly drawn  hands), (poorly drawn face), (mutation), (deformed breasts), (ugly), blurry, (bad proportions), (extra limbs),(wings), (1Boy:2.0), Son, Brother, Nephew, Cousin (male), Teenager, Young man, Man, Gentleman, Father, Husband, Boyfriend, Fiancé, Groom , Widower, Divorcé, Uncle, Grandfather, Great-grandfather, Godfather,low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal  quality,bad quality,worst quality,error,text,glitch,",
     " 🐶高颜质动物": ",动物负面|(1girl:2.0),low quality,normal quality,bad  quality,worst quality,error ,text,glitch, low quality ,normal quality,bad quality,worst quality,error,text,glitch,",
     " 🏠高颜质场景": ",场景负面|(1girl:2.0),1girl,(((1girl))),Organism, Living being, Creature, Life form,  Species, Flora, Fauna, Microorganism, Multicellular, Unicellular, Eukaryote, Prokaryote, Mammal, Reptile, Bird, Fish, Insect, Arthropod, Amphibian, Bacteria, Fungi. Simple, Brief, Easy to understand, Concise, Careless, Rough, Harsh, Indiscriminate, Unrefined, Crude, Inaccurate, Imprecise, Plain, Unsophisticated, Coarse, Vague , Inarticulate, Limited, Incomplete, Superficial, Unidimensional",
     " 🎨高颜质画家": ",画家负面|low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
     " 👾高颜质怪物": ",怪物负面|(1girl:2.0),low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality ,normal quality,bad quality,worst quality,error,text,glitch,",
     " 👾 Max怪物": ",怪物负面|(1girl:2.0),low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal  quality,bad quality,worst quality,error,text,glitch,"

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageDynamic = {
     "No": "", 
     "大叔的10种颜色": ",随机颜色|{RED|GREEN|BLUE|WHITE|BLACK|PINK|GOLDEN|GREY|BROWN|SILVER|AKUSEMA},4K",
     "大叔的28种哺乳动物": ",哺乳动物|{(Mammals:1.3)|(Dog:1.3)|(Cat:1.3)|(Horse:1.3)|(Cow:1.3)| (Pig:1.3)|(Sheep:1.3)|(Goat:1.3)|(Deer:1.3)|(Moose:1.3)|(Bear:1.3)|(Elephant:1.3)|(Giraffe:1.3)|(Lion :1.3)|(Tiger:1.3)|(Chimpanzee:1.3)|(Gorilla:1.3)|(Bat:1.3)|(Dolphin:1.3)|(Whale:1.3)|(Seal:1.3)|(Kangaroo:1.3 )|(Koala:1.3)|(Sloth:1.3)|(Rat:1.3)|(Rabbit:1.3)|(Hamster:1.3)|(Ferret:1.3)|(Guinea pig:1.3)|(Birds:1.3 )},",
     "大叔的11种鸟类动物": ",鸟类动物|{(Chicken:1.3)|(Turkey:1.3)|(Duck:1.3)|(Goose:1.3)|(Pigeon:1.3)| (Sparrow:1.3)|(Parrot:1.3)|(Eagle:1.3)|(Hawk:1.3)|(Falcon:1.3)|(Ostrich:1.3)|(Reptiles:1.3)},",
     "大叔的5种爬行动物": ",爬行动物|{(Snake:1.3)|(Lizard:1.3)|(Turtle:1.3)|(Crocodile:1.3)|(Alligator:1.3)} ,",
     "大叔的5种鱼类": ",鱼类|{(Fish:1.3)|(Goldfish:1.3)|(Trout:1.3)|(Salmon:1.3)|(Tuna:1.3)|(Shark :1.3)},",
     "大叔的7种昆虫": ",昆虫|{(Insects:1.3)|(Bee:1.3)|(Ant:1.3)|(Butterfly:1.3)|(Grasshopper:1.3)|(Beetle :1.3)|(Spider:1.3)},",
     "大叔的7种两栖动物": ",两栖动物|{(Amphibians:1.3)|(Frog:1.3)|(Toad:1.3)|(Salamander:1.3)|(Arachnids:1.3)| (Scorpion:1.3)}",
     "大叔的50个视角": "视角|{loverhead shot|low-angle shot|flat shot|looking to the side|looking away|looking back|looking down |looking up|looking afar|from behind|from below|facing away|ass focus|solo focus|blurry background|simple background|desired color background|selfie|split screen|full  body selfie|head down|stare down|charging forward|hedge|okiru|darkpulsegg|hug from behind|left-to-right manga|fingering from behind|right-to-left comic |johnny from scratch|looking at viewer|looking at another|looking to the side|looking away|looking down|pussy peek|when you see it|looking at  object|looking at phone|peeking|looking at animal|youkan|looking outside|no-kan|watching television|side-tie peek|watching|looking at hand|kanna|kanniiepan|leotard  peek|looking at food|kanba girls high school uniform|kanna asuke|kanchou|mr. game & watch|kanten|game & watch|king crimson|shourou kanna| firewatch|looking at hands|kannabi no mikoto|looking at screen|invisible wall}",
     "大叔的27个镜头": "镜头|{(fisheye, 10mm, zoomed out, F/21.3, very far away, sharp) | (super wide  angle, 20mm, zoomed out, F/11.0, far away, sharp) | (wide angle, 25mm, 35mm, zoomed out, F/5.6, medium  distance, sharp) | (portrait, 50mm, F/2.8, 1m away) | (telephoto, 100mm, F/5.6, far away, sharp) |  (super telephoto, F/11.0, 200mm, 300mm, very far away, sharp) | (macro, extremely close, extremely detailed) | (close up) ,worms-eye view) | (birds-eye view),distant) | (dutch angle:1.3) | (intense angle :1.3) | (cinematic angle : 1.3) | (dramatic angle :1.3) | (dynamic angle :1.3) | (wide shot:1.3) | (perspective:1.3) | (foreshortening:1.3)  | (upside-down:1.3) | (motion blur:1.3) | (depth of field:1.3) | (overall view:1.3) | (concept art: 1.3) | (hip focus:1.3) | (pov:1.3) | (blurry background:1.3) | (profile:1.3) | (facing away:1.3) |  (looking at viewer,(from side:1.2),( head tilt:1.65))}",
     "大叔的10个视图": "视图|{Orthographic projection|Plan view|Front view|Side view|Top view|Bottom view|Isometric view|Auxiliary view|Section  view|Detail view}",
     "大叔的34个表情": "表情|{(Amusing:1.3)|(Angry:1.3)|(Cosy:1.3)|(Depressing:1.3)|(Disgusting:1.3)|(Embarrassing: 1.3)|(Evil:1.3)|(Fearful:1.3)|(Frightening:1.3)|(Grim:1.3)|(Guilty:1.3)|(Happy:1.3)|(Hopeless:1.3)|(Lonely:1.3) |(Lustful:1.3)|(Peaceful:1.3)|(Proud:1.3)|(Relieving:1.3)|(Romantic:1.3)|(Sad:1.3)|(Shameful:1.3)|(Hopeful:1.3)|( Energetic:1.3)|(Satisfying:1.3)|(Surprising:1.3)|(Warm)|(Fascinating)|(Interesting)|(Dire)|(Terrifying)|(Elusive)|(Frantic)|(Serene)|( Evil)}",
     "大叔的20个哭泣": "表情|{(cry:0.1)|(cry:0.2)|(cry:0.3)|(cry:0.4)|(cry:0.5)|(cry: 0.6)|(cry:0.7)|(cry:0.8)|(cry:0.9)|(cry:1.0)|(cry:1.1)|(cry:1.2)|(cry:1.3)|(cry:1.4) |(cry:1.5)|(cry:1.6)|(cry:1.7)|(cry:1.8)|(cry:1.9)|(cry:2.0)}"

}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageStyleNegatives = {
     "No":"", 
   "大叔魔法1-三视图":"(logo:2.0),(artist_logo:2.0),tile_wall, tiles,low quality,normal quality,bad quality,worst quality,error,text,glitch , low quality,normal quality,bad quality,worst quality,error,text,glitch, (title), text, panels, speech bubbles, signature, ((barcode)),  margin, sticker",
   "大叔魔法2-爆炸粒子风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法3-捡垃圾魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法4-深海巨物恐惧症":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法5-怪东西":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法6-金色抽卡书":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法7-亮晶晶召唤术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法8-城市巨大化":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法9-怀孕风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法10-小说封面":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法11-小小樱花":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法12-禁域之术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法13-节庆快乐":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst   quality,error,text,glitch,",
   "大叔魔法14-三色泡法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法15-星星泡泡法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法16-群星的魔法少女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法17-大宇宙根源":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法18-山水小注画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法19-山水田园画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法20-中国纯风画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法21-中国道家画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法22-中国水墨画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法23-水墨颜色画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法24-元素混沌画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法25-孔灯庙会画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法26-皇家观星术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法27-神兵咒武器":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法28-神兵咒载具":",low quality,normal quality,bad quality,worst  quality,error ,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法29-晴海气泡术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法30-无限剑制法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法31-素墨古风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法32-鬼角女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法33-国风少女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法34-国风建筑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法35-紫晶女巫":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法36-少女水果汽水":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法37-赛博朋克·雨":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法38-赛博朋克风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法39-链金银术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法40-断墨水风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法41-锁链蛇环":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法42-色块分离法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法43-湿身连体风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法44-湿身风A":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法45-湿身风B":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法46-海之舞法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法47-病娇女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法48-秋收野营术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法49-V领烟雨江南":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法50-高领烟雨江南":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法51-老男人的魅力A":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法52-老男人的魅力B":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法53-水下魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法54-水中魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法55-水晶魔法A":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法56-水晶魔法B":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法57-凤凰战法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法58-仙法草术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法59-冬日时光":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法60-冰火双法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法61-冰系魔改":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法62-冰系魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法63-冰之魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法64-烟雨江南":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法65-风雪公主":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法66-风雪神咒":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法67-夏夜之狐":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法68-彼岸花法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法69-彼岸花海":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法70-空之精灵":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法71-空间冰法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法72-空间魔法":",low quality,normal quality,bad quality,worst   quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法73-血歌禁术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法74-血之公主":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法75-血之魔法1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法76-血之魔法2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法77-美人鱼法1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法78-美人鱼法2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法79-美人鱼法3":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法80-白虎画1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法81-白虎画2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法82-春之猫1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法83-春之猫2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法84-秋水法1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法85-秋水法2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法86-银杏法1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法87-银杏法2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法88-萌兽咒1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法89-萌兽咒2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法90-黄昏法1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法91-黄昏法2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法92-死尸术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法93-死灵法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法94-自然法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法95-入星海":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法96-天选术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法97-白骨法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法98-白蛇画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法99-幻之时":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法100-幻碎梦":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法101-月下蝶":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法102-月亮法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法103-月蝶舞":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法104-冬雪法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法105-卡牌法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法106-古漫法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法107-末日风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法108-水森法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法109-水墨法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法110-水镜术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法111-水魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法112-火羽术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法113-火莲术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法114-火烧云":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法115-王城法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法116-西幻术":",low quality,normal quality,bad quality,worst  quality ,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法117-西游记":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法118-彷徨术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法131-星空法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法132-星源法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法133-星语术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法134-星银法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法140-科幻风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法141-结晶法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法142-虹彩法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法143-风魔法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法144-修仙画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法145-核爆法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法146-桃花法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法147-浮世绘":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法148-留影术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法149-秘境法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法150-森火法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法151-森林冰":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法152-森林法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法153-森罗法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法154-焰山骑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法155-华丽术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法156-阳光法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法157-云中现":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法158-黄金律":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法159-黑金法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法160-园林风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法161-暗鸦法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法162-暗锁法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst   quality,error,text,glitch,",
   "大叔魔法163-灭世镜":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法164-烟水月":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法165-烟花法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法166-碎梦法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法167-碰水法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法168-圣光法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法169-圣域法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法170-苇名法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法171-诡谲法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法172-雷男法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法173-梦里花":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法174-缥缈术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法175-蒸汽城":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法176-裸背风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法177-堕天使":",low quality,normal quality,bad quality,worst  quality, error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法178-堕天法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法179-堕落法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法180-废土法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法181-废墟法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法182-数码姬":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法183-穷奇录":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法184-学院法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法185-机工房":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法186-融合法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法187-蔷薇法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法188-艺墨风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法189-飘花法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法190-黯冰法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法191-骨架":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法192-笼中鸟":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法193-★分割语法左黑发,右金发":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal  quality,bad quality,worst quality,error,text,glitch,",
   "大叔魔法194-分割左黑发右金发":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法195-分割左黑发右金发配合Latent Couple":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal  quality,bad quality,worst quality,error,text,glitch,",
   "大叔魔法196-分割四个需配合Latent Couple":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality, bad quality,worst quality,error,text,glitch,",
   "大叔魔法197-黑暗破碎风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法198-史诗级怪物":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法199-科幻女甲风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法200-很胖的盔甲战士":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法201-异形怪物无法判断":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法202-不可思议的乌龟":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法203-素材游戏化":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法204-经典西方龙":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法205-经典雪景":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法206-骷髅水母奥义":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法207-魔兽化风格":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法208-史诗战槌战争":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法209-日本恐怖漫画风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法210-超逼真美女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法211-日式漫画风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法212-写实女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法213-自制女孩在瓶子里":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法214-综合动画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法215-关在方瓶女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法216-圆瓶女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法217-写实机械蜘蛛":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法218-机械蜘蛛":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法219-上帝说给你手":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法220-神说手不可触碰":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法221-史蒂文食人的嘴":",low quality,normal quality,bad quality,worst  quality,error,text,glitch , low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法222-极致萝莉风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法223-怪异宝可梦":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法224-卡通宇宙篮":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法225-宇宙生物在街道":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法226-科幻胚胎仓":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法227-夜晚动作姿势":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法228-高清夜晚的昆虫":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法229-幻想元素艺术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法230-青色虫子摄影":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法231-末日城市":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法232-迷宫透视建筑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法233-战船和机":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法234-复合建筑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法235-银河中的运动模糊":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法236-在冬天旅馆喝醉":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法237-马车旅程":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法238-赛车旅程":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法239-印象主义":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法240-炼金术士生活":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法241-高清撞击地面":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法242-远景星空物":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法243-战争与和平":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法244-巴士虫子机器人":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法245-ex机器人":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法246-冰山上的工厂":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法247-漫画女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法248-高清一男二女随机":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法249-高清二女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法250-测试怀孕xd":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法251-增加细节":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法252-1995高清细节":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法253-绿发猛男":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法254-官绘细节":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法255-可爱女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法256-可爱男孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法257-雷电将军(横)":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法258-流浪者":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法259-温迪(横)":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法260-钟离(立绘)":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法261-刻晴(竖)":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法262-可莉(上半身)":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法263-美女烟火秀":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法264-色情001":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法265-HHH":",low quality,normal quality,bad quality,worst   quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法266-黑暗盔甲骑士风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法267-成人小萝莉吐舌头":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法268-极致色情":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法269-极致诱惑背影":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法270-极致诱惑穿内衣睡着":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法271-极致诱惑不穿内衣睡":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法272-动画少女一字腿":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法273-背影":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法274-露米哑背影":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法275-清纯警花":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法276-测试图露米哑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法277-测试图美女哈尔":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法278-测试图美女系A":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法279-掀裙风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法280-模组1号":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法281-模组2号":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法282-模组3号":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法283-印度风格":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法284-揉胸动画":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法285-多种视角":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法286-半人马":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法287-我的妹妹不可能这么可爱":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法288-五更琉璃":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法289-新垣1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法290-新垣2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法291-公主抱":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法292-二手发光":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法293-高难度动作":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法294-左右对称二人":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst  quality,error,text,glitch,",
   "大叔魔法295-邪神妹":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法296-机器生物体":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法297-零波零":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法298-明日香":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法299-刀剑妹":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法300-诗乃":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法301-亚斯娜":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法302-冷笑":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法303-壁尻":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法304-死神":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst quality ,error,text,glitch,",
   "大叔魔法305-机械女武神":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法306-中式女武神":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法307-盔甲女武神":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法308-机械铠姬 改":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法309-机械物种":",low quality,normal quality,bad quality,worst   quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法310-机械娘召唤":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法311-机器科学":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法312-机械化身体机械交":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法313-机械姬法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法314-机娘水法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法315-机械巨龙与少女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality ,worst quality,error,text,glitch,",
   "大叔魔法316-机器风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法317-真人电子少女":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法318-战争机器":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法319-钢铁巨兽":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法320-女黑白机械风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法321-机娘2":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法322-机娘1":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法323-写实巨龙风格":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法324-机械龙法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法325-墨龙萝":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法326-龙女幻想":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法327-龙骑士":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法328-龙兽法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法329-少年与龙":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法330-破碎霜龙":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法331-冰龙之术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法332-冰霜龙息":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法333-水龙法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法334-青龙法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法335-写实矮人族":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法336-写实城堡风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法337-写实水下生物":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法338-写实邪恶生物":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法339-恶魔风":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法340-湿天使":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法341-城市崩坏版":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法342-比基尼铠甲精灵":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法343-蓝色史莱姆娘":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad  quality,worst quality,error,text,glitch,",
   "大叔魔法344-杀手风格":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法345-漂亮的猫":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法346-紫罗兰色双重曝光":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法347-复古照片":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法348-超级英雄回忆录":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法349-科幻肖像":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法350-多维纸工艺":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法351-复杂的女英雄":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法352-天启战士":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法353-有机纵向":",low quality,normal quality,bad quality,worst  quality ,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法354-狗狗戴眼镜":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法355-海上的房子":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法356-大理石艺术":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法357-夜晚的车":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法358-牛头人":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法359-吃汉堡":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法360-中世纪女装":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality, worst quality,error,text,glitch,",
   "大叔魔法361-动感女孩":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法362-蕃茄配方":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法363-食材配方":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法364-猛男法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,",
   "大叔魔法364-小人物法":",low quality,normal quality,bad quality,worst quality,error,text,glitch, low quality,normal quality,bad quality,worst  quality,error,text,glitch,"
}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageDynamicNegatives = {
     "No":"", 
     "大叔的10种颜色":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的28种哺乳动物":"low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的11种鸟类动物":",low quality ",
     "大叔的5种爬行动物":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy,  bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature , watermark, username,",
     "大叔的11种鸟类动物":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy,   bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature , watermark, username,",
     "大叔的5种鱼类":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的7种昆虫":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的7种两栖动物":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy,  bad hands, text, error, missing fingers, extra  digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature , watermark, username,",
     "大叔的50个视角":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的27个镜头":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的10个视图":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的34个表情":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,",
     "大叔的20个哭泣":",low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer  digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw, lowres, bad anatomy, bad  hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature,  watermark, username,"
}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ImageStyle = {
"No":"", 
   "大叔魔法1-三视图":",(concept_art_1.3),(profile_1.3),(turnaround:1.4), (reference sheet), (masterpiece:1.3), best quality,  (official art:1.3), illustration, hyper detailed, toned, (((full body))),Orthographic projection, Plan view, Front view, Side view,  Top view, Bottom view, Isometric view, Auxiliary view, Section  view, Detail view,",
   "大叔魔法2-爆炸粒子风":",Cartoon character with Dripping gloss particle explosion, extremely detailed, sharp focus, wide view, full body shot,  smooth, digital illustration, by james jean, by banksy and mcbess,",
   "大叔魔法3-捡垃圾魔法":",(best quality),(masterpiece),(an extremely delicate and beautiful girl),wearing white dress,Golden eyes,(( (white messy hair))),Shining wings,angel,white hair,soft lighting,(((Lie in the garbage))),((dirty)),many garbage background, extremely detailed 4k CG,original,male",
   "大叔魔法4-深海巨物恐惧症":",((best quality)), ((masterpiece)), ((ultra-detailed)),(illustration),(oil paint), It was raining hard at night,(thalassophobia),(Huge eyes),Only his head was above the water,(Monster),(Phobia of giant objects), (heavy fog),from below,(ship),searchlight,You can't see the whole picture",
   "大叔魔法5-怪东西":",non-human,spooky,confusion,",
   "大叔魔法6-金色抽卡书":",(maestro:1.2),(superb quality:1.2),(extremely detailed CG unity 8k wallpaper:1.3),(a 16- year-old girl:1.3),(magic array:1.2),(a heavy book with a black cover and a gold border:1.4),(the book is  floating in the air:1.4),(the book is in front of the girl:1.4),(purple particles in the air:1.5),(focus on  the face:1.4),(a detailed facial description:1.4),(cobalt blue hair:1.4),( golden eyes:1.4),(dark purple robe1.3),(the  book covers hands:1.5),(flat breast:2.0),(front view:1.4),(golden hourglass:1.3),",
   "大叔魔法7-亮晶晶召唤术":",1girl sitting on the surface of water with large crystal flowers in her hand,the petals float past  her,fantasy, ((masterpiece)),best quality,long pink hair,purple eyes with pink pupil,flower crown,(floating hair),frilled dress with flower,paradise ,flower ornament,ribbon,happiness,[[[open mouth]]],nebula,beautiful detailed eyes,looking at viewer,{an extremely delicate and beautiful},from above,( floating crystal (flower:1.3) around her:1.5),",
   "大叔魔法8-城市巨大化":",cityscape,{{{full body}}},{{{black_thighhighs}}},adorable girl,{{{small city}}},{{ {giantess}}},{{{giga size}}},no shoes,minimap,{{{long leg}}},((({{{standing in the city}}})) ),{{from below}}},{{{{thin legs}}}},beautiful detailed sky,girl standing in the city,beautiful detailed sky,extremely detailed,nfsw ,{{{1000 meters tall}}},{{{city destoy}}},{{{open eyes wide}}},highresbuilding,city,destruction,size difference,outdoors,crushing,skyscraper ,building ruins,road,giant,,",
   "大叔魔法9-怀孕风":",{best quality}, {{masterpiece}}, {highres}, original, extremely detailed 8K wallpaper, 1girl, {an  extremely delicate and beautiful},,blunt_bangs,blue_eyes,black hair,sheer tulle dress,garter straps garter belt,Xiao Qingyi Single ponytail cheongsam black,Pregnancy, cross-part  tattoos, lewd tattoos,",
   "大叔魔法10-小说封面":",official art,(sketch), (finely detailed backgroundhighly detailed) , (sit),((full body)),(high-heeled  shoes),(Skirt above knee),(flower background),color ink, pencil paint, masterpiece, ilustration,",
   "大叔魔法11-小小樱花":",masterpiece, best quality, {{masterpiece}},{{best   quality}},{ultra-detailed},{illustration},{{an  extremely delicate and beautiful}},{dynamic angle},china,1girl,{beautiful detailed eyes},cute pink eyes,detailed face,upper body,messy floating hair,desheveled  hair,light pink hair,focus,perfect hands,cherry blossoms, {Flying cherry blossom petals},ink,chinese pianting,solo,ponytail,{sketch}, chinese mountain,",
   "大叔魔法12-禁域之术":",8k Wallpaper,grand,(((masterpiece))), (((best quality))), ((ultra-detailed)),  (illustration),  ((an extremely delicate and beautiful)),dynamic angle,(((masterpiece))),rose adorns hair,(((white BugBats))),solo  focus,corrugated,Flying red petals,Holy lighting,(covered in blood),oken glass,(broken screen),transparent glass,((((broken white clock)))), (roseleaf),(Blood drop)),((Blood fog)),(black smoke),((Black feathers floating in the air)),(Fire butterflies),((( (flame melt)))),((wind))",
   "大叔魔法13-节庆快乐":",(((masterpiece))),(high quality),((depth of field)),extremely detailed CG unity 8k wallpaper,( showered confetti),(((1girl:1.2))),((birthday crown)),((crowd surrounded the girl)),(bright heavenly realm room),(((smile) )),blush stickersest,elegant dress with many frills,((Starry Eyes)),((beautiful hair)),big cake,small_breasts",
   "大叔魔法14-三色泡法":",(((masterpiece))), best quality,  ((Default RGB color space - sRGB):1.9), ( best illumination, best shadow, an extremely delicate and beautiful), Beautiful detailed girl, (extremely delicate and beautiful girls), beautiful face, ((extremely_beautiful_detailed_anime_face )), cute face, bright skin, long wavy curly hair, dishevelled hair, detailed clothes, (detailed face, detailed eyes, detailed background, detailed  skin,)",
   "大叔魔法15-星星泡泡法":",illustration,masterpiece,wallpaper,artbook,best quality,highly detailed,ultra-detailed,solo,cinematic lighting,dramatic angle,original,{detailed  cute anime face},{{{an extremely delicate and beautiful girl}}},{{{loli}}},(((white fourpetal flower hair ornament))),( ((wreath))), extremely detailed,beautiful detailed eyes,small breast,{beautiful detailed glow},white dress,((frills)),long bright wavy white hair, Halter dress, beautiful detailed white necklace,((((((surrounded by beautiful detailed colorful_ Bubble)))))),(((lots of_ big_ colorful_ Bubble) )),((((((surrounded by beautiful detailed cute star)))))),{{{{arms behind back }}}}, flower request,((falling  petals)),pearl], depth of field,stars in the eyes,messy floating hair, coloredinner hair,wind,starfish,crab,shell,bubbles,sandbeach,night,moon  light,sea,(((over the sea))),gorgeous,fantasism,nature,refined rendering,original,contour deepening,",
   "大叔魔法16-群星的魔法少女":",(((glitter Hair))), (((((extremely detailed CG))))), ((8k wallpaper)) ,((((glitter gloves)))),((beautiful detailed glitter hair)),((Tender texture hand)),(fantasy), ((((masterpiece)))),  long shot, (arcane vi),  (magic circle), (magical girl),  colorful hair, (((loli))), (long hair),  Lolita, shiny skin, shiny hair, hair ornament, pink ribbon, shoulders, visible through hair, hairs between eyes, cute, highlight hair, neck  ring, solo, Gradient hair, white hair, sea of sakura, full body, pink silk stockings, (pink angel wings ), glitter wings,  pink Feather, flying, gemstone necklace,  (extremely delicate and beautiful), best quality, ((starry sky)), star river array stars,  complicated   background,  Beautiful night sky, meteor shower, city, colorful, long shot, (comet),",
   "大叔魔法17-大宇宙根源":",masterpiece,(best quality),(illustration),(extremely detailed CG unity 8k wallpaper),(CG),1 girl,solo, ",
   "大叔魔法18-山水小注画":",(((masterpiece))),best quality,((illustration)),((((beautiful detailed girl)))),((( extremely detailed CG 8k wallpaper))),((official art)),(1girl:2.5),((solo)),((loli)),((petite)),(((female  focus on))),(macro shot:1.5),(focus on face),portrait of girl,The girl is in the center of the frame,((( Close-up of girl))),((long black hair)),(very long hair),(floating hair),((diamond and glaring eyes)),((( beautiful detailed cold face))),handsome,((a cute and anime face)),beautiful eyes,(green eyes),bangs,bare shoulders,(((a girl  wears clothes black and white hanfu))),small breasts,(super clothes detailed),((white sleeves)),(((edged hanfu))),black ribbon,  wide sleeves,looking_at_viewer,Perfect details,(((gold fringes))),(((armsbehind back))),silk,((sleeves past fingers)),((standing)),(( (Ancient palace background))), chinese place on the mountain,(((((chinese style architecture))))) behind the girl,depth of field,beautiful  sky,((beautiful cloud)),mountain,((((waterfall)))) from the mountaintop,mist,beautiful and delicate water,((beautiful detailed background)),( (((wudang)))),a girl in ((zhangjiajie)),dramatic angle,Chinese classical wooden tower,(Chinese ancient multistoried buildings),colorful,Pine,1girl,handsome ",
   "大叔魔法19-山水田园画":",(((((extremely detailed CG))))), ((8k wallpaper)), Rural scenery, (((masterpiece) )), tile-roofed house child, (1girl:1.5), mountain, (brook), path, field, sun cloud, sunny day, sun light, butterfly , blue sky, countryside,  {golden rice fields}, river, house, wind, solo, dress, cute, shiny skin, shiny hair, hair  ornament, ribbon, shoulders, visible through hair, hairs between eyes, extremely delicate and beautiful, hand on hair, cicada on tree, water, black  hair, from side,",
   "大叔魔法20-中国纯风画":",(((masterpiece))),(((best quality))),((ultra-detailed))((extremely detailed CG)), ((8k_wallpaper))((an extremely delicate and beautiful)),dynamic angle,floating, (beautiful detailed eyes),an extremely delicate and beautiful girl,(red moon ), starry sky,shine,frills,half closed eyes,red eyes,burning,detailed light,(black_hair),bloom,(((miko))),((hair pink flowers)) ,{aqua eyes},(((small breast))),((miko)),(long_hair),,",
   "大叔魔法21-中国道家画":",((illustration)), ((floating hair)), ((extremely_detailed_eyes_and_face)),((chromatic aberration)), ((caustic)) , lens flare, dynamic angle,  ((portrait)),  (1 girl), ((solo)), ((cute face)), ((hidden hands) ), asymmetrical bangs, eye shadow, ((Giant Tai Chi)),((colorful refraction)), (beautiful detailed sky), ((dark intense shadows)) , ((cinematic lighting)), ((overexposure)), (expressionless),  blank stare, big top sleeves, ((frills)), (((small breast) )), pleated skirt, ((sharp focus)), ((masterpiece)), (((best quality))), ((extremely detailed)), colorful, hdr, (((cheongsam))),(((Exquisite Chinese sword))),((Scattered runes)),(((magnificent ancient pagoda))),Architectural community,Fluttering long hair, (((Mysterious Dragon))),gentle wind,(((Yellow  paper all over the sky))),((Spells written on paper)),(Yellow paper all  over the sky),((Antique glasses)),Dragon pattern,((A solemn atmosphere)),(beautiful and delicate eyes),((Black and white dress  pattern)),(Yellow glass light column),((mysterious)),((Chinese architecture)),",
   "大叔魔法22-中国水墨画":",1girl, Chinese girl,{{{ink wash painting}}}, {{ink splashing}}",
   "大叔魔法23-水墨颜色画":",1girl, Chinese girl,{{Phoenix}},{{{color ink wash painting}}}, {{ink splashing}},{{ color splashing}}",
   "大叔魔法24-元素混沌画":",((best quality)) ,((masterpiece)),(highres),ultra-detailed,extremely detailed CG,pastel color,sketch,water  color,illustration,extremely,detailed,wallpaper,(an extremely delicate and beautiful),(1 girl:1.5),(solo),(Perfect and delicate face), (beautiful detailed  deep eyes),(in crown made of ram skull),(extremely detailed gorgeous tiara), jellyfish phoenix, bioluminiscent, plasma,fire, water, wind,  creature, super intricate ornaments,(flowing),Close to the camera,beautiful and aesthetic",
   "大叔魔法25-孔灯庙会画":",{{best qualiy}},{{masterpiece}},{{ultra-detailed}}, extremely detailed CG, extremely detailed 8K  wallpaper, HD background,{{Kongming Lantern in the Sky}},Crowds,artbook,{{detailed light}},Birds in the background,{an extremely delicate and  beautiful},{{one girl}},The skirt sways with the wind,Fine clouds,Beautiful and meticulous starry sky,Archaic wind,the Forbidden City,Extremely  detailed background,Tiananmen,chinese style architecture ,Overexposure,Beautiful starlight,{Population background},{{A large number of people}} ,People in the surrounding background, market,Prosperity and liveliness,intricate detail,Raytracing,Beautiful and meticulous water surface,{Traditional Chinese Costume},hair ornament,tassel,black long hair,intricate detail,{gorgeous  hanfu},{Long sleeve},{{Hidden hand}},Reflective,blush,Fixed angle of view,Expressionless,Jelly like light lipstick,Extremely detailed shadows,{{{lantern  shaped like a lotus flower}}},{single sidelock},sparkle,{{Flying Kongming Lamp}},Booming Flowers and a Full Moon,{{Lantern on  the water}}",
   "大叔魔法26-皇家观星术":",{Bright stars},{{best quality}}, {{masterpiece}}, {{ultra-detailed}}, {illustration},  {an extremely delicate and beautiful}, {beautiful detailed eyes}, {{extremely clothes}},  cinematic lighting, 1 girl, princess, (extremely delicate  and   beautiful),((extremely_detailed_eyes_and_face)), (aqua eyes, glooming eyes), (long hair, hair ring, navy blue hair), (detailed hair accessories , fantasy cloth, intricated filigree, tiara), sorrow look, medium breast, (starry night, constellation, depth of   field, skyscape:1.3) " ,
   "大叔魔法27-神兵咒武器":",CYBERPUNK scifi WEAPONS, concept,extremely detailed CG unity 8k ,wallpaper",
   "大叔魔法28-神兵咒载具":",CYBERPUNK scifi,Vehicle, motor vehicle, armor, tank, high -tech, concept,red black",
   "大叔魔法29-晴海气泡术":",(((masterpiece))),((best quality)), (beautiful detailed eyes),(illustration),high contrast,(extremely  detailed CG unity 8k wallpaper),small breasts,(cinematiclighting),long brown hair,(solo),(((hanfu))),(cat ears),grey  eyes,dramatic  angle  ,depth of field,((sparkle background)),(((underwater))),coral,((1 gril)),(((Tyndall effect))),(underwater forest), (sunlight),floating hair,(beautiful detailed water),((extremely delicate and beautiful girls)),",
   "大叔魔法30-无限剑制法":",I am the bone of my sword,",
   "大叔魔法31-素墨古风":",Upper body, dramatic angle, female focus, Beijing Opera, (with arms behind), gorgeous Hanfu, wide  sleeves, ((1 girl, Chinese girl, lovely face), delicate muscle lines, beautiful hands, (single bun, tassels, hairpin), (Chinese painting , ink painting, splash, splash, sketch, dye), (color) watercolor painting, (((illustrations, masterpieces, high quality, beautiful paintings, complicated  details, original works))",
   "大叔魔法32-鬼角女孩":",(((masterpiece))), best quality, illustration,{{{highly detailed}}},extremely detailed CG unity 8k  wallpaper,((ultra-detailed)),{{depth of field}}, (((beautiful detailed eyes))), 1girl,{{{{ two medium oni horn}} }}, {horn},{{{solo}}},{{aka   oni}},{white hair},{{crystal clear hair}},long hair, {beautiful detailed  eyes},{{{{{church}}}}},{{Gorgeous background}},{{{a little Expose  chest}}},expressionless,{{elegent}},{{black  red dress}},black ribbon,face stain with little blood,{{{wholesale slaughter}}},backround higanbana,{{Ukiyoe's cloud}},{{Red eye shadow} }",
   "大叔魔法33-国风少女":",((masterpiece)), ((best quality)), ((masterpiece)), ((best quality)), ((official  art)), (extremely detailed CG unity 8k wallpaper), ((ultra-detailed)), ((illustration)), traditional chinese painting,((Chinese wind)), ((a girl)), (single), staring, fairy,hair_ornament, earrings, jewelry, very long hair, messy_hair, bare shoulders, ribbons,hairs between eyes , beautiful detailed sky,full body,close-up,arms behind back,Taoist robe, thighs,ribbon, bare shoulders, aloft, mist-shrouded,chinadre,overexposure,{wet  clothes},medium breast,solo,{doll},Bare thigh,best quality,highly detailed,masterpiece,ultra-detailed,illustration,incredibly_absurdres,intense angle ,pleated dress,chinese style architecture ,single hair bun,white_hair,red_eyes,sideways glance,cold attitude,eyeshadow,eyeliner,eyes visible through hair,no shoes,ribbon-trimmed sleeves,earrings,necklace,tiara,medium_breasts,sunlight ,reflection light,ray tracing,loli,Phoenix crown and rosy robe,blush",
   "大叔魔法34-国风建筑":",((masterpiece)), ((best quality)), ((masterpiece)),((official art)), (extremely detailed  CG unity 8k wallpaper), ((ultra-detailed)), ((illustration)), traditional chinese painting,((Chinese wind)),beautiful detailed sky,aloft, mist -shrouded,chinadress,overexposure, highly detailed,masterpiece,ultra-detailed,illustration,intense angle,chinese style architecture,sunlight,reflection light,ray tracing,((Outdoor)),White Jade  Capital in the sky, five cities on the twelfth floor,((macroscopic)),overlook,The Milky Way is bright,Bright lights,night,bright moon,the  purple air comes from the east -- a propitious omen,((prospect))",
   "大叔魔法35-紫晶女巫":",((illustration)), ((floating hair)), ((chromatic aberration)), ((caustic)), lens flare,  dynamic angle,  ((portrait)),  (1 girl), ((solo)), cute face, ((hidden hands)), asymmetrical bangs, (beautiful  detailed eyes), eye  shadow,  ((magic_circle)), (floating glass fragments), ((colorful refraction)), (beautiful detailed sky), ((dark  intense shadows)), ((cinematic lighting)), ((overexposure)), (expressionless),  blank stare, big top sleeves, ((frills)), ( ((small breast))), ((sharp focus)), ((masterpiece)), (((best quality))), ((extremely detailed)), colorful, hdr ,(magnificent clothes),(frills),(chtholly),(long purple hair),((black witch hat)),(((witch))),((cloak)),(ribbon- trimmed sleeves),earrings,black_feathers,",
   "大叔魔法36-少女水果汽水":",((masterpiece)), best quality, (beautiful water), (extremely detailed CG unity 8k wallpaper,masterpiece, best  quality, ultra-detailed), (best illumination, (best shadow), an extremely delicate and beautiful), ((detailed clothes, ((detailed face)),  detailed eyes, detailed background, detailed skin)), ((water eyes)), floating hair, neck ribbon, handled hair, dynamic pose, beautiful face , extremely_beautiful_detailed_anime_face, cute face, bright skin,((lemon slice):1.6), ((ice block):1.4),   ((Splashing bubbles):1.2),(( 1girl ) ), (((yellow hair))), yellow eyes, very long hair, bikini, ((upper body):1.3),",
   "大叔魔法37-赛博朋克·雨":",masterpiece, best quality, ultra-detailed,1girl,beautiful detailed girl,(teen),detailed eyes,glowing eyes,(cyberpunk  clothes",
   "大叔魔法38-赛博朋克风":",{{ write or paint realistically }} ,{{ Hi-Q(high quality) }},{{ The  masterpiece }}, {best quality}, {{masterpiece}} true-life ,cyberpunk,white hair,Red pupil,1girl,sideways,Delicate face,Perfect skin,Highly detailed, glow,The perfect eye,Detailed clothing,Shadows of reality,neon lamp,The floating hair,The perfect background,The perfect outfit,gorgeous costume,Colorful costumes,Colorful  clothes,Detailed background,pinnacle of work,incredibly_absurdres,colorful,",
   "大叔魔法39-链金银术":",(((masterpiece))),best quality, illustration,(beautiful detailed girl), a girl ,solo,bare shoulders,flat_chst ,diamond and glaring eyes,beautiful detailed cold face,very long blue and sliver hair,floaing black feathers,wavy hair,black and white sleeves,gold and  sliver fringes,a (blackhole) behind the girl,a silver triple crown inlaid with obsidian,(sit) on the black ((throne)), (depth ) of (field)",
   "大叔魔法40-断墨水风":",dramatic angle,(fluttered detailed ink splashs), (illustration),(((1 girl))),(long hair),( rain:0.6),(expressionless ,hair ornament:1.4),there is an ancient palace beside the girl,chinese clothes,(focus on), color Ink wash painting ,(ink splashing),color splashing,((colorful)),[sketch], Masterpiece,best quality, beautifully painted,highly detailed,(denoising:0.7),[splash ink],yin  yang,",
   "大叔魔法41-锁链蛇环":",(extremely detailed CG unity 8k wallpaper),masterpiece,best quality,ultra-detailed,(best illumination),best shadow,an  extremely delicate and beautiful,dynamic angle,floating,finely detail,(bloom),(shine),glinting stars,classic,(painting),(sketch),Depthoffield,1girl,(Medusa),solo, (Long green snake like hair),Glowing eyes,Big eyes,(Strange eyes emitting purple light),Beautiful and cold face,Loose hair,Floating green smell, Bare shoulders,extremely delicate and beautiful girls,beautiful detailed eyes,glowing   eyes,(((Chain))),((Black rope)),(cage),(blood),(Higanbana ),(snake)",
   "大叔魔法42-色块分离法":",(((masterpiece))), best quality, illustration,{{{highly detailed}}},((ultra-detailed)),( 1girl:1.5),beautiful girl,{{{{Color blocks are separated by clear black lines}}}},{{{{Gorgeous hair,(((Hair color patches  are separated by clear black lines)))}}}},aqua theme,beautiful eyes,Sportiness,{{solo}},{{colorful}},{{{{{ligne Claire} }}}},{{{Hierarchical color blocks}}},{{Bright color}},{{Color to draw shadow effect}},{{{{Clear and powerful shadow  lines}}}},{{{background(blue sky)}}},{{color block stroke}},{{Clear color block}},{{{style of COGECHA}} },Draw the light dark boundary,{{Vector illustration}},{{{{Thick and clear black lines}}}},{{{{{Each color block is  clearly distinguished}}}}},{{black lines are drawn on the edge of each color block}},{{{Clear hair}}},{{Hair  black edge stroke}},{{Exaggerated color}}",
   "大叔魔法43-湿身连体风":",overexposure,{wet clothes},medium breast,solo,{doll},Bare thigh,best quality,highly detailed,masterpiece,ultra- detailed,illustration,",
   "大叔魔法44-湿身风A":",((extremely detailed CG unity 8k wallpaper)),masterpiece,(an extremely delicate and beautiful),floating hair,dynamic  angle,cinematic lighting,(wet),wet clothes,see-through raincoat,((ropiness)),slime,substance,((1girl)), long while hair, messy_hair, on  the ocean, beautiful detailed eyes, undressing, transparent,heart in eye, heart-shaped pupils, sex,underwear,breast_grab,rain,Take a shower,((reflective eyes )), ((hair dripping)), water eyes,drunk,light blush",
   "大叔魔法45-湿身风B":",original, masterpiece,best quality,official art,(extremely detailed CG unity 8k wallpaper), (extremely fine and  beautiful:1.2),(beautiful and clear background:1.3),floating hair,(dynamic angle:1.3),cinematic lighting,(medium breast),(wet),wet clothes,(see- through raincoat:1.2),(water drips on the screen:1.3),strong rim light, ((ropiness)),(slime:1.2),((1girl)), (very  long hair:1.3),(white hair), (messy_hair:1.3), (on the ocean:1.1), (beautiful detailed eyes:1.2),  undressing,     transparent,heart in eye,    heart-shaped pupils,   (beautiful detailed face:1.3),sex,underwear,hand on own chest,rain,Take a shower ,(reflective eyes:1.3), (hair dripping:1,2), water eyes,drunk,light blush,",
   "大叔魔法46-海之舞法":",{{detailed background}},{{{looking at viewer}}},{{{facing viewer}}},{{{{{ {cloes to}}}}}}},cinematic lighting, volume lighting, bloom effect, light particles,masterpiece,{{{{highres}}}},Unity Creations,contour deepening ,high contrast,game cg,{{{{extremely detailed CG unity 8k wallpaper}}}},intricate detail,{{solo}},{shark gril},{Translucent open  navel dress made of tulle},barefoot sandals,{The dance skirt with wavy lines is made of silk},{Ribbon made of tulle},{small_breasts} },{Delicate skin},beautiful detailed eyes,{{shed tears}},{White hair},{Blue eyes},Pick dyeing,A few wisps of blue hair, {shark hair ornament},{Wet clothes},{shark hood},looking_at_viewer,Bubbles, beautiful and detailed bubbles, beautiful and detailed oceans, beautiful and   detailed   corals , corals, seaweeds, sea beds, gravels, { top-down light }, { light tracing }, {dim light}, beautiful and detailed water ,Ray refraction,Dream like benthos,Transparent fish,{Purple glowing jellyfish},Pearl,gemstone,{Trapped in  bubbles},ocean bottom,tropical fish,kentaurosu,fairey swordfish, clownfish ,seaweed,{Dreamy},Magic Array,Magic jewel,{Huge clock},{clocks and watches},Pointer,Crystal ball,Chain,Eye shadow,10s",
   "大叔魔法47-病娇女孩":",{{masterpiece}},1 girl,best quality,Stain blood on the body,Yandere,Yandere smiles,",
   "大叔魔法48-秋收野营术":",((illustration)), ((floating hair)), ((chromatic aberration)),(extremely detailed CG unity 8k wallpaper ),1girl, autumn, autumn_leaves, bare_tree, black_hair, burning, campfire, cherry_blossoms, evening, falling_leaves, fire, flame, forest, ginkgo_leaf, gradient_sky, holding_leaf,  leaf, long_sleeves, maple_leaf, molten_rock, nature, orange_flower, orange_sky, orange_theme, outdoors, petals, river, scenery, sky, solo, standing, sunset, tree,  twilight, water, wisteria",
   "大叔魔法49-V领烟雨江南":",(((masterpiece))), (((best quality))),dynamic angle,1girl,(solo), china_dress, chinese_clothes, (lake), mountainous_horizon,((hands_behind_back)),blue_hair, green_hair, gradient hair, ((rain)),green_eyes,blue eyes,smile,((wet_hair)),((wet_clothes)),  depth of field,(medium_breasts),upper_body,skinny,overcast,((watercolor_\(medium\))),from_side,looking_at_viewer,((yellow moon)),(full_moon),(robe with an  intricate pattern),necklace,chinese girl,transparent,cleavage,jewelry,pendant, (((masterpiece))), (((best quality))),dynamic angle,1girl,(solo),  china_dress, chinese_clothes,(lake), mountainous_horizon,((hands_behind_back)),blue_hair, green_hair,((rain)),green_eyes,blue eyes,smile,((wet_hair)),((wet_clothes)),  depth of field,bare_arms,bare_shoulders,(medium_breasts),upper_body,skinny,overcast,((watercolor_\(medium\))),from_side,looking_at_viewer,yellow_moon,full_moon",
   "大叔魔法50-高领烟雨江南":"(((masterpiece))), (((best quality))),dynamic angle,1girl,(solo), china_dress, chinese_clothes,( lake), mountainous_horizon,((hands_behind_back)),blue_hair, green_hair, gradient hair, ((rain)),green_eyes,blue eyes,smile,((wet_hair)),((wet_clothes)),  depth of field,bare_arms,bare_shoulders,(medium_breasts),upper_body,skinny,overcast,((watercolor_\(medium\))),from_side,looking_at_viewer,((yellow moon)),(full_moon),(robe  with an intricate pattern),necklace,chinese girl, (((masterpiece))), (((best quality))),dynamic angle,1girl,(solo), china_dress, chinese_clothes ,(lake), mountainous_horizon,((hands_behind_back)),blue_hair, green_hair,((rain)),green_eyes,blue eyes,smile,((wet_hair)),((wet_clothes)), depth of  field,bare_arms,bare_shoulders,(medium_breasts),upper_body,skinny,overcast,((watercolor_\(medium\))),from_side,looking_at_viewer,yellow_moon,full_moon,",
   "大叔魔法51-老男人的魅力A":",best quality,masterpiece,ultra-detaild,young man,gentleman,young man,  black coat,handsome man,male focus  on,gorgeous hat,(macro shot:1.5),middle aged man,Realistic, medal,sacrificial clothing,whiskers,father,wide shoulder,,(1man:1.5),solo,precious robe, extremely detailed CG,clock tower,crisscross streets,detailed light, shabby building,character focus,detailed background,vast city, floated hair,castle,",
   "大叔魔法52-老男人的魅力B":",best quality,masterpiece,tight white gloves,ultra-detaild,delicate and handsome face,general,lean face,belt,diagonal  leather  bag,short hair,Shining eyes,serious expression,Ferocious eyes,scary scar through eyes,weather-beated face,epaulet,detailed eyes,glory ribbon,Military trousers,young  man,Military uniform,man,handsome man,male focus on,army cap,middle aged man,Realistic",
   "大叔魔法53-水下魔法":",(((masterpiece))),(((best quality))),((ultra-detailed)),((underwater)),(illustration), (beautiful detailed water),((coral)),open tuck,((extremely delicate and beautiful girls)),dynamic angle,floating,(beautiful detailed eyes),(detailed light ),(loli),floating hair,glowing eyes,pointy ears,(splash),underwater),((fishes)),white hair,green right eye,iceblue left eye,leaves dress ,feather,nature,(sunlight),(underwater forest),(painting),(bloom),(detailed glow),drenched,seaweed,fish,(((Tyndall effect))),face to face ",
   "大叔魔法54-水中魔法":",{{best quality}}, {{masterpiece}}, {ultra-detailed}, {illustration}, ((underwater)),{a  girl},{{beautiful detailed eyes}}, {detailed light},upper body, altocumulus,clear sky,shiny hair, colored inner hair, (Brilliant light),glass  tint,((Ambient light)),((Colorful blisters)),depth of field,",
   "大叔魔法55-水晶魔法A":",masterpiece,{{{best quality}}},(illustration)),{{{extremely detailed CG unity 8k wallpaper}}},game_cg ,(({{1girl}})),{solo}, (beautiful detailed eyes),((shine eyes)),goddess,fluffy hair,messy_hair,ribbons,hair_bow,{flowing hair},  (glossy hair), (Silky hair),((white stockings)),(((gorgeous crystal armor))),cold smile,stare,cape,(((crystal wings)) ),((grand feathers)),((altocumulus)),(clear_sky),(snow mountain),((flowery flowers)),{(flowery bubbles)},{{cloud map plane} },({(crystal)}),crystal poppies,({lacy}) ({{misty}}),(posing sketch),(Brilliant light),cinematic lighting,((thick_coating)), (glass tint),(watercolor),(Ambient light),long_focus,(Colorful blisters),ukiyoe style",
   "大叔魔法56-水晶魔法B":",(world_masterpiece),(((best quality))) ,(illustration),(ultra-detailed) ,extremely detailed CG unity 8k wallpaper,((1girl)), (many crystals),crystal butterfly wings,(((crystal palace))),crystal butterfly,petal flowing,crystal necklace,(((upper body))),crystal flower,crystal eye and Silk hair,(many jewels on the ground),hidden hands",
   "大叔魔法57-凤凰战法":",Please draw a picture, a very detailed CG unified 8k wallpaper, (masterpiece), the best quality,  illustration,Chinese painting, splash, color splash, (phoenix background), (1 girl 1.3), moist skin, expressionless, (golden eyes), complex patterns,  phoenix girl, feather headdress, shawl, scorched, chest, beautiful details, eyes, fine details, very close to the audience, standing, fighting state , Full of tension",
   "大叔魔法58-仙法草术":",masterpiece, {best quality}, Amazing, beautiful detailed eyes, finely detailed, Depth of field, extremely detailed  CG unity 8k wallpaper,",
   "大叔魔法59-冬日时光":",(masterpiece), best quality, (illustration),Amazing, (((1girl))),(((solo))), (beautifully  detailed eyes), cinematic lighting,finely detail, Depth of field, extremely detailed CG unity 8k wallpaper, city at night,(((blonde hair))) ,((blue eyes)), long_hair, (beautifully detailed eyes), beautifully detailed sky, cinematic lighting, glowing eyes, brown coat, red scarf, glowing  eyes, lights, earrings, winter, lamp, beautifully detailed city,   The fluttering snowflakes, upper body, masterpiece, best quality",
   "大叔魔法60-冰火双法":",((ink)),((watercolor)),{{best quality},(expressionless),((illustration)),(beautiful detailed girl) ,(beautiful detailed eyes),world masterpiece theater,depth of field,(blue spark),anime face,black gauze skirt,(red and blue hair),blue eyes ,focus_on_face,medium_breasts,(((((messy_long_hair))))),Bare shoulder,very_close_to_viewers,burning sky,navel,((bustier)),flame,Rainbow in the sky,((Flames burning  ice)),(((Fire  butterflys ))),(((ice crystal texture wings))),(Flying sparks),(detailed ice),{{a lot of  luminous ice crystals}},((burning feathers)),{feathers_made_of_ice},(frozen feathers),{{{ice and fire together}}",
   "大叔魔法61-冰系魔改":",(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow,detailed ice,beautiful  detailed water,(beautiful detailed eyes),expressionless,beautiful detailed white gloves, (floating palaces:1.2),azure hair,disheveled hair,long bangs, hairs between eyes,  (skyblue dress),black ribbon,white bowties,midriff,{{{half closed eyes}}},,big forhead,blank stare,flower,large top sleeves,(((ice  crystal texture wings))),{{{{{{{{Iridescence and rainbow hair:2.5}}}}}}},{{{{{{detailed cute anime face}} }}}},{{loli}},{{{{{watercolor_(medium)}}}},(((masterpiece)))",
   "大叔魔法62-冰系魔法":",(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow,detailed ice,beautiful detailed  water,(beautiful detailed eyes),expressionless,(floating palaces),azure hair,disheveled hair,long bangs, hairs between eyes,(skyblue dress),black ribbon,white  bowties,big forhead,blank stare,flower,large top sleeves,(low twintails),beautiful bule eyes,flat_chest,((((1 girl))), (solo), very  long blue and sliver hair,",
   "大叔魔法63-冰之魔法":",(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow,detailed ice,beautiful detailed  water,(beautiful detailed eyes),expressionless,(floating palaces),azure hair,disheveled hair,long bangs, hairs between eyes,(skyblue dress),black ribbon,white  bowties,midriff,{{{half closed eyes}}},big forhead,blank stare,flower,large top sleeves",
   "大叔魔法64-烟雨江南":",(((masterpiece))), (((best quality))),1girl,(solo), depth of field,((watercolor)) ,",
   "大叔魔法65-风雪公主":",{{mterpiece}}, {{{best quality}}}, {{ultra-detailed}}, {{illustration}}, ((disheveled  hair)), ((frills)),  dynamic angle, big top sleeves, floating, beautiful detailed sky, on beautiful detailed snow,{{princess}}" ,
   "大叔魔法66-风雪神咒":",(highres:1.5), highly detailed, (solo:1.5),(masterpiece:1.5),(best quality:1.5), Amazing,  extremely detailed wallpaper, an extremely delicate and beautiful, 1girl ,((high resolution illustration)), (bishoujo), (long hair), black hair, ( game cg), medium_breasts, visible through hair,((red eyes,glowing eyes)), bangs, serious face, (((Chinese cloth: 1.5, white shirt ,detached sleeves, long sleeves,bare shoulders, hair_ribbon, hair_ornament))),hair between eyes, (snow forest),(watercolor:0.7),winter {fighting_stance}",
   "大叔魔法67-夏夜之狐":",original, (masterpiece), (illustration), (extremely fine and beautiful), (perfect details), (unity CG  8K wallpaper:1.05), (beautiful and clear background:1.25), (depth of field:0.7), (1 cute girl with (2 fox ear:0.9 ) and (fox tail on the back:1.2) stands aside the river:1.15). (cute:1.3), (detailed beautiful eyes:1.3), (beautiful  face:1.3), silver hair, silver ear, (pink hair:0.7), (pink ear:0.7), long hair, (japanese kimomo:1.25), ( hair blowing with the wind:1.1), (blue eye:1.1), (little girl:1.1), butterflys flying around, (moon light:0.6), tree,  (summer), (night:1.2), (close-up:0.35), (gloves:0.8), solo",
   "大叔魔法68-彼岸花法":",(((masterpiece))),((best quality)), (beautiful detailed eyes),(illustration),high contrast,(extremely detailed  CG unity 8k wallpaper),expressionless,(cinematiclighting),((beautiful detailed sky)),long hair,(solo),(((kimono))),(((miko))), red eyes,dramatic angle ,depth of field,Flying petals, wind,(sparkle background),(fog),(red spider lily),(((Girl holding flower)) ),",
   "大叔魔法69-彼岸花海":",(((masterpiece))),(((best quality))),((ultra-detailed))((extremely detailed CG)),(( 8k_wallpaper)),dynamic angle,floating, (beautiful detailed eyes),an extremely delicate and beautiful girl,upper body,ink wash painting,(Chinese wind),black   eyes ,burning,detailed light,(black hair),(red spider lily:1.25),aqua eyes,(hair flower:1.3),bloom,single,starry sky,hair ornament, earrings,  jewelry, very long hair, messy hair, bare shoulders, half closed eyes,bloom,(((Chivalrous))),fairy,(hanfu:1.3),(medium breast: 1.2),(eyeshadow,red eyeliner:1.15),(eyes visible through hair:1.2),((solo))",
   "大叔魔法70-空之精灵":",best quality,highly detailed,masterpiece,ultra-detailed,illustration,1 girl,small breast,beautiful and delicate water,ultra-detailed, beautiful detailed eyes,beautiful detailed water,masterpiece,bare_shoulder,frills,randomly distributed clouds,ink,extremely detailed,side blunt bangs,feather,Bright stars,skyblue dress,cinematic lighting, blue eyes,starry detailed water,beautiful detailed sky,beautiful detailed glow,dynamic angle,best quality,8k_wallpaper,depth of field,starry sky,extremely detailed CG unity  8k wallpaper,best illustration,extremely detailed CG,loli,shine,sunlight,world masterpiece theater,white_hair,extremely_detailed_eyes_and_face,glowing eyes,an extremely delicate and beautiful,white bowties",
   "大叔魔法71-空间冰法":",[[majamari]],((illustration)), ((floating hair)), ((chromatic aberration)), ((caustic)) , lens flare, dynamic angle,  ((portrait)),  (1 girl), ((solo)), cute face, ((hidden hands)), asymmetrical  bangs, (beautiful detailed eyes), eye shadow, ((huge clocks)),  ((glass strips)), (floating glass fragments), ((colorful  refraction)), (beautiful detailed sky), ((dark intense shadows)), ((cinematic lighting)), ((overexposure)), (expressionless),  blank stare , big top sleeves, ((frills)), hair_ornament,ribbons, bowties, buttons, (((small breast))), pleated skirt, ((sharp focus)) , ((masterpiece)), (((best quality))), ((extremely detailed)), colorful, hdr,(((crystals texture Hair))),Crystallization of  clothes,{{{{Crystalline purple gemstone gloves}}}},(gemstone of body), ((Detailed crystallized clothing))",
   "大叔魔法72-空间魔法":",((illustration)), ((floating hair)), ((chromatic aberration)),  ((caustic)), lens flare,   dynamic angle,  ((portrait)),  (1 girl), ((solo)), cute face, ((hidden hands)), asymmetrical bangs, (beautiful  detailed eyes), eye shadow, ((huge clocks)),  ((glass strips)), (floating glass fragments), ((colorful refraction)), (beautiful  detailed sky), ((dark intense shadows)), ((cinematic lighting)), ((overexposure)), (expressionless),  blank stare, big top sleeves , ((frills)), hair_ornament, ribbons,   bowties , buttons, (((small breast))), pleated skirt, ((sharp focus)), ((masterpiece) ), (((best quality))), ((extremely detailed)), colorful, hdr",
   "大叔魔法73-血歌禁术":",((best quality)), ((masterpiece)), ((ultra-detailed)), (illustration), (detailed light) , (an extremely delicate and beautiful),((solo)),a girl",
   "大叔魔法74-血之公主":",8k Wallpaper,grand,(((masterpiece))), (((best quality))), ((ultra-detailed)), ( illustration), ((an extremely delicate and beautiful)),((full body,)),dynamic angle,detailed cute anime face,((loli)),(((masterpiece) )),an extremely delicate and beautiful girl,white hair,long hair,red eyes,smile,[sharp teeth],small breast,black clothes,black headwear,black hairband ,(white lace gloves),((((((((((loil)))))))))),colored inner hair,orange_hair ornament,rose adorns hair,((( (vampire)))),(((white BugBats))),solo focus,corrugated,Flying red petals,Holy lighting,(covered in blood),oken glass,(broken screen) ,transparent glass,((((broken white clock)))),(roseleaf),(Blood drop)),((Blood fog)),(black smoke),((Black feathers  floating in the air)),(Fire butterflies),((((flame melt)))),((wind))",
   "大叔魔法75-血之魔法1":",((solo)),best quality,Amazing,1girl,extremely detailed CG unity 8k wallpaper, masterpiece,(loli),(white  hair),(((red streaked hair))), red eyes, (((full body))),(red hair), (((((Hold a red  sword))))), (angry face),(beautiful detailed eyes), ((Blood drop)),((Blood fog)),light shafts, soft focus, character  focus,disheveled hair,long bangs, hairs between eyes, looking at viewer,lowing hair,((Splashing blood))),Long hair,((Bloodstain)),Fighting  stance,{{{{{watercolor_(medium)}}}},(((masterpiece))),((white clock)),((ultra-detailed)),((Covered in blood)), flowing hair,Exquisite Flame, {{{{{{extremely beautiful detailed anime face}}}}}},dynamic angle, floating, (shine), extremely delicate and  beautiful girls, bright skin, (best illustration), (best shadow), finely detail, Depth of field (bloom), (painting),{ very delicate  light, perfect and delicate limbs},beautiful detailed dress,Flying red petals,Holy lighting",
   "大叔魔法76-血之魔法2":",masterpiece, best quality, best quality,Amazing,1girl,finely detail,Depth of field,extremely detailed CG unity 8k  wallpaper, masterpiece, full body,(loli),(white hair), red streaked hair, red eyes, (full body),red hair, (((with  sword))),   angry face,(beautiful detailed eyes), Blood drop,Blood fog, floating hair,light shafts, soft focus, character focus,disheveled hair, long bangs, hairs between eyes, looking at viewer,lowing hair, floating, Splashing blood,Long hair,(Bloodstain)",
   "大叔魔法77-美人鱼法1":",{long hair},{revealing dress}, {elbow gloves },{{{{beautiful mermaid}}}},{smirk}, {nose blush },stretch,Bare arms,Bare navel, (incredibly_absurdres), best quality,beautiful detailed eyes, blue_hair, (highly  detailed beautiful fishtail:1.6),   (((human hands))), (((masterpiece))), (blue_eyes), ((medium_breasts)), (the lower body is a fish:1.9)AND(no  human thigh:1.2), seaweed, (full body), (white seashell), (curved and slender fish tail), (the lower body is bare: 1.1), {beautiful tailfin}, ((underwater)), (illustration), detailed water, ((a extremely delicate and beautiful girl)), (underwater forest) , ((sunlight)), ((fishes)), (floating), watercolor_(medium), ((an extremely delicate and beautiful)), ((coral)), floating  hair, glowing eyes, (splash), (detailed glow), ((Tyndall effect)), (landscape), hair_ornament, (small whirlpool), ((The sensation  of water flowing)), (detailed scales on a mermaid)",
   "大叔魔法78-美人鱼法2":",(((masterpiece))),(((best quality))),((ultra-detailed)),((underwater)),(illustration), (beautiful detailed water),((solo)),((1girl)), {solo},(loli), (((detailed anima face))),(white hair), disheveled  hair, hairs between eyes,(messy hair),   long hair,blue eyes, (beautiful detailed eyes), ((Gradient color eyes)),((((  girl in the huge shell)))), {Mermaid ears},Flosse Hand,bare shoulders, white stockings, white dress, ((detailed clothes)),wet  clothes,arms behind back,(sunlight),(underwater forest),(painting),(bloom),(detailed glow),drenched,seaweed,(jellyfish),watercolor_(medium),detailed background,fluttered  detailed splashs, beautiful detailed sky,,Crystallization of clothes,{{{{Crystalline purple gemstone gloves}}}},(gemstone of body), ((Detailed crystallized  clothing)),((dark intense shadows)), ((cinematic lighting)),",
   "大叔魔法79-美人鱼法3":",(((masterpiece))),(((best quality))),((ultra-detailed)),((underwater)),(illustration), (beautiful detailed water),((solo)),((1girl)),(loli), (((detailed anima face))),(white hair), disheveled hair, hairs  between eyes,(messy hair), long hair,blue eyes, (beautiful detailed eyes), ((Gradient color eyes)), (((Mermaid ears))) ,((flippers)),,{{{{diaphanous blue gloves}}}}",
   "大叔魔法80-白虎画1":",((masterpiece)),best quality, ((illustration)),,original,extremely detailed wallpaper,(((beijing opera))),  (sketch),(wash painting),((color splashing)),((ink splashing)),((((dyeing)))),((Chinese painting)),((colorful)) (beautiful and delicate mountain),(solo),(Fantasy creatures),((Chinese white tiger)),(solo;1.8),Black markings,(white tiger),((solo) ),beautiful and delicate golden eyes,Huge clawsBig and strong,Diabolical,Tyrannica,(mountains),",
   "大叔魔法81-白虎画2":",((masterpiece)),((best quality)),(ultra-detailed),(illustration),((an extremely delicate and beautiful) ),(((beijing opera))), ((sketch)),((wash painting)),((ink splashing)),((((dyeing)))),((Chinese painting )),{{Big and strong and white tiger}} ,solo,Diabolical,(huge legendary tiger King),(tiger and tiger),（Golden tiger eyes）, (A fierce tiger),dynamic angle, {chinese legendary},{ferocious},Ambient light,fog,[cloud],mountain,Pine trees on the cliff",
   "大叔魔法82-春之猫1":",original, (masterpiece), (illustration), (extremely fine and beautiful), perfect detailed, photorealistic, (beautiful and  clear background:1.25), (depth of field:0.7), (1 cute girl with (cat ear and cat tail:1.2) stands in the garden :1.1), (cute:1.35), (detailed beautiful eyes:1.3), (beautiful face:1.3), casual, silver hair, silver ear, (blue hair: 0.8), (blue  ear:0.8), long hair, coat, short skirt, hair blowing with the wind, (blue eye:1.2), flowers, ( little girl:0.65), butterflys flying around",
   "大叔魔法83-春之猫2":",original, (masterpiece), (illustration), (extremely fine and beautiful), perfect detailed, photorealistic, (beautiful and  clear background:1.25), (depth of field:0.7), (1 cute girl with (cat ear and cat tail:1.2) stands in the garden :1.1), (cute:1.35), (detailed beautiful eyes:1.3), (beautiful face:1.3), casual, silver hair, silver ear, (blue hair: 0.8), (blue ear:0.8), long hair, coat, short skirt, hair blowing with the wind, (blue eye:1.2), flowers, ( little girl:0.65), butterflys flying around",
   "大叔魔法84-秋水法1":",((masterpiece)), ((best quality)), ((ultra-detailed)), (super fine illustration), extremely  detailed CG unity 8k wallpaper , (an extremely delicate and beautiful) ,(((ink))) ,(((((water color))))) ,  ((((falling yellow leaves)))) , (((breeze))) , ((reflective water)) , ((beautiful and delicate water)) ,  (depth of field) , (upper body :1.2) , (lens flare) , (((1 girl))) , (solo) , (young  girl) , medium_breasts , bare shoulders , (hanfu:1.2) , (blue hair:1.2) , hair between eyes , ((messy hair)) ,  (blue eyes:1.2) , detailed eyes , detailed comic face , wide sleeves , long sleeves , ((gold hair stick)) ,(blue  ribbon) , (blue tassel) , outdoors , backlighting , sitting , middle finger , (light particles:1.2) , (((wet)))  , ((lotus)) , ((ripples ))",
   "大叔魔法85-秋水法2":",(masterpiece)), ((best quality)), ((ultra-detailed)), (((super fine illustration))),  extremely detailed CG unity 8k wallpaper , (an extremely delicate and beautiful) ,(((ink))) ,(((water color))) , ( (((falling yellow flowers)))) , ((breeze)) , ((reflective water)) , ((beautiful and delicate water)) , (depth  of field) , (upper body :1.2) , (lens flare) , (((1 girl))) , (solo) , (young girl)  , medium_breasts , bare shoulders , (hanfu:1.2) , (blue hair:1.2) , hair between eyes , ((messy hair)) , (bloned  eyes:1.2) , detailed and beautiful eyes , wide sleeves , long sleeves , ((gold hair stick)) ,(blue ribbon) , ( blue tassel) , outdoors , backlighting , sitting , middle finger , (light particles:1.2) , (((wet))) , ((lotus))  , ((ripples )) ((rain))",
   "大叔魔法86-银杏法":"{{best qualiy}},{{masterpiece}},{{ultra-detailed}}, extremely detailed CG, extremely detailed 8K wallpaper,  HD background,Crowds,artbook,Birds in the background,{an extremely delicate and beautiful},{{one girl}},The skirt sways with the wind,Fine  clouds,Beautiful and meticulous starry sky,Archaic wind,Extremely detailed background,chinese style architecture ,Overexposure,intricate detail,Raytracing,{Traditional Chinese Costume},hair ornament, tassel,black long hair,intricate detail,{gorgeoushanfu},{Long sleeve},{{Hidden hand}},Reflective,blush,Fixed angle of view,Expressionless,Jelly like light  lipstick,Extremely detailed shadows,{single sidelock},sparkle,{{{Ginkgo biloba}}},{{{ginkgo trees}}}, flying and falling, golden and beautiful, The leaves falling slowly in the wind,{{{Ginkgo}}},{{Beautiful and light fallen leaves}},{{autumn}},{The golden sunshine}, {A warm wind},{The vigorous tree trunk},",
   "大叔魔法87-银杏法":"{{best qualiy}},{{masterpiece}},{{ultra-detailed}}, extremely detailed CG, extremely detailed 8K wallpaper,  HD background,Crowds,artbook,Birds in the background,{an extremely delicate and beautiful},{{one girl}},The skirt sways with the wind,Fine  clouds,Beautiful and meticulous starry sky,Archaic wind,Extremely detailed background,chinese style architecture ,Overexposure,intricate detail,Raytracing,{Traditional Chinese Costume},hair ornament, tassel,black long hair,intricate detail,{gorgeoushanfu},{Long sleeve},{{Hidden hand}},Reflective,blush,Fixed angle of view,Expressionless,Jelly like light  lipstick,Extremely detailed shadows,{single sidelock},sparkle,",
   "大叔魔法88-萌兽咒1":",{sunlight},chibi,solo, {{extremely light},transparent glass,flowers,night,Full moon night,moonlight,{{anime  cat, anime style, cat,silver, anime eyes, blush, japanese, pixiv, scorbunny style,sylveon style,rockruff style,raichu style, Flareon style,  jewelpet style,extremely detailed CG unity 8k ,wallpaper,Red Ribbon,Chinese knot collar, red scarf,eastern,asia,acient china,{{komasan,Komane}},Chinese  style cloth,shy}}",
   "大叔魔法89-萌兽咒2":",spring day,sakura,forest,lake,beautiful detailed sky,looking_at_sky,{{anime cat, anime style, cat, anime  eyes, blush, japanese, pixiv, alolan vulpix style,sylveon style,rockruff,fennekin style, Flareon style, jewelpet style,extremely detailed CG unity 8k ,wallpaper ,knock down,fall to the ground,both eyes closed,bell collar, red scarf,happy}},running",
   "大叔魔法90-黄昏法1":",(((ruins))), ((masterpiece)), (illustration), (highres), (((best quality))),  (disheveled hair), ((ultra-detailed)), (beautiful detailed red eyes), 1girl, (((metal frame black and red armour))),  black hair, blood on face,  cloud, ((embers)), hair between eyes, (((burning sword))), long hair, (((solo ))), (((sunset))), ((upper body)), (breeze), overexposure, (complex pattern), medium breasts, (lighting particle),  (lens flare), (red  torn cape), (looking at the viewer), (chromatic aberration),   depth of field, (profile), upper   body , ((bishoujo)), expressionless, bands, (profile),",
   "大叔魔法91-黄昏法2":",{{{masterpiece}}}, {{best quality}}, {{super fine illustration}}, {{beautiful and delicate  water}}, {{beautiful and detailed eyes}, {very detailed light}, {perfect and delicate limbs}, {nature}, {painting}, {water  bloom}, {delicate glow},   {{very fine 8KCG wallpaper}}, lavender eyes, peach pink pupils, whole body, white hair, luminous eyes , an extremely delicate and beautiful girl, (1 girl), medium chest circumference, dynamic angle, (Violet dress with gold decoration), (long  hair floating everywhere), (beautiful hair decoration), (delicate wet dress), (nsfw), (breeze), long hair blown up, ((messy hair  style)), (long bangs between eyes), wrinkled skirt, Flowers meadow, near the water edge, (((sunset)), (less stars form  a circle), randomly distributed clouds, (rivers), (willows with branches falling into the water)",
   "大叔魔法92-死尸术":",A puppet is playing solo,A zombie is writing poetry,A machine is acting,A human is crying",
   "大叔魔法93-死灵法":",cinematic lighting, ((best  quality)),((single_human_girl)),((((upper_body)))),((extremely_detailed_eyes_and_face)),ink ,(((bone))), (((ribs))), one girl, a young girl, upper body, rose, black hair, blue eyes,curly  hair,greyscale,no shadow, simple background, bright skin,Cherry blossoms",
   "大叔魔法94-自然法":",{{{masterpiece}}}, {{best quality, super fine illustration , beautiful and delicate water,The finest grass }}. ((beautiful eyes)),{ very delicate light, perfect and delicate limbs}, {nature, painting, water spray},{{ fine luminescence  ,very   fine 8K CG wallpaper}},Lavender eyes, pink pupils, whole body, white hair, bright eyes,( (an extremely delicate and beautiful  girl)), ((1 girl)), medium bust, dynamic angle, (white dress with gold decoration), (long hair flowing with the wind,  beautiful hair ornaments, delicate wet skirt, nsfw, breeze, long bangs between eyes), wrinkled skirt, (staring blankly, lovely big eyes),messy_hair ,payot,Lateral braid,(Tulle lace white skirt) Flowers and grass meadow, near the water edge, ((sunset, starry sky in a circle) , randomly distributed clouds, (((river))), splashing water, falling petals",
   "大叔魔法95-入星海":",{{best quality}}, {{masterpiece}}, {{ultra-detailed}}, {illustration}, {detailed light},  {an extremely delicate and beautiful}, a girl, {beautiful detailed eyes}, stars in the eyes, messy floating hair, colored inner hair,  Starry sky adorns hair, depth of field",
   "大叔魔法96-天选术":",Please draw a picture of an exquisite girl in a princess dress with delicate gold metal decorations. She  stands there looking at me",
   "大叔魔法97-白骨法":",cinematic lighting, ((best quality)),((single_human_girl)),((((upper_body)))),((extremely_detailed_eyes_and_face)),(( church)),((annoyed)),((ink)),((illustration)),depth of field,((frown)),((expression)),((red_eyes)),(((( white_hair)))),((extremely detailed)),((watercolor)),((anime face)),(skull_on_dress),(((yokozuwari))),((detailed_skeleton_church)),(((beautiful_detailed_black_gothic_Empire_Waist_Dress ))),(((dramatic_angle))),medium_breast,(8k_wallpaper),((bright_eyes)), (looking_at_viewers),((close_to_viewers)),((masterpiece)),(((((messy_long_hair))) )),((((1girl)))),lens_flare,light_leaks",
   "大叔魔法98-白蛇画":",((masterpiece)),best quality, ((illustration)),,original,extremely detailed wallpaper,(((beijing opera))),  (sketch),(wash painting),((color splashing)),((ink splashing)),((((dyeing)))),((Chinese painting)),((colorful))( beautiful and delicate water),(((a white snake))),((solo)),delicate lines,lake,water,sky,((West Lake)),(Chinese tradional  building)",
   "大叔魔法99-幻之时":",{masterpiece},{best quality},{1girl},Amazing,beautiful detailed eyes,finely detail,Depth of field,extremely detailed  CG,original, extremely detailed wallpaper,loli,white_hair,magic_circle,cat_ears,long_hair,white_hair/yellow_eyes,wand,pentagram,clock, {masterpiece},{best quality},{1girl},Amazing,beautiful  detailed eyes,finely detail,Depth of field,extremely detailed CG,original, extremely detailed  wallpaper,loli, white_hair",
   "大叔魔法100-幻碎梦":",8k Wallpaper,grand,(((masterpiece))), (((best quality))), ((ultra-detailed)), ( illustration), ((an extremely delicate and beautiful)),dynamic angle,rainbow hair,detailed cute anime face,((loli)),(((masterpiece))),an  extremely delicate and   beautiful girl,flower,cry,water,corrugated,flowers tire,broken glass,(broken screen),atlantis,transparent glass",
   "大叔魔法101-月下蝶":",大叔魔法101-月下蝶|extremely detailed CG unity 8k wallpaper, masterpiece, best quality,highly detailed,(thick clouds :1.3),a white moon,white flowers,(a sea of white flowers,floating white petals:1.5), white butterfly,(an extremely beautiful girl:1.5) ,dancing ballet,silver long hair,floating hair,(extremely cute face,extremely detailed face:1.5),chiffon dress,small breasts,petite,aestheticism painting,(full body, female focus,dramatic angle:1.5),moonlight,ray tracing,relastic shadow,",
   "大叔魔法102-月亮法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), ((an  extremely delicate and beautiful)),cinematic angle,floating, (beautiful detailed eyes), (detailed light),cinematic lighting, beautifully detailed sky,",
   "大叔魔法103-月蝶舞":",(((masterpiece))),(((best quality))),((ultra-detailed))((extremely detailed CG)),( (8k_wallpaper))((an extremely delicate and beautiful)),dynamic angle,floating, (beautiful detailed eyes),(Fire butterflies:1.25),",
   "大叔魔法104-冬雪法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration),beautiful detailed  sky ,night,stars,(1girl)((an extremely delicate and beautiful girl)),red eyes,dramatic angle,small breasts,(((full body))),hood ,cold face and white shirt,(((long white hair))),(red hair),(red plum blossom),((winter)),(((snowflakes))) {{{{{{detailed cute anime face}}}}}},cinmatic lighting,((red and white flowers)),hairs between eyes, expressionless, young girl, (((Facing the lens))),(starry sky),((Beautiful face)),((full body)),(sitting),depth_of_field,((colorful)),scenery,hair_flower, lantern,christmas,(starfall)",
   "大叔魔法105-卡牌法":",((best quality)), ((masterpiece)),(highres),ultra-detailed,illustration,extremely,detailed,wallpaper,(an extremely  delicate and beautiful), 1girl,(solo),(Perfect and delicate face), (beautiful detailed deep eyes),upper body,two-tone hair,red and white , shiny hair,Eye shadow, gemstone adorns hair,(Flying Scattered playing card:1.3),(Flying Scattered gold coins),(Regular playing cards),((arms  behind back)),(wind),beautiful and aesthetic,extremely detailed CG,pastel color,sketch,water color",
   "大叔魔法106-古漫法":",{{China}}, {best quality}, {{masterpiece}}, illustration, original, {{90's}}. {{ Aestheticism Painting}}, {{retro artstyle}}, {{{Ink wash painting}}}, Oil Painting, cinematic angle, {{ultra-detailed}}, {{ fluttered detailed ink splashs}}, {peony forest}}, detailed background, extremely beautiful girl, exquisite beautiful face, beautiful detailed eyes, black hair,  scattered long hair, earlock, a faint smile, Meticulous Han Dynasty Costume,  chignon, emerald bracelet, earrings, {extremely detailed 8K wallpaper},",
   "大叔魔法107-末日风":",full body,Blood Mist, background_Urban rooftop,1 girl,despair,blood sakura,((masterpiece)), (((best quality) )), ((ultra-detailed)),  ((illustration)), ((disheveled hair)),Blood Cherry Blossom,torn clothes,crying with eyes open,solo,Blood  Rain,bandages,Gunpowder smoke,beautiful deatailed shadow, Splashing blood,dust,tyndall effect",
   "大叔魔法108-水森法":",(extremely detailed CG unity 8k wallpaper),(((masterpiece))), (((best quality))), ((ultra -detailed)), (best illustration),(best shadow), ((an extremely delicate and beautiful)),dynamic angle,floating, solo,((1girl)),{long  wavy curly hair},expressionless,((white idol dress)), anglesailor dress,(detailed wet clothes),silk shawl,bikini,underboob, frills,cute anime face, blush,(beautiful detailed eyes), (detailed light),feather, nature, (sunlight), river, (forest),(((floating palace))),beautiful and delicate  water,(painting),(sketch),(bloom),(shine),",
   "大叔魔法109-水墨法":",masterpiece, best quality, {{masterpiece}}, best quality,{beautiful detailed eyes},1girl,finely detail,Depth of  field, masterpiece,{extremely detailed CG unity 8k wallpaper},{chinese ink painting},ink and wash",
   "大叔魔法110-水镜术":",{best quality},{{masterpiece}},",
   "大叔魔法111-水魔法":",((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)), ((disheveled  hair)), ((frills)), (1 girl), (solo), dynamic angle, big top sleeves, floating, beautiful detailed sky, on beautiful  detailed water, beautiful detailed eyes, overexposure, (fist), expressionless, side blunt bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders , (((small breast))), detailed wet clothes, blank stare, pleated skirt, flowers",
   "大叔魔法112-火羽术":",(ink and wash style),sharpened,original,((an extremely delicate and beautiful)),detailed face,Perfect details, ((burning flame adorns eyes)),,wind,Flying ashes,Flying flame,(the burning city),((Twilight light)),arms behind back,Flying ashes,Flying  flame,(((1girl))),Infernal,((small breasts)),((flowing light adorns hair)),(floating ashes),young girl,shiny hair,bright pupils ,((photorealistic)),(((ultra-detailed))),((illustration)),(((masterpiece))),(((best quality))),((extremely detailed CG unity8k  wallpaper)),((depth of field)),highlight,light particles, chiaroscuro,colorful",
   "大叔魔法113-火莲术":",solo,an extremely delicate and beautiful girl,{beautiful detailed eyes},{large top sleeves},red eyes,{burning },floating,black hair,long hair,{gothic},small breast,{best quality},{highly detailed},{masterpiece},{ultra-detailed},{best illustration},(lotus  flowers:1.2),(burning:1.3),(Flames burning around:1.4),red eyes,loli,(Fire butterflys:1.1),(ink)",
   "大叔魔法114-火烧云":",(((masterpiece))),best quality, illustration,beautiful detailed glow,(beautiful detailed eyes), (dark magician girl:1.1 ),big forhead,flower,large top sleeves,Floating ashes, Beautiful and detailed explosion, red moon, fire,Fire cloud, Wings on fire, a cloudy  sky, smoke of gunpowder, burning, black dress, (beautiful detailed eyes),expressionless,beautiful detailed white gloves, Dove of peace, (floating cloud: 1.2),azure hair,disheveled hair,long bangs, hairs between eyes, black kneehighs, black ribbon,white bowties,midriff,{{{half closed eyes}}}, ",
   "大叔魔法115-王城法":",大叔魔法115-王城法|best quality,masterpiece,ultra- detailed,king,detailed face,resplendent crown,precious robe,face up,{prosperous  city},depth of field,headdress,slik clothes,exquisite skin,conquer,extremely detailed CG,{clock tower},{crisscross streets},detailed light, {shabby building} ,{background focus},{detailed background},{vast city},  (Vertical pupil:1.2), float hair, shiny hair, colored inner hair, castle,side  view,",
   "大叔魔法116-西幻术":",(extremely detailed CG unity 8k wallpaper,masterpiece, best quality, ultra-detailed),(best illumination, best shadow,  an extremely delicate and beautiful), classic, (impasto,photorealistic, painting, realistic, sketch,portrait),",
   "大叔魔法117-西游记":",大叔魔法117-西游记|((masterpiece)),best quality, ((illustration)),original,extremely detailed wallpaper,((beijing opera ))), (sketch),(wash painting),((color splashing)),((ink splashing)),((((dyeing)))),((Chinese painting)),( (colorful))(beautiful   and delicate fire),(a monkey,Chinese mythology,solo,a tall man like monkey in armour,human body and monky face,( ((monkey king))),(solo),(((Journey to the west))), ,golden cudgel,jingubang,fly up to the cloudy regions,sky,sky ,sky, cloud,cloud,chinese teadional building,fly up to the cloudy regions,simple bancground,",
   "大叔魔法118-彷徨术":",((masterpiece)), (((best quality))), (ultra-detailed:1.5), ((illustration)), ((disheveled  hair)),(1girl),solo,ambiguous gender,animal ears,artist name,black footwear,black gloves ,black pants,black ribbon,blood,blood from eyes,blood  from mouth,blood on clothes,bloodonface,blue coat,blue hair,boots,building,bulletproof vest,cat ears,cattail,caution tape,A broken building,character name,city, cityscape,cloud,cloudy sky,coat,corpse,crane (machine),crystal,cuts,eyelashes,gloves,green eyes,grey coat,hood,hood down,hood up,hooded coat,impaled, injury,keep out,ladder,leg ribbon,lightning,long hair,looking up,mask, meteor,open clothes,open coat,outdoors,pants,parted lips,railing,rain,ribbon,rooftop ,sidelocks,sky,skyscraper, tail,very long hair,(Heavy   rains),",
   "大叔魔法119-忘穿水":",extremely detailed CG unity 8k wallpaper,best quality,noon,beautiful detailed  water,long black hair,beautiful detailed girl ,serafuku,view straight on,eyeball,hair flower,close up",
   "大叔魔法120-刻刻帝":",(((crystals texture Hair))),{{{{{extremely detailed CG}}}}},{{8k_wallpaper}},{{ {{Crystalline purple gemstone gloves}}}},((beautiful detailed Glass hair)),((Glass shaped texture hand)),((Crystallize texture body)),Gem  body,Hands as clear as jewels,Crystallization of clothes,((crystals texture skin)),sparkle, lens flare, light leaks, Broken glass,{{{{Detailed  Glass shaped clothes}}}}, ((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)), ((disheveled  hair)), ((frills)), (1 girl), (solo), dynamic angle, big top sleeves, floating, beautiful detailed gemstone sky, gemstone  sea, beautiful detailed eyes, overexposure, side blunt bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders, (((small breast))) , pleated skirt, crystals texture flowers, ((Detailed crystallized clothing)),(gemstone of body),solo focus,{{{{{{{{Iridescence and rainbow  hair:2.5}}}}}}},{{{{{{detailed cute anime face}}}}}},{{loli}},{{{{{watercolor_(medium)}}}} ,(((masterpiece))),(((clock))),(((red))),(((blood))),fi nely detail,Depth of field,Blood drop,Blood   fog",
   "大叔魔法121-金石法":",Hide hands,(Magic circle),Principal,((Gem)),elegant,(holy),extremely detailed 8k wallpaper,(painting),( ((ink))),(depth of field),((best quality)),((masterpiece)),(highres),(((ink))),(illustration),cinematic lighting,( (ultra detailed)),(watercolor),detailed shadow,(((1girl))),(detailed flooding feet),(((((long top sleeves past fingers))))) ,((motion)),beautiful detailed fullbody,(leg up),(((sapphire frills))),(((yokozuwari in the golden cage))),gold cage,( birdcage),{{{very long dress cover feet}}},(translucent fluttering dress with lace},{{detailed skin}},(((long Bright wavy hair) )),Juliet_sleeve,(((hands hide in puffy sleeves))),((bare shoulders)),flat_chst,((Crystal shoes)),((((arms behind back)) )),(((extremely detailed cute anime face))),Jewelry decoration,((expressionless)),(Iridescent Gem Headwear),(Beautiful detailed gemological eyes),((melting  silver and gold)),looking_at_viewer,{detailed bare foot},Obsidian bracelet,,gold arm ring,(Precious refraction),{splash},{{optical phenomena}},detailed  glow,(lightroom),(shine),chains,reflective,Gemological ornaments,Cosmic background of nebula,((silver thorns)),(huge golden clock core above),gear,falling  petals,Window pane,beautiful water,Colored crystal,mirror,Silver frame,canopy,detailed Diamonds,(Columnar crystal),(Columnar crystal),Latin Cross Budded,(Sputtered broken glass  from inside to outside),(flow),dark",
   "大叔魔法122-章鱼娘":",(((masterpiece))),(((best quality))),((ultra-detailed)),((underwater)),(illustration),( beautiful detailed water),((solo)),((1girl)),(loli), (((detailed anima face))),(white hair), disheveled hair, hairs  between eyes,(messy hair), long hair,blue eyes, (beautiful detailed eyes), ((Gradient color eyes)),in the rain,((((Octopus  girl)))), {Mermaid ears},Flosse Hand,bare shoulders, white stockings, white dress, ((detailed clothes)),wet clothes,arms behind back ,(sunlight),(underwater forest),(painting),(bloom),(detailed glow),drenched,seaweed,(jellyfish),watercolor_(medium),detailed background,fluttered detailed splashs, beautiful  detailed sky,,Crystallization of clothes,{{{{Crystalline purple gemstone gloves}}}},(gemstone of body), ((Detailed crystallized clothing)),((dark  intense shadows)), ((cinematic lighting)),",
   "大叔魔法123-雪月法":",hiten_1, (((masterpiece))),best quality, illustration,beautiful detailed glow,detailed ice,beautiful detailed water,red  moon,snowflake, (beautiful detailed eyes),expressionless,beautiful detailed white gloves, (floating cloud:1.2),azure hair,disheveled hair,long bangs, hairs between eyes , dark dress, (dark magician girl:1.1),black kneehighs, black ribbon,white bowties,midriff,{{{half closed eyes}}},big forhead,blank  stare,flower,large top sleeves,",
   "大叔魔法124-唤鹅法":",violet evergarden,violet evergarden \(series\, violet evergarden, violet_evergarden,((best quality)), ((masterpiece)),  ((ultra-detailed)), (illustration), ((detailed light)), (an extremely delicate and beautiful), a girl, solo, (cute face) , expressionless, (beautiful detailed eyes),sky,could,blonde hair,blue eyes,braid,Green brooch, short hair,white Lace  scarf,cloud,dress,eyebrows visible   through hair,hair between eyes,hair intakes,Cyan blue jacket,jewelry,letters_around, (letter),blue eyes, looking at viewer,Red headband,sky,garden,by  Kyoani,white dress,Dark blue top,long_sleeves,letters background,[[[[[Jokul]]]]],by Kyoani",
   "大叔魔法125-恶兽法":",{High definition}}, {Clear background}, {Full body portrait}, watercolor, high detail, high picture  quality, {masterpiece}, {Best quality}, 4k picture quality, high detail, rough, game cg, gray, terror, horror, gray tone, collapsed  buildings, rain, fog, 1 knight, red eyes, rusted armor, huge size, grief of frost, Lich King, Blood pool, trample,  behead, dragon, soul of darkness",
   "大叔魔法126-城堡法":",(((masterpiece))),best quality, illustration,beautiful detailed glow,detailed ice,beautiful detailed water,red moon, ( magic circle:1,2), (beautiful detailed eyes),expressionless,beautiful detailed white gloves, own hands clasped, (floating palaces:1.1),azure hair,disheveled  hair,long bangs, hairs between eyes, dark dress, (dark magician girl:1.1),black kneehighs, black ribbon,white bowties,midriff,{{{half closed  eyes}}},,big forhead,blank stare,flower,large top sleeves,",
   "大叔魔法127-星之彩":",((best quality)), ((masterpiece)), ((ultra-detailed)), (illustration), (detailed light),  (an extremely delicate and beautiful), a girl, cute face, upper body, two legs, long dress, (beautiful detailed eyes), stars in  the eyes, messy floating hair, colored inner hair, Starry sky adorns hair, (lots_of_big_colorful_Bubble), [pearl], [Galaxy], depth of field" ,
   "大叔魔法128-星天使":",{{best quality}}, {{masterpiece}}, {{ultra-detailed}}, {illustration}, {detailed light},  {an extremely delicate and beautiful}, {beautiful detailed eyes}, {sunlight}, {{extremely light}}, {{extremely clothes}}, {{{Holy  Light}}}, dynamic angle, a girl, {{angel}}, solo, {{{loli}}}, Light particle, very_long_hair, white_hair, yellow_eyes, { {glowing eyes}}, {{{expressionless}}}, [[light_smile]], [[[[white Tulle skirt]]]], {white silk}, looking_at_viewer, { {{{angel_wings}}}}, {{large_wings}}, multiple_wings, {angel_halo}, [[[starry sky]]], {{dusk_sky}}, {{Floating light spot }}, {{Lots of feathers}}",
   "大叔魔法129-星火术":",(((battlefield))), ((smoke of gunpowder)), (wind), (horizon), [starry sky],  beautiful detailed cold tint sky, ((detailed landscape)), dynamic angle, extremely detailed background, ((super fine illustration)), ((masterpiece)),  ((very detailed light))",
   "大叔魔法130-星冰乐":",大叔魔法130-星冰乐|(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow ,detailed ice,beautiful detailed water,(beautiful detailed eyes),expressionless,beautiful detailed white gloves, (floating palaces:1.3),azure hair,disheveled hair,long bangs,  hairs between eyes, (skyblue dress),black ribbon,white bowties,midriff,{{{half closed eyes}}},,big forhead,blank stare,flower,large top  sleeves,(((ice crystal texture wings)))",
   "大叔魔法131-星空法":",((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)), ((disheveled  hair)), beautiful detailed eyes, (1girl:1.2),(solo), dynamic angle, dark magician girl,(black kneehighs:1.1),(starry tornado:1.4) ,  starry Nebula, ((frills)), beautiful detailed sky, beautiful detailed eyes,evil smile, expressionless,hairs between eyes,  white  hair,pleated skirt ,((disreveled hair))",
   "大叔魔法132-星源法":",best quality,Amazing,Beautiful golden eyes,finely detail,Depth of field,extremely detailed CG unity 8k wallpaper, masterpiece ,(((Long dark blond hair))),((red mediumhair)),(1 girl),(white stockings ),(((((medium_breasts,))))),( hair ribbon),Exposing cleavage,((Beautiful butterflies in detail)),(((halter dress ))),huge ahoge,particle,(((solo))),(Background of  details),standing,(Starry sky in beautiful detail),(((gloom (expression) depressed))),(Hazy fog),(((Very long hair))), {Fluttering hair},{Thick hair},{{{Gelatinous texture}}},{profile},(Ruins of beautiful details),(((Standing on the surface of the  sea))),{Close-up of people},{{{Smooth skin}}},(((upper body))),(Smooth and radiant skin),(Smooth and  radiant face),Perfect details,Beautifully gorgeous necklace,Authentic skin texture,{Cleavage},{{{Authentic and detailed face}}},(unexposed :1.5)",
   "大叔魔法133-星语术":",((masterpiece)), ((best quality)), ((illustration)), extremely detailed,style girl, long shot,  small breast,light grey very_long_hair, scifi hair ornaments, beautiful detailed deep eyes, beautiful detailed sky, beautifuldetailed water, cinematic lighting, dramatic angle,  (very long sleeves), frills, formal, close to viewer, (an extremely delicate and beautiful),best quality,highres,official art,extremely detailed CG  unity 8k wallpaper, ((starry sky)), star river,array stars, Holy, noble, ((oilpainting)) , ((wallpaper 8k CG)),  (realistic), Concept Art, vary blue and red and orange and pink hard light, intricate light, dynamic hair, haircut, dynamic fuzziness, beautiful  and aesthetic, intricate light, manga and anime",
   "大叔魔法134-星银法":",(extremely detailed CG unity 8k wallpaper,masterpiece, best quality, ultra-detailed),illustration,dynamic angle, floating,  finely detail,  (bloom), (shine), glinting stars,",
   "大叔魔法135-星霞海":",dream,(((extremely detailed CG unity 8k wallpaper))),{painting},(((ink))),amazing,Depth  of field,{{best quality}},{{masterpiece}},highres,dynamic angle,(illustration),cinematic lighting,{1girl},((wavy silver hair)),((loli) ),((extremely_detailed_eyes_and_face)),(detailed flooding bare feet:1.5),translucent pink skirt,gemological hair,french braid,pointy ears,looking at viewer,{{translucent fluttering  skirt}},yellow hairpin,{{white dress with pink lace with yellow decoration}},sleeves past wrists,((sleeves past fingers)),walking_motion,strapless dress, ocean waves,wind,(((glistening light of waves))),{detailed sunset glow},(floating flow),((coral)),(Luminous),coast,{floating colorful  bubbles},beautiful detailed sky,{fluorescence},detailed shadow,(conch),beautiful detailed water,drenched,starfish,meteor,rainbow,(seabirds),{glinting stars}, (glowworm) ,(splash),,detailed cloud,shell,{fireworks}",
   "大叔魔法136-星鬓法":",masterpiece, best quality, illustration, stars in the eyes,dishevelled hair,Starry sky adorns hair,1 girl,sparkling  anime eyes,beautiful detailed eyes, beautiful detailed stars,blighting stars,emerging  dark purple across with white hair,multicolored hair,beautiful detailed eyes,beautiful detailed  sky, beautiful detailed water, cinematic lighting, dramatic angle,",
   "大叔魔法137-春水术":",((((((SOLO)))))),((((((1GIRL)))))), ,((((FLOWING RIVER )))),(((FULL BODY))),MASTERPIECE, (BEST QUALITY), aMAZING, BEAUTIFUL DETAILED EYES, FINELY DETAILED, dEPTH OF FIELD, EXTREMELY DETAILED  cg UNITY 8K WALLPAPER,(((CUTE ANIMAL FACE))), (((A GIRL WEARS cLOTHES bLACK AND WHITE tAOIST ROBES))),((eXTREMELY  GORGEOUS MAGIC STYLE)),((((GOLD AND SILVER LACE)))),(((((GORGEOUS DETAILED EYES))))),((GORGEOUS DETAIL FACE))] ,((((SMALL BREAST)))),(((EXTREMELY DETAILED GORGEOUS TIARA))),((WHITE HAIR ORNAMENT)),(GOLD GORGEOUS NECKLACE),((tHE CHARACTER  IS IN THE CENTER OF THE FRAME)),((BRIGHT PUPILS)),((((MELT))))",
   "大叔魔法138-流沙法":",cinematic lighting, ((best quality)),((extremely_detailed_eyes_and_face)),((((ink)))),((illustration)),depth  of field,((extremely detailed)),((watercolor)),((anime face)),(((dramatic_angle))),medium_breast,(8k_wallpaper),((bright_eyes)), (looking_at_viewers) ,(an detailed organdie dress),(((((very_close_to_viewers))))),((sleepy)),((masterpiece)),((((((surrounded_by_heavy_floating_sand_flow_and_floating_sharp_stones)))))),( ((((messy_long_hair))))),((((veil)))),focus_on_face,(upper_body),(bare_shoulder),((((1girl)))),(golden_bracelet),(long yarn) ,((sunset)),lens_flare,light_leaks,((detailed_beautiful_desert_with_cactus)),medium_wind,(detailed_beautiful_sky)",
   "大叔魔法139-狡兽法":",大叔魔法139-狡兽法|((masterpiece)),best quality, ((illustration)),original,extremely detailed wallpaper,((( beijing opera))), (sketch),(wash painting),((color splashing)),((ink splashing)),((((dyeing)))),((Chinese painting) ),((colorful))(beautiful and delicate mountain),Stone figure,(solo),(Fantasy creatures),dog body,((Chinese jiao)),(((Horns))) ,Horns,(golden dog body:1.3),(golden lion head), Leopard print,(solo), Canines,lion head,fly up to the cloudy regions,fly  up to the cloudy regions Big and   strong,Diabolical,Tyrannica,simple background",
   "大叔魔法140-科幻风":",((((1girl)))),original,((an extremely delicate and beautiful)),detailed face,Perfect details,Science fiction ,sense of digital,((running code in the eyes)),((Crashing database)),Cold tint theme,0 and 1 code,solo,bule light,Digital  background,expressionless,((Running data adorns hair)),((Running data adorns face)),(Garbled code),Running data,Running code,Virtual,((digitization)) ,(source code),binary,young girl,shiny hair,bright pupils,With data composition,light particles,((intricate detail)),((((ultra-detailed))), ((illustration)),(((masterpiece))),(((best quality))),((extremely detailed CG unity 8k wallpaper)),((depth of field)), highlight,sharpening",
   "大叔魔法141-结晶法":",(((crystals texture Hair))),{{{{{extremely detailed CG}}}}},{{8k_wallpaper}},{{{ {Crystalline purple gemstone gloves}}}},((beautiful detailed Glass hair)),((Glass shaped texture hand)),((Crystallize texture body)),Gem body ,Hands as clear as jewels,Crystallization of clothes,((crystals texture   skin)),sparkle, lens flare, light leaks, Broken glass,{{{{Detailed  Glass shaped clothes}}}},       ((masterpiece)), (((best quality))), ((ultra-detailed)), ((illustration)),  ((disheveled hair)), ((frills)), (1 girl), (solo), dynamic angle, big top sleeves, floating, beautiful detailed gemstone  sky, gemstone sea, beautiful detailed eyes, overexposure,  side blunt bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders, ((( small breast))),  pleated skirt, crystals texture flowers, ((Detailed crystallized clothing)),(gemstone of body),solo focus",
   "大叔魔法142-虹彩法":",((extremely detailed CG)),((8k_wallpaper)),(((masterpiece))),((best quality)),watercolor_(medium), ((beautiful detailed starry sky)),cinmatic lighting,loli,princess,very long rainbow hair,side view,looking at viewer,full body,frills,(far from viewer ),((extremely detailed face)),((an extremely delicate and beautiful girl)),((extremely detailed cute anime face)),((extremely detailed eyes) ),(((extremely detailed body))),(ultra detailed),illustration,((bare stomach)),((bare shoulder)),small breast,((sideboob)),(( ((floating and rainbow hair)))),(((Iridescence and rainbow hair))),(((extremely detailed sailor dress))),((((Iridescence and  rainbow dress)))),(Iridescence and rainbow eyes),beautiful detailed hair,beautiful detailed dress,dramatic angle,expressionless,(big top sleeves),frills,blush,(ahoge )",
   "大叔魔法143-风魔法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), (1  girl), (solo), ((an extremely delicate and beautiful)), little girl, ((beautiful detailed sky)), beautiful detailed eyes, side blunt  bangs, hairs between eyes, ribbons, bowties, buttons, bare shoulders, (small breast), blank stare, pleated skirt, close to viewer, ( (breeze)), Flying splashes,  Flying petals, wind",
   "大叔魔法144-修仙画":",{masterpiece},{bestquality},{impasto},{{{{illustration}}}},{dynamic angle},clockbackground,{{{{{colorful  lightning}}}}},(an exremely delicate and beautiful),(classic),{a girl},long hair,black hair,blue_eyes,dot nose,gloom (expression) depressed ,bandaid on cheek,scar on cheek,hanfu chinese knot,{muguet},{straw hat},arms behind back,fighting_stance,from side,{{tsukemon}},poem,{ kazagumo},{clift},{{lightning bolt symbol}},blood,fairy, tonebreath of fire,ink,{{solo}},{light trail},glowing butterfly,light particles, shooting star,{kendo},multiple swords,ruin,",
   "大叔魔法145-核爆法":",(((masterpiece))),best quality, illustration,(beautiful detailed girl),beautiful detailed glow,((flames of war )),(((nuclear explosion behide))),rain,detailed lighting,detailed water,(beautiful detailed eyes),expressionless,palace,azure hair,disheveled hair,long bangs,hairs  between eyes,(whitegrey dress),black ribbon,white bowties,midriff,big forhead,blank stare,flower,long sleeves",
   "大叔魔法146-桃花法":",((masterpiece)),((best quality)),(ultra-detailed),(illustration),((an extremely delicate and beautiful)) ,(dynamic angle),chinese dragon,china,1girl,(beautiful detailed eyes),cute pink eyes,green pupil,detailed face,upper body,messy floating hair,disheveled hair ,focus,perfect hands",
   "大叔魔法147-浮世绘":"大叔魔法147-浮世绘|best quality, ((((masterpiece)))),  (( illustration)), extremely detailed wallpaper,(Chinese  ink painting)((silhouette)), watercolor, limited palette, (fantasy), long shot, , (extremely delicate and beautiful), long shot, (ink  and wash), (Chinese ink painting),((colorful)),  (((beijing opera))),(sketch),diamond and glaring eyes, beautiful detailed  cold face, extremely delicate beautiful girls, glowing eyes, (wash painting),((colorsplashing)),((ink splashing)),((((dyeing)))),( (chinese painting)),(((ink and wash))), (beautiful detailed girl),(beautiful detailed eyes),low twin braids,(low twintails:1.2), small_breasts,azure hair,long bangs, hairs between eyes,white bowties,big forhead,blank stare,beautiful bule eyes,(1 girl:2.0), (solo), very  long blue and sliver hair,(perfect female body:1.2),(skyblue dress),anklet,(chinese style architecture:1.5),chinadre, traditional chinese painting,(( Chinese wind)),",
   "大叔魔法148-留影术":",1male,solo,(Masterpiece), ((best quality)),beautifully painted,highly detailed,detailed clothes,detailed face,detailed eyes, {{intricate detail}},detailed background,dramatic shadows,black and white,monochrome,{{comic}},cross necklace,Cassock",
   "大叔魔法149-秘境法":",(extremely detailed CG unity 8k wallpaper),(((masterpiece))), (((best quality))), ((ultra -detailed)), (best illustration),(best shadow), ((an extremely delicate and beautiful)),dynamic angle,floating, fairyland,dynamic angle,sea of  flowers,beautiful detailed garden,wind,classic,spring, (detailed light),feather, nature, (sunlight), river, forest,(((floating palace))),((the  best building)),beautiful and delicate water,(painting),(sketch),(bloom),(shine)",
   "大叔魔法150-森火法":",((((ink)))),((watercolor)),((best quality)),(spirit),((illustration)),(( (1 girl))),(beautiful detailed eyes),world masterpiece theater,depth of field,(Burning forest),spark,anime face,Black gauze skirt,(red_hair), blue_eyes,focus_on_face,medium_breasts,(((((messy_long_hair))))),Bare shoulder,very_close_to_viewers,veil,light_leaks,Burning sky,navel,((bustier)),flame,Red Gem Necklace,Rainbow  in the sky,Flames burning around,A burning church,(((Fire butterflys ))),(Flying sparks)",
   "大叔魔法151-森林冰":",((((ink))),((watercolor)),world masterpiece theater, ((best quality)),depth of field,( (illustration)),(1 girl),anime face,medium_breast,floating,beautiful detailed sky,looking_at_viewers,an detailed organdie dress,very_close_to_viewers,bare_shoulder,golden_bracelet,focus_on_face,messy_long_hair,veil,upper_body,, lens_flare,light_leaks,bare shoulders,detailed_beautiful_Snow Forest_with_Trees, spirit,grey_hair,White clothes,((Snowflakes)),floating sand flow,navel,(beautiful detailed eyes), (8k_wallpaper)",
   "大叔魔法152-森林法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), ((an  extremely delicate and beautiful)),dynamic angle,floating, (beautiful detailed eyes), (detailed light) (1girl), loli, small_breasts, floating_hair,  glowing  eyes, pointy_ears, white hair, green eyes,halter dress, feather, leaves, nature, (sunlight), river, (forest),(painting),(sketch),( bloom)",
   "大叔魔法153-森罗法":",super fine illustration,masterpiece, best quality,{beautiful   detailed eyes},1girl,finely detail,Depth of field, 4k  wallpaper,bluesky,cumulus,wind,insanely detailed frills,extremely detailed lace,BLUE SKY,very long hair,Slightly open mouth,high ponytail,silver hair,small Breasts,cumulonimbus  capillatus,slender waist,There are many scattered luminous petals,Hidden in the light yellow flowers,Depth of field,She bowed her head in frustration,Many  flying drops of water,Upper body exposed,Many scattered leaves,branch ,angle ,contour deepening,cinematic angle ,{{{Classic decorative border}}}",
   "大叔魔法154-焰山骑":",(((masterpiece))),((illustration)),amazing,(((best quality))),(illustration),extremely detailed 8k  cg,floating cloak,burning cloak,((extremely delicate and beautiful girl)),brown hair,floating messy hair,(detailed face),cold face,looking at viewer, determined eyes ,knight,((cloak)),bloodstain,white silver armor,shoulder armor,body armor,(gauntlets),black delicate skirt,((character focus)), mountainous  horizon,volcano,dark sky,burning,(((flying ember))),(flame particle:1.1),bloodstain ,dramatic light, depth of field,lens flare",
   "大叔魔法155-华丽术":",( masterpiece:1.2),(best quality:1.2),(illustration:1.5),1girl,chinese dragon,chinese girl,female focus on, (color splashing:1.2),(colorful:1.2), (color Ink wash painting:1.2),(ink splashing:1.2),sketch, Masterpiece,best quality, beautifully painted,highly  detailed,",
   "大叔魔法156-阳光法":",{masterpiece},{best quality},{1girl},Amazing,beautiful detailed eyes,solo,finely detail,Depth of field,extremely detailed  CG,original, extremely detailed wallpaper,{{highly detailed skin}},{{messy_hair}},{small_breasts},{{longuette},{grassland},{yellow eyes},full body , incredibly_absurdres,{gold hair}.lace,floating hair,Large number of environments,the medieval ,grace,A girl leaned her hands against the fence,ultra-detailed ,illustration, birds,Altocumulus,8kwallpaper,hair_hoop,long_hair,gem necklace,hair_ornament,prospect,water eyes,wind,breeze,god ray,lawn,Mountains and lakes in the distance,The  skirt sways with the wind,The sun shines through the trees,A vast expanse of grassland,fence,Blue sky,bloom,smile,glow,The grass sways  in the wind",
   "大叔魔法157-云中现":",(((((China Kirin))))),firing fur,Sunset,{masterpiece},{{Hands hidden inside the sleeves} },arms behind back,((((Flowing long long sleeves",
   "大叔魔法158-黄金律":",{{masterpiece}}, best quality, Amazing, {beautiful detailed eyes}, {1girl}, extremely detailed CG unity  8k wallpaper, highly detailed, official_art, highres, original, blonde hair, yellow eyes, white skin, slim legs, mature female, sunrise, golden sky , magnificent architecture, beautiful detailed sky, overexposure, detailed background, delicate gold metal decorations",
   "大叔魔法159-黑金法":"大叔魔法159-黑金法|{{{{masterpiece}}}},{{best quality}},{{official art}},{{extremely detailed  CG unity 8k wallpaper}},{{an extremely delicate and beautiful girl}},{extremely delicate and beautiful face},cold expression,yellow eyes,messy long  hair,streaked hair,gradient and black hair,beautiful detailed eyes,{{{black chinese dress with  phoenix}}},Gilded,dramatic angle,{{hairpin}}, { cape},small golden ornaments,{{black flame}},{{phoenix}},chinese dragon,{{phoenix with big black wings}},fluid,",
   "大叔魔法160-园林风":",{masterpiece},{Suzhou Garden},best quality,Photo,illustration,{an extremely delicate and beautiful},Amazing,{Depth of  field},extremely detailed CG unity 8k wallpaper,{cover you with flowers as rain},non-humanoid",
   "大叔魔法161-暗鸦法":",(((masterpiece))),best quality, extremely detailed CG unity 8k, illustration, contour deepening beautiful detailed glow ,(beautiful detailed eyes), (1 girl:1.1), ((Bana)), large top sleeves, Floating black ashes, Beautiful and detailed black, red  moon, ((The black clouds)), (black Wings) , a black cloudy sky, burning, black dress, (beautiful detailed eyes), black  expressionless, beautiful detailed white gloves, (crow), bat, (floating black cloud:1.5),white and black hair, disheveled hair, long bangs,  hairs between eyes, black knee-highs, black ribbon, white bowties, midriff,{{{half closed eyes}}},((Black fog)), Red eyes , (black smoke), complex pattern, ((Black feathers floating in the air)), (((arms behind back)))",
   "大叔魔法162-暗锁法":",{{{{{masterpiece}}}}},{{{{best quality}}}},illustration,{{beautiful detailed girl}},( ((beautiful detailed lighting))),beautiful detailed eyes,(((((disheveled hair))))),{{{beautiful detailed dress}}},midriff,{{female girl }},((off-shoulder jacket)),sailor dress,((((darkside)))),{{{{{bust}}}},{{{{{watercolor_(medium)}}} }},wholeblack bloomer,wet clothes,wet skin,flowers,hollow eyes,hollow night,hollow knight,{{{{{chain}}}}},dark soul,abyssal ship,deep  dark,darkness,{{{{female girl}}}}},{{{small breast}}},death garden,{{{{emotionless eyes}}}},{{{cthulhu}} },((((extremely detailed dark clouds)))),{{{{{extremely detailed CG unity 8k wallpaper}}}}},(((extremely detailed face)) ),(((jitome))),((((dark_persona)))),{{ruins}},{{{{{{beautiful deatailed shadow}}}}}},{{{{chain  storm}}}}},{{{{chain ring}}},",
   "大叔魔法163-灭世镜":"大叔魔法163-灭世镜|{best quality},{{masterpiece}}, {highres},original,extremely detailed wallpaper,illustration,{1girl :2},(((solo))),Sheer white dress.Grey hair.Jewel-eyes.small_breast.{{disdainful}},Delicate face,{Multi-stacked magic array,towards the  south,Firing,firebolt}.{Multi-stacked magic array,towards the south,Firing,red-fireball}.((background:sky,towards the south,Firing,four huge swords. And ground,towards the south,Firing,Sword-array:1)).sharp,{The girl,Firing,Magicm,Light of Extinction, Attack",
   "大叔魔法164-烟水月":",((masterpiece)), ((best quality)), ((ultra-detailed)), (((illustration))), extremely  detailed CG unity 8k wallpaper , (an extremely delicate and beautiful) , (((1 girl))) , (((solo))) , (colorful ) , (((young girl))) , bare shoulders , medium_breasts , (hanfu:1.2) , (blue hair:1.2) , (water like hair ) , hair between eyes , ((messy hair)) , long hair, blonde eyes , detailed eyes , comic face , wide sleeves ,  ((gold hair stick)) ,(blue ribbon) , (gold tassel) , sitting, outdoors , backlighting , Ambient light , ((reflective water )) , ((beautiful and delicate water)) , (((falling yellow petals))) , ((breeze)) , (east asian architecture background: 1.2) , ((mountain background)) , (moon background) ((((depth of field)))) , (dramatic angle)  , (light particles : 1.2)) , ((ripple)) , (water drop) , (((wet))) ((fog)) , ((cloud)) , (looking at  viewer), (ink) , (watercolor) , ((((dyeing))))",
   "大叔魔法165-烟花法":",((extremely detailed CG unity 8k wallpaper)),(masterpiece), (best quality), (ultra-detailed), (best  illustration),(best shadow), (an extremely delicate and beautiful), ((((1girl)))), dynamic angle, floating, finely detail, (bloom ), (shine), glinting stars, ((((best detailed fireworks)))), ((((depth of field)))), (((hanabi))) , Beautiful detailed girl, (((backlight))), extremely delicate and beautiful girls, ((summer long skirt)), (((solo))), best  detailed hair, ((beautiful detailed water)),   night sky, (((small breast))), beautiful detailed sky, beautiful detailed eyes, ((( arms behind back))), long hair, (((dynamic angle))), long skirt",
   "大叔魔法166-碎梦法":",(masterpiece), black hair,red eyes,1girl,solo,((delicate face)),((an extremely delicate and beautiful )),strange,Space opera,Space port,robot arm,elbow_gloves,night,glisten,stare,cyberpunk,((((citylight)))),((masterpiece)), (((best quality ))), (beautiful detailed eyes),((ultra-detailed)), ((illustration)), ((disheveled hair)),science fiction,bodysuit,Mechanical armor headdress,( bare shoulders)",
   "大叔魔法167-碰水法":",(watercolor), ((extremely detailed CG unity 8k wallpaper)), (game cg), ((masterpiece)),  ((best quality)), ((ultra-detailed)), (1 girl), (solo), (best illustration), (extremely detailed illustration), ((disheveled  hair)), ((beautiful detailed lighting)), (from above), ((an extremely delicate and beautiful)), cinematic lighting, dynamic angle, detailed  wet clothes, blank stare, overexplosure, floating, (beautiful detailed eyes), side blunt bangs, small breasts, black long straight, red eyes,   aqua  eyes, gradient eyes, black hair, very long hair, blunt bangs, ((blood)), white dress, frills, bowties, ((expressionless)),  extremely beautiful detailed water, ((lying on the lake)), ((hairs curling in the water)), (bloodred water:1.5), (red  background:1.3), swirl,",
   "大叔魔法168-圣光法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), (detailed  light),((an extremely delicate and beautiful)),(beautiful detailed eyes), (sunlight),(angel),solo,young girls,dynamic angle,floating, bare_shoulders,looking_at_viewer  ,wings ,arms_up,halo,Floating white silk,(Holy Light),just like silver stars imploding we absorb the light of day",
   "大叔魔法169-圣域法":",((masterpiece)), (((best quality))),extremely detailed CG unity 8k wallpaper,illustration,artbook,((1girl) ),lewear,small beast,beautiful detailed eyes,red eyes,white hair,long_hair,beautiful detailed starry sky,beautiful starry detailed water,barefoot,flower ribbon,angel,dramatic  angle,white gloves, solo,>_<,ameth_(princess_connect!),snow, ice,full body shot,tiara,white_thighhighs,torn_thighhighs,silver plastron,",
   "大叔魔法170-苇名法":",dramatic_shadow,ray_tracing, ((best quality)),(((beautiful_detailed_dark_midnight_sky))),((((yellow_full_moon)))),(holding_wine_gourd),( ((((surrounded_by_floating_sakura))))),dramatic_angle,(leaning_on_huge_stone),(((bare_shoulder))),((((very_close_to_viewer)))),(((tispy))),(((sleepy))) ,((far_from_viewer)),(((extremely_beautiful_detailed_anime_face_and_eyes))),((((((1girl)))))),((((open_hakama)))),((samurai)),(ink),( (i llustration)),depth of field,(((((beautiful_detailed_pampas_grass_field))))),watercolor,((upper_body)),medium_breast,(bright_eyes),((masterpiece)),((messy_white_long_hair))" ,
   "大叔魔法171-诡谲法":",大叔魔法171-诡谲法|best quality, ((((masterpiece)))), ((illustration)), extremely detailed wallpaper,{ {obscure}},{{{{Elder Gods}}}},storm,tiny,dark,{{{Naiatotipu}}},Indescribable, ,Blood pouring,{{ behind the back}}, {magic circle},(bright smile:1.5),strange,saintlike,(sketch),(wash painting),((colorsplashing)),watercolor, limited palette, (fantasy), long shot  , long shot",
   "大叔魔法172-雷男法":",A man with has short black hair, a round hat, no facial features, a high collar coat , Flashes of lightning from the hands,full body,, (((masterpiece))), (((best quality))), ((ultra-detailed)), ( illustration), (detailed light),((Expressionless)),, (((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration) , (detailed light),((an extremely delicate and beautiful)),((man)),((lightning in hand)),Lightning surrounds men,(((Lightning chain ))),Suspended crystal, with lightning inside the crystal,((Suspended colorless crystal))",
   "大叔魔法173-梦里花":",masterpiece, best quality,1girl sitting on the grass with flowers,hand between legs,the petals float past her ,fantasy,((masterpiece)),best quality,long pink hair,blue eye,flower crown,(floating hair),frilled dress with flower,stream,paradise,flower ornament,ribbon ,happiness,[[open mouth]],garden,beautiful detailed eyes,looking at viewer,{an extremely delicate and beautiful},from above,",
   "大叔魔法174-缥缈术":",masterpiece, best quality, 1girl,solo,an extremely delicate and beautiful girl,extremely detailed,an extremely delicate and beautiful ,starry detailed water,beautiful detailed starry sky,beautiful detailed eyes,bare shoulders,big forhead,black ribbon,large top sleeves,long bangs,beautiful detailed glow,blue  eyes,shine,azure hair,messy_long_hair,finely detail,{watercolor_medium},masterpiece,breeze,floating,feather,forest,{bloom},floating,dynamic angle,{detailed light},beautiful and delicate  water,{best illustration},flowers,{best shadow},nature,{{an extremely delicate and beautiful}},fairyland,{{ultra-detailed}},{extremely detailed CG  unity 8k wallpaper},mist encircles the mountains,{shine},{{{best quality}}},{sunlight},classic,{painting},river,{sketch},{{{masterpiece} }}",
   "大叔魔法175-蒸汽城":",flat color, (solo:1.5), (masterpiece:1.5), (best quality:1.5), amazing, beautiful detailed, extremely  detailed wallpaper, extremely detailed CG unity 8k wallpaper, extremely delicate and beautiful, finely detailed, extremely detailed wallpaper, cinematic lighting, fantasy, official  art, wide angle, (depth of field: 1.8), (fantasy city, detailed Victorian architecture, industrial: 1.5, steampunk: 1.8, impasto: 1.5) , (factory, dome, arch, detailed clock tower: 1.3, bridge, many detailed skyscrapers: 1.8, industrial pipes, chimneys: 1.3, orange city  lights, railroads: 1.8, train yards: 1.8), (night, beautiful night sky: 1.5), (city scape, scenery)",
   "大叔魔法176-裸背风":",((best quality)), ((masterpiece)), ((ultra-detailed)),  (illustration), (((back)) ) , (((neck))), (an extremely delicate and beautiful),((beautiful detailed eyes)), messy floating hair, colored inner hair, depth  of field, (1girl), full body,   highres, (extremely detailed CG unity 8k wallpaper), cinematic lighting, dynamic angle, ((detailed shadow)) , ((cute)), ((cute face)), ((detailed face)), (detailed skin), ((visible shoulder)), (((delicate detailed  fullbody))), (((black fluttering dress with lace))), ((long dress)), (necklace), (earings), (blonde hair), ( (color)), (small breast), ((complex patterns)), (highlight hair), (gradient hair), ((ribbons)), (longshot), (dark  intense shadows), ((solo)), (smiling), (blue eyes), ((glowing eyes)), (soft focus), ((visible through hair) ), (disheveled hair), (bare shoulders), ((looking back)), ((detailed back)), ((bar",
   "大叔魔法177-堕天使":",大叔魔法177-堕天使A|(((masterpiece))), (((best quality))), ((ultra-detailed)),  (illustration), (detailed light),((an extremely delicate and beautiful)),(young girl),(solo),portrait of girl,(black eyes as bright  as diamonds),black long hair,fallen angel,(black wings:1.8),, bare_shoulders,dynamic angle,expressionless,looking_at_viewer ,arms_down,best illumination, best shadow, an  extremely delicate and beautiful), Floating black feathers,balck silk around,dead flowers,(sunlight),",
   "大叔魔法178-堕天法":",{{masterpiece}},{best quality},{solo},highres,extremely detailed CG wallpaper,extremely detailed figure,Amazing,perspective, one girl inside the {The blue and icy Church and flowers meadows} with very long black hair and hold a {luminous} Blue Holy  Sword in hands,night with richly layered clouds and clouded moon in the detailed sky,{many} glowing black {feathers},extremely detailed eyes,finely  detail,detailed face,angel,{black wing},Depth of field,{sacred feeling},{full body},Proportional coordination",
   "大叔魔法179-堕落法":",((masterpiece)),(((best quality))),((ultra-detailed)),((((full body)))),( unhelpless),tear,crying,((((( falling from the sky))))),(( Weathering With You)),(((full body))),(illustration) , (1 girl),((falling)),tear,((face towards the sky)),(hair flows upwards),((illustration)),((disheveled hair)), anime screeshot,((frills)),(1 girl),big top sleeves, floating,beautiful detailed isky,beautiful detailed eyes,overexposure,,expressionless,side blunt bangs,hairs  between eyes, ribbons,bowties,buttons,bare shoulders,(((small breast))), detailed  clothes,blank stare",
   "大叔魔法180-废土法":",(((masterpiece))), best quality, illustration,(((1girl))),((cute anime face)),(beautiful  detailed girl),expressionless,cold attitude, red pupils, short hair, white hair,(((beautiful detailed eyes))),jacket,cracked floor,damaged classroom,Tables  and chairs in disarray,The residual eaves DuanBi,beautiful sky,cumulus,mouldy,floating,wind,Dead end machine,(broken robot),(Mechanical girl)",
   "大叔魔法181-废墟法":",(extremely detailed CG unity 8k wallpaper,masterpiece, best quality, ultra-detailed), (best illumination, best shadow,  an extremel,medium_breasts,grey_hair,delicate and beautiful), dynamic angle, floating, finely detail, Depth of field (bloom), (shine), glinting stars,  classic,  ((illustration)), (painting), (sketch),magic clock, magic circle,(((dust))),broken glass, broken chain, ruins,  tower of fantasy background,(broken moon),((1_girl)),solo,long_hair,magical_girl,loli,eyeball,brown_eyes,gothic_lolita,black ribbon",
   "大叔魔法182-数码姬":",((best quality)), ((masterpiece)), ((ultra-detailed)), extremely detailed CG, (illustration),  ((detailed light)), (an extremely delicate and beautiful),(((((cyan and purple theme))))),Perfect details,((upper body)) ,Science fiction,sense of digital,((data analysis)),(((virtual technology))),(((soul girl))),((((young girl)))) ,shiny hair,white hair,blue eyes,bright pupils,(light source),electronic,((behind-the-head headphones)),((Crashing database)),0 and 1  code,solo,bule light,Digital background,expressionless,(Garbled code),((Running data)),((Running code)),((Virtual)),((digitization)),( source code),binary,With data composition,highlight,(((depth of field))",
   "大叔魔法183-穷奇录":",大叔魔法183-穷奇录|((masterpiece)),best quality, ((illustration)),original,extremely detailed wallpaper,((( beijing opera))), (sketch),((wash painting)),((ink splashing)),((((dyeing)))),((Chinese painting)),((beijing  opera))), (sketch),(wash painting),(ink splashing),dyeing,((Chinese painting)), ((a mythical ferocious animal)),{{The bull }},{{ long horns}},{{With wings on its back}},(Red and black wings,)(solo),mountain,Big and strong,Diabolical, Tyrannical",
   "大叔魔法184-学院法":",{best quality}, {{masterpiece}}, {highres}, extremely detailed CG, extremely detailed 8K wallpaper, extremely  detailed character, {an extremely delicate and beautiful}, portrait, illustration, solo focus, straight-on, dramatic angle, depthoffield, {{cinematiclighting}}, outdoors , {{{character({{{a girl}}}, solo, loli, {{{{full body}}}}, standing, expressionless, [[[light smile] ]], cute, beautiful detailed eyes, blue eyes, [long legs], {very_long_hair}, blonde hair, wavy_hair, [shiny hair],   {{ Gothic_Lolita } }, blue_white skirt, {{short skirt}}, black_Headdress, bowknot, {{{hair ornament}}}, [hair flower], stocking, [[Garter]],  Lace, cross-laced footwear, ribbon-trimmed sleeves)}}}, [background(building architecture, {{gothic architecture}}, starry sky, outdoors, church,  {castle}, [[fantasy]])]",
   "大叔魔法185-机工房":",flat color, (solo:1.5), (masterpiece:1.5), (best quality:1.5), amazing, beautiful detailed, extremely  detailed wallpaper, extremely detailed CG unity 8k wallpaper, extremely delicate and beautiful, finely detailed, extremely detailed wallpaper, cinematic lighting, fantasy, official  art, detailed background, (portrait: 1.5), solo, 1 girl, a (mechanician) girl in a (factory: 1.8), (teenage girl,  cute, blue eyes, blonde medium hair, bangs, light smile, big breasts), (belt, black tank top, black tank top: 1.5,  brown lace-up high boots: 1.5, black gloves, black shorts, thighhighs, pocket watch, cleavage, bare shoulder, navel: 1.5, wrench, goggles : 2), (industrial: 1.5, steampunk: 1.5, impasto: 1.5), (indoor, assembly line, valves: 1.3, steamer: 1.3, clockwork,  driving rods: 1.3, engines: 1.5, piezometer: 1.3, gears: 1.8)",
   "大叔魔法186-融合法":",a girl,Phoenix girl,fluffy hair,war,a hell on  earth,Beautiful and detailed explosion,Cold machine,Fire  in  eyes,World War,burning,Metal texture,Exquisite cloth,Metal carving,volume,best quality,normal hands,Metal details,Metal scratch,Metal defects,{{masterpiece}},best  quality,official art,4k,best quality,extremely detailed CG unity 8k,illustration,highres,masterpiece,contour deepening,Azur Lane,Girls' Front,Magical,Cloud Map Plan, contour deepening,long-focus,Depth of field,a cloudy sky,Black smoke,smoke of gunpowder, long-focus,Mature, resolute eyes, burning, burning sky,  burning hair,Burn oneself in flames, fighting,Covered in blood,complex pattern,battleing,Flying flames,Flame whirlpool,Doomsday Scenes,float,Splashing blood,on the  battlefield,Bloody scenes,Good looking flame,Exquisite Flame,Exquisite Blood,photorealistic,Watercolor,colourful, (((masterpiece))),best quality, illustration,beautiful detailed glow,detailed  ice,beautiful detailed water,red moon, (magic circle:1,2), (beautiful detailed eyes),expressionless,beautiful detailed white gloves, own hands clasped,  (floating palaces:1.1),azure hair,disheveled hair,long bangs, hairs between eyes, dark dress, (dark magician girl:1.1),black kneehighs, black  ribbon,white bowties,midriff,{{{half closed eyes}}},,big forhead,blank stare,flower,large top sleeves,, (((masterpiece))),best quality , illustration,(beautiful detailed girl),beautiful detailed glow,detailed ice,beautiful detailed water,(beautiful detailed eyes),expressionless,beautiful detailed white gloves, (floating  palaces:1.2),azure hair,disheveled hair,long bangs, hairs between eyes, (skyblue dress),black ribbon,white bowties,midriff,{{{half closed eyes} }},,big forhead,blank stare,flower,large top sleeves,(((ice crystal texture wings)),(((ice and fire melt)))",
   "大叔魔法187-蔷薇法":",(((masterpiece))), (((best quality))), ((ultra-detailed)), (illustration), ((an  extremely delicate and beautiful)), beautiful detailed eyes,(detailed light),(beautiful deatailed shadow), 1girl, (loli), (small_breasts), floating_hair,   glowing eyes, black hair,red eyes, sad, lolita, bare shoulders, white_dress, ((rose)),(vines), (blood), cage, bandage,  red rope, ((sketch)),(painting)",
   "大叔魔法188-艺墨风":",( masterpiece:1.2),(best quality:1.2),(illustration:1.5),1girl,chinese dragon,chinese girl,female focus on ,(color splashing:1.2),(colorful:1.2), (color Ink wash painting:1.2),(ink splashing:1.2),sketch, Masterpiece,best quality, beautifully painted, highly detailed,",
   "大叔魔法189-飘花法":",((ink)),(water color),bloom effect,((best quality)),((world masterpiece)),((illustration) ),(white_hair),(gold_eye),(((1girl))),(beautiful detailed girl),golden_eye,((extremely_detailed_eyes_and_face)),long_hair,detailed,detailed_beautiful_grassland_with_petal,flower,butterfly,necklace,smile,petal, (silver_bracelet),(((surrounded_by_heavy_floating_petal_flow)))",
   "大叔魔法190-黯冰法":",{{{Surrounded by beautiful detailed black ice crystal}}},{masterpiece},highres,best quality,{an extremely delicate  and beautiful},watercolor,beautiful detailed eyes,Depth of field,extremely detailed CG unity 8k wallpaper,{{1girl}},very long hair,asymmetrica side bangs, {{crystal  texture hair}},shiny slik,white hair,standing,bright pupils,divine,majestic,{detailed ice},detailed ((frost)),gradient blue eyes,(( (translucent detailed black crystal detached sleeves))),(black royal backless dress),black skirt of ice crystals,floating dress,expressionless,silk skin,{{detailed  black crystal flying butterfly}},{{{floating blackice lotus}}},{{shiny blackice crystal}},Crushed ice,detailed crystal texture,bloom,prismatic light,sharpened, ((transparent crystal breasts)),(((transparent crystal skin))),shine blackcrystal tiara necklace and earrings,eyelashes,bright pupils,lightblack eyeshadow,eyeliner, starry crystal  tiara,big breasts,gradient crystal arms,ray tracing,cinematic angle,backlight,lens flare,depth of field,",
   "大叔魔法191-骨架":",masterpiece,sketch,Skeleton,{{{on Skeletonhorse}}},masterpiece,sketch,highly detailed,blood splatter,hell,{{{blood sword}} },spread out,crown,necklace,night temple,Reaper,terror,angry,king, apocalypse, multiple arms,devil,panorama,fisheye lens, angel, from below,worship,throne, ",
   "大叔魔法192-笼中鸟":",{{water}},{ {colorful bubles}}, {{colorful stars}},{{solo}},{an extremely delicate and  beautiful girl},{{people in the cage}}, {falling feathers},legs in water,night skirt,white hair,Confused Eyes,beautiful detailed eyes,red  eyes,smile,{{blood}}, earrings ,silvery cross,Sitting,whole body drawing,fog ,white skin,shackles,grave,lace,hair accessory,loli,rose, moon ,blak sky,{{big white wings behind people}},",
   "大叔魔法193-★分割语法左黑发,右金发":",Amazing, beautiful detailed eyes, (2girls:1.3), masterpiece, (best quality:1.3),  finely detail,depth_of_field, extremely detailed CG unity 8k wallpaper AND (best quality:1.3), 2girl, black_hair, red_eyes, (arms_behind_back) AND (best quality: 1.3), 2girl, blonde_hair, blue_eyes, (arms_behind_back)",
   "大叔魔法194-分割左黑发右金发":",Amazing, beautiful detailed eyes, (2girls:1.3), masterpiece, (best quality:1.3), finely detail ,depth_of_field, extremely detailed CG unity 8k wallpaper AND (best quality:1.3), 2girl, black_hair, red_eyes, (arms_behind_back) AND (best   quality:1.3 ) ,  2girl, blonde_hair, blue_eyes, (arms_behind_back)",
   "大叔魔法195-分割左黑发右金发配合Latent Couple":",Amazing, beautiful detailed eyes, (2girls:1.3), masterpiece, (best quality:1.3),  finely detail,depth_of_field, extremely detailed CG unity 8k wallpaper AND (best quality:1.3), 2girl, black_hair, red_eyes, (arms_behind_back) AND (best quality :1.3), 2girl, blonde_hair, blue_eyes, (arms_behind_back)",
   "大叔魔法196-分割四个需配合Latent Couple":",大叔魔法196-分割四个需配合Latent Couple|masterpiece, best quality, ((4girls))f multiple girls , light smile, sea, beach, sunset,AND masterpiece, best quality, 4girls,default, white dress, wing hair ornament, twinteils,AND masterpiece, best  quality, 4girls, default,dress, blue eyes, white hair, black dress,AND masterpiece, best quality, 4girls,default, purple.eyes, purple hair,  ribbon,AND masterpiece, best quality, 4girls,default, blue eyes, brown hair, pink hair bowjacket, neckerchief",
   "大叔魔法197-黑暗破碎风":",Collapse, shake, destroy, violence, cruelty, craziness, fragmentation, crushing, ruthlessness,",
   "大叔魔法198-史诗级怪物":",magic the gathering commanders and frightening beast fight, magnificent, close up, details, sharp focus, elegant,  highly detailed, illustration, by Jordan Grimmer and greg rutkowski and PiNe and Imoko and wlop and maya takamura, intricate, beautiful, Trending artstation,  pixiv, digital Art.",
   "大叔魔法199-科幻女甲风":",a warrior robot astronaut, floral! horizon zero dawn machine, posing for a fight intricate, elegant,  highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha, 8  k ",
   "大叔魔法200-很胖的盔甲战士":",space marine warrior full body cyberpunk horror scifi extremely high detail portrait dnd, painting by kyoung hwan  kim, anh dang, 鳕 鱼, thomas guedes, pixiv trend, trending on artstation, 8 k ",
   "大叔魔法201-异形怪物无法判断":",gorey fleshmetal cyborg daemonhost, by antonio j. manzanedo, giger, alex grey, android jones, wayne barlowe , philippe druillet, raymond swanland, cyril rolando, josephine wall, harumi hironaka, trending on artstation ",
   "大叔魔法202-不可思议的乌龟":",a cell shaded cartoon giant lovecraftian mechanized turtle from howl's moving castle ( 2 0 0 4 ),  on a desert road, full body, illustration, wide shot, very subtle colors, post grunge, concept art by josan gonzales, wlop, by  james jean, victo ngai, trending on artstation, hq, deviantart, art by artgem ",
   "大叔魔法203-素材游戏化":",Concept art of the new League of Legends Champion on Summoner's Rift, Isometric, Digital Painting, Trending on  Artstation, Character Reference Sheet",
   "大叔魔法204-经典西方龙":",A beautiful and very detailed photo of a huge lich dragon with wings spread out in a night  of storm clouds and red lightning streaking down from the sky. He has large circular horns like those of a bighorn ram, red eyes,  and a few pieces of his flesh missing or torn, and green smoke coming from his dark greenish body, majestic, exalted, elegant,  epic, 4k, 8k, trending on Artstation, digital art",
   "大叔魔法205-经典雪景":",a hyper realistic professional photographic view picture of a heavenly snow mountain with a dark blue lake in front  of it, photographic filter unreal engine 5 realistic hyperdetailed 8k ultradetail cinematic concept art volumetric lighting, fantasy artwork, very beautiful scenery, very realistic  painting effect, hd, hdr, cinematic 4k wallpaper, 8k, ultra detailed, high resolution, artstation trending on artstation in the style of Albert  Dros glowing rich colors powerful imagery nasa footage drone footage drone photography",
   "大叔魔法206-骷髅水母奥义":",close-up portrait goddess skull, thorax, x-ray, backbone, jellyfish phoenix head, nautilus, orchid, betta  fish, bioluminiscent  creatures, dark deep complex air bubbles in background, intricate artwork by Tooth Wu and wlop and beeple. octane render, trending  on artstation, greg rutkowski very coherent symmetrical artwork. cinematic, black and white, contrasted, hyper realism, high detail, octane render, 8k",
   "大叔魔法207-魔兽化风格":",A painting of Kobold trending on artstation in the style of Greg Rutkowski",
   "大叔魔法208-史诗战槌战争":",a photorealistic hyperrealistic render of an epic close quarters last stand battle between an outnumbered squad of space  marines and genestealers from warhammer 4 0 k by greg rutkowski, james paick, wlop, nicolas bouvier sparth, artgerm, dramatic moody sunset lighting,  long shadows, volumetric, cinematic atmosphere, octane render, artstation, 8 k ",
   "大叔魔法209-日本恐怖漫画风":",a comic book style japanese horror bloody girl with large eyes standing infront of a shrine by dan  mumford, yusuke murata and junji ito, blood lines, yokai, shinigami, tentacles, smoke, eyes, shurikens, kanji, 8k, unreal engine, trending  on artstation, pixiv, intricate details, volumetric lighting",
   "大叔魔法210-超逼真美女":",photo of a gorgeous anime girl in bikini in the style of stefan kostic, realistic, half body  shot, sharp focus, 8 k high definition, insanely detailed, intricate, elegant, art by stanley lau and artgerm, extreme bokeh foliage ",
   "大叔魔法211-日式漫画风":",full body portrait character concept art, anime key visual of a confused girl, studio lighting delicate features  finely detailed perfect face directed gaze, gapmoe yandere grimdark, trending on pixiv fanbox, painted by akihiko yoshida from bbwchan, makoto shinkai takashi takeuchi , krenz cushart, studio ghibli ",
   "大叔魔法212-写实女孩":",a portrait of a full body beautiful asian girl, young with long hair, safi'jiiva armor, horror  scene, hyper - realistic, very detailed, intricate, very sexy pose, slight smile expression, unreal engine, dramatic cinematic lighting rendered by octane,  8 k, detailed ",
   "大叔魔法213-自制女孩在瓶子里":",A minigirl trapped in a huge Baote bottle with water on it's side , by Cyril Rolando,  in container,air_bubble, blue_eyes, bubble, long_hair, solo, splashing, submerged, thighhighs, water, water_drop,  photo of a gorgeous anime girl in  bikini in the style of stefan kostic, realistic, half body shot, sharp focus, 8 k high definition, insanely detailed, intricate, elegant,  art by stanley lau and artgerm, extreme bokeh foliage",
   "大叔魔法214-综合动画":",integrated, anime,{{selfie of schoolgirl, kawaii}}, [[[close-up full body]]], site-seeing  spot, photo background, cinematic angle",
   "大叔魔法215-关在方瓶女孩":", A minigirl trapped in a  bottle with water on it's side ,by Cyril Rolando, in  container,air_bubble, blue_eyes, bubble, long_hair, solo, splashing, submerged, thighhighs, water, water_drop,  photo  of a gorgeous anime girl in bikini  in  the style of stefan kostic, realistic, half body shot, sharp focus, 8 k high definition, insanely detailed, intricate, elegant, art by  stanley lau and artgerm, extreme bokeh foliage,(Off in Square bottle:2.0),",
   "大叔魔法216-圆瓶女孩":",1girl, bikini, blue_eyes, breasts, collarbone, in_container, long_hair, looking_at_viewer, medium_breasts, partially_submerged, solo, swimsuit,  {{{{{in_container}}}}},{minigirl },air_bubble, blue_eyes, bubble, long_hair, solo, splashing,   submerged, thighhighs, water, water_drop,   photo   of a gorgeous anime girl in bikini in the style of stefan kostic, realistic, half body shot, sharp focus, 8 k high definition,  insanely detailed, intricate, elegant, art by stanley lau and artgerm, extreme bokeh foliage",
   "大叔魔法217-写实机械蜘蛛":",steampunk spider, biomechanical, very coherent symmetrical artwork, horror, 3 d model, unreal engine realistic render,  8 k, micro detail, intricate, elegant, highly detailed, centered, digital painting, artstation, smooth, sharp focus,   illustration, artgerm, tomasz  alen   kopera, by wlop ",
   "大叔魔法218-机械蜘蛛":",steampunk spider, biomechanical, very coherent symmetrical artwork, horror, 3 d model, unreal engine realistic render, 8  k, micro detail, intricate, elegant, highly detailed, centered, digital painting, artstation, smooth, sharp focus, illustration, artgerm, tomasz alen kopera , by wlop ",
   "大叔魔法219-上帝说给你手":",And the Lord said, Let there be hands so that the fingers may have friends.And from  the void formed hands to connect fingers",
   "大叔魔法220-神说手不可触碰":",And the Lord said, Let there be fingers. And void began to take form",
   "大叔魔法221-史蒂文食人的嘴":",Steven Tyler as Jaws",
   "大叔魔法222-极致萝莉风":",masterpiece,loli,looking at viewer,white hair,long hair,1girl,hair ornament,hair flower,cute,white flower,white  knee high,parted lips,dynamic angle,blurry,light blue skirt,animal_ear,{{{{{masterpiece}}}}},{{{{{best quality,highres,blurring sides, strong illumination}}}}}};{{8k,original art,realistic,ray tracing,hdr}},{{{{full body}}}}{{{strongly close up of  face}}};{{{{by famous artist; by paul hedley}}}}{one girl},{young loli},2 arms;{beautiful,extremely detailed,long, blue,wavy,flowing,glossy hair,parting with long pigtails,seldom forelock,hairstipes on temples};{beautiful,highly detailed,fair skin}{beautiful,detailed,reflective,light blue  eyes; beautiful,detailed blue scattered eyebrows};{beautiful,highly detailed,bit effeminate face; thin chin,light blush,tranquil expression};{beautiful ears}masterpiece,loli ,looking at viewer,white hair,long hair,1girl,hair ornament,hair flower,cute,white flower,white knee high,parted lips,dynamic angle,blurry,light blue  skirt,animal_ear,{{{{{masterpiece}}}}},{{{{{best quality,highres,blurring sides,strong illumination}}}}}};{{8k,original art, realistic,ray tracing,hdr}},{{{{full body}}}}{{{strongly close up of face}}};{{{{by famous artist; by  paul hedley}}}}{one girl},{young  loli},2 arms;{beautiful,extremely detailed,long,blue,wavy,flowing,glossy hair,parting with long pigtails, seldom forelock,hairstipes on temples};{beautiful,highly detailed,fair skin}{beautiful,detailed,reflective,light blue eyes; beautiful,detailed blue scattered eyebrows};{beautiful, highly detailed,bit effeminate face; thin chin,light blush,tranquil expression};{beautiful ears}",
   "大叔魔法223-怪异宝可梦":",Pokemon weirdness",
   "大叔魔法224-卡通宇宙篮":",space opera esque",
   "大叔魔法225-宇宙生物在街道":",Bootleg copies of Cyan, a cute squid-like stuffed animal, secretly built by aliens, begin to  replicate themselves when no one is looking and their numbers soon clog the streets of the city  -v 4",
   "大叔魔法226-科幻胚胎仓":",a baby embryo in a futuristic labs glass container with cyan holographic digital displays with statistics on screen  v 4",
   "大叔魔法227-夜晚动作姿势":",beautiful star studded night , looking at the evening sky , forest silhoette , dark water lake ,  cyan shooting stars lighting up the night sky , milky way , full length dynamic action pose ,,Eads pindot , , highly detailed ,  hyperdetailed, hypermaximalist, hyperrealistic, cinematic, epic, octane render, ultra HD, 8k inner glow ,3 d, up light , strobe light v 4 ",
   "大叔魔法228-高清夜晚的昆虫":",cyan colored fireflys dotted all over the marsh , beautiful sight on a starry night ,highly detailed  , hyperdetailed, hypermaximalist, hyperrealistic, cinematic, epic, octane render, ultra HD, 8k inner glow ,3 d, up light , strobe light - -q 2 --v 4 --v 4",
   "大叔魔法229-幻想元素艺术":",a gargantuan tree the size of a skyscraper burning with flames of cyan against a backdrop of a  starlit night sky, cyan colored fire, illustrated fantasy art, low angle, dramatic scene --ar  --s 200 --no frame, crop,  text, signature, watermark, blur --q 2 --v 4",
   "大叔魔法230-青色虫子摄影":",acro photography of a cyan bug --v 4",
   "大叔魔法231-末日城市":",bizarre futuristic living cityscape, surreal cyan alien brutalist architecture, by Tetsuya Ishida, by HR Giger, by Peter  Gric, by Dariusz Zawadzki, by Naoto Hattori, by Joe Fenton, dramatic photograph --v 4 --ar  --chaos 50 --no  border, frame",
   "大叔魔法232-迷宫透视建筑":",isometric cross section interior rooms technopunk Fusion Reactor double helix, geometric, modern, wires, panels, lazers,  gauges, pipes, plasma, neon, tokamoks experiment, iter, lightning, tower, center, multi-leveled, night, technical drawing blueprints, ghibli, beksinky,  james gurney --ar  --v 4",
   "大叔魔法233-战船和机":",filling the burning skies is an armada of giant dieselpunk battleship airships, echelons of gargantuan flying war  machines. glorious imperial sky navy , majestic cumulus clouds. epic movie scene photo inspired by ww2, studio ghibli, juan   geminez and top  military   sci fi. --q 2 --ar  --v 4",
   "大叔魔法234-复合建筑":",busy street on wasteland pastel and steel industrial dull rustic metallic space station complex architecture into beautiful day environment , rivers and streams bright glowing and flowing down the streets, huge air polygonal round corners   intake gates with shutters, stone maze, living   pastel  color pods towering skyscrapers at cliff edge, mad max like color pallet kitbash car era shapes , The 5th element,The Matrix, photography award , ultra realistic, wide angle, high detail, volumetric light at mid day nice sky, Trending on artstation,Unreal engine hyper realistic photography magazine  --ar  --v 4 ",
   "大叔魔法235-银河中的运动模糊":",webway in galaxy, motion blur, enviroment --ar  --v 4",
   "大叔魔法236-在冬天旅馆喝醉":",shattrath city in the inn, travelers drinking at the bar, snowy environment outside, snow storm outside , dynamic lighting, dramatic, lighting --v 4",
   "大叔魔法237-马车旅程":",epic western fantasy world, oregon trail wagon on road, large floating islands of deserts, swamplands, and grasslands , western towns, dirt roads, large scale environment concept, hyper-realistic, hyper-detailed, high resolution, cinematic composition, octane render, photoreal, high  details, 8k, artstation trending, photography, hyperrealistic, vray renderer --ar --v 4 ",
   "大叔魔法238-赛车旅程":",ant merged with super car, space as background, cinematic shot, cinematic light, 8k, hyper realistic, hyper  detailed, photograph, abstract --v 4",
   "大叔魔法239-印象主义":",sweet dreams are made of this, art by Shaun Tan, art by James Abbott McNeill Whistler, oil  paint on canvas, impresionism art, symbol art, muddy colors, broken surface, ambient light, --ar --v 4",
   "大叔魔法240-炼金术士生活":",an Alchemist's Workshop, glass flasks, tubes, glass pipes, stoppers, books, Cyan Fluids, cyan glow,  smoke, an ancient man asleep in a chair with a book covering his face,3 - Photorealistic, Zoomout, sharp focus, ultra realistic, cinematic  lighting, octane render, unreal engine- 8k --ar  --v 4 --q 2",
   "大叔魔法241-高清撞击地面":",futuristic scifi life pod burning up in the atmosphere, cyanoethylation explosions, heavily cratored planet, night,  🔥💥   🌊👽🌟  --ar  --v 4",
   "大叔魔法242-远景星空物":",cyanthropic generative effect in landscape, dramatic strange mysterious cosmic scifi spacecore, Simon Stålenhag and hr geiger and  Dariusz Zawadski and Jakub Rozalski and takeshi oga, anamorphic, negative space, detailed, horizon line, massive scale, unnatural lighting, 4k --q 2  --v 4 --upbeta --ar  --no words,wording,letters,lettering,title",
   "大叔魔法243-战争与和平":",Future war and peace",
   "大叔魔法244-巴士虫子机器人":",Bus to bug to battle droid",
   "大叔魔法245-ex机器人":",Ex-S gundam, RX-93, cyberpunk, full body, ultra  high detail, 8k, photography, taken on   a Sigma 35mm F1.4 ART DG HSM Lens for Canon DSLRs in the style of Sandra Chevrier --v 4 --q 2 -- v 4 --ar",
   "大叔魔法246-冰山上的工厂":",Pollution Factory on top of iceberg --v 4",
   "大叔魔法247-漫画女孩":",book, bookshelf, computer, controller, game_controller, gamepad, greyscale, headphones, long_hair, lying, messy_room, monochrome, multiple_girls , phone, playstation_controller, skirt, tissue_box,((1girl)), (solo), (perfect anatomy), (realistic:1.5), (photo background), (light-shadow  symmetry face), ((direct sunlight face)), (detailed:1.2), (masterpiece:1.5), (bishoujo), (dynamic angle), (dynamic hair),  ((dynamic pose), (finaly detailed beautiful eyes and detailed face), (detailed sky), (beautiful detailed eyes), (colorful:1.15), ( dramatic light), (high quality), (light eyes), (extremely high detail), (cute face), swept bangs, long hair, parted lips,  blush, bangs, traditional media, limited light, (disheveled hair), beautiful detailed glow,   (loli:1.6), best quality, (black eyes:   1.25 ), eyelash, (see through hair), Blunt bangs, see through, (illumination: 1.2), (nouveau: 1.5), (cowboy shot), blue  sky, (cloud:1.14), open mouth, bra visible through clothes, T-shirts, Skirt, high ponytail, (wind), street, thighs, light  smile, ",
   "大叔魔法248-高清一男二女随机":",(Masterpiece:1.1), (best quality:1.1), ((chromatic aberration)), ((caustic)), dynamic  angle, ((ultra-detailed)), (illustration:1.1), (girl:1.2), (beautiful detailed girl:1.2), ((disheveled hair)), (anime girl :1.2), beautiful detailed   glow, detailed, Cinematic light, intricate detail, highres, ((a nine year old blonde girl and her parents sit  on a blanket at the beach and watch through sun go down in the style of Carl larsson, )), trending on ArtStation Pixiv,  high detail, sharp focus,   smooth, aesthetic, rule of thirds, scape of, floating object, ",
   "大叔魔法249-高清二女":",(Masterpiece:1.1), (best quality:1.1), ((chromatic aberration)), ((caustic)), dynamic angle,  ((ultra-detailed)), (illustration:1.1), (girl:1.2), (beautiful detailed girl:1.2), ((disheveled hair)), (anime girl:1.2 ), beautiful detailed glow, detailed, Cinematic light, intricate detail, highres, ((a nine year old blonde girl and her parents sit on  a blanket at the beach and watch through sun go down in the style of Carl larsson, )), trending on ArtStation Pixiv, high  detail, sharp focus, smooth, aesthetic, rule of thirds, scape of, floating object, ",
   "大叔魔法250-测试怀孕xd":",(Masterpiece:1.1), (best quality:1.1), ((chromatic aberration)), ((caustic)), dynamic angle,  ((ultra-detailed)), (illustration:1.1), (girl:1.2), (beautiful detailed girl:1.2), ((disheveled hair)), (anime girl:1.2 ), beautiful detailed glow, detailed, Cinematic light, intricate detail, highres, ((a nine year old blonde girl and her parents sit on  a blanket at the beach and watch through sun go down in the style of Carl larsson, )), trending on ArtStation Pixiv, high  detail, sharp focus, smooth, aesthetic, rule of thirds, scape of, floating object,, {best quality}, {{masterpiece}}, {highres},  original, extremely detailed 8K wallpaper, 1girl, {an extremely delicate and beautiful},,blunt_bangs,blue_eyes,black hair,sheer tulle  dress,garter straps garter  belt ,Xiao Qingyi Single ponytail cheongsam black,Pregnancy, cross-part tattoos, lewd tattoos,",
   "大叔魔法251-增加细节":",(Masterpiece:1.1), (best quality:1.1), ((chromatic aberration)), ((caustic)), dynamic angle,  ((ultra-detailed)), (illustration:1.1), (1girl:1.2), (beautiful detailed girl:1.2), ((disheveled hair)), beautiful detailed glow,  detailed, Cinematic light, intricate detail, highres, ((box full of clouds, Hiroaki Tsutsumi style)), trending on ArtStation Pixiv, high detail,  sharp focus, smooth, aesthetic, rule of thirds, ",
   "大叔魔法252-1995高清细节":",(Masterpiece:1.1), (best quality:1.1), ((chromatic aberration)), ((caustic)), dynamic angle,  ((ultra-detailed)), (illustration:1.1), (1girl:1.2), (beautiful detailed girl:1.2), ((disheveled hair)), beautiful detailed glow,  detailed, Cinematic light, intricate detail, highres, ( from a point and click graphic adventure game made in 1995, pixel art, retro)) , trending on ArtStation Pixiv, high detail, sharp focus, smooth, aesthetic, rule of thirds,",
   "大叔魔法253-绿发猛男":",1man,high quality, muscular, long curly hair, green hair, yellow eyes, brown skin, colorful, pirate  ship, cumulonimbus clouds, lighting, blue",
   "大叔魔法254-官绘细节":",(masterpiece:1.3), highres, best quality, official art,1girl, upper body, petite, cute, long hair , brown hair, blue eyes, (camisole),happy,(bright) sun lighting",
   "大叔魔法255-可爱女孩":",1girl, brown_eyes, brown_hair, chibi, full_body, jacket, long_hair, smile, solo, transparent_background",
   "大叔魔法256-可爱男孩":",1boy, eyes, hair, chibi, full_body, jacket, solo, transparent_background,cute,",
   "大叔魔法257-雷电将军(横)":",Raiden Shogun, upper_body, looking at viewer,",
   "大叔魔法258-流浪者":",Wanderer",
   "大叔魔法259-温迪(横)":",venti, upper body, looking at viewer,",
   "大叔魔法260-钟离(立绘)":",zhongli, yellow eyes, looking at viewer,",
   "大叔魔法261-刻晴(竖)":",Keqing, sailor shirt, midriff, skirt",
   "大叔魔法262-可莉(上半身)":",klee, upper body, looking at viewer,",
   "大叔魔法263-美女烟火秀":",sun, lens flare, jewelry, stage lights, bracelet, sunlight, diffraction spikes, sparkle, light rays, bokeh , earrings, breasts, glint, spotlight, sunbeam, long hair, stage, lights, shooting star, navel, light, sunrise, black hair, ^^^ , condensation trail, armlet, mole, looking at viewer, rainbow, bangs, pelvic curtain, multiple girls, bangle, sky, revealing clothes, large breasts , open mouth, hoop earrings, necklace, fireworks, dress, sparkle background, brown eyes, thighs",
   "大叔魔法264-色情001":",(masterpiece:1.3), highres,best quality,official art,1girl,nsfw,medium brown hair,blue eyes,medium breasts,pussy, spread legs, sitting,",
   "大叔魔法265-HHH":",1boy, 1girl, bracelet, breasts, brown_hair, hetero, jewelry, kasumi_\(doa\), large_breasts, leg_lift, long_hair,  navel, nipples, nude, penis, pussy, sex, stripper_pole, thighhighs, uncensored, vaginal,   white_legwear",
   "大叔魔法266-黑暗盔甲骑士风":",SFW, Masterpiece, best quality, high detail, by Gaston BussiÃ¨re, Claude Monet, Artstation, flame  particles, light particles, zoomed out, (full body:1.3), Golem, armored, full armor, metal skin, metal face, full helmet, inside  a metalworking factory, 1boy, eyes, hair, chibi, full_body, jacket, long_hair, solo, transparent_background,cute,, a gargantuan tree the size of a  skyscraper burning with flames of cyan against a backdrop of a starlit night sky, cyan colored fire, illustrated fantasy art, low angle, dramatic  scene --ar  --s 200 --no frame, crop, text, signature, watermark, blur --q 2 --v 4",
   "大叔魔法267-小萝莉吐舌头":",(masterpiece:1.33),(best quality:1.33),(extremely detailed CG unity 8k wallpaper:1.21), (official  art),(illustration),1girl,(loli:1.33),(petite:1.33),long brown hair,bangs,solo,highly detailed,open mouth,wet tongue,a lot of saliva ,(oral invitation),beautiful detailed face,naked,(heart shaped pupils:1.33),looking at you,lighting blush,streaming tears,depth of field,",
   "大叔魔法268-极致色情":",delicate, masterpiece, beautiful detailed, colourful, finely detailed, intricate details, nsfw, (1 girl:1.1), solo , (from front:1.3), (a beautiful 17 age years old cute Korean girl:1.3), instagram, (kpop idol, korean mixed), ( white hair + low tied hair:1.3), (50mm Sigma f/1.4 ZEISS lens, F1.4, 1/800s, ISO 100, photograpy:1.1),  (large breast:1.0), (photorealistic:0.8), pornography, (denim suspenders skirt:1.3), (beaming smile:1.2), (street, leg raise on  bench, panties:1.2),",
   "大叔魔法269-极致诱惑背影":",delicate, masterpiece, beautiful detailed, colourful, finely detailed, intricate details, nsfw, (1 girl:1.1),  solo, (from front:1.3), from above, (a beautiful 17 age years old cute Korean girl:1.3), instagram, (kpop idol, korean  mixed), (white hair + low tied hair:1.3), (50mm Sigma f/1.4 ZEISS lens, F1.4, 1/800s, ISO 100,  photograpy:1.1), (medium breast:1.0), (photorealistic:0.8), pornography, (thong lingerie:1.3), (beaming smile:1.2), (lying on bed , sleeping, closed eyes:1.2),",
   "大叔魔法270-极致诱惑穿内衣睡着":",delicate, masterpiece, beautiful detailed, colourful, finely detailed, intricate details, nsfw, (1 girl:1.1 ), solo, (from front:1.3), (from above:1.1), (a beautiful 17 age years old cute Korean girl:1.3), instagram,  (kpop idol, korean mixed), (white hair + low tied hair:1.3), (50mm Sigma f/1.4 ZEISS lens, F1.4, 1/ 800s, ISO 100, photograpy:1.1), (medium breast:1.0), (photorealistic:0.8), pornography, (open white shirt, thong panties:1.3), ( beaming smile:1.2), (lying on bed, sleeping, closed eyes:1.2),",
   "大叔魔法271-极致诱惑不穿内衣睡":",delicate, masterpiece, beautiful detailed, colourful, finely detailed, intricate details, nsfw, (1 girl:1.1 ), solo, (from front:1.3), (from above:1.1), (a beautiful 17 age years old cute Korean girl:1.3), instagram,  (kpop idol, korean mixed), (white hair + curved bob hair:1.3), (50mm Sigma f/1.4 ZEISS lens, F1.4, 1/ 800s, ISO 100, photograpy:1.1), (medium breast:1.0), (photorealistic:0.8), pornography, (open  white shirt, micro panties:1.3),  ( beaming smile:1.2), (lying on bed, sleeping, closed eyes, nipple:1.2),",
   "大叔魔法272-动画少女一字腿":",KAWAII ,JAPANESE girl , (Straight leg,standing on one leg,leg_lift, standing_split to show CROTCH,CAMISOLE ) ,pleated skirt,SMILING,5 fingers,looking at viewer,FROM SIDE,LARGE BREAST,",
   "大叔魔法273-背影":",a woman in a white bra laying on a bed with her legs crossed and her butt exposed, with  her head resting on her hand on her chest, by Terada Katsuya",
   "大叔魔法274-露米哑背影":",octane render, a woman in a white bra laying on a bed with her legs crossed and  her butt exposed, with her head resting on her hand on her chest, by Terada Katsuya, rumia, ((perfect body)), 1girl,  red ribbon, red necktie, blonde hair, black skirt, red eyes, short hair, solo",
   "大叔魔法275-清纯警花":",delicate, masterpiece, beautiful detailed, colourful, finely detailed, intricate details, (1 girl:1.1), solo, ( from front:1.3), looking at viewer, (a beautiful 19 age olds cute Korean girl:1.3), instagram, (kpop idol, korean mixed),  (white hair + long ponytail hair:1.3), (50mm Sigma f/1.4 ZEISS lens, F1.4, 1/800s, ISO 100, photograpy:1.1 ), (large breast:1.0), (photorealistic:0.8), (police uniform, navy pencil skirt:1.3), (beaming smile:1.2), (crosswalk, police  hat, straight on, thigh:1.2),",
   "大叔魔法276-露米哑":",★[rumia ((perfect body)) 1girl red ribbon red necktie blonde hair black skirt red eyes short  hair solo]",
   "大叔魔法277-美女哈尔":",★[masterpiece best quality looking at viewer portrait 1girl blonde hairharu]",
   "大叔魔法278-美女系A":",★[atelier_(series)atelier_ryzaatelier_ryza_2atelier_ryza_3azur_lanereisalin_stoutreisalin_stout_(late_night_alchemist)official_artpromotional_art1girlarchitecturearmpitsbarefootblanketbreastsbrown_eyesbrown_hairclosed_mouthcollarboneeast_asian_architecturefeethair_ribbonlarge_breastslegslooking_at_viewerlyingnavelofficial_alternate_costumeon_stomachpillowribbonshirtshort_hairsolostomachthe_posetoestreeunderwearwhite_shirt]",
   "大叔魔法279-掀裙风":",★[clothes liftshirt liftNo underwearstandingopen mouthclenched teethgloom (expression)shadedshaded facedisgustannoyedlooking at viewerlift up topwearlooking downperspective from below]" ,
   "大叔魔法280-模组1号":",★[photograph of a (small 5 year old girl:1.15) teen young girl 1girl long dress cute  hat red bow (((child))) full body ((analog photo)) (detailed) ZEISS studio quality 8k (((photorealistic))) ((detailed )) transfer ((colorful)) (portrait)   50mm bokeh]",
   "大叔魔法281-模组2号":",★[photograph of a (12 year old girl:1.15) teen young girl running waves 1girl black bikini  crop top sun hat blue sunglasses (((child))) standing on beach (upper body:1.3) ((analog photo)) (detailed) ZEISS studio  quality 8k (((photorealistic))) ((detailed)) transfer ((colorful)) (portrait) 50mm bokeh]",
   "大叔魔法282-模组3号":",★[photograph of a masterpiece high quality (beautiful nude sexy 22 year old :1.15) standing (woman :1.2) large  breasts on bed nude 1girl (full body:1.3) cameltoe ((analog photo)) (detailed) ZEISS studio quality 8k (((photorealistic ))) ((detailed)) transfer ((colorful)) (portrait) 50mm bokeh]",
   "大叔魔法283-印度风格":",★[indian style]",
   "大叔魔法284-揉胸动画":",★[1boy1 girlhands on another's breast  breast grab]",
   "大叔魔法285-多种视角":",★[three views from front back and sidecostume setup materials]",
   "大叔魔法286-半人马":",★[{{{centaur}}} {{horse_girl}} {hoof} midriff {monster_girl} shiny hair medium_breasts]",
   "大叔魔法287-我的妹妹不可能这么可爱":",★[masterpiecebest quality1girllooking up ore no imouto ga konna ni kawaii wake ga nai1girl kousaka_kirino crossed  armsorange hair",
   "大叔魔法288-五更琉璃":",★[gokou ruri Gothic & Lolita ore no imouto ga konna ni kawaii wake ga nai best_qualityultra-detailedillustrationperfect_detailedshiny] ",
   "大叔魔法289-新垣1":",★[{{{{{aragaki_ayase}}}}}ore_no_imouto_ga_konna_ni_kawaii_wake_ga_naiNavy blue long straight hairNavy blue eyes16 years oldserafuku]",
   "大叔魔法290-新垣2":",★[{{{{{aragaki_ayase}}}}}2010ssketchore_no_imouto_ga_konna_ni_kawaii_wake_ga_naiofficial{{{{{blue}}}}} long straight hairNavy blue eyessummer serafuku (red_tiewhite shirtgray collar)gray skirt]",
   "大叔魔法291-公主抱":",★[a boy carries a girl in his arms]",
   "大叔魔法292-二手发光":",★[{arms raised in the air} {{{extend arms straight out}}} 1girl full body]",
   "大叔魔法293-高难度动作":",★[back shot symmetrical twerk dance upside-down face full body]",
   "大叔魔法294-左右对称二人":",★[doppelganger pose]",
   "大叔魔法295-邪神妹":",★[1girl blonde hair bangs blunt bangsgreen eyes blue dress small breast [puffy sleeves?] juliet sleeves long  sleeves frilled skirt long hair curly hair smile [[[[nun?]]]] open mouth cross necklace megami magazine loli]",
   "大叔魔法296-机器生物体":",★[masterpiecebest qualitylens 135mm f1.8 (upper body:0.7) (from above:1.3) looking up full body  masterpiecebest qualitymasterpiecebest qualitymasterpiece(1girl:1.15763) best qualityhyper extreme detailedby famous artist modern  retro computer Retro IT gadgets many cables intravenous drip( (Organic body: 0.6):1) (serial experiments lain:1.1)make eye contact(Faint lips:0.2)mana machine mana lightbackground mana laboratory[[[cyborg]]] metallic mixture( Luminous pattern of electronic circuits:0.8) brown hair ((short hair)) bob cut (swept bangs) (short_hair_with_long_locks:1.2) (Single sidelock:1.6) brown  eyes jitome wide eyed (Harf closed eye:1.2) ((((tareme)))) (expressionless:1.2) (clear face:1.2) empty eyes vacant eyes  androgynous (pale skin:0.65) dark circles under  the eyesshiny skin shiny hair( a x hair ornament:1.1) (Asymmetrical hair:1.15) highly detailed  small breasts teen (iwakura lain:1.0) Lots of cables connected to the body.]",
   "大叔魔法297-零波零":",★[ayanami rei]",
   "大叔魔法298-明日香":",★[souryuu asuka langley]",
   "大叔魔法299-刀剑妹":",★[{{{{{{sinon}}}}}}{{{{{{{{{{{{{Wear Square hair ornaments(black ) {{{{{{{{{{{next to}}}}}}}}}}} both eyes.}}}}}}}}}}}}}{{{{{ {{{{{{{black suqare ornaments.}}}}}}}}}}}}{{{{{{{{{{{{{{White scarf}}}}}}}} }}}}}} with {{{{{{{line pattern}}}}}}}.   {{{{{{{{{{{{{green eye}}}}}} }}}}}}}short hair{{{{{{{{{{green cropped jacket}}}}}}}}}}}  {{{{{aqua short hair}} }}}cropped jacket  open jacket{{{{ {{{{{White}}}}} and black innerwear}}}}arm under breasts  clothing cutout black  shortsfingerless gloves  leptosomatic habit one person long sleevestiny breastssmall breastsslender legs{{skinny}}{{{{{sword art online}}}}}{{{{{1girl}} }}}]",
   "大叔魔法300-诗乃":",★[sword art online {{{{{asada_shino }}}}} 1girl {{black hair}} brown eyes glasses short  hair with long locks school uniform black scarf [sinon]]",
   "大叔魔法301-亚斯娜":",★[asuna(sao)]",
   "大叔魔法302-冷笑":",★[authentic faceauthentic skin texturemasterpiecehighly detailed {{1girl}}solo loli girlschool uniformhead tiltleaning forward[embarrassed]incoming kissclosed eyespov{close  up}{{lips focus}}looking at viewer]",
   "大叔魔法303-壁尻":",★[wallbend over backwards]",
   "大叔魔法304-死神":",★[full body portriatGothic dres cool beautiful girl huge Grim reaper animate cute face silver hair detailed beautiful eyes  white background ]",
   "大叔魔法305-机械女武神":",★[parameters(((masterpiece))) best quality illustrationone dragon knight girl with formal  (mecha:0.2",
   "大叔魔法306-中式女武神":",★[parameters(((masterpiece))) best quality illustrationone dragon knight girl with formal  (mecha:0.2",
   "大叔魔法307-盔甲女武神":",★[parameters(((masterpiece))) best quality illustrationone dragon knight girl with formal  (mecha:0.2",
   "大叔魔法308-机械铠姬 改":",★[masterpiece best quality illustration beautiful detailed eyescolorful backgroundmechanical prosthesismecha coverageemerging dark purple across with white hairpig  tailsdisheveled hairfluorescent purplecool movementrose red eyesbeatiful detailed cyberpunk citymulticolored hairbeautiful detailed glow1 girl expressionlesscold expressioninsanity long bangslong hair lacedynamic composition motion ultra - detailed incredibly  detailed a lot of details amazing fine details and brush strokes smooth hd semirealistic anime cg concept art digital painting]",
   "大叔魔法309-机械物种":",★[{{masterpiece}} flat chestbest quality}{highres}soloflat_chesta girl inside the church with white hair and blue  pupil surrounded by {many} glowing {feathers} in cold facedetailed facenight with bright colorful lights whith richly layered clouds and clouded moon in the  detailed sky{a lot of glowing particles}high  ponytailmecha clothesrobot girlcool movementsliver bodysuit{filigree}delicate and (intricate) hair((sliver)) and (broken) bodyblue  streaked hairfull bodyDepth of field sitting on a {blue star}]",
   "大叔魔法310-机械娘召唤":",★[masterpiecebest quality1girl Cyberpunkextremely detailedice crystal texture wingsblack ribbonbest illustrationdetailed lightdepth of fieldmecha clothesbest shadowhairs between eyesTiny Breasts  street scenerylooking awayfantasytaut clothesleather armorstanding]",
   "大叔魔法311-机器科学":",★[{{{{{alternate form}}}} femelaextremely detailed 8k wallpaper{gets gangbang}[[[nsfw]]]1girl android  bangs cable cyborg eyebrows_visible_through_hair gears grey_background greyscale joints long_hair looking_at_viewer machine machinery mechanical_arms mechanical_parts monochrome robot robot_joints science_fiction single_mechanical_arm solo spot_color tube wire]",
   "大叔魔法312-机械化身体机械交":",★[nsfwthe girl Lying down on Solid square tableboundcablehandcuffsfettersgear{{{Rotating drills}}}{{{two transparent milking  hose are attached to the nipple}}}{{{hose attacked to Cameltoe}}}Restrainedoil leakmachine Mechanical 1girl{{{{tmechanical hose Plugged in}}}}  mecanical bodysuitscience fiction arm cannon cyborg  small breastsTube between the legsmachine legsThe hose is coming into her crotchplugopen legshuman factorycomputerduring an operationsex toysbroken left armbroken  right   reg]",
   "大叔魔法313-机械姬法":",★[{{{solo}}}highres{best quality};{highly detailed}beautiful detailed blue eyeslight blushexpressionlesswhite hairhair fluttering in  the windmechanical arm armormechanical body armorclothesriding motor{bodysuitruins of city in warfireburning carsburning buildingsair force fleet in the skyduskbird see]",
   "大叔魔法314-机娘水法":",★[(masterpiece) best quality{full body}((1 girl))((beauty detailed eye)){mechahuge_filesize}(bare  shoulders)science fictionhighly detailedillustrationextremely detailed CG unity wallpapersubmergecinematic lightingdramatic angle{{beautiful face}}posingcausticsfine water surfaceMechanical wingMetal wingsMecha wing{mecha clothes}robot girlbeautiful detailed face ]",
   "大叔魔法315-机械巨龙与少女":",★[1girlprincessfemale focus onbody(photo realistic:1.5){{a mechanical dragon with a majestic body}} illustrationmasterpiecebest  qualityhighly detailedultra-detailedcloudoceanoutdoorsrainsnowingbuildingcitycity_lightscloudy_skyconstellationlight_particlesshooting_star]",
   "大叔魔法316-机器风":",★[Too many Droidsin the styles of Dr. Seuss Peter Max and H. R. Giger --v  4]",
   "大叔魔法317-真人电子少女":",★[ (masterpiece) ((realistic)) 1girl best quality extremely detailed (beautiful girl) (maid outfit) ( (cyborg arms)) ((cyborg torso)) small breasts cyborg arms small details detailed face sad smile red eyes white hair half closed eyes looking  at viewer (solo) gradient background cinematic filmic telephoto depth of field lens distortion lens  flare white balance strobe light volumetric lighting dramatic  lighting little  haze ray tracing reflections detailed intricate elegant]",
   "大叔魔法318-战争机器":",★[SFW Masterpiece best quality high detail by Gaston BussiÃ¨re Claude Monet Artstation flame particles light particles zoomed  out (full body:1.3) Golem armored full armor metal skin metal face full helmet inside a metalworking factory]",
   "大叔魔法319-钢铁巨兽":",★[(best quality) ((masterpiece)) (highres) blasphemy mysterious sacred holy divine antichrist illustration ((MechanicalMonsteri) ) (extremely detailed cg) non-humanoid ((Remus GoD machine-Fenrir)) masterpiece powerful extremely detailed CG unity 8k wallpaper art oflight artist style  hyper machine Transformation by mechanization Mechanicalweapon]",
   "大叔魔法320-女黑白机械风":",★[(best quality) ((masterpiece)) (highres) originalcacredholymysteriouscoatextremely detailed wallpaper 1girl monochrome (an extremely delicate  and beautiful) mecha gears]",
   "大叔魔法321-机娘2":",★[((master piece))best quality illustration 1girl small breast beautiful detailed eyes beautiful detailed cyberpunk city flat_  chest beautiful detailed hair wavy hair beautiful detailed street mecha clothes robot girl cool movement sliver   bodysuit (filigree) dragon wings colorful background a   dragon  stands behind the girl rainy days (lightning effect) beautiful detailed sliver dragon arnour (cold face)]",
   "大叔魔法322-机娘1":",★[{{masterpiece}} flat chestbest quality}{highres}soloflat_chesta girl inside the church with white hair and blue  pupil surrounded by {many} glowing {feathers} in cold facedetailed facenight with bright colorful lights whith richly layered clouds and clouded moon in the  detailed sky{a lot of glowing particles}high ponytailmecha clothesrobot girlcool movementsliver bodysuit{filigree}delicate and (intricate) hair((sliver)) and (broken)  bodyblue streaked hairfull bodyDepth of field sitting on   a {blue star}]",
   "大叔魔法323-写实巨龙风格":",★[fractal dragon head Dieselpunk Teslapunk Spacepunk Trey Ratcliff Cindy Sherman full body portrait action shot portrait ultra  realistic photorealisim deeply real amazing detail mind-blowing detail Moonlight Engine Unreal Engine Surrealistic lighting Volumetric lighting God rays]",
   "大叔魔法324-机械龙法":",★[{{master piece}}best qualityillustration1girlsmall breastbeatiful detailed eyesbeatiful detailed cyberpunk cityflat_chestbeatiful detailed hairwavy hairbeatiful detailed steetmecha clothesrobot  girlcool movementsliver bodysuit{filigree}dargon wingscolorful backgrounda dragon  stands behind the girlrainy days{lightning effect}beatiful detailed sliver dragon arnour（cold face）]",
   "大叔魔法325-墨龙萝":",★[墨龙黑|This, appears, to, be, an, exquisitely, detailed, Chinese, ink, painting,  depicting, an, extremely, cute, girl, surrounded, by, a, large, dragon. The, dragon, is, intricately, detailed, with, a,  fleshed-out, head, and, encircles, the, girl, against, a, backdrop,   of, clouds. The, girl's, delicate, features, are,  directed, towards, and, engage, the, viewer, as, she, wears, a, Gothic, Lolita-style, layered, skirt, and, her,  long, hair, flows, effortlessly. The, painting, conveys, a, highly, nuanced, and, intricate, feel, utilizing, both, colored, and , ink, techniques, to, add, vibrancy, and, depth, to, the, image. The, use, of, a, cowboy, shot,  in, the, composition, places, emphasis, on, the, girl, as, the, focal, point, highlighting, the, allure, and, charm,  of, the, feminine, form.]",
   "大叔魔法326-龙女幻想":",★[(masterpiece) (best quality) (super delicate) (illustration) (extremely delicate and beautiful) (dynamic angle ) white and black highlights (legendary Dragon Queen:1.3)(1 girl) Hanfu (complex details) (beautiful and delicate eyes) golden eyes green pupils  delicate face upper body messy floating hair messy hair focus perfect hands (fantasy wind)]",
   "大叔魔法327-龙骑士":",★[extremely detailed CG unity 8k wallpaper (masterpiece) best quality illustration (1 girl) wet skin expressionless yellow  eyes (anger) horns (silver armor) metal complex pattern corner cape indifference]",
   "大叔魔法328-龙兽法":",★[((the dragon Lord:2)Magical animalChinese mythical beast:0.7Super fine furColorful eyesIntricate details)flameMythical background4kVirtual engineOctane  renderingHDsolo]",
   "大叔魔法329-少年与龙":",★[(masterpiece) (best quality) (super delicate) (illustration) (extremely delicate and beautiful) (dynamic angle ) thick hair (Chinese dragon background) (a young man with black hair and a young man with white hair and horn decorations) interaction  Hanfu (complex details) (beautiful and delicate eyes) golden eyes green pupils delicate face upper body messy floating hair messy hair focus Exquisite hands  (Fantasy Wind)]",
   "大叔魔法330-破碎霜龙":",★[masterpiecebest quality ((best quality)) ((masterpiece)) ((ultra-detailed)) (illustration) (detailed light ) (an extremely delicate and beautiful) a girl solo (beautiful detailed eyes) blue dragon eyes (((Vertical pupil))) two-tone hair: blue and white shiny hair colored inner hair (blue Dragonwings) blue_hair ornament ice adorns hair [dragon horn] depth of field{{{{Crystalline purple  gemstone gloves}}}}(gemstone of body) ((Detailed crystallized clothing))(((masterpiece)))flowerflowers tirebroken glass(broken screen)atlantistransparent glass]",
   "大叔魔法331-冰龙之术":",★[((( Frost Wyrm))) huge((solo))uppon body(dragon dance)(masterpiece)(best quality) beatuiful detalied headbeatuiful detalied faceAmazingfinely detailDepth of fieldextremely detailed CGoriginal extremely detailed wallpaper((beautiful detailed background))dynamic angle(beautiful detailed glow)  (extremely delicate  and beautiful)storming]",
   "大叔魔法332-冰霜龙息":",★[((best quality)) ((masterpiece)) ((ultra-detailed)) extremely detailed CG (illustration) (( detailed light)) (an extremely delicate and beautiful) a girl solo ((upper body)) ((cute face)) expressionless (beautiful detailed eyes)  blue dragon eyes (Vertical pupil:1.2) white hair  shiny hair colored inner hair (Dragonwings:1.4) [Armor_dress] blue wings blue_hair ornament ice adorns  hair [dragon horn] depth of field [ice crystal] (snowflake) [loli] [[[[[Jokul]]]]]]",
   "大叔魔法333-水龙法":",★[Fantasy creatures((magic  Morphling))  (detail dragon head)(beautiful detailed water state)(masterpiece)(best  quality)Amazingfinely detailabysmal seaDepth of fieldextremely detailed CGoriginal extremely detailed wallpaper((beautiful detailed background))dynamic angle(beautiful detailed glow)  (extremely delicate and beautiful )shinesplashing water around]",
   "大叔魔法334-青龙法":",★[大叔魔法334-青龙法|★[(masterpiece))best quality ((illustration))originalextremely detailed wallpaper](((beijing opera) )) (sketch)(wash painting)((color splashing))((ink splashing))((((dyeing))))((Chinese painting))((colorful))(beautiful and  delicate and trees)]Fantasy creatures(((chinese dragon)))(Chinese qinglong)((solo))(green dragon―guardian spirit of the east in Daoism)( chinese green dragon)(big faucet:1.5)green scalesbeautiful and delicate golden dragon hornsbig golden eyeslong dragon's beard[long green and snake body]beautiful detailed bodydragon  horn((Beautiful and meticulous golden dragon pupil))]Big and strongDiabolicalTyrannical]mountainsea(water)cloud(sky)palace((beautiful detailed background))]",
   "大叔魔法335-写实矮人族":",★[dwarf geared for battle with legendary battleaxe medival battle ready desolate landscape artstation cgsociety 4 k ultra  detailed god rays]",
   "大叔魔法336-写实城堡风":",★[A massive city of 300000 people with a golden citadel one of the most breathtaking castles in  the world]",
   "大叔魔法337-写实水下生物":",★[tropical ocean underwater turtles rare fish coral reef iain m. banks neal asher j. c.  staff anime studio dorothea lange framestore animal logic purely real completely real impersonal lighting volumetric lighting]",
   "大叔魔法338-写实邪恶生物":",★[Goldorg demonic orc from Moria new leader of the Gundabad strong muscular body ugly figure dirty grey  skin burned wrinkled face body interlaced with frightening armor metal coatings crossing head heavy muscular figure cinematic shot detailed trending on Artstation dark blueish environment  demonic backlight unreal engine 8k photorealistic ultra realistic]",
   "大叔魔法339-恶魔风":",★[nsfw {black hair} {{{{{medium hair}}}}} {{{{{{{large breasts}}} }}} {{{{{devil wings}}}} {{{demon tail}}} {{{{{completely nude}}}}} {{devil horns}} 1girl  {{{{{solo girl}}}}} {{{{{{{{succubus}}}}}}}} evil smile monster girl]",
   "大叔魔法340-湿天使":",★[{{{masterpiece}}}{{{best quality}}} {{ultradetailed}} {{detailed light}}{{an extremely  delicate and beautiful}}{beautiful detailed eyes} {sunlight}{angel}soloyoung girlsfloating bare_shoulderswings  mechanical halo halo leaking energy Floating white silk{Holy Light}  white hair twintails {industrial} factory with many cables and pipes [[steampunk]] small breasts {see-through} {see-through silhouette} {see-through  dress} lace thighhighs  lace panties cameltoe see-through sleeves dynamic angle navy eyes and aqua eyes expressionless looking at viewer [looking down]]",
   "大叔魔法341-城市崩坏版":",★[cityscape{{{full body}}}{{{black_thighhighs}}}adorable girl{{{small city}}}{{{giantess }}}{{{giga size}}}no shoesminimap{{{long leg}}}((({{{standing in the city}}}))){{from below}} }{{{{thin legs}}}}beautiful detailed skygirl standing in the citybeautiful detailed skyextremely detailednfsw{{{1000 meters tall}}}{{{city destoy}} }{{{open eyes wide}}}highresbuildingcity{{{destruction}}}size differenceoutdoorscrushingskyscraperbuilding ruinsroad{{{collapse}}}{{{crack}}}]",
   "大叔魔法342-比基尼铠甲精灵":",★[{best quality} {{masterpiece}} {highres} original extremely detailed 8K wallpaper 1girl {an extremely delicate  and beautiful}feet out of frameincredibly_absurdresdetailed backgroundflowers meadowsgame cgTamano Kedama(style)illustrationPerfect female bodyaquagradient eyesbeautiful detailed eyesdouble bun very long hair pointy ears  (( bikini armor))(((black bodysuit))) ((see-through)) medium breastsblonde_hairgreen_eyeswarizahair ornamentblushsitting]",
   "大叔魔法343-蓝色史莱姆娘":",★[{best quality} {{{masterpiece}}} {highres} original extremely detailed 8K wallpaper 1girl { an extremely delicate and beautiful}pov crotchfeet out of frameincredibly_absurdresfloating sakurachinese style architectureillustrationUnity CreationsTamano Kedama (style)long wavy curly hairgradient hairblushbeautiful detailed eyesslime dressribbonmedium_breastsSkin made  of waterwetaquagradient eyesslime hairslime legsskin made of slimeslime arms (slime girl:1.5) (Undine:1.5)underboob((((blue skin))))nsfw]",
   "大叔魔法344-杀手风格":",★[{{{masterpiece}}} best qualityextremely detailed CG unity 8k wallpaperpetiteyoung girl1girlcute facesolowhite shirttaut shirtlong sleeves shirtmedium lace -up corsetlong skirtbrown pleated skirtblue bowtiemedium breastfrench braidlong brown hairgrey eyesslim waistoutdoorsuburbsblue sky with clouds;lowresbad anatomybad hands text error missing fingersextra digit fewer digits  cropped worstquality low quality normal qualityjpegartifactssignature watermark usernameblurrybad feetextra fingersfewer digitsextra limbsextra armsextra legsmalformed limbsfused fingerstoo many fingerslong neckhuge breastscross-eyedbad facebad proportionscleavage dresspoorly drawn  asymmetric eyescoatmutated handsmutated breastsflat_chestnsfw]",
   "大叔魔法345-漂亮的猫":",★[A plush long-haired cat with entirely rich scarlet fur and golden eyes exquisite detail 30-megapixel  4k 85-mm-lens sharp-focus intricately-detailed long exposure time f/8 ISO 100 shutter-speed 1/125 diffuse-back-lighting award-winning photograph  facing-camera looking-into-camera monovisions elle small-catchlight low-contrast High-sharpness facial-symmetry depth-of-field golden-hour ultra-detailed photography  --v  4]",
   "大叔魔法346-紫罗兰色双重曝光":",★[character design double exposure shot front profile of a beautiful flowerpunk woman filled with a flaming   violet  forest dark beauty filled with flowery forest --v 4]",
   "大叔魔法347-复古照片":",★[1960s biker girl. technicolor old movie film grain scratches dirt and imperfections. film lighting. . very  detailed face proportional face open eyes photorealistic very detailed arms sharp focus ultra realistic ultra detailed cinematic   lighting photographic Eastman Kodak Color Negative film  5251   50T shot on panavision super ps . no arms. --v 4]",
   "大叔魔法348-超级英雄回忆录":",★[sweaty fatso batman resting in poolwindswept inlighted --v 4 --upbeta]",
   "大叔魔法349-科幻肖像":",★[A glamour portrait of a gorgeous futuristic cyberpunk cyborg woman looking like Angelababy in style of Marcin Nagreba  and Tim Flach wearing intricate haute couture clothing jewellery and headpiece out of focus geometric shapes flying around inside a futuristic building as background dark  cyan and orange tones and dramatic light no text sharp focus editorial portrait --v 4 --upbeta]",
   "大叔魔法350-多维纸工艺":",★[multi dimensional paper cut craft paper illustration tunnel stars and planets vine ornate detailed violet scarlet oil  --v 4]",
   "大叔魔法351-复杂的女英雄":",★[chiaroscuro Sailor Moon Batman James Jean pop cyberpunk western steampunk tiny scarlet roses ornate colorful Banner Saga  --chaos 20 --v 4]",
   "大叔魔法352-天启战士":",★[a stunning interpretation of a man wearing a yellow gaskmask post-apocalyptic by Nick Knight portrait highly detailed  and intricate golden ratio glow ominous haunting cinematic cgsociety unreal engine studio lighting rim lighting --v 4   --q 2] " ,
   "大叔魔法353-有机纵向":",★[photography by Marcin Nagraba handsome ornate male god of pearls and lace with ornate mushroom crown and suit  holding moss and large moths red and cyan color gel lighting geometric shadows on face Alphonse Mucha details and composition   by Rebecca Millen  -- q  2 --v 4]",
   "大叔魔法354-狗狗戴眼镜":",★[Retrowave malinois dog with glasses character designstickerFull body shot anime style Trigger Studio style manga art comics  inking graffiti art graphic neon colors golden ratio composition design for tshirt --v 4]",
   "大叔魔法355-海上的房子":",★[a large luxurious mansion built on a jagged rock in the sea lighthouse tower a small Harbor  and a cute boat fluffy clouds and rainbow crashing waves chibi Kawaii cartoon style vibrant colors --v 4]",
   "大叔魔法356-大理石艺术":",★[Marble Bronze Polished Chrome Clear Glass Rough Granite Ice Cracked and Crumbling Marble Rusted Iron Pieces of Driftwood  Sculptured into a Pieces of Scrap Metal Sculptured into a]",
   "大叔魔法357-夜晚的车":",★[dutch angle photo silhouette of a [insert car name here] with the car lights piercing the  dense fog low light dark mode --q 2 --v 4]",
   "大叔魔法358-牛头人":",★[(minotaur:1.66) (hooves:1.33) (cow tail:1.33) (bull head merged at neck:1.77) ( body fur:1.66)]",
   "大叔魔法359-吃汉堡":",★[(masterpiece:1.2) (8k dynamic angle official art detailed intricate:1.2) (anime_screencap:0.9) (style of  Studio Ghibli style of K-On:1.2) (style of stardew valley:1.05) SFW 1girl solo focus (cute anime girl holding and eating a  burger at a fast food restaurant:1.3) (colorful beautiful hair:1.1) rainbow hair multicolored hair braids ponytail eating food]",
   "大叔魔法360-中世纪女装":",★[(masterpiece:1.2) (8k dynamic angle official art line-art detailed intricate:1.2) (runescape:1.2)  blonde long hair barbarian woman sexy beautiful elegant skimpy armor cleavage navel blue mythical magical shield spear armor boots thighs perfect body perfect face beige  gray armor beige loincloth spikes on shoulder pads black necklace with a red jewel medium breasts muscular abs perfectly drawn hands elegant helmet]",
   "大叔魔法361-动感女孩":",★[SFW (style of zora theme:1.2) (style of machine:1.3) (style of space:1.2) ( style of android:1.1) from below looking away hotel Embarrassed Blush claw pose standing (Solo Focus:1.3) (masterpiece:1.3) best quality lineart hyper  extreme detailed (full body: 13",
   "大叔魔法362-蕃茄配方":",★[Extremely detailed CG unity 8k wallpaper some noodles 200g curry roux 300g beef 2 tomatoes a slice of  fried egg 20g butter a pinch of salt and pepper 1 bay leaf]",
   "大叔魔法363-食材配方":",★[Extremely detailed CG unity 8k wallpaper150g rice 200g curry roux 300g beef 2 onions1 pineapple 20g butter 1  tablespoongrated garlica pinch of salt and pepper 1 bay leaf 1 tablespoon honey]",
   "大叔魔法364-猛男法":"[(masterpiece:1.3),(Super strong:1.3), muscular, ripped, buff, hunky, beefcake, Adonis, Hercules, jock , He-Man",
   "大叔魔法364-小人物法":",masterpiece, best quality, masterpiece,highly detailed,1girl,solo,fullbody,lying,chibi,"


}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class Script(scripts.Script):
     txt2img_prompt = None
     img2img_prompt = None
     def after_component(self, component, **kwargs):
         if kwargs.get('elem_id') == 'txt2img_prompt':
             self.txt2img_prompt = component
         if kwargs.get('elem_id') == 'img2img_prompt':
             self.img2img_prompt = component

     def title(self):
         return "风格神器-大叔终极版"

     def ui(self, is_img2img):

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

         with gr.Tab("自定义单字提词"):
             with gr.Row():
                 with gr.Column():
                         gr.Tab( "01★括号控制法")
                         with  gr.Column():
                              gr.Markdown (
                         """
                       ★ (A:1.4),输入单字后调整1.4将增强约40%。 \n
                         """)
                         with  gr.Row():
                             AStrength = gr.Textbox(label="强化术", placeholder="输入单字" )
                             BStrength = gr.Slider(0.1, 2.0, value=1.4, step= 0.1 , label="强度值") 
                             CStrength  = gr.Button('Go')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             with gr.Row():
                 with gr.Column():
                      gr.Tab("02★渐变控制法", align='center')
                      with gr.Column():
                           gr.Markdown( """★[A:B:0.5],A是第一个先画的,0.5这是整个过程的50%\n
                      B是改变,0.5代表开始转换过程的百分比。 """)
                      with gr.Row():
                          AFrom = gr.Textbox(label="从这里开始", placeholder="输入单字 A" )
                          ATo  = gr.Textbox(label="到这里结束", placeholder="输入单字 B" )
                      with gr.Row():
                          AAStrength = gr.Slider(0.05, 0.95, value=0.5, step=0.05, label ="强度值")    
                          AAA  = gr.Button('Go')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             with gr.Row():
                 with gr.Column():  
                     gr.Tab("03★混合控制法", align='center')
                     with gr.Column():
                          gr.Markdown (
                         """ [A|B],两个提示词混合
                      因此每个奇数处理A提词,每个偶数处理B提词。  
                         """)
                     with gr.Row():
                         BFrom = gr.Textbox( label="开始", placeholder="输入单字 A")
                         BTo = gr.Textbox(label="结束", placeholder="输入单字 B")  
                         BBB  = gr.Button('Go')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             with gr.Row():
                 with gr.Column():
                     gr.Tab("04★AND连接法", align='center')
                     with gr.Column():
                         gr.Markdown (
                         """ [A AND B],A和B物件连接法，前后强度可调整
                     此语法适合搭配  ControlNet和Latent Couple
                         """)

                     with gr.Row():
                         DFrom = gr.Textbox(label="从这里开始", placeholder="输入单字 A")
                     with gr.Row():
                         DFStrength  = gr.Slider(0.05, 0.95, value=0.5, step=0.05, label= "强度值")    
                     with gr.Row():
                         DTo = gr.Textbox(label="到这里结束", placeholder="输入单字 B")
                     with gr.Row():
                         DTStrength  = gr.Slider(0.05, 0.95, value=0.5, step=0.05, label= "强度值")  
                     with gr.Row():
                         DDD = gr.Button('Go')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             with gr.Row():

                 gr.Markdown('关注 [大叔风格终极GT版](https://www.youtube.com/@user-vp1wu7mv9c) 记得关注大叔')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

             if self.txt2img_prompt is not None:
                 CStrength.click(fn=lambda p,x,y: p + "(" + x + ":" +  str(y) + ")",
                     inputs  = [self.txt2img_prompt,AStrength,BStrength],
                     outputs = [self.txt2img_prompt])

                 AAA.click(fn=lambda p,x,y,z: p + "[" + x + ":"  + y + ":" + str(z) + "]",
                     inputs  = [self.txt2img_prompt,AFrom,ATo,AAStrength],
                     outputs = [self.txt2img_prompt])

                 BBB.click(fn=lambda p,x,y: p + "[" + x + "|" +  y + "]",
                     inputs  = [self.txt2img_prompt,BFrom,BTo],
                     outputs = [self.txt2img_prompt])

                 DDD.click(fn=lambda p,x,y,z,g: p + "[" + "(" +  x + ":" + str(z) + ")" + " AND " + "(" + y + ":" + str( g) + ")" + "]",
                     inputs=[self.txt2img_prompt, DFrom, DTo, DFStrength, DTStrength],
                     outputs=[self.txt2img_prompt])

             if self.img2img_prompt is not None:
                 CStrength.click(fn=lambda p,x,y: p + "(" + x + ":" +  str(y) + ")",
                     inputs  = [self.img2img_prompt,AStrength,BStrength],
                     outputs = [self.img2img_prompt])

                 AAA.click(fn=lambda p,x,y,z: p + "[" + x + ":"  + y + ":" + str(z) + "]",
                     inputs  = [self.img2img_prompt,AFrom,ATo,AAStrength],
                     outputs = [self.img2img_prompt])

                 BBB.click(fn=lambda p,x,y: p + "[" + x + "|" +  y + "]",
                     inputs  = [self.img2img_prompt,BFrom,BTo],
                     outputs = [self.img2img_prompt])

                 DDD.click(fn=lambda p,x,y,z,g: p + "[" + "(" +  x + ":" + str(z) + ")" + " AND " + "(" + y + ":" + str( g) + ")" + "]",
                     inputs=[self.img2img_prompt, DFrom, DTo, DFStrength, DTStrength],
                     outputs=[self.img2img_prompt])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

             #with gr.Blocks(css=".gradio-container {background-color: red}"):
         with gr.Tab("大叔终极魔法"):
             if self.txt2img_prompt is not None:
                 with gr.Row():
                     Samworker = gr.Button('大叔的控制系-独特风！')
                     Samworker.click(fn=lambda x: random.choice(大叔职业) +","+ random.choice(大叔动作) +","+ random.choice(大叔场景)+",", 
                         inputs  = [self.txt2img_prompt],
                         outputs = [self.txt2img_prompt])
 
                     Samworker = gr.Button('大叔的终极魔法风格365种！')
                     Samworker.click(fn=lambda x: random.choice(大叔魔法) +","+ random.choice(大叔职业) +","+ random.choice(大叔背景)+",", 
                         inputs  = [self.txt2img_prompt],
                         outputs = [self.txt2img_prompt])
                     Samworker = gr.Button('大叔的随机系-固定上色！')
                     Samworker.click(fn=lambda x: random.choice(大叔纯色) +","+ random.choice(大叔头发) +","+ random.choice(大叔皮肤)+","+ random.choice(大叔眼睛) +",", 
                         inputs  = [self.txt2img_prompt],
                         outputs = [self.txt2img_prompt])
 
             if self.img2img_prompt is not None:
                 with gr.Row():
                     Samworker = gr.Button('大叔控制系-特别风！')
                     Samworker.click(fn=lambda x: random.choice(大叔职业) +","+ random.choice(大叔动作) +","+ random.choice(大叔场景)+",", 
                         inputs  = [self.img2img_prompt],
                         outputs = [self.img2img_prompt])
 
                     Samworker = gr.Button('大叔禁咒系-终极魔法风格363种！')
                     Samworker.click(fn=lambda x: random.choice(大叔魔法) +","+ random.choice(大叔职业) +","+ random.choice(大叔背景)+",", 
                         inputs  = [self.img2img_prompt],
                         outputs = [self.img2img_prompt])
                     Samworker = gr.Button('大叔随机系-自动上色')
                     Samworker.click(fn=lambda x: random.choice(大叔纯色) +","+ random.choice(大叔头发) +","+ random.choice(大叔皮肤)+","+ random.choice(大叔眼睛) +",", 
                         inputs  = [self.img2img_prompt],
                         outputs = [self.img2img_prompt])

             with gr.Row():
                 poImageTheme = gr.Dropdown(list(ImageTheme.keys()), label="强化系-禁术终极美颜术", value ="No")
             with gr.Row():
                 poImageDynamic = gr.Dropdown(list(ImageDynamic.keys()), label="辅助系-需配合动态提词-颜色系",  value="No")
             with gr.Row():
                 poResultType = gr.Dropdown(list(ResultType.keys()), label="图片风格", value="No")
                 poResultScenarios = gr.Dropdown(list(ResultScenarios.keys()), label="场景风格", value="No")
                 poResultSpecies = gr.Dropdown(list(ResultSpecies.keys()), label="表情风格", value="No")
                 poResultStyle = gr.Dropdown(list(ResultStyle.keys()), label="视觉风格", value="No")
                 poResultColors = gr.Dropdown(list(ResultColors.keys()), label="色彩风格", value="No")
                 poImageView = gr.Dropdown(list(ImageView.keys()), label="镜头风格", value="No")
             with gr.Row():
                 poImageStyle = gr.Dropdown(list(ImageStyle.keys()), label="强化系-终极大叔魔法咒语363种", value ="No")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             with gr.Row():

                 gr.Markdown('关注 [大叔风格终极GT版](https://www.youtube.com/@user-vp1wu7mv9c)')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#poResultConcept,poCoreResultType,poResultTypeStrength,
# poResultConcept, poCoreResultType,poResultTypeStrength, 
         return [poImageDynamic,poImageTheme, poResultType, poResultScenarios, poResultSpecies, poResultStyle, poResultColors, poImageView, poImageStyle]

     def run(self, p, poImageDynamic, poImageTheme, poResultType, poResultScenarios, poResultSpecies, poResultStyle, poResultColors, poImageView, poImageStyle):
         p.do_not_save_grid = True
         # Add the prompt from above
         p.prompt += ImageDynamic[poImageDynamic] + ResultType[poResultType] + ResultScenarios[poResultScenarios] + ResultSpecies[poResultSpecies] + ResultStyle[poResultStyle] +  ResultColors[poResultColors] + ImageView[poImageView] + ImageStyle[poImageStyle] + ImageTheme[poImageTheme]
        
         #p.negative_prompt += ResultType[poResultType] + ResultScenarios[poResultScenarios] + ResultSpecies[poResultSpecies] + ResultStyle[poResultStyle] + #ResultColors[poResultColors]  + ImageView[poImageView] + ImageStyle[poImageStyle] + ImageTheme[poImageTheme] + ImageDynamic[poImageDynamic]

         p.negative_prompt += ResultTypeNegatives[poResultType] + ImageStyleNegatives[poImageStyle] + ImageThemeNegatives[poImageTheme] + ImageDynamicNegatives[poImageDynamic]

         proc = process_images(p)
         return proc
