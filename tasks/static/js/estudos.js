
console.log("olá, Mundo !")


//console.log(`O valor de variavel é ${varialvel_local}`)

var valor1 = 1
var valor2 = 2

if(valor1 === 1){
    /* o let serve somente para arqui dentro do escopo*/
    let valor1 = 100
    let valor2 = 200
    //console.log(valor1, valor2)
}

//console.log(valor1, valor2)


function x() {
    y = 100;   // Lança a exceção ReferenceError em modo restrito (strict mode)
    var z = 2;
  }
  
  //x();
  
  //console.log(y); // logs "1"
  //console.log(z); // Lança a exceção ReferenceError: z não foi definida fora da função x()
  

  var a;
  //console.log(a);                // mostra "undefined" ou "" dependendo do naveador.
  //console.log('still going...'); // mostra "still going...".
