from django import forms

from func1.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # 依據Topic模型來建立表單
        fields = ['text'] # 表單只有text欄位
        labels = {'text': ''} # 不要在text欄位加標籤

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # 定義一個文字區塊寬度為80欄