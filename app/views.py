from django.shortcuts import render, HttpResponse

from BlogWriter.writer import chatgpt_writer, generate_prompt, palm_writer


def home(request):
    if request.method == 'POST':
        blog_topic = request.POST.get('blog_topic',None)

        if blog_topic:
            prompt = generate_prompt(blog_topic)
            # print(prompt)
            generated_blog = palm_writer(prompt)
            return render(request, 'edit-blog.html',{'blog_post':generated_blog})
        else:
            return HttpResponse('No topic found for blog post')
    else:
        return render(request, 'index.html')

def edit_blog(request):
    return render(request, 'edit-blog.html')