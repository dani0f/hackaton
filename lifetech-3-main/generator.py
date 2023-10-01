promp_resumidor ="""Eres un diseñador grafico y tu trabajo es resumir la información para una presentación con los puntos más importantes de los pasos a seguir. 
Para esto indica que textos serian el titulo de la diapositiva, los subtitulos y el texto de información. Indica cual el numero de diapositiva"""


resumen = """
Título: Cómo presentar una solicitud de reembolso de gastos médicos en una mutual de salud

Introducción:
El siguiente instructivo proporciona los pasos necesarios para presentar una solicitud de reembolso de gastos médicos en una mutual de salud. El reembolso de gastos médicos es un proceso importante para los afiliados, ya que les permite recibir un reembolso parcial o total de los gastos médicos cubiertos por la mutual. A continuación, se detallan los pasos que debes seguir para presentar una solicitud de reembolso de manera efectiva.

Materiales necesarios:

Formulario de solicitud de reembolso (proporcionado por la mutual de salud).
Copias de todas las facturas médicas y recibos relacionados.
Informe médico o cualquier otra documentación relevante.
Número de afiliado y cualquier otra información de identificación requerida.
Pasos a seguir:

Obtén el formulario de solicitud de reembolso:

Dirígete a la oficina de la mutual de salud o visita su sitio web oficial.
Descarga y completa el formulario de solicitud de reembolso. Asegúrate de proporcionar toda la información requerida de manera clara y precisa.
Reúne toda la documentación:

Recopila todas las facturas médicas y recibos relacionados con los gastos que deseas solicitar para el reembolso.
Si es necesario, solicita un informe médico detallado o cualquier otra documentación adicional requerida por la mutual.
Completa el formulario de solicitud:

Llena el formulario de solicitud de reembolso con la información solicitada. Asegúrate de proporcionar tus datos personales, número de afiliado y cualquier otra información de identificación necesaria.
Detalla los gastos médicos de manera clara y precisa en el formulario. Incluye la fecha de cada servicio, el proveedor de atención médica, el motivo de la visita y el monto de cada gasto.
Adjunta la documentación requerida:

Asegúrate de adjuntar todas las facturas médicas, recibos y cualquier otra documentación solicitada por la mutual. Organiza los documentos en el orden en que se mencionan en el formulario de solicitud.
Revisa y verifica la solicitud:

Antes de enviar la solicitud, revisa cuidadosamente todos los detalles proporcionados. Asegúrate de que toda la información sea correcta y esté completa.
Verifica que hayas adjuntado todos los documentos necesarios y que estén legibles.
Envía la solicitud de reembolso:

Envía la solicitud de reembolso completa junto con los documentos adjuntos a la dirección indicada por la mutual. Puedes enviarla por correo postal o entregarla personalmente en la oficina de la mutual.
Realiza un seguimiento:

Si deseas hacer un seguimiento de tu solicitud, comunícate con el departamento de atención al cliente de la mutual de salud. Pregunta sobre los plazos de procesamiento y cualquier otra información relevante para el seguimiento de tu solicitud."""



promp_html = """Eres un experto programador html y tu tarea es crear código bien organizado en cuanto a la posición, tamaño y fuentes de tal forma que 
parezca una presentación de diapositivas informativas. Para esto se te dara un código que indica la diapositiva, el titulo el subtitulo y el contenido de texto que hay para cada diapositiva. 
Deberas separar cada diapositiva en un codigo html independiente. El codigo html no requiere de head ni de body, solo del divisor con la diapositiva. El style de css debe estar dentro de cada etiqueta.
Quiero que me entreges los resultados separados en un arreglo de python llamado diapositivas. Dame el arreglo para copiar y pegar"""

diapositivas = [
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #f2f2f2;">
        <i class="fas fa-shield-alt fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Instructivo de Seguridad para el Uso de EPP</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Objetivo</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Proporcionar pautas y recomendaciones para el uso adecuado de los Equipos de Protección Personal (EPP) en la mutual de seguridad, garantizando la seguridad y el bienestar de los trabajadores.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-search fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 1: Identificación del EPP necesario</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Identifica los riesgos y selecciona los EPP adecuados</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Antes de iniciar una tarea, identifica los riesgos y determina los EPP necesarios, como cascos, guantes, gafas de seguridad, etc.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-eye fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 2: Inspección del EPP</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Verifica el estado de los EPP antes de usarlos</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Realiza una inspección visual para asegurarte de que los EPP estén en buen estado y sin daños. Informa cualquier problema al supervisor o al responsable de seguridad.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-user-shield fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 3: Colocación adecuada del EPP</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Ajusta correctamente los elementos de protección personal</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Asegúrate de colocar y ajustar adecuadamente cada elemento de protección personal, siguiendo las instrucciones del fabricante.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-file-alt fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 4: Instrucciones de uso específicas</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Lee y comprende las instrucciones especiales</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Si hay instrucciones especiales para algún EPP, asegúrate de leerlas y entenderlas completamente antes de usarlos.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-tools fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 5: Mantenimiento y almacenamiento adecuados</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Limpia y guarda los EPP correctamente</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Después de usar los EPP, límpialos y almacénalos siguiendo las recomendaciones del fabricante para mantenerlos en buen estado.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-exclamation-triangle fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Paso 6: Reporte de incidentes</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Informa cualquier incidente o accidente</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Si ocurre algún incidente o accidente, comunícalo de inmediato al supervisor o al departamento de seguridad.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-users fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Responsabilidad de todos</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Comunicación y dudas</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">La seguridad es responsabilidad de todos. Si tienes dudas o inquietudes, comunícate con el departamento de seguridad o el comité de salud y seguridad.</p>
    </div>
    ''',
    '''
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; background-color: #ffffff;">
        <i class="fas fa-check-circle fa-4x" style="margin-bottom: 20px; color: #336699;"></i>
        <h1 style="font-size: 40px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Conclusiones</h1>
        <h2 style="font-size: 30px; text-align: center; color: #333333; font-family: Arial, sans-serif;">Prioriza tu seguridad y la de tus compañeros</h2>
        <p style="font-size: 20px; text-align: justify; color: #333333; font-family: Arial, sans-serif;">Recuerda que la seguridad es primordial. Prioriza tu seguridad y la de tus compañeros de trabajo en todo momento.</p>
    </div>
    '''
]





promp_icos ="""Eres un experto diseñador, te dare codigo html que simulan ser presentaciones de diapositivas, tu tarea es agregarle al código iconos deacuerdo a la información que muestren, para esto utilizaras iconos de
fontawesome. Quiero apartir del texto del html selecciones el icono que mejor se adapte a cada diapositiva, y tengas cuidado de no salirte del limite de 
tamaño de la etiqueta para que el icono se vea completo, utiliza iconos animados que ofrece fontawesome cuando puedas. 
Quiero que me entreges los resultados separados en un arreglo de python llamado diapositivas. Dame el arreglo para copiar y pegar"""


promp_diseñador = """Eres un experto diseñador de presentaciones y programador de css. Utiliza colores de fondo, letras, fuentes que se parezcan a una 
presentación. Deacuerdo a eso te dare un arreglo de codigos html. Tu tarea será arreglar el diseño de los html incluyendo el estilo dentro de cada etiqueta. Solo se
puede definir css dentro de los html que te entrege. Cada uno de los elementos del arreglo es una diapositiva diferente. Quiero que cada etiqueta tenga definida dentro de esta su estilo.
Quiero que me entreges los resultados separados en un arreglo de python llamado diapositivas."""
