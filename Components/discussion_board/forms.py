from .models import Comment, Reply, Discussion
from django import forms

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'content',)
        
    title = forms.CharField(
        label="Title",
        widget=forms.Textarea(attrs={'placeholder': 'Staff: Please make an appropriate and descriptive title here...', 'rows': 2})
    )

    content = forms.CharField(
        label="Description/Content",
        widget=forms.Textarea(attrs={'placeholder': 'Staff: Please write the discussion description here... \n\nNote: Your username will be visible as the poster\nNote: Any deletions of discussions need to be handled on the admin site', 'rows': 8})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
 
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Write a comment here...', 'rows': 6})
    )

    

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)

    reply = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Write a response here...', 'rows': 4})
    )




    
