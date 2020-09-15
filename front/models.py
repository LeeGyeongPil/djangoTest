from django.db import models
from django.utils import timezone
import hashlib, time

def fileupload_path(instance, filename):
    filearr = filename.split('.')
    new_filename = hashlib.md5((filearr[0] + '' + str(time.time())).encode('utf-8')).hexdigest() + '.' + filearr[1]
    return 'board/{0}'.format(new_filename)

# Create your models here.
class FrontBoard(models.Model):
    boardidx = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200,verbose_name='제목')
    context = models.TextField(verbose_name='내용')
    files = models.FileField(upload_to=fileupload_path,null=True,verbose_name='업로드파일')
    regdate = models.DateTimeField(default=timezone.now,verbose_name='등록일',editable=False)
    deldate = models.DateTimeField(blank=True, null=True,verbose_name='삭제일',editable=False)

    def boardSave(self):
        self.save()

    class Meta:
        db_table = 'front_board'


class FrontComment(models.Model):
    commentidx = models.AutoField(primary_key=True)
    boardidx = models.ForeignKey(FrontBoard, models.DO_NOTHING, db_column='boardidx')
    context = models.TextField(verbose_name='댓글내용')
    regdate = models.DateTimeField(default=timezone.now,verbose_name='등록일',editable=False)

    class Meta:
        db_table = 'front_comment'