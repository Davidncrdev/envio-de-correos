import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Función para leer el contenido HTML desde un archivo
def leer_archivo_html(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Configuración del servidor SMTP de Hostinger
smtp_server = "smtp.hostinger.com"
smtp_port = 465
smtp_user = "info@fyvestudio.pro"
smtp_password = "poKqy5-xebmox1332-wonvut"

# Datos del correo
remitente = "info@fyvestudio.pro"
destinatario = "nicolasaravena@fyvestudio.pro"
asunto = "Descubre Cómo Fyve Studio Pro Puede Impulsar Tu Empresa"

# Leer el contenido HTML del archivo
cuerpo_del_correo_html = leer_archivo_html("presentacion_fyve_studio.html")

# Crear el mensaje
mensaje = MIMEMultipart("alternative")
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

# Adjuntar el cuerpo del correo en HTML
mensaje.attach(MIMEText(cuerpo_del_correo_html, 'html'))

try:
    # Conectar al servidor SMTP usando SSL
    servidor = smtplib.SMTP_SSL(smtp_server, smtp_port)
    servidor.login(smtp_user, smtp_password)

    # Enviar el correo
    servidor.sendmail(remitente, destinatario, mensaje.as_string())

    # Cerrar la conexión
    servidor.quit()
    print("Correo enviado exitosamente")

except Exception as e:
    print(f"Error al enviar el correo: {e}")
