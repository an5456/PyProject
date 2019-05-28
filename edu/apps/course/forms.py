from django import forms

# 这是form表单的过滤

# 更新任务状态（某个人完成了多长时间的视频观看，是否已全部完成，没有记录就新建）
class updatetaskForm(forms.Form):
    catalogid = forms.CharField(label="目录id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dotime = forms.CharField(label="完成时间", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userid = forms.CharField(label="用户id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

# 这个方法已废弃对应上面的新建
class addtaskForm(forms.Form):
    catalogid = forms.CharField(label="目录id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userid = forms.CharField(label="用户id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

# 获取播放界面信息
class playForm(forms.Form):
    catalogid = forms.CharField(label="目录id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    courseid = forms.CharField(label="课程id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userid = forms.CharField(label="用户id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
