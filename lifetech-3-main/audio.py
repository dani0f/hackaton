from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play

# Texto que deseas convertir a voz
texto = "Diapositiva 1: Información y RequisitosEn esta diapositiva, nos centraremos en obtener información sobre la Sociedad Mutual y verificar los requisitos de afiliación. Esto puede incluir detalles como la edad mínima, ubicación geográfica y cuotas de ingreso o periódicas. Es importante familiarizarse con estos requisitos antes de proceder."

# Crear un objeto gTTS
tts = gTTS(texto, lang='es')

# Guardar el archivo de audio generado
nombre_archivo = "audio_salida.mp3"
tts.save(nombre_archivo)

# Reproducir el archivo de audio
audio = AudioSegment.from_file(nombre_archivo, format="mp3")
play(audio)
