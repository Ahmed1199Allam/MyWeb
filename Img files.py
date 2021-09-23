import os
from PIL import Image

# assign directory
directory = 'E:/IEEE/Website/beeb/assets/Images/Gallery/blank'
 
# iterate over files in
# that directory
t_file= open('E:/IEEE/Website/beeb/txt.txt','w')
x=''
suffix = 'G'
cnt =1
for filename in os.scandir(directory):
    if filename.is_file():
        old_name =filename.path
        image = Image.open(old_name)
        new_image = image.resize((346, 347))
        new_image.save(old_name)
        new_name = filename.path[:42]+'/'+suffix+str(cnt)+'.png'
            os.rename(old_name, new_name)
        cnt += 1
        # q=path.split('\\')
        # # for i in range(len(path)):
        # #     if path[i] == '\\':
        # #         path[i] = '/'
        # q='/'.join(q)
        s = '<a id="rcorners_events" style="float: left; width:346px; height:347px; background: url({{site.baseurl}}/'+new_name[21:]+');"></a>\n'
        t_file.write(s)
        x +='<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>'
t_file.write(x)
t_file.close()