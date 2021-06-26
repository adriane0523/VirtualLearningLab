

<h1 align="center">E-Learning Lab</h1>
<h5 align="center"> (previously Virtual Learning Lab) </h5>


<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
</p>

<br>

## :dart: About ##
This website is for a Non-profit in South Africa called Bridge2Africa.
The website is a learning platform aiming to bring STEM content to students all over the world. The website contains different courses where students can learn 
and an admin panel to add classes. It uses the Django admin tools and user 
authentication technology.

The project is now part of ASU's EPICS program where they are aiming to improve this website and working with our Community Partner Bridge2Africa to help increase access of STEM education all throughout in South Africa.


(You can use username: demo, password: demo1 to login to the website) 

Admin panel demo: https://www.youtube.com/embed/PvA5yy0Z74E



## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org)
- [Django](https://www.djangoproject.com/)
- [HTML/CSS]

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) 
Download Python 3.7.9 at https://www.python.org/
Download an IDE, preferably VS code. Load project into the IDE

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/iamTanTan/E-Learning_Lab_Spring_2021.git

# Access
$ cd E-Learning_Lab_Spring_2021/

# create a virutal enviroment to install your dependencies,
$ python -m venv venv

#activate it you should see (venv)
$ venv/Scripts/activate

#install dependencies
$ pip install -r requirements.txt

#run the app
$ python manage.py runserver

#helpful commands:
#updating static/assets folder
$ python manage.py collectstatic

#updating database models
python manage.py makemigrations
python manage.py migrate
```

## Whats in the project ##

Admin Panel component
https://elearning-lab.org/admin/
<website link>/admin => Developer admin panel (this came with Djano)

https://elearning-lab.org/admin_panel/
<website link>/admin_panel => “user” admin panel (created)
There are two different admin panels, one is meant for a developer to look over and the other one is meant for the organization to use. I personally thought the admin panel for developers is confusing to the normal user so creating another admin panel for the Birdge2Africa organizations was needed. However, the user Admin panel still uses elements of the developer admin panel.
Student Component
https://elearning-lab.org/student/welcome/28e4a600-54f3-476b-93d3-8c97d06f7283
Holds the different course home, modules, connect, reading material, and assessments. Assessments uses google form for quizzes

Home Component
https://elearning-lab.org/
Holds the UI for the main page

Courses Component
https://elearning-lab.org/courses
Holds the UI for courses

Virutallearninglab folder
Main folder, it holds the UI for login and register, base templates for each page, routing, and settings of the project

asset/static folder=> holds the css files and images (there are two because when website is deployed it looks at static folder)
media folder => upload photos (currently not working)

## Related links ##
installing pip - https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

login and register - https://levelup.gitconnected.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73

Django tutorial - https://docs.djangoproject.com/en/3.1/intro/tutorial01/

Django portfolio - https://realpython.com/get-started-with-django-1/

## Dependencies ##
https://pypi.org/project/django-embed-video/
https://pypi.org/project/django-ckeditor/
https://pypi.org/project/django-tinymce/

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.
Created by: Phillippe Adriane Inocencio & ASU EPICS
&#xa0;

<a href="#top">Back to top</a>
