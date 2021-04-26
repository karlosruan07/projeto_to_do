
x = 1

function teste1() {
    x = 10 //cria uma variável global e sobrescreve a antiga
    var y = 20//cria uma variável local para a função
    //console.log(x, y)

    function teste2() {
        x = 100//cria uma variável global e sobrescreve a antiga
        y = 200
        z = 300
    }
    teste2()
    console.log(x, y, z)
}

teste1()
console.log(x, z)
console.log(typeof(y))


