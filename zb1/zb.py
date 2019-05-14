# coding:utf-8
LESSON = 1
CNT = 52

head = '''<html>
   <head>
      <title>Russian Vocabulary</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
      <link rel="stylesheet" href="bootstrap.min.css">
      <script src="jquery.min.js"></script>
      <script src="popper.min.js"></script>
      <script src="bootstrap.min.js"></script>
      <script src="howler.core.min.js"></script>
      <script src="howler.min.js"></script>
      <style>
         body {
            padding-top: 2em;
            background-color: #F8F8F8;
         }
         tr {
            background-color: white;
         }
         td {
            word-break: break-all;
         }
      </style>
   </head>
   <body>
      <div class="container">
         <h3>第%d课</h3>
         <table class="table">
            <tbody>'''
tail = '''            </tbody>
         </table>
      </div>
   </body>
   <script>
      var sound = new Howl(
      );
      function m(p){
        sound.play(p);
      }
      $('table tr').each(function(a,b){
        $(b).click(function(){
          $('table tr').css('background','white');
          $(this).css('background','#E8E8E8');
        });
      });
   </script>
</html>'''
word = '''а|[连]而，可是
и|[连]和，还有
у|[前]（二格）（表领属关系）属于......的；（表所处）在......旁边
мама|妈妈
мы|我们
ум|智慧
на|[前](四格)往......上；（六格）在......上
но|[连]但是
он|[代]他；它
папа|爸爸
по|[前]（三格）沿着......；每逢
бом|嘡（钟声）
бум|热闹；热潮
бон|（流送木材的）栏木浮栅
вы|[代]你们；您
вон|[语气]那就是
ты|[代]你
та|[代]那；那个（阴性）
то|[代]那；那个（中性）
там|[副]在那里
тут|[副]在这里
том|卷，册
тон|音，调
вот|[语气]这就是
да|[语气]是；是的
до|[前]（二格）到，至，距（表示空间和时间距离的长短）
дом|房子
дым|烟
дам|（我）给
иду!|（我）步行去
два|[数]两个
лом|铁棍，铁杆
мол|[语气，用作插入语]（据某人）说
мул|马骡
мыл|洗（过去时）
был|有，在，到，去（的过去时）
алло!|[感]喂！（打电话用语）
ла!мпа|灯
она!|[代]她；它
фо!то|照片
вода!|水
э!то|这，这是
луна!|月亮
до!ма|[副]在家里
Анна|安娜（女）
Ива!н|伊万（男）
Анто!н|安东（男）
Алла|阿拉（女）
Ира|伊拉（女）
Инна|茵娜（女）
Ван Лин|王玲
Дон|顿河'''
ac = [
('а!','а́'),
('е!','е́'),
('и!','и́'),
('о!','о́'),
('у!','у́'),
('ы!','ы́'),
('э!','э́'),
('ю!','ю́'),
('я!','я́'),
]
for t in ac:
  x,y = t
  word = word.replace(x,y)
words = word.split("\n")

print head%LESSON
for i in xrange(0,CNT):
    r,c = words[i].split('|')[0],words[i].split('|')[1]
    print '''               <tr onclick="m('%03d')">'''%(i+1)
    print '''                  <td>%s</td>'''%r
    print '''                  <td>%s</td>'''%c
    print '''               </tr>'''
print tail
