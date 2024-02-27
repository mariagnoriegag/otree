from otree.api import *


doc = """
Your description
"""


class C(BaseConstants):
    NAME_IN_URL = 'simple_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

#datos del participante
class Player(BasePlayer):

    datos_quiz_name = models.StringField(label='¿Cuál es tu nombre?')
    datos_quiz_age = models.StringField(label='¿Cuál es tu edad?')
    datos_quiz_gender = models.IntegerField(
        label='¿Cuál es tu género?',
        choices=[
            [1, 'Masculino'],
            [2, 'Femenino'],
            [3, 'Otro']
        ],
        widget=widgets.RadioSelect
    )
#quiz de atencion
    a_quiz_1 = models.IntegerField(
        choices=[[0, 'Verdadero'], [1, 'Falso']],
        widget=widgets.RadioSelectHorizontal,
        label='Existen dos tipos de tareas: regulares y urgentes'
    )
    a_quiz_2 = models.IntegerField(
        choices=[[0, 'Verdadero'], [1, 'Falso']],
        widget=widgets.RadioSelectHorizontal,
        label='Todas los correos de reclamos están visibles en el inbox'
    )
    a_quiz_3 = models.IntegerField(
        choices=[[0, 'Inbox'], [1, 'WhatsApp'], [2, 'Mensaje de texto']],
        widget=widgets.RadioSelectHorizontal,
        label='Todas las tareas llegarán a través de un ...'
    )

    a_quiz_4  = models.IntegerField(
        choices=[[0, '25'], [1, '30'], [2, '40']],
        widget=widgets.RadioSelectHorizontal,
        label='¿Cúantos puntos ganas si respondes un reclamo urgente dentro de lo 16 minutos?'
    )

    a_quiz_5  = models.IntegerField(
        choices=[[0, '10'], [1, '15'], [2, '5']],
        widget=widgets.RadioSelectHorizontal,
        label='¿Cuántos puntos ganas si responder un reclamo regular (no urgente) dentro de los 20 minutos?'
    )

    a_quiz_6  = models.IntegerField(
        choices=[[0, '2'], [1, '1'], [2, '0']],
        widget=widgets.RadioSelectHorizontal,
        label='¿Cuántos puntos pierdes si tienes un error?'
    )
#ansiedad
    b_quiz_1 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='1. Me siento nervioso, ansioso o al límite'
    )
    
    b_quiz_2 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='2. No me siento capaz de detener o controlar la preocupación'
    )

    b_quiz_3 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='3. Me preocupo demasiado por diferentes cosas'
    )

    b_quiz_4 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='4. Tengo problemas para relajarme'
    )

    b_quiz_5 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='5. Me es difícil quedarme quieto'
    )

    b_quiz_6 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='6. Me molesto o irrito fácilmente'
    )

    b_quiz_7 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='7. Siento miedo, como si algo terrible pudiera suceder'
    )
#quiz de multitasking
    b_quiz_8 = models.IntegerField(
        choices=[[1, 'Trabajar secuencialmente durante esa hora'],[2, ' '],[3, 'Indiferente'],[4, ' '], [5, 'Trabajar simultáneamente']],
        widget=widgets.RadioSelect,
        label='1. Imagina que regresas al trabajo después de unas vacaciones y encuentras una pila de cartas en tu escritorio, 200 correos electrónicos en tu bandeja de entrada y diez mensajes en el contestador automático. Además, imagina que tienes una reunión dentro de una hora y quieres prepararte para varios temas tratados en esta reunión'
    )

    b_quiz_9 = models.IntegerField(
        choices=[[0, 'Trabajar secuencialmente los cinco proyectos'],[2, ' '],[3, 'Indiferente'],[4, ' '], [5, 'Trabajar simultáneamente los cinco proyectos']],
        widget=widgets.RadioSelect,
        label='2. Imagine que ha recibido cinco grandes proyectos a principios de año y que la fecha límite para los cinco proyectos es el final del año. Depende de usted cuándo planea trabajar en ellos.'
    )

    b_quiz_10 = models.IntegerField(
        choices=[[0, 'Reanudar la tarea interrumpida después de la llamada telefónica'],[2, ' '],[3, 'Indiferente'],[4, ' '], [5, 'Cambiar a otra tarea']],
        widget=widgets.RadioSelect,
        label='3. Imagina que llevas una hora trabajando en una tarea cuando te interrumpe una llamada telefónica.'
    )
#quiz ansiedad después
    e_quiz_1 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='1. Me sentí nervioso, ansioso o al límite'
    )
    
    e_quiz_2 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='2. No me sentí capaz de detener o controlar la preocupación'
    )

    e_quiz_3 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='3. Me preocupé demasiado por diferentes cosas'
    )

    e_quiz_4 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='4. Tuve problemas para relajarme'
    )

    e_quiz_5 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='5. Me fue difícil quedarme quieto'
    )

    e_quiz_6 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='6. Me molesté o irrité fácilmente'
    )

    e_quiz_7 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='7. Sentí miedo, como si algo terrible pudiera suceder'
    )
#quiz del flow
    f_quiz_1 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='1. Sentí la cantidad justa de desafío'
    )

    f_quiz_2 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='2. Mis pensamientos/actividades funcionaron con fluidez y sin problemas'
    )

    f_quiz_3 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='3. No noté el paso del tiempo'
    )

    f_quiz_4 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='4. No tuve dificultad para concentrarme'
    )

    f_quiz_5 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='5. Mi mente estaba completamente clara'
    )

    f_quiz_6 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='6. Estuve totalmente concentrado en lo que estoy haciendo'
    )

    f_quiz_7 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='7. Los pensamientos correctos ocurrían por sí solos'
    )
    f_quiz_8 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='8. Supe lo que tenía que hacer en cada paso del camino'
    )
    f_quiz_9 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='9. Sentí que tenía todo bajo control'
    )

    f_quiz_10 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='10. Estuve completamente perdido en mis pensamientos'
    )

    f_quiz_11 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='11. Algo importante para mí está en juego aquí'
    )
    f_quiz_12 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='12. Cometí algún error en el juego'
    )
    f_quiz_13 = models.IntegerField(
        choices=[[1, '1'],[2, '2'],[3, '3'],[4, '4'],[5, '5']],
        widget=widgets.RadioSelect,
        label='13. Me preocupé en fallar'
    )


    ## CASE 1 - SIMPLE
#Definicion de campos - formulario 1
    case_1_step_1_nombre = models.StringField()
    case_1_step_1_apellido = models.StringField()
    case_1_step_1_codigo = models.StringField()
    case_1_step_1_tipo_seguro = models.StringField()
    case_1_step_1_fecha_vencimiento = models.StringField()

#Creacion de campos enteros pregunta 2
    case_1_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

# Creacion de campos enteros pregunta 3
    case_1_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )
# Creacion de campos enteros pregunta 4
    case_1_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )



    ## CASE 2 - SIMPLE

    case_2_step_1_nombre = models.StringField()
    case_2_step_1_apellido = models.StringField()
    case_2_step_1_codigo = models.StringField()
    case_2_step_1_tipo_seguro = models.StringField()
    case_2_step_1_fecha_vencimiento = models.StringField()

    case_2_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )


    case_2_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_2_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 3 - SIMPLE

    case_3_step_1_nombre = models.StringField()
    case_3_step_1_apellido = models.StringField()
    case_3_step_1_codigo = models.StringField()
    case_3_step_1_tipo_seguro = models.StringField()
    case_3_step_1_fecha_vencimiento = models.StringField()

    case_3_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_3_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_3_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 6 - SIMPLE

    case_6_step_1_nombre = models.StringField()
    case_6_step_1_apellido = models.StringField()
    case_6_step_1_codigo = models.StringField()
    case_6_step_1_tipo_seguro = models.StringField()
    case_6_step_1_fecha_vencimiento = models.StringField()

    case_6_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )


    case_6_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_6_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 8 - SIMPLE

    case_8_step_1_nombre = models.StringField()
    case_8_step_1_apellido = models.StringField()
    case_8_step_1_codigo = models.StringField()
    case_8_step_1_tipo_seguro = models.StringField()
    case_8_step_1_fecha_vencimiento = models.StringField()

    case_8_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_8_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_8_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 10 - SIMPLE

    case_10_step_1_nombre = models.StringField()
    case_10_step_1_apellido = models.StringField()
    case_10_step_1_codigo = models.StringField()
    case_10_step_1_tipo_seguro = models.StringField()
    case_10_step_1_fecha_vencimiento = models.StringField()

    case_10_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_10_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_10_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )

    ## CASE 11 - SIMPLE

    case_11_step_1_nombre = models.StringField()
    case_11_step_1_apellido = models.StringField()
    case_11_step_1_codigo = models.StringField()
    case_11_step_1_tipo_seguro = models.StringField()
    case_11_step_1_fecha_vencimiento = models.StringField()

    case_11_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_11_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_11_step_4_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 4 - COMPLEX

    case_4_step_1_nombre = models.StringField()
    case_4_step_1_apellido = models.StringField()
    case_4_step_1_codigo = models.StringField()
    case_4_step_1_tipo_seguro = models.StringField()
    case_4_step_1_fecha_vencimiento = models.StringField()

    case_4_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_4_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_4_step_4_propietario = models.StringField()
    case_4_step_4_placa = models.StringField()

    case_4_step_5_1 = models.IntegerField(
        choices=[
            [1, 'Sí, la información proporcionada en el reclamo es consistente con el Informe Técnico.'],
            [2, 'No, la información proporcionada en el reclamo es inconsistente con el Informe Técnico.']
        ],
        widget=widgets.RadioSelect
    )

    case_4_step_6_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 5 - COMPLEX

    case_5_step_1_nombre = models.StringField()
    case_5_step_1_apellido = models.StringField()
    case_5_step_1_codigo = models.StringField()
    case_5_step_1_tipo_seguro = models.StringField()
    case_5_step_1_fecha_vencimiento = models.StringField()

    case_5_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_5_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_5_step_4_propietario = models.StringField()
    case_5_step_4_placa = models.StringField()

    case_5_step_5_1 = models.IntegerField(
        choices=[
            [1, 'Sí, la información proporcionada en el reclamo es consistente con el Informe Técnico.'],
            [2, 'No, la información proporcionada en el reclamo es inconsistente con el Informe Técnico.']
        ],
        widget=widgets.RadioSelect
    )

    case_5_step_6_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )



    ## CASE 7 - COMPLEX

    case_7_step_1_nombre = models.StringField()
    case_7_step_1_apellido = models.StringField()
    case_7_step_1_codigo = models.StringField()
    case_7_step_1_tipo_seguro = models.StringField()
    case_7_step_1_fecha_vencimiento = models.StringField()

    case_7_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_7_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_7_step_4_propietario = models.StringField()
    case_7_step_4_placa = models.StringField()

    case_7_step_5_1 = models.IntegerField(
        choices=[
            [1, 'Sí, la información proporcionada en el reclamo es consistente con el Informe Técnico.'],
            [2, 'No, la información proporcionada en el reclamo es inconsistente con el Informe Técnico.']
        ],
        widget=widgets.RadioSelect
    )

    case_7_step_6_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )


    ## CASE 9 - COMPLEX

    case_9_step_1_nombre = models.StringField()
    case_9_step_1_apellido = models.StringField()
    case_9_step_1_codigo = models.StringField()
    case_9_step_1_tipo_seguro = models.StringField()
    case_9_step_1_fecha_vencimiento = models.StringField()

    case_9_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_9_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_9_step_4_propietario = models.StringField()
    case_9_step_4_nombre = models.StringField()
    case_9_step_4_direccion = models.StringField()
    case_9_step_4_placa = models.StringField()

    case_9_step_5_1 = models.IntegerField(
        choices=[
            [1, 'Sí, la información proporcionada en el reclamo es consistente con el Informe Técnico.'],
            [2, 'No, la información proporcionada en el reclamo es inconsistente con el Informe Técnico.']
        ],
        widget=widgets.RadioSelect
    )

    case_9_step_6_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )

    ## CASE 12 - COMPLEX

    case_12_step_1_nombre = models.StringField()
    case_12_step_1_apellido = models.StringField()
    case_12_step_1_codigo = models.StringField()
    case_12_step_1_tipo_seguro = models.StringField()
    case_12_step_1_fecha_vencimiento = models.StringField()

    case_12_step_2_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_12_step_3_1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_12_step_4_propietario = models.StringField()
    case_12_step_4_placa = models.StringField()

    case_12_step_5_1 = models.IntegerField(
        choices=[
            [1, 'Sí, la información proporcionada en el reclamo es consistente con el Informe Técnico.'],
            [2, 'No, la información proporcionada en el reclamo es inconsistente con el Informe Técnico.']
        ],
        widget=widgets.RadioSelect
    )

    case_12_step_6_1 = models.IntegerField(
        choices=[
            [1, 'El reclamo es aceptado'],
            [2, 'El reclamo es rechazado']
        ],
        widget=widgets.RadioSelect
    )

    ## EXTRA METRICS

#Para calcular metricas
#Definicion para registrar inicio y fin de tareas
    start_date = models.StringField()
    end_date = models.StringField()

#Definicion de casos urgentes / booleano
    case_1_urgent = models.BooleanField()
    case_2_urgent = models.BooleanField()
    case_3_urgent = models.BooleanField()
    case_4_urgent = models.BooleanField()
    case_5_urgent = models.BooleanField()
    case_6_urgent = models.BooleanField()
    case_7_urgent = models.BooleanField()
    case_8_urgent = models.BooleanField()
    case_9_urgent = models.BooleanField()
    case_10_urgent = models.BooleanField()
    case_11_urgent = models.BooleanField()
    case_12_urgent = models.BooleanField()

#Deficion de tiempo de inicio
    case_1_start_time = models.StringField()
    case_2_start_time = models.StringField()
    case_3_start_time = models.StringField()
    case_4_start_time = models.StringField()
    case_5_start_time = models.StringField()
    case_6_start_time = models.StringField()
    case_7_start_time = models.StringField()
    case_8_start_time = models.StringField()
    case_9_start_time = models.StringField()
    case_10_start_time = models.StringField()
    case_11_start_time = models.StringField()
    case_12_start_time = models.StringField()

#Definicion de tiempo de finalización de tareas
    case_1_end_time = models.StringField()
    case_2_end_time = models.StringField()
    case_3_end_time = models.StringField()
    case_4_end_time = models.StringField()
    case_5_end_time = models.StringField()
    case_6_end_time = models.StringField()
    case_7_end_time = models.StringField()
    case_8_end_time = models.StringField()
    case_9_end_time = models.StringField()
    case_10_end_time = models.StringField()
    case_11_end_time = models.StringField()
    case_12_end_time = models.StringField()

    case_1_solution_time = models.StringField()
    case_2_solution_time = models.StringField()
    case_3_solution_time = models.StringField()
    case_4_solution_time = models.StringField()
    case_5_solution_time = models.StringField()
    case_6_solution_time = models.StringField()
    case_7_solution_time = models.StringField()
    case_8_solution_time = models.StringField()
    case_9_solution_time = models.StringField()
    case_10_solution_time = models.StringField()
    case_11_solution_time = models.StringField()
    case_12_solution_time = models.StringField()

    case_1_error_count = models.StringField()
    case_2_error_count = models.StringField()
    case_3_error_count = models.StringField()
    case_4_error_count = models.StringField()
    case_5_error_count = models.StringField()
    case_6_error_count = models.StringField()
    case_7_error_count = models.StringField()
    case_8_error_count = models.StringField()
    case_9_error_count = models.StringField()
    case_10_error_count = models.StringField()
    case_11_error_count = models.StringField()
    case_12_error_count = models.StringField()

    list_intr_id = models.StringField()
    list_intr_time = models.StringField()
    pass


# PAGES
class Task(Page):    
    timeout_seconds = 30 * 60
    form_model = 'player'
    form_fields = [
        'case_1_step_1_nombre', 'case_1_step_1_apellido', 'case_1_step_1_codigo', 'case_1_step_1_tipo_seguro', 'case_1_step_1_fecha_vencimiento', 'case_1_step_2_1', 'case_1_step_3_1', 'case_1_step_4_1',
        'case_2_step_1_nombre', 'case_2_step_1_apellido', 'case_2_step_1_codigo', 'case_2_step_1_tipo_seguro', 'case_2_step_1_fecha_vencimiento', 'case_2_step_2_1', 'case_2_step_3_1', 'case_2_step_4_1',
        'case_3_step_1_nombre', 'case_3_step_1_apellido', 'case_3_step_1_codigo', 'case_3_step_1_tipo_seguro', 'case_3_step_1_fecha_vencimiento', 'case_3_step_2_1','case_3_step_3_1', 'case_3_step_4_1',
        'case_6_step_1_nombre', 'case_6_step_1_apellido', 'case_6_step_1_codigo', 'case_6_step_1_tipo_seguro', 'case_6_step_1_fecha_vencimiento', 'case_6_step_2_1', 'case_6_step_3_1', 'case_6_step_4_1',
        'case_8_step_1_nombre', 'case_8_step_1_apellido', 'case_8_step_1_codigo', 'case_8_step_1_tipo_seguro', 'case_8_step_1_fecha_vencimiento', 'case_8_step_2_1', 'case_8_step_3_1', 'case_8_step_4_1',
        'case_10_step_1_nombre', 'case_10_step_1_apellido', 'case_10_step_1_codigo', 'case_10_step_1_tipo_seguro', 'case_10_step_1_fecha_vencimiento', 'case_10_step_2_1', 'case_10_step_3_1', 'case_10_step_4_1',
        'case_11_step_1_nombre', 'case_11_step_1_apellido', 'case_11_step_1_codigo', 'case_11_step_1_tipo_seguro', 'case_11_step_1_fecha_vencimiento', 'case_11_step_2_1', 'case_11_step_3_1', 'case_11_step_4_1',

        'case_4_step_1_nombre', 'case_4_step_1_apellido', 'case_4_step_1_codigo', 'case_4_step_1_tipo_seguro', 'case_4_step_1_fecha_vencimiento', 'case_4_step_2_1', 'case_4_step_3_1', 'case_4_step_4_propietario',  'case_4_step_4_placa', 'case_4_step_5_1', 'case_4_step_6_1',
        'case_5_step_1_nombre', 'case_5_step_1_apellido', 'case_5_step_1_codigo', 'case_5_step_1_tipo_seguro', 'case_5_step_1_fecha_vencimiento', 'case_5_step_2_1', 'case_5_step_3_1', 'case_5_step_4_propietario','case_5_step_4_placa', 'case_5_step_5_1', 'case_5_step_6_1',
        'case_7_step_1_nombre', 'case_7_step_1_apellido', 'case_7_step_1_codigo', 'case_7_step_1_tipo_seguro', 'case_7_step_1_fecha_vencimiento', 'case_7_step_2_1',  'case_7_step_3_1', 'case_7_step_4_propietario',  'case_7_step_4_placa', 'case_7_step_5_1', 'case_7_step_6_1',
        'case_9_step_1_nombre', 'case_9_step_1_apellido', 'case_9_step_1_codigo', 'case_9_step_1_tipo_seguro', 'case_9_step_1_fecha_vencimiento', 'case_9_step_2_1', 'case_9_step_3_1', 'case_9_step_4_propietario', 'case_9_step_4_placa', 'case_9_step_5_1', 'case_9_step_6_1',
        'case_12_step_1_nombre', 'case_12_step_1_apellido', 'case_12_step_1_codigo', 'case_12_step_1_tipo_seguro', 'case_12_step_1_fecha_vencimiento', 'case_12_step_2_1', 'case_12_step_3_1', 'case_12_step_4_propietario', 'case_12_step_4_placa', 'case_12_step_5_1', 'case_12_step_6_1',
        
        'case_1_urgent', 'case_2_urgent', 'case_3_urgent', 'case_4_urgent', 'case_5_urgent', 'case_6_urgent', 'case_7_urgent', 'case_8_urgent', 'case_9_urgent', 'case_10_urgent', 'case_11_urgent', 'case_12_urgent',
        'case_1_start_time', 'case_2_start_time', 'case_3_start_time', 'case_4_start_time', 'case_5_start_time', 'case_6_start_time', 'case_7_start_time', 'case_8_start_time', 'case_9_start_time', 'case_10_start_time', 'case_11_start_time', 'case_12_start_time',
        'case_1_end_time', 'case_2_end_time', 'case_3_end_time', 'case_4_end_time', 'case_5_end_time', 'case_6_end_time', 'case_7_end_time', 'case_8_end_time', 'case_9_end_time', 'case_10_end_time', 'case_11_end_time', 'case_12_end_time',
        'case_1_solution_time', 'case_2_solution_time', 'case_3_solution_time', 'case_4_solution_time', 'case_5_solution_time', 'case_6_solution_time', 'case_7_solution_time', 'case_8_solution_time', 'case_9_solution_time', 'case_10_solution_time', 'case_11_solution_time', 'case_12_solution_time',
        'case_1_error_count', 'case_2_error_count', 'case_3_error_count', 'case_4_error_count', 'case_5_error_count', 'case_6_error_count', 'case_7_error_count', 'case_8_error_count', 'case_9_error_count', 'case_10_error_count', 'case_11_error_count', 'case_12_error_count',
        'list_intr_id', 'list_intr_time',
        'start_date', 'end_date'
    ]
    pass

# PAGES
class TasksProgressBar(Page):    
    timeout_seconds = 30 * 60
    form_model = 'player'
    form_fields = [
        'case_1_step_1_nombre', 'case_1_step_1_apellido', 'case_1_step_1_codigo', 'case_1_step_1_tipo_seguro', 'case_1_step_1_fecha_vencimiento', 'case_1_step_2_1', 'case_1_step_3_1', 'case_1_step_4_1',
        'case_2_step_1_nombre', 'case_2_step_1_apellido', 'case_2_step_1_codigo', 'case_2_step_1_tipo_seguro', 'case_2_step_1_fecha_vencimiento', 'case_2_step_2_1', 'case_2_step_3_1', 'case_2_step_4_1',
        'case_3_step_1_nombre', 'case_3_step_1_apellido', 'case_3_step_1_codigo', 'case_3_step_1_tipo_seguro', 'case_3_step_1_fecha_vencimiento', 'case_3_step_2_1','case_3_step_3_1', 'case_3_step_4_1',
        'case_6_step_1_nombre', 'case_6_step_1_apellido', 'case_6_step_1_codigo', 'case_6_step_1_tipo_seguro', 'case_6_step_1_fecha_vencimiento', 'case_6_step_2_1', 'case_6_step_3_1', 'case_6_step_4_1',
        'case_8_step_1_nombre', 'case_8_step_1_apellido', 'case_8_step_1_codigo', 'case_8_step_1_tipo_seguro', 'case_8_step_1_fecha_vencimiento', 'case_8_step_2_1', 'case_8_step_3_1', 'case_8_step_4_1',
        'case_10_step_1_nombre', 'case_10_step_1_apellido', 'case_10_step_1_codigo', 'case_10_step_1_tipo_seguro', 'case_10_step_1_fecha_vencimiento', 'case_10_step_2_1', 'case_10_step_3_1', 'case_10_step_4_1',
        'case_11_step_1_nombre', 'case_11_step_1_apellido', 'case_11_step_1_codigo', 'case_11_step_1_tipo_seguro', 'case_11_step_1_fecha_vencimiento', 'case_11_step_2_1', 'case_11_step_3_1', 'case_11_step_4_1',

        'case_4_step_1_nombre', 'case_4_step_1_apellido', 'case_4_step_1_codigo', 'case_4_step_1_tipo_seguro', 'case_4_step_1_fecha_vencimiento', 'case_4_step_2_1', 'case_4_step_3_1', 'case_4_step_4_propietario',  'case_4_step_4_placa', 'case_4_step_5_1', 'case_4_step_6_1',
        'case_5_step_1_nombre', 'case_5_step_1_apellido', 'case_5_step_1_codigo', 'case_5_step_1_tipo_seguro', 'case_5_step_1_fecha_vencimiento', 'case_5_step_2_1', 'case_5_step_3_1', 'case_5_step_4_propietario','case_5_step_4_placa', 'case_5_step_5_1', 'case_5_step_6_1',
        'case_7_step_1_nombre', 'case_7_step_1_apellido', 'case_7_step_1_codigo', 'case_7_step_1_tipo_seguro', 'case_7_step_1_fecha_vencimiento', 'case_7_step_2_1',  'case_7_step_3_1', 'case_7_step_4_propietario',  'case_7_step_4_placa', 'case_7_step_5_1', 'case_7_step_6_1',
        'case_9_step_1_nombre', 'case_9_step_1_apellido', 'case_9_step_1_codigo', 'case_9_step_1_tipo_seguro', 'case_9_step_1_fecha_vencimiento', 'case_9_step_2_1', 'case_9_step_3_1', 'case_9_step_4_propietario', 'case_9_step_4_placa', 'case_9_step_5_1', 'case_9_step_6_1',
        'case_12_step_1_nombre', 'case_12_step_1_apellido', 'case_12_step_1_codigo', 'case_12_step_1_tipo_seguro', 'case_12_step_1_fecha_vencimiento', 'case_12_step_2_1', 'case_12_step_3_1', 'case_12_step_4_propietario', 'case_12_step_4_placa', 'case_12_step_5_1', 'case_12_step_6_1',
        
        'case_1_urgent', 'case_2_urgent', 'case_3_urgent', 'case_4_urgent', 'case_5_urgent', 'case_6_urgent', 'case_7_urgent', 'case_8_urgent', 'case_9_urgent', 'case_10_urgent', 'case_11_urgent', 'case_12_urgent',
        'case_1_start_time', 'case_2_start_time', 'case_3_start_time', 'case_4_start_time', 'case_5_start_time', 'case_6_start_time', 'case_7_start_time', 'case_8_start_time', 'case_9_start_time', 'case_10_start_time', 'case_11_start_time', 'case_12_start_time',
        'case_1_end_time', 'case_2_end_time', 'case_3_end_time', 'case_4_end_time', 'case_5_end_time', 'case_6_end_time', 'case_7_end_time', 'case_8_end_time', 'case_9_end_time', 'case_10_end_time', 'case_11_end_time', 'case_12_end_time',
        'case_1_solution_time', 'case_2_solution_time', 'case_3_solution_time', 'case_4_solution_time', 'case_5_solution_time', 'case_6_solution_time', 'case_7_solution_time', 'case_8_solution_time', 'case_9_solution_time', 'case_10_solution_time', 'case_11_solution_time', 'case_12_solution_time',
        'case_1_error_count', 'case_2_error_count', 'case_3_error_count', 'case_4_error_count', 'case_5_error_count', 'case_6_error_count', 'case_7_error_count', 'case_8_error_count', 'case_9_error_count', 'case_10_error_count', 'case_11_error_count', 'case_12_error_count',
        'list_intr_id', 'list_intr_time',
        'start_date', 'end_date'
    ]
    pass

#pagina de ingreso de datos del participante
class DatosQuiz(Page):
    form_model = 'player'
    form_fields = [
        'datos_quiz_name', 'datos_quiz_age', 'datos_quiz_gender'
    ]
    pass

#pagina de instrucciones

class Instrucciones(Page):
    form_model = 'player'
    form_fields = []
    pass

class AtentionQuiz(Page):
    form_model = 'player'
    form_fields = [
        'a_quiz_1', 'a_quiz_2', 'a_quiz_3', 'a_quiz_4', 'a_quiz_5', 'a_quiz_6'
    ]
    pass

class BeginQuiz(Page):
    form_model = 'player'
    form_fields = [
        'b_quiz_1', 'b_quiz_2', 'b_quiz_3', 'b_quiz_4', 'b_quiz_5', 'b_quiz_6', 'b_quiz_7'
    ]
    pass

class MultiQuiz(Page):
    form_model = 'player'
    form_fields = [
        'b_quiz_8', 'b_quiz_9', 'b_quiz_10'
    ]
    pass


class EndQuiz(Page):
    form_model = 'player'
    form_fields = [
        'e_quiz_1', 'e_quiz_2', 'e_quiz_3', 'e_quiz_4', 'e_quiz_5', 'e_quiz_6', 'e_quiz_7'
    ]
    pass

class FlowQuiz(Page):
    form_model = 'player'
    form_fields = [
        'f_quiz_1', 'f_quiz_2', 'f_quiz_3', 'f_quiz_4', 'f_quiz_5', 'f_quiz_6', 'f_quiz_7',
        'f_quiz_8', 'f_quiz_9', 'f_quiz_10', 'f_quiz_11', 'f_quiz_12', 'f_quiz_13'
    ]
    pass

#page_sequence = [DatosQuiz, Instrucciones, AtentionQuiz, BeginQuiz, MultiQuiz, Task, EndQuiz, FlowQuiz] #DatosQuiz,Instrucciones, AtentionQuiz, BeginQuiz,MultiQuiz, Task, EndQuiz, FlowQuiz
# page_sequence = [Task]
page_sequence = [TasksProgressBar]

# aplicar la barra de progreso
