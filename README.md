### Email Adding for sending email verification for Testing
`
Pip Install -r requirements.txt` (install the package first)
Create a `.env`  file inside the src folder
Create `.gitignore` inside src folder
![image](https://github.com/CADT-CAPSTONE-PROJECTS-I/CAPPLY-/assets/112000019/b34b750a-b3bf-40a8-bc4f-6e11d6853ad9)


—----In the .env file put code below
# Secret Key
SECRET_KEY = 'django-insecure-sztl#wi8mxd++-__gc!trsw@44cennz*4463f8-!!p_*1uv*g9'
# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_PORT=587
EMAIL_HOST_USER=a7d4deb84d835f
EMAIL_HOST_PASSWORD=7be2218ced679e
EMAIL_USE_TLS=True


—-------Change email info according to your Mailtrap account

NOTE: Since in settings.py, the info has already been updated. You can just run the code to test if the email verification is working or not 
![image](https://github.com/CADT-CAPSTONE-PROJECTS-I/CAPPLY-/assets/112000019/f984ad3a-c553-46c0-bbe5-ef8058601d7f)
<picture>
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="[https://github.com/CADT-CAPSTONE-PROJECTS-I/CAPPLY-/assets/112000019/f984ad3a-c553-46c0-bbe5-ef8058601d7f]" width="100">
</picture>

** no need to type in settings.py
