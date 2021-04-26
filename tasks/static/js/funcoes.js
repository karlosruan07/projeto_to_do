

function soma(valor1, valor2){
    return console.log(valor1 + valor2)
}

function subtracao(valor1, valor2) {
    return console.log(valor1 - valor2)
}

function multiplicacao(valor1, valor2) {
    return console.log(valor1 * valor2)
}

function divisao(valor1, valor2) {
    return console.log(valor1 / valor2)
}

function resto_divisao(valor1, valor2) {
    return console.log(valor1 % valor2)
}

function operador_and(valor1, valor2, valor3, valor4) {
    if(valor1 < valor2 && valor3 < valor4){
        return console.log(`A operção foi verdadeira`)
    }
}

function operador_or(valor1, valor2) {
    if(valor1 == "Ruan" || valor2 == "Carlos"){
        console.log('Uma das entradas são verdadeiras')
    }
}

function diferenca(valor1, valor2) {
    if(valor1 != valor2){
        console.log('Há diferença entre os parâmetros.')
    }
}

function igual_valor_tipo(valor1, valor2) {
    if (valor1 !== valor2) { // === analiza o tipo e o valor se são iguais, !== verifica se o valor e o tipo são diferentes.
        console.log('Os valores e os tipos são difirentes')
    } else {
        console.log('Os valores saõ iguais.')
        console.log('')
        console.log(typeof(valor1))
        console.log(typeof(valor2))
    }
}

function inversor(valor1) {
    console.log(`O valor passado foi o ${valor1} e a invesão agora é ${~valor1}`)
}


soma(100, 50)
subtracao(100, 50)
multiplicacao(2, 4)
divisao(10, 2)
resto_divisao(10, 2)
operador_and(1,2,3,4)
operador_or("Ruan", "Tavares")
diferenca("Ruan", "Carlos")
igual_valor_tipo(1,1)
inversor(5)
