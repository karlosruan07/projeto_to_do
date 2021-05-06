
function done() {
    window.location = "/filtro/done"
}

function doing() {
    window.location = "/filtro/doing"
}

/* {% extends 'base.html' %}

{% load static %}

{% block content %}

    <script>
        if(confirm("Deseja apagar ?")){

            alert('Apagado')
            window.location = "{% url 'deletar_tarefa' id=id %}"
        }
        else{
            alert('Cancelado com sucesso.')
            window.location = "{% url 'lista_tarefas' %}"
        }
    </script>

{% endblock %} */