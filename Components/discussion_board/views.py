from .models import Discussion, Comment, Reply
from Components.courses.models import Courses
from .forms import CommentForm, ReplyForm, DiscussionForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
import datetime

#  View for the 'discussions.html' which displays a list of discussions for a given course id
@login_required
def discussions(request, id_field):
    discussions = Discussion.objects.all().filter(courses = (str)(id_field))
  
    # Render not exists if no discussions exist yet
    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    # New Discussion POST Form
    new_discussion = None
    
    if request.method == 'POST':
        discussion_form = DiscussionForm(request.POST)
        if discussion_form.is_valid():
            # Create Discussion object but don't save to database yet
            new_discussion = discussion_form.save(commit=False)
            # Assign the current course to the discussion board         
            new_discussion.courses = Courses.objects.get(id=id_field)
            new_discussion.created_by = request.user
            # Save the comment to the database
            new_discussion.save()
            # Set form to default state after submit
            discussion_form = DiscussionForm()

    else:
        discussion_form = DiscussionForm()

    context = {
        "discussions": discussions,
        "DiscussionForm": discussion_form,   
    }

    return render(request, "discussions.html", context)



# View for the 'discussion_detail.html' displays a particular board (pk) and its comments and replies
@login_required
def discussion_detail(request, id_field, pk):
    # Retrieve current discussion and its specific comments
    discussions = Discussion.objects.all().filter(courses = (str)(id_field) )

    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    discussion = discussions.get(pk=pk)    

    # Retrieve all comments associated with the discussion according to user selected order

    # default order is by number of up votes
    order = "-num_vote_up"
    if (request.GET.get('order')):
        order = request.GET.get('order')
        if (order == "newest"):
            order = "-created_on"
        if (order == "best"):
            order = "-num_vote_up"

    all_comments = discussion.comments.all().order_by(order)

    # Use paginator display only 20 comments at a time
    paginator = Paginator(all_comments, 20)
    page = request.GET.get('page', '1')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    # New Comment POST Form
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current user and current discussion board to new comment
            new_comment.created_by = request.user
            new_comment.parent_discussion = discussion
            # Save the comment to the database
            new_comment.save()
            # Set form to default state after submit
            comment_form = CommentForm()

            # Reload after creating comment
            return redirect(Discussion.get_absolute_url(discussion))

    else:
        comment_form = CommentForm()


    # New Reply POST Form 
    new_reply = None
    
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():

            # Get the parent id from the comment that will be replied to            
            parent_id = request.POST.get('parent_id')
            parent_comment = Comment.objects.get(id=parent_id)
            # Create Reply object but don't save to database yet
            new_reply = reply_form.save(commit=False)
            # Assign the current user and current comment to new reply
            new_reply.comment = parent_comment
            new_reply.created_by = request.user
            # Save the reply to the database
            new_reply.save()
            # Set form to default state after submit
            reply_form = ReplyForm()

            return redirect(Discussion.get_absolute_url(discussion))

    else:
        reply_form = ReplyForm()


    context = {'discussion': discussion,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form,
                'new_reply': new_reply,
                'reply_form': reply_form,
                'order': order,
                }

    return render(request, 'discussion_detail.html', context)



@login_required
def delete_comment(request, pk):
    
    # delete_comment or flag as removed if replies exist
    deleted_comment = Comment.objects.get(pk=pk)
    discussion = deleted_comment.parent_discussion

    # Enable delete options for comment creator or staff member
    if (request.user == deleted_comment.created_by or request.user.is_staff):
        if not deleted_comment.replies.exists():
            deleted_comment.delete()
            
        else:
            deleted_comment.is_removed = True
            deleted_comment.save()

    return redirect(Discussion.get_absolute_url(discussion))
           
    

@login_required
def delete_reply(request, pk):
    # get particular reply instance
    deleted_reply = Reply.objects.get(pk=pk)

    # get the parent discussion in order to redirect after deletion
    parent_comment = deleted_reply.comment
    discussion = parent_comment.parent_discussion

    # Enable and perform deletion for reply creator or staff member
    if(request.user == deleted_reply.created_by or request.user.is_staff):
        deleted_reply.delete()

        # If the parent comment is removed and has no replies, instead of rendering the placeholder,
        # delete the comment outright to save space in database and in the discussion
        if (parent_comment.is_removed and not parent_comment.replies.exists()):
            parent_comment.delete()

    return redirect(Discussion.get_absolute_url(discussion))
           

           
@login_required
def update_comment(request, pk):
    # get particular comment instance
    comment = Comment.objects.get(pk=pk)
    discussion = comment.parent_discussion  

    # pass the object as instance in form
    comment_form = CommentForm(request.POST or None, instance = comment)

    # save the updated data from the form
    if comment_form.is_valid(): 
        comment_form.save() 

    return redirect(Discussion.get_absolute_url(discussion))


@login_required
def update_reply(request, pk):
    # get particular reply instance
    reply = Reply.objects.get(pk=pk)

    # get the parent discussion in order to redirect after
    comment = reply.comment
    discussion = comment.parent_discussion 

    # pass the object as instance in form
    reply_form = ReplyForm(request.POST or None, instance = reply)

    # save the updated data from the form
    if reply_form.is_valid(): 
        reply_form.save() 

    return redirect(Discussion.get_absolute_url(discussion))


@login_required
@csrf_protect
def upvote_comment(request, pk):
    
    # Retrieve comment from upvote event 
    comment = Comment.objects.get(pk=pk)
    user = request.user
    
    if request.is_ajax() and request.method == "POST":
        if (comment.votes.exists(user.id)):
            comment.votes.delete(user.id)
        
        else:
            comment.votes.up(user.id)
        
        data = {
            "count": comment.votes.count(),
        }
        
        return JsonResponse(data)
    else:
        return HttpResponse(400, 'Invalid form')


@login_required
@csrf_protect
def upvote_reply(request, pk):
    
    # Retrieve reply from upvote event 
    reply = Reply.objects.get(pk=pk)
    user = request.user
    
    if request.is_ajax() and request.method == "POST":
        if (reply.votes.exists(user.id)):
            reply.votes.delete(user.id)
        
        else:
            reply.votes.up(user.id)
        
        data = {
            "count": reply.votes.count(),
        }
        
        return JsonResponse(data)
    else:
        return HttpResponse(400, 'Invalid form')
