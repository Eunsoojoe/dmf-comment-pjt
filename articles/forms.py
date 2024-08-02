from django import forms
from .models import Article, Comment


# 자동으로 생성된 폼 꾸며보기.
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )



    class Meta():
        model = Article    # 장고가 자동적으로 Article 구조에 맞게 form 생성
        fields = "__all__"

class CommentForm(forms.ModelForm):
    # CommentForm을 도와주는 부가적인 요소들.
    class Meta():
        model = Comment
        # fields = '__all__'
        # fields => 추가할 필드 이름 목록

        # fields = ('content',)
        # exclude => 제거할 필드 이름 목록
        exclude = ('article', )