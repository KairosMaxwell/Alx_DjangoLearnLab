from django import forms
from taggit.forms import TagWidget
from django import forms
from .models import Comment







class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(help_text="Add comma-separated tags", required=False)

    TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),


    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            instance.save()
            if tags:
                tag_names = [tag.strip() for tag in tags.split(',')]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    instance.tags.add(tag)
        return instance


# class TagWidget(forms.ModelForm):
#     pass

class ModifyPostForm(PostForm):
    TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),

class UpdateForms(PostForm):
    TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),
