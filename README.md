# artsetforme_public

Public repository of webapp for artsetforme association
 
To run the server, make sure to set the env var "DJANO_SETTINGS_MODULE" with value "artsetforme.settings.production" on the production server.

To use mailing functionnalities, please modifify the name of the env var and assign them a correct value.

!Notification for new articles makes more sense in Blogpost app than in Backoffice app. Unsure about best practice.

This application uses this templates : https://startbootstrap.com/theme/grayscale with this licence : https://github.com/startbootstrap/startbootstrap-grayscale/blob/master/LICENSE

--
### Presentation of the app :

This application is a Django web application destined to facilitate interactions between customers and organization (which is this case is L'Atelier Arts et Forme and will be from now on reffered to as AEF).
<br>
<br>
The web app has 3 main functions :
<br>
* A presentation app, which highlights the aspects of AEF and the main informations (who/what/why/where)
<br>
* A blog app, which lets editor post blogposts, preferably in editor created categories. This has several advantages : the user can filter which category he wants to see, and AEF can notify every person subscribed to a category that a post has been made on the website
<br>
* A newsletter app that lets editor(s) send an email to users subscribed to a category. In this version, AEF chose not to include attachments or images which simplifies the app but those parts are commented out, not deleted IIRC
<br>

--

### Installation

1. Requires : Python3 (built with 3.8 and 3.9, should work well with later versions, unsure about earlier versions) ; PostgreSQL (here : ver.13), pip
2. Optionnal --> Create a virtual env using the tool of your choice `pip install -r requirements.txt` to install the dependencies
3. Set env variables, either with dotenv or not(not used in the project so you'll need to tinker the code a bit) - Needed in settings : **email backend** `AEF_EMAIL_USER` , `AEF_EMAIL_PASSWORD` < Credentials to log in on an adress mail, here gmail is used. **DATABASES** : `AEF_DB`, the database name ; `PG_USER` and `PG_PWD` the credentials of the database user , `AEF_DB_PORT` and `AEF_ENVIRO`, the last one specifies *development* or *production*
4. execute : `python manage.py makemigrations` and `python manage.py migrate` to create the tables of the database and establish the relationships
5. execute : `python manage.py createsuperuser` and create a superuser
6. execute `python manage.py runserver` to run it locally in development

